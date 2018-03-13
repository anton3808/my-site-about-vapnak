from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect



import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.
from django.core.mail import EmailMessage



def send(request):
    # return HttpResponseRedirect('../')
    contact_person = request.POST.get('contact_person', '')
    phone = request.POST.get('phone', '')
    cargo = request.POST.get('cargo', '')
    cod_cargo_railway = request.POST.get('cod_cargo_railway', '')
    load_station = request.POST.get('load_station', '')
    cod_load_station = request.POST.get('cod_load_station', '')
    unloading_station = request.POST.get('unloading_station', '')
    cod_unloading_station = request.POST['cod_unloading_station']



    contact_message = "Контактна особа: %s, номер телефона: %s, вантаж: %s, код вантажу по залізниці: %s, станція навантаження: %s, код станції навантаження: %s, станція вивантаження: %s, код станція вивантаження: %s"%(contact_person, phone, cargo, cod_cargo_railway, load_station, cod_load_station, unloading_station, cod_unloading_station)
    

    from_addr = 'tpk_triumph@ukr.net'
    to_addr = 'tpk_triumph@ukr.net'

    username = 'tpk_triumph@ukr.net'
    password = 'Sad_!123'

    msg = MIMEMultipart()

    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Organization of cargo transportation'
    msg.attach(MIMEText(contact_message))

    try:
        server = smtplib.SMTP_SSL('smtp.ukr.net:2525')
    except TimeoutError:
        return HttpResponseRedirect('/')


    server.login(username,password)

    if contact_person and phone and cargo and cod_cargo_railway and load_station and cod_load_station and unloading_station and cod_unloading_station:       
        try:
            server.sendmail(from_addr,to_addr,msg.as_string())
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        server.quit()
        return HttpResponseRedirect('../')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')









def index(request):
	return render(request, 'services/wrapper.html')



def services_search_mobile(request):
        seach_text = request.GET['text-field']
        seach_names_about = set(["про компанію", "Про компанію", "ПРО Компанію", "ПРО КОМПАНІЮ", "Про компанию", "про компанию", "Про Компанию", "ПРО КОМПАНИЮ", "about company", "About company", "About Company", "ABOUT company", "About COMPANY", "ABOUT COMPANY", "home"])

        seach_names_production = set(["продукція", "Продукція", "ПРОДУКЦІЯ", "Продукция", "продукция", "ПРОДУКЦИЯ", "production", "Production", "PRODUCTION"])
        
        seach_names_contact = set(["контакти", "Контакти", "КОНТАКТИ", "Контакты", "контакты", "КОНТАКТЫ", "contact", "Contact", "CONTACT"])

        seach_names_reviews = set(["відгуки", "Відгуки", "ВІДГУКИ", "Отзывы", "отзывы", "ОТЗЫВЫ", "reviews", "Reviews", "REVIEWS"])

        seach_names_services = set(["наші послуги", "Наші послуги", "НАШІ ПОСЛУГИ", "послуги", "Послуги", "ПОСЛУГИ", "Наши услуги", "наши услуги", "УСЛУГИ", "Услуги", "услуги", "НАШИ УСЛУГИ", "our services", "Our services", "OUR SERVICES", "services", "Services", "SERVICES"])


        if seach_text in seach_names_production:
            return HttpResponseRedirect("../../production/")
        elif seach_text in seach_names_about:
            return HttpResponseRedirect("../../")
        elif seach_text in seach_names_contact:
            return HttpResponseRedirect("../../contact/")
        elif seach_text in seach_names_reviews:
            return HttpResponseRedirect("../../reviews/")
        elif seach_text in seach_names_services:
            return HttpResponseRedirect("../../services/")
        else:
            return render(request, 'error/wrapper.html')








