from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def send_email_4(request):
    user_surname = request.POST.get('user_surname', '')
    user_name = request.POST.get('user_name', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    select_fraction = request.POST.get('select_fraction', '')
    enterprise = request.POST.get('enterprise', '')
    delivery_period = request.POST.get('delivery_period', '')
    message = request.POST['message']
    # message = request.POST.get('message', '')

    subject = "Contact form(dla kombikormov i pidkormku ptizu)"
    from_email = settings.EMAIL_HOST_USER
    to_email = from_email
    if message:
    	contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: %s, текстов повідомлення: %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period, message)
    else:
    	contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period)
    
    if user_surname and user_name and email and phone and select_fraction and enterprise and delivery_period:
        try:
            send_mail(subject, contact_message, from_email, ['antonsadlov@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('../')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')


def send_email_3(request):
    user_surname = request.POST.get('user_surname', '')
    user_name = request.POST.get('user_name', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    select_fraction = request.POST.get('select_fraction', '')
    enterprise = request.POST.get('enterprise', '')
    delivery_period = request.POST.get('delivery_period', '')
    message = request.POST['message']
    # message = request.POST.get('message', '')

    subject = "Contact form(dla zukrovoi promuslovosti)"
    from_email = settings.EMAIL_HOST_USER
    to_email = from_email
    if message:
    	contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: %s, текстов повідомлення: %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period, message)
    else:
    	contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period)
    if user_surname and user_name and email and phone and select_fraction and enterprise and delivery_period:
        try:
            send_mail(subject, contact_message, from_email, ['antonsadlov@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('../')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')




def send_email_2(request):
    user_surname = request.POST.get('user_surname', '')
    user_name = request.POST.get('user_name', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    select_fraction = request.POST.get('select_fraction', '')
    enterprise = request.POST.get('enterprise', '')
    delivery_period = request.POST.get('delivery_period', '')
    message = request.POST['message']
    # message = request.POST.get('message', '')

    subject = "Contact form(dla rozkusnenya gruntu i vodoyom)"
    from_email = settings.EMAIL_HOST_USER
    to_email = from_email
    if message:
    	contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: %s, текстов повідомлення: %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period, message)
    else:
    	contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period)
    if user_surname and user_name and email and phone and select_fraction and enterprise and delivery_period:
        try:
            send_mail(subject, contact_message, from_email, ['antonsadlov@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('../')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')







def send_email_1(request):
    contact_person = request.POST.get('contact_person', '')
    phone = request.POST.get('phone', '')
    cargo = request.POST.get('cargo', '')
    cod_cargo_railway = request.POST.get('cod_cargo_railway', '')
    load_station = request.POST.get('load_station', '')
    cod_load_station = request.POST.get('cod_load_station', '')
    unloading_station = request.POST.get('unloading_station_period', '')
    cod_unloading_station = request.POST['cod_unloading_station']
    # cod_unloading_station = request.POST['cod_unloading_station']




    subject = "Contact form(dla metalurgii ta vurobnukiv vapna)"
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
	return render(request, 'production_en/wrapper.html')


def successView(request):
    return HttpResponse('Success! Thank you for your message.') 





def production_en_search_mobile(request):
    # if request.GET:
        seach_text = request.GET['text-field']
        seach_names_about = set(["про компанію", "Про компанію", "ПРО Компанію", "ПРО КОМПАНІЮ", "Про компанию", "про компанию", "Про Компанию", "ПРО КОМПАНИЮ", "about company", "About company", "About Company", "ABOUT company", "About COMPANY", "ABOUT COMPANY", "home"])

        seach_names_production = set(["продукція", "Продукція", "ПРОДУКЦІЯ", "Продукция", "продукция", "ПРОДУКЦИЯ", "production", "Production", "PRODUCTION"])
        
        seach_names_contact = set(["контакти", "Контакти", "КОНТАКТИ", "Контакты", "контакты", "КОНТАКТЫ", "contact", "Contact", "CONTACT"])

        seach_names_reviews = set(["відгуки", "Відгуки", "ВІДГУКИ", "Отзывы", "отзывы", "ОТЗЫВЫ", "reviews", "Reviews", "REVIEWS"])

        seach_names_services = set(["наші послуги", "Наші послуги", "НАШІ ПОСЛУГИ", "послуги", "Послуги", "ПОСЛУГИ", "Наши услуги", "наши услуги", "УСЛУГИ", "Услуги", "услуги", "НАШИ УСЛУГИ", "our services", "Our services", "OUR SERVICES", "services", "Services", "SERVICES"])


        if seach_text in seach_names_production:
            return HttpResponseRedirect("../../../en/production/")
        elif seach_text in seach_names_about:
            return HttpResponseRedirect("../../../en/")
        elif seach_text in seach_names_contact:
            return HttpResponseRedirect("../../../en/contact/")
        elif seach_text in seach_names_reviews:
            return HttpResponseRedirect("../../../en/reviews/")
        elif seach_text in seach_names_services:
            return HttpResponseRedirect("../../../en/services/")
        else:
            return render(request, 'error_en/wrapper.html')