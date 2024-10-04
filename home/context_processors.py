from .models import ContactUs
from .template_manager import language_switcher
from .models import AboutUs, FirstTitle

def current_language(request):

    contactus = ContactUs.objects.first()
    aboutus = AboutUs.objects.first()
    first_title = FirstTitle.objects.first()
    output = {}
    output.update(language_switcher(contactus, "contact"))
    output.update(language_switcher(aboutus, "about"))
    output['contact_phone'] = contactus.phone_number
    output['contact_email'] = contactus.email 
    output['contact_location'] = contactus.location
    output['web_title'] = first_title.fa_title

    return output