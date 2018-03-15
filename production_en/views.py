from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def send_email_4(request):
    # return HttpResponseRedirect('../')
    user_surname = request.POST.get('user_surname', '')
    volume = request.POST.get('volume', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    select_fraction = request.POST.get('select_fraction', '')
    enterprise = request.POST.get('enterprise', '')
    delivery_period_1 = request.POST.get('delivery_period_1', '')
    delivery_period_2 = request.POST.get('delivery_period_2', '')
    message = request.POST['message']



    if select_fraction == "1":
        select_fraction = "0-5 мм"
    elif select_fraction == "2":
        select_fraction = "0-20 мм"
    elif select_fraction == "3":
        select_fraction = "20-40 мм"
    elif select_fraction == "4":
        select_fraction = "40-80 мм"
    elif select_fraction == "5":
        select_fraction = "80-120мм"




    if delivery_period_1 == "1":
        delivery_period_1 = "січеня"
    elif delivery_period_1 == "2":
        delivery_period_1 = "лютого"
    elif delivery_period_1 == "3":
        delivery_period_1 = "березня"
    elif delivery_period_1 == "4":
        delivery_period_1 = "квітня"
    elif delivery_period_1 == "5":
        delivery_period_1 = "травня"
    elif delivery_period_1 == "6":
        delivery_period_1 = "червня"
    elif delivery_period_1 == "7":
        delivery_period_1 = "липня"
    elif delivery_period_1 == "8":
        delivery_period_1 = "серпня"
    elif delivery_period_1 == "9":
        delivery_period_1 = "вересня"
    elif delivery_period_1 == "10":
        delivery_period_1 = "жовтня"
    elif delivery_period_1 == "11":
        delivery_period_1 = "листопада"
    elif delivery_period_1 == "12":
        delivery_period_1 = "грудня"





    if delivery_period_2 == "1":
        delivery_period_2 = "січень"
    elif delivery_period_2 == "2":
        delivery_period_2 = "лютий"
    elif delivery_period_2 == "3":
        delivery_period_2 = "березень"
    elif delivery_period_2 == "4":
        delivery_period_2 = "квітень"
    elif delivery_period_2 == "5":
        delivery_period_2 = "травень"
    elif delivery_period_2 == "6":
        delivery_period_2 = "червень"
    elif delivery_period_2 == "7":
        delivery_period_2 = "липень"
    elif delivery_period_2 == "8":
        delivery_period_2 = "серпень"
    elif delivery_period_2 == "9":
        delivery_period_2 = "вересень"
    elif delivery_period_2 == "10":
        delivery_period_2 = "жовтень"
    elif delivery_period_2 == "11":
        delivery_period_2 = "листопад"
    elif delivery_period_2 == "12":
        delivery_period_2 = "грудень"

    
    if message:
        contact_message = "Контактна особа: %s, почта: %s, номер телефона: %s, обєм вантажу: %s, фракція: %s, підприємство: %s, період доставки: з %s по %s, текстов повідомлення: %s"%(user_surname, email, phone, volume, select_fraction, enterprise, delivery_period_1, delivery_period_2, message)
    else:
        contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: з %s по %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period_1, delivery_period_2)
    

    # from_addr = 'tpk_triumph@ukr.net'
    # to_addr = 'tpk_triumph@ukr.net'

    # username = 'tpk_triumph@ukr.net'
    # password = 'Sad_!123'


    from_addr = 'antonsadlov@ukr.net'
    to_addr = 'antonsadlov@ukr.net'

    username = 'antonsadlov@ukr.net'
    password = 'antoha2003'
    
    msg = MIMEMultipart()

    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Contact form(dla kombikormov i pidkormku ptizu)'
    msg.attach(MIMEText(contact_message))

    try:
        server = smtplib.SMTP_SSL('smtp.ukr.net:2525')
    except TimeoutError:
        return HttpResponseRedirect('/')

    server.login(username,password)

    if user_surname and volume and email and phone and select_fraction and enterprise and delivery_period_1 and delivery_period_2:
        try:
            server.sendmail(from_addr,to_addr,msg.as_string())
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        server.quit()
        return HttpResponseRedirect('../')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')
    


