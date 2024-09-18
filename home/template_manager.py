from .models import FirstTitle, ContactUs, AboutUs, Services


def language_switcher(model_object, lang, usecase, option="", option2="") :
	# extension for choosing the right attribute from the model

	context = {

		f'{usecase}_title{option}':model_object.get_title(lang),
		f'{usecase}_description{option}':model_object.get_description(lang)

	}

	return context