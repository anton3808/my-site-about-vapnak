from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def send_email_4(request):
    user_surname = request.POST.get('user_surname', '')
    volume = request.POST.get('volume', '')
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
        contact_message = "Контактна особа: %s, почта: %s, номер телефона: %s, обєм вантажу: %s, фракція: %s, підприємство: %s, період доставки: %s, текстов повідомлення: %s"%(user_surname, email, phone, volume, select_fraction, enterprise, delivery_period, message)
    else:
        contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period)
    if user_surname and volume and email and phone and select_fraction and enterprise and delivery_period:
        try:
            send_mail(subject, contact_message, from_email, ['antonsadlov@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('../')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')


def send_email_3(request):
    user_surname = request.POST.get('user_surname', '')
    volume = request.POST.get('volume', '')
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
        contact_message = "Контактна особа: %s, почта: %s, номер телефона: %s, обєм вантажу: %s, фракція: %s, підприємство: %s, період доставки: %s, текстов повідомлення: %s"%(user_surname, email, phone, volume, select_fraction, enterprise, delivery_period, message)
    else:
        contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period)
    if user_surname and volume and email and phone and select_fraction and enterprise and delivery_period:
        try:
            send_mail(subject, contact_message, from_email, ['antonsadlov@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('../')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')




def send_email_2(request):
    user_surname = request.POST.get('user_surname', '')
    volume = request.POST.get('volume', '')
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
        contact_message = "Контактна особа: %s, почта: %s, номер телефона: %s, обєм вантажу: %s, фракція: %s, підприємство: %s, період доставки: %s, текстов повідомлення: %s"%(user_surname, email, phone, volume, select_fraction, enterprise, delivery_period, message)
    else:
        contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period)
    if user_surname and volume and email and phone and select_fraction and enterprise and delivery_period:
        try:
            send_mail(subject, contact_message, from_email, ['antonsadlov@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('../')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')







def send_email_1(request):
    user_surname = request.POST.get('user_surname', '')
    volume = request.POST.get('volume', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    select_fraction = request.POST.get('select_fraction', '')
    enterprise = request.POST.get('enterprise', '')
    delivery_period = request.POST.get('delivery_period', '')
    message = request.POST['message']
    # message = request.POST.get('message', '')

    subject = "Contact form(dla metalurgii ta vurobnukiv vapna)"
    from_email = settings.EMAIL_HOST_USER
    to_email = from_email
    if message:
        contact_message = "Контактна особа: %s, почта: %s, номер телефона: %s, обєм вантажу: %s, фракція: %s, підприємство: %s, період доставки: %s, текстов повідомлення: %s"%(user_surname, email, phone, volume, select_fraction, enterprise, delivery_period, message)
    else:
        contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period)
    if user_surname and volume and email and phone and select_fraction and enterprise and delivery_period:
        try:
            send_mail(subject, contact_message, from_email, ['antonsadlov@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('../')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')



def index(request):
	return render(request, 'production/wrapper.html')


def successView(request):
    return HttpResponse('Success! Thank you for your message.') 








def production_search_mobile(request):
    # if request.GET:
        seach_text = request.GET['text-field']
        seach_names_about = set(["про компанію", "Про компанію", "ПРО Компанію", "ПРО КОМПАНІЮ", "Про компанию", "про компанию", "Про Компанию", "ПРО КОМПАНИЮ", "about company", "About company", "About Company", "ABOUT company", "About COMPANY", "ABOUT COMPANY", "home"])

        seach_names_production = set(["продукція", "Продукція", "ПРОДУКЦІЯ", "Продукция", "продукция", "ПРОДУКЦИЯ", "production", "Production", "PRODUCTION"])
        
        seach_names_contact = set(["контакти", "Контакти", "КОНТАКТИ", "Контакты", "контакты", "КОНТАКТЫ", "contact", "Contact", "CONTACT"])

        seach_names_reviews = set(["відгуки", "Відгуки", "ВІДГУКИ", "Отзывы", "отзывы", "ОТЗЫВЫ", "reviews", "Reviews", "REVIEWS"])

        seach_names_services = set(["наші послуги", "Наші послуги", "НАШІ ПОСЛУГИ", "послуги", "Послуги", "ПОСЛУГИ", "Наши услуги", "наши услуги", "УСЛУГИ", "Услуги", "услуги", "НАШИ УСЛУГИ", "our services", "Our services", "OUR SERVICES", "services", "Services", "SERVICES"])


        if seach_text in seach_names_production:
            return HttpResponseRedirect("../production/")
        elif seach_text in seach_names_about:
            return HttpResponseRedirect("/")
        elif seach_text in seach_names_contact:
            return HttpResponseRedirect("../contact/")
        elif seach_text in seach_names_reviews:
            return HttpResponseRedirect("../reviews/")
        elif seach_text in seach_names_services:
            return HttpResponseRedirect("../services/")
        else:
            return render(request, 'error/wrapper.html')
