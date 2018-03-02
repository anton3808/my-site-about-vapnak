from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
	return render(request, 'about_ru/wrapper.html')


def about_ru_search(request):
	# if request.GET:
		seach_text = request.GET['text-field']
		seach_names_about = set(["про компанію", "Про компанію", "ПРО Компанію", "ПРО КОМПАНІЮ", "Про компанию", "про компанию", "Про Компанию", "ПРО КОМПАНИЮ", "about company", "About company", "About Company", "ABOUT company", "About COMPANY", "ABOUT COMPANY", "home"])

		seach_names_production = set(["продукція", "Продукція", "ПРОДУКЦІЯ", "Продукция", "продукция", "ПРОДУКЦИЯ", "production", "Production", "PRODUCTION"])
		
		seach_names_contact = set(["контакти", "Контакти", "КОНТАКТИ", "Контакты", "контакты", "КОНТАКТЫ", "contact", "Contact", "CONTACT"])

		seach_names_services = set(["наші послуги", "Наші послуги", "НАШІ ПОСЛУГИ", "послуги", "Послуги", "ПОСЛУГИ", "Наши услуги", "наши услуги", "УСЛУГИ", "Услуги", "услуги", "НАШИ УСЛУГИ", "our services", "Our services", "OUR SERVICES", "services", "Services", "SERVICES"])

		seach_names_reviews = set(["відгуки", "Відгуки", "ВІДГУКИ", "Отзывы", "отзывы", "ОТЗЫВЫ", "reviews", "Reviews", "REVIEWS"])


		if seach_text in seach_names_production:
			return HttpResponseRedirect("../../ru/production/")
		elif seach_text in seach_names_about:
			return HttpResponseRedirect("/")
		elif seach_text in seach_names_contact:
			return HttpResponseRedirect("../../ru/contact/")
		elif seach_text in seach_names_reviews:
			return HttpResponseRedirect("../../ru/reviews/")
		elif seach_text in seach_names_services:
			return HttpResponseRedirect("../../ru/services/")
		else:
			return render(request, 'error_ru/wrapper.html')







def about_ru_search_mobile(request):
	# if request.GET:
		seach_text = request.GET['text-field']
		seach_names_about = set(["про компанію", "Про компанію", "ПРО Компанію", "ПРО КОМПАНІЮ", "Про компанию", "про компанию", "Про Компанию", "ПРО КОМПАНИЮ", "about company", "About company", "About Company", "ABOUT company", "About COMPANY", "ABOUT COMPANY", "home"])

		seach_names_production = set(["продукція", "Продукція", "ПРОДУКЦІЯ", "Продукция", "продукция", "ПРОДУКЦИЯ", "production", "Production", "PRODUCTION"])
		
		seach_names_contact = set(["контакти", "Контакти", "КОНТАКТИ", "Контакты", "контакты", "КОНТАКТЫ", "contact", "Contact", "CONTACT"])

		seach_names_reviews = set(["відгуки", "Відгуки", "ВІДГУКИ", "Отзывы", "отзывы", "ОТЗЫВЫ", "reviews", "Reviews", "REVIEWS"])

		seach_names_services = set(["наші послуги", "Наші послуги", "НАШІ ПОСЛУГИ", "послуги", "Послуги", "ПОСЛУГИ", "Наши услуги", "наши услуги", "УСЛУГИ", "Услуги", "услуги", "НАШИ УСЛУГИ", "our services", "Our services", "OUR SERVICES", "services", "Services", "SERVICES"])


		if seach_text in seach_names_production:
			return HttpResponseRedirect("../../ru/production/")
		elif seach_text in seach_names_about:
			return HttpResponseRedirect("/")
		elif seach_text in seach_names_contact:
			return HttpResponseRedirect("../../ru/contact/")
		elif seach_text in seach_names_reviews:
			return HttpResponseRedirect("../../ru/reviews/")
		elif seach_text in seach_names_services:
			return HttpResponseRedirect("../../ru/services/")
		else:
			return render(request, 'error_ru/wrapper.html')