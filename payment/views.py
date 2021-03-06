from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def send(request):
    # return HttpResponseRedirect("production/")
    contact_person = request.POST.get('contact_person', '')
    phone = request.POST.get('phone', '')
    cargo = request.POST.get('cargo', '')
    cod_cargo_railway = request.POST.get('cod_cargo_railway', '')
    load_station = request.POST.get('load_station', '')
    cod_load_station = request.POST.get('cod_load_station', '')
    unloading_station = request.POST.get('unloading_station', '')
    cod_unloading_station = request.POST['cod_unloading_station']




    subject = "Оrganization of cargo transportation"
    from_email = settings.EMAIL_HOST_USER
    to_email = from_email
    contact_message = "Контактна особа: %s, номер телефона: %s, вантаж: %s, код вантажу по залізниці: %s, станція навантаження: %s, код станції навантаження: %s, станція вивантаження: %s, код станція вивантаження: %s"%(contact_person, phone, cargo, cod_cargo_railway, load_station, cod_load_station, unloading_station, cod_unloading_station)
    
    if contact_person and phone and cargo and cod_cargo_railway and load_station and cod_load_station and unloading_station and cod_unloading_station:       
        try:
            send_mail(subject, contact_message, from_email, ['antonsadlov@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('../')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')






def index(request):
	return render(request, 'payment/wrapper.html')



def payment_search(request):
	# if request.GET:
		seach_text = request.GET['text-field']
		
		seach_names_production = set(["продукція", "Продукція", "ПРОДУКЦІЯ", "Продукция", "продукция", "ПРОДУКЦИЯ", "production", "Production", "PRODUCTION"])

		seach_names_contact = set(["контакти", "Контакти", "КОНТАКТИ", "Контакты", "контакты", "КОНТАКТЫ", "contact", "Contact", "CONTACT"])

		seach_names_reviews = set(["відгуки", "Відгуки", "ВІДГУКИ", "Отзывы", "отзывы", "ОТЗЫВЫ", "reviews", "Reviews", "REVIEWS"])

		seach_names_about = set(["про компанію", "Про компанію", "ПРО Компанію", "ПРО КОМПАНІЮ", "Про компанию", "про компанию", "Про Компанию", "ПРО КОМПАНИЮ", "about company", "About company", "About Company", "ABOUT company", "About COMPANY", "ABOUT COMPANY", "home"])

		if seach_text in seach_names_production:
			return render(request, 'production/wrapper.html')
		elif seach_text in seach_names_contact:
			return render(request, 'contact/wrapper.html')
		elif seach_text in seach_names_reviews:
			return render(request, 'reviews/wrapper.html')
		elif seach_text in seach_names_about:
			return render(request, 'about/wrapper.html')
		else:
			return HttpResponseRedirect("/")


# def form_services(request):
#     return HttpResponseRedirect("contact/")
    # return render(request, 'about/wrapper.html')






