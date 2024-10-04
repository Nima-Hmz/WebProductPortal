from .models import FirstTitle, ContactUs, AboutUs


def language_switcher(model_object, usecase, option="", option2="") :
	# extension for choosing the right attribute from the model

	context = {

		f'{usecase}_title{option}':model_object.fa_title,
		f'{usecase}_description{option}':model_object.fa_description	

	}

	return context