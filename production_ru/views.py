from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def send_email_4_ru(request):
    return HttpResponseRedirect('../')
    # user_surname = request.POST.get('user_surname', '')
    # volume = request.POST.get('volume', '')
    # email = request.POST.get('email', '')
    # phone = request.POST.get('phone', '')
    # select_fraction = request.POST.get('select_fraction', '')
    # enterprise = request.POST.get('enterprise', '')
    # delivery_period = request.POST.get('delivery_period', '')
    # message = request.POST['message']

    
    # if message:
    #     contact_message = "Контактна особа: %s, почта: %s, номер телефона: %s, обєм вантажу: %s, фракція: %s, підприємство: %s, період доставки: %s, текстов повідомлення: %s"%(user_surname, email, phone, volume, select_fraction, enterprise, delivery_period, message)
    # else:
    #     contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period)
    

    # from_addr = 'antonsadlov@ukr.net'
    # to_addr = 'antonsadlov@ukr.net'

    # username = 'antonsadlov@ukr.net'
    # password = 'antoha2003'

    # msg = MIMEMultipart()

    # msg['From'] = from_addr
    # msg['To'] = to_addr
    # msg['Subject'] = 'Contact form(dla kombikormov i pidkormku ptizu)'
    # msg.attach(MIMEText(contact_message))

    # try:
    #     server = smtplib.SMTP_SSL('smtp.ukr.net:2525')
    # except TimeoutError:
    #     return HttpResponseRedirect('/')

    # server.login(username,password)

    # if user_surname and volume and email and phone and select_fraction and enterprise and delivery_period:
    #     try:
    #         server.sendmail(from_addr,to_addr,msg.as_string())
    #     except BadHeaderError:
    #         return HttpResponse('Invalid header found.')
    #     server.quit()
    #     return HttpResponseRedirect('../')
    # else:
    #     return HttpResponse('Make sure all fields are entered and valid.')
    


def send_email_3_ru(request):
    return HttpResponseRedirect('../')
    # user_surname = request.POST.get('user_surname', '')
    # volume = request.POST.get('volume', '')
    # email = request.POST.get('email', '')
    # phone = request.POST.get('phone', '')
    # select_fraction = request.POST.get('select_fraction', '')
    # enterprise = request.POST.get('enterprise', '')
    # delivery_period = request.POST.get('delivery_period', '')
    # message = request.POST['message']

    
    # if message:
    #     contact_message = "Контактна особа: %s, почта: %s, номер телефона: %s, обєм вантажу: %s, фракція: %s, підприємство: %s, період доставки: %s, текстов повідомлення: %s"%(user_surname, email, phone, volume, select_fraction, enterprise, delivery_period, message)
    # else:
    #     contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period)
    

    # from_addr = 'antonsadlov@ukr.net'
    # to_addr = 'antonsadlov@ukr.net'

    # username = 'antonsadlov@ukr.net'
    # password = 'antoha2003'

    # msg = MIMEMultipart()

    # msg['From'] = from_addr
    # msg['To'] = to_addr
    # msg['Subject'] = 'Contact form(dla zukrovoi promuslovosti)'
    # msg.attach(MIMEText(contact_message))

    # try:
    #     server = smtplib.SMTP_SSL('smtp.ukr.net:2525')
    # except TimeoutError:
    #     return HttpResponseRedirect('/')

    # server.login(username,password)

    # if user_surname and volume and email and phone and select_fraction and enterprise and delivery_period:
    #     try:
    #         server.sendmail(from_addr,to_addr,msg.as_string())
    #     except BadHeaderError:
    #         return HttpResponse('Invalid header found.')
    #     server.quit()
    #     return HttpResponseRedirect('../')
    # else:
    #     return HttpResponse('Make sure all fields are entered and valid.')
    




def send_email_2_ru(request):
    return HttpResponseRedirect('../')
    # user_surname = request.POST.get('user_surname', '')
    # volume = request.POST.get('volume', '')
    # email = request.POST.get('email', '')
    # phone = request.POST.get('phone', '')
    # select_fraction = request.POST.get('select_fraction', '')
    # enterprise = request.POST.get('enterprise', '')
    # delivery_period = request.POST.get('delivery_period', '')
    # message = request.POST['message']

    
    # if message:
    #     contact_message = "Контактна особа: %s, почта: %s, номер телефона: %s, обєм вантажу: %s, фракція: %s, підприємство: %s, період доставки: %s, текстов повідомлення: %s"%(user_surname, email, phone, volume, select_fraction, enterprise, delivery_period, message)
    # else:
    #     contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period)
    

    # from_addr = 'antonsadlov@ukr.net'
    # to_addr = 'antonsadlov@ukr.net'

    # username = 'antonsadlov@ukr.net'
    # password = 'antoha2003'

    # msg = MIMEMultipart()

    # msg['From'] = from_addr
    # msg['To'] = to_addr
    # msg['Subject'] = 'Contact form(dla rozkusnenya gruntu i vodoyom)'
    # msg.attach(MIMEText(contact_message))

    # try:
    #     server = smtplib.SMTP_SSL('smtp.ukr.net:2525')
    # except TimeoutError:
    #     return HttpResponseRedirect('/')

    # server.login(username,password)

    # if user_surname and volume and email and phone and select_fraction and enterprise and delivery_period:
    #     try:
    #         server.sendmail(from_addr,to_addr,msg.as_string())
    #     except BadHeaderError:
    #         return HttpResponse('Invalid header found.')
    #     server.quit()
    #     return HttpResponseRedirect('../')
    # else:
    #     return HttpResponse('Make sure all fields are entered and valid.')

    







