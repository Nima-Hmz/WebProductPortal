from .models import ContactUs
from .template_manager import language_switcher
from .models import AboutUs

def current_language(request):

    contactus = ContactUs.objects.first()
    aboutus = AboutUs.objects.first()
    output = {}
    output.update(language_switcher(contactus, "contact"))
    output.update(language_switcher(aboutus, "about"))
    output['contact_phone'] = contactus.phone_number
    output['contact_email'] = contactus.email 
    output['contact_location'] = contactus.location

    return output