def send_email_3(request):
    # return HttpResponseRedirect('../')
    user_surname = request.POST.get('user_surname', '')
    volume = request.POST.get('volume', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    select_fraction = request.POST.get('select_fraction', '')
    enterprise = request.POST.get('enterprise', '')
    delivery_period_1 = request.POST.get('delivery_period_1', '')
    delivery_period_2 = request.POST.get('delivery_period_2', '')
    message = request.POST['message']



    if select_fraction == "1":
        select_fraction = "40-80 мм"
    elif select_fraction == "2":
        select_fraction = "80-120мм"




    if delivery_period_1 == "1":
        delivery_period_1 = "січеня"
    elif delivery_period_1 == "2":
        delivery_period_1 = "лютого"
    elif delivery_period_1 == "3":
        delivery_period_1 = "березня"
    elif delivery_period_1 == "4":
        delivery_period_1 = "квітня"
    elif delivery_period_1 == "5":
        delivery_period_1 = "травня"
    elif delivery_period_1 == "6":
        delivery_period_1 = "червня"
    elif delivery_period_1 == "7":
        delivery_period_1 = "липня"
    elif delivery_period_1 == "8":
        delivery_period_1 = "серпня"
    elif delivery_period_1 == "9":
        delivery_period_1 = "вересня"
    elif delivery_period_1 == "10":
        delivery_period_1 = "жовтня"
    elif delivery_period_1 == "11":
        delivery_period_1 = "листопада"
    elif delivery_period_1 == "12":
        delivery_period_1 = "грудня"





    if delivery_period_2 == "1":
        delivery_period_2 = "січень"
    elif delivery_period_2 == "2":
        delivery_period_2 = "лютий"
    elif delivery_period_2 == "3":
        delivery_period_2 = "березень"
    elif delivery_period_2 == "4":
        delivery_period_2 = "квітень"
    elif delivery_period_2 == "5":
        delivery_period_2 = "травень"
    elif delivery_period_2 == "6":
        delivery_period_2 = "червень"
    elif delivery_period_2 == "7":
        delivery_period_2 = "липень"
    elif delivery_period_2 == "8":
        delivery_period_2 = "серпень"
    elif delivery_period_2 == "9":
        delivery_period_2 = "вересень"
    elif delivery_period_2 == "10":
        delivery_period_2 = "жовтень"
    elif delivery_period_2 == "11":
        delivery_period_2 = "листопад"
    elif delivery_period_2 == "12":
        delivery_period_2 = "грудень"

    
    if message:
        contact_message = "Контактна особа: %s, почта: %s, номер телефона: %s, обєм вантажу: %s, фракція: %s, підприємство: %s, період доставки: з %s по %s, текстов повідомлення: %s"%(user_surname, email, phone, volume, select_fraction, enterprise, delivery_period_1, delivery_period_2, message)
    else:
        contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: з %s по %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period_1, delivery_period_2)
    

    # from_addr = 'tpk_triumph@ukr.net'
    # to_addr = 'tpk_triumph@ukr.net'

    # username = 'tpk_triumph@ukr.net'
    # password = 'Sad_!123'


    from_addr = 'antonsadlov@ukr.net'
    to_addr = 'antonsadlov@ukr.net'

    username = 'antonsadlov@ukr.net'
    password = 'antoha2003'

    msg = MIMEMultipart()

    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Contact form(dla zukrovoi promuslovosti)'
    msg.attach(MIMEText(contact_message))

    try:
        server = smtplib.SMTP_SSL('smtp.ukr.net:2525')
    except TimeoutError:
        return HttpResponseRedirect('/')

    server.login(username,password)

    if user_surname and volume and email and phone and select_fraction and enterprise and delivery_period_1 and delivery_period_2:
        try:
            server.sendmail(from_addr,to_addr,msg.as_string())
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        server.quit()
        return HttpResponseRedirect('../')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')
    