def send_email_1_ru(request):
    return HttpResponseRedirect('../')
    # user_surname = request.POST.get('user_surname', '')
    # volume = request.POST.get('volume', '')
    # email = request.POST.get('email', '')
    # phone = request.POST.get('phone', '')
    # select_fraction = request.POST.get('select_fraction', '')
    # enterprise = request.POST.get('enterprise', '')
    # delivery_period = request.POST.get('delivery_period', '')
    # message = request.POST['message']

    
    # if message:
    #     contact_message = "Контактна особа: %s, почта: %s, номер телефона: %s, обєм вантажу: %s, фракція: %s, підприємство: %s, період доставки: %s, текстов повідомлення: %s"%(user_surname, email, phone, volume, select_fraction, enterprise, delivery_period, message)
    # else:
    #     contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period)
    

    # from_addr = 'antonsadlov@ukr.net'
    # to_addr = 'antonsadlov@ukr.net'

    # username = 'antonsadlov@ukr.net'
    # password = 'antoha2003'

    # msg = MIMEMultipart()

    # msg['From'] = from_addr
    # msg['To'] = to_addr
    # msg['Subject'] = 'Contact form(dla metalurgii ta vurobnukiv vapna)'
    # msg.attach(MIMEText(contact_message))

    # try:
    #     server = smtplib.SMTP_SSL('smtp.ukr.net:2525')
    # except TimeoutError:
    #     return HttpResponseRedirect('/')

    # server.login(username,password)

    # if user_surname and volume and email and phone and select_fraction and enterprise and delivery_period:
    #     try:
    #         server.sendmail(from_addr,to_addr,msg.as_string())
    #     except BadHeaderError:
    #         return HttpResponse('Invalid header found.')
    #     server.quit()
    #     return HttpResponseRedirect('../')
    # else:
    #     return HttpResponse('Make sure all fields are entered and valid.')



def index(request):
	return render(request, 'production_ru/wrapper.html')


def successView(request):
    return HttpResponse('Success! Thank you for your message.') 



def production_ru_search_mobile(request):
    # if request.GET:
        seach_text = request.GET['text-field']
        seach_names_about = set(["про компанію", "Про компанію", "ПРО Компанію", "ПРО КОМПАНІЮ", "Про компанию", "про компанию", "Про Компанию", "ПРО КОМПАНИЮ", "about company", "About company", "About Company", "ABOUT company", "About COMPANY", "ABOUT COMPANY", "home"])

        seach_names_production = set(["продукція", "Продукція", "ПРОДУКЦІЯ", "Продукция", "продукция", "ПРОДУКЦИЯ", "production", "Production", "PRODUCTION"])
        
        seach_names_contact = set(["контакти", "Контакти", "КОНТАКТИ", "Контакты", "контакты", "КОНТАКТЫ", "contact", "Contact", "CONTACT"])

        seach_names_reviews = set(["відгуки", "Відгуки", "ВІДГУКИ", "Отзывы", "отзывы", "ОТЗЫВЫ", "reviews", "Reviews", "REVIEWS"])

        seach_names_services = set(["наші послуги", "Наші послуги", "НАШІ ПОСЛУГИ", "послуги", "Послуги", "ПОСЛУГИ", "Наши услуги", "наши услуги", "УСЛУГИ", "Услуги", "услуги", "НАШИ УСЛУГИ", "our services", "Our services", "OUR SERVICES", "services", "Services", "SERVICES"])


        if seach_text in seach_names_production:
            return HttpResponseRedirect("../../../ru/production/")
        elif seach_text in seach_names_about:
            return HttpResponseRedirect("../../../ru/")
        elif seach_text in seach_names_contact:
            return HttpResponseRedirect("../../../ru/contact/")
        elif seach_text in seach_names_reviews:
            return HttpResponseRedirect("../../../ru/reviews/")
        elif seach_text in seach_names_services:
            return HttpResponseRedirect("../../../ru/services/")
        else:
            return render(request, 'error_ru/wrapper.html')