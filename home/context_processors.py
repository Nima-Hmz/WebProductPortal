from .models import ContactUs
from .models import AboutUs, FirstTitle

def current_language(request):

    contactus = ContactUs.objects.first()
    aboutus = AboutUs.objects.first()
    first_title = FirstTitle.objects.first()
    output = {}
    output['aboutus_title'] = aboutus.fa_title
    output['aboutus_description'] = aboutus.fa_description
    output['contact_description'] = contactus.fa_description
    output['contact_title'] = contactus.fa_title
    output['contact_phone'] = contactus.phone_number
    output['contact_email'] = contactus.email 
    output['contact_location'] = contactus.location
    output['web_title'] = first_title.fa_title

    return output