def send_email_2(request):
    # return HttpResponseRedirect('../')
    user_surname = request.POST.get('user_surname', '')
    volume = request.POST.get('volume', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    select_fraction = request.POST.get('select_fraction', '')
    enterprise = request.POST.get('enterprise', '')
    delivery_period_1 = request.POST.get('delivery_period_1', '')
    delivery_period_2 = request.POST.get('delivery_period_2', '')
    message = request.POST['message']



    if select_fraction == "1":
        select_fraction = "0-1 мм"
    elif select_fraction == "2":
        select_fraction = "0-5 мм"
    elif select_fraction == "3":
        select_fraction = "0-20 мм"
    elif select_fraction == "4":
        select_fraction = "20-40 мм"




    if delivery_period_1 == "1":
        delivery_period_1 = "січеня"
    elif delivery_period_1 == "2":
        delivery_period_1 = "лютого"
    elif delivery_period_1 == "3":
        delivery_period_1 = "березня"
    elif delivery_period_1 == "4":
        delivery_period_1 = "квітня"
    elif delivery_period_1 == "5":
        delivery_period_1 = "травня"
    elif delivery_period_1 == "6":
        delivery_period_1 = "червня"
    elif delivery_period_1 == "7":
        delivery_period_1 = "липня"
    elif delivery_period_1 == "8":
        delivery_period_1 = "серпня"
    elif delivery_period_1 == "9":
        delivery_period_1 = "вересня"
    elif delivery_period_1 == "10":
        delivery_period_1 = "жовтня"
    elif delivery_period_1 == "11":
        delivery_period_1 = "листопада"
    elif delivery_period_1 == "12":
        delivery_period_1 = "грудня"





    if delivery_period_2 == "1":
        delivery_period_2 = "січень"
    elif delivery_period_2 == "2":
        delivery_period_2 = "лютий"
    elif delivery_period_2 == "3":
        delivery_period_2 = "березень"
    elif delivery_period_2 == "4":
        delivery_period_2 = "квітень"
    elif delivery_period_2 == "5":
        delivery_period_2 = "травень"
    elif delivery_period_2 == "6":
        delivery_period_2 = "червень"
    elif delivery_period_2 == "7":
        delivery_period_2 = "липень"
    elif delivery_period_2 == "8":
        delivery_period_2 = "серпень"
    elif delivery_period_2 == "9":
        delivery_period_2 = "вересень"
    elif delivery_period_2 == "10":
        delivery_period_2 = "жовтень"
    elif delivery_period_2 == "11":
        delivery_period_2 = "листопад"
    elif delivery_period_2 == "12":
        delivery_period_2 = "грудень"

    
    if message:
        contact_message = "Контактна особа: %s, почта: %s, номер телефона: %s, обєм вантажу: %s, фракція: %s, підприємство: %s, період доставки: з %s по %s, текстов повідомлення: %s"%(user_surname, email, phone, volume, select_fraction, enterprise, delivery_period_1, delivery_period_2, message)
    else:
        contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: з %s по %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period_1, delivery_period_2)
    

    # from_addr = 'tpk_triumph@ukr.net'
    # to_addr = 'tpk_triumph@ukr.net'

    # username = 'tpk_triumph@ukr.net'
    # password = 'Sad_!123'


    from_addr = 'antonsadlov@ukr.net'
    to_addr = 'antonsadlov@ukr.net'

    username = 'antonsadlov@ukr.net'
    password = 'antoha2003'

    msg = MIMEMultipart()

    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Contact form(dla rozkusnenya gruntu i vodoyom)'
    msg.attach(MIMEText(contact_message))

    try:
        server = smtplib.SMTP_SSL('smtp.ukr.net:2525')
    except TimeoutError:
        return HttpResponseRedirect('/')

    server.login(username,password)

    if user_surname and volume and email and phone and select_fraction and enterprise and delivery_period_1 and delivery_period_2:
        try:
            server.sendmail(from_addr,to_addr,msg.as_string())
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        server.quit()
        return HttpResponseRedirect('../')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')

    







def send_email_1(request):
    # return HttpResponseRedirect('../')
    user_surname = request.POST.get('user_surname', '')
    volume = request.POST.get('volume', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    select_fraction = request.POST.get('select_fraction', '')
    enterprise = request.POST.get('enterprise', '')
    delivery_period_1 = request.POST.get('delivery_period_1', '')
    delivery_period_2 = request.POST.get('delivery_period_2', '')
    message = request.POST['message']



    if select_fraction == "1":
        select_fraction = "0-5 мм"
    elif select_fraction == "2":
        select_fraction = "0-20 мм"
    elif select_fraction == "3":
        select_fraction = "20-40 мм"
    elif select_fraction == "4":
        select_fraction = "40-80 мм"
    elif select_fraction == "5":
        select_fraction = "80-120мм"




    if delivery_period_1 == "1":
        delivery_period_1 = "січеня"
    elif delivery_period_1 == "2":
        delivery_period_1 = "лютого"
    elif delivery_period_1 == "3":
        delivery_period_1 = "березня"
    elif delivery_period_1 == "4":
        delivery_period_1 = "квітня"
    elif delivery_period_1 == "5":
        delivery_period_1 = "травня"
    elif delivery_period_1 == "6":
        delivery_period_1 = "червня"
    elif delivery_period_1 == "7":
        delivery_period_1 = "липня"
    elif delivery_period_1 == "8":
        delivery_period_1 = "серпня"
    elif delivery_period_1 == "9":
        delivery_period_1 = "вересня"
    elif delivery_period_1 == "10":
        delivery_period_1 = "жовтня"
    elif delivery_period_1 == "11":
        delivery_period_1 = "листопада"
    elif delivery_period_1 == "12":
        delivery_period_1 = "грудня"





    if delivery_period_2 == "1":
        delivery_period_2 = "січень"
    elif delivery_period_2 == "2":
        delivery_period_2 = "лютий"
    elif delivery_period_2 == "3":
        delivery_period_2 = "березень"
    elif delivery_period_2 == "4":
        delivery_period_2 = "квітень"
    elif delivery_period_2 == "5":
        delivery_period_2 = "травень"
    elif delivery_period_2 == "6":
        delivery_period_2 = "червень"
    elif delivery_period_2 == "7":
        delivery_period_2 = "липень"
    elif delivery_period_2 == "8":
        delivery_period_2 = "серпень"
    elif delivery_period_2 == "9":
        delivery_period_2 = "вересень"
    elif delivery_period_2 == "10":
        delivery_period_2 = "жовтень"
    elif delivery_period_2 == "11":
        delivery_period_2 = "листопад"
    elif delivery_period_2 == "12":
        delivery_period_2 = "грудень"

    
    if message:
        contact_message = "Контактна особа: %s, почта: %s, номер телефона: %s, обєм вантажу: %s, фракція: %s, підприємство: %s, період доставки: з %s по %s, текстов повідомлення: %s"%(user_surname, email, phone, volume, select_fraction, enterprise, delivery_period_1, delivery_period_2, message)
    else:
        contact_message = "Фамілія: %s, імя: %s, почта: %s, номер телефона: %s, фракція: %s, підприємство: %s, період доставки: з %s по %s"%(user_surname, user_name, email, phone, select_fraction, enterprise, delivery_period_1, delivery_period_2)
    

    # from_addr = 'tpk_triumph@ukr.net'
    # to_addr = 'tpk_triumph@ukr.net'

    # username = 'tpk_triumph@ukr.net'
    # password = 'Sad_!123'


    from_addr = 'antonsadlov@ukr.net'
    to_addr = 'antonsadlov@ukr.net'

    username = 'antonsadlov@ukr.net'
    password = 'antoha2003'

    msg = MIMEMultipart()

    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Contact form(dla metalurgii ta vurobnukiv vapna)'
    msg.attach(MIMEText(contact_message))

    try:
        server = smtplib.SMTP_SSL('smtp.ukr.net:2525')
    except TimeoutError:
        return HttpResponseRedirect('/')

    server.login(username,password)

    if user_surname and volume and email and phone and select_fraction and enterprise and delivery_period_1 and delivery_period_2:
        try:
            server.sendmail(from_addr,to_addr,msg.as_string())
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        server.quit()
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