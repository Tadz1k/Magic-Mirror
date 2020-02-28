from tkcalendar import Calendar as T_cal
import tkinter.ttk as ttk
import tkinter as tk
from weather import Weather
from news import News
from tkinter import *
import threading
import time
from PIL import Image, ImageTk
import datetime
from cal import Calendar
import mail
import schedule
from sql_connection import Connection

print("Tworzę obiekty kanałów informacyjnych...")
# Obiekty kanałów informacyjnych
news = News()
weather = Weather()

print("Konfiguruję wygląd interfejsu...")
# Konfigurowanie okna głównego
root = tk.Tk()
root.tk.call('encoding', 'system', 'utf-8')
root.bind("<Escape>", exit)
#TRZY PONIŻEJ - FULLSCREEN
#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.overrideredirect(1)
#root.geometry("%dx%d+0+0" % (w, h))
print("Tworzę zmienne globalne...")
tk.Label(text="Magic Mirror").pack()
root.configure(background='black')
news_val = StringVar()
weather_val = StringVar()
hour_val = StringVar()
cal_val = StringVar()
hol_val = StringVar()
u_hol_val = StringVar()
day_val = StringVar()
mail_val = StringVar()
notes1_val = StringVar()
notes2_val = StringVar()
notes3_val = StringVar()

# Zmienne globalne
default_font = "Roboto 40"
info_font = "Roboto 11"
calendar_font = "Consolas"
holidays_font = "Roboto 10 italic"
holidays2_font = "Roboto 9"
actual_news = ['a', 'b', 'c']
news_counters = 0
weather_icon = ImageTk.PhotoImage(Image.open('icons/50d.png'))
handle_counter = 0

# Załadowanie wszystkich ikon do pamięci podręcznej
print("Wczytuję ikony do pamięci podręcznej...")
i_01d = ImageTk.PhotoImage(Image.open('icons/01d.png'))
i_01n = ImageTk.PhotoImage(Image.open('icons/01n.png'))
i_02d = ImageTk.PhotoImage(Image.open('icons/02d.png'))
i_02n = ImageTk.PhotoImage(Image.open('icons/02n.png'))
i_03d = ImageTk.PhotoImage(Image.open('icons/03d.png'))
i_03n = ImageTk.PhotoImage(Image.open('icons/03n.png'))
i_04d = ImageTk.PhotoImage(Image.open('icons/04d.png'))
i_04n = ImageTk.PhotoImage(Image.open('icons/04n.png'))
i_09d = ImageTk.PhotoImage(Image.open('icons/09d.png'))
i_09n = ImageTk.PhotoImage(Image.open('icons/09n.png'))
i_10d = ImageTk.PhotoImage(Image.open('icons/10d.png'))
i_10n = ImageTk.PhotoImage(Image.open('icons/10n.png'))
i_11d = ImageTk.PhotoImage(Image.open('icons/11d.png'))
i_11n = ImageTk.PhotoImage(Image.open('icons/11n.png'))
i_13d = ImageTk.PhotoImage(Image.open('icons/13d.png'))
i_13n = ImageTk.PhotoImage(Image.open('icons/13n.png'))
i_50d = ImageTk.PhotoImage(Image.open('icons/50d.png'))
i_50n = ImageTk.PhotoImage(Image.open('icons/50n.png'))
icons = {'01d': i_01d, '01n': i_01n, '02d': i_02d, '02n': i_02n, '03d': i_03d, '03n': i_03n, '04d': i_04d, '04n': i_04n,
         '09d': i_09d, '09n': i_09n, '10d': i_10d, '10n': i_10n, '11d': i_11d, '11n': i_11n, '13d': i_13d, '13n': i_13n,
         '50d': i_50d, '50n': i_50n}

print("Tworzę pola tekstowe...")
# Labels
info_label = tk.Label(root, textvariable=news_val, font=info_font, bg='black', fg='white').pack(side=BOTTOM, anchor=S)
hour_label = Label(root, textvariable=day_val, font=holidays2_font, bg='black', fg='white').pack()
day_label = Label(root, textvariable=hour_val, font=default_font, bg='black', fg='white').pack()
#holiday_label = Label(root, textvariable=hol_val, font=holidays_font, bg='black', fg='white', justify='left')\
    #.pack()
#u_holiday_label = Label(root, textvariable=u_hol_val, font=holidays2_font, bg='black', fg='white', justify='center')\
    #.pack()
u_mail_label = Label(root, textvariable=mail_val, font=holidays2_font, bg='black', fg='white', justify='center')\
    .pack()
weather_label = Label(root, textvariable=weather_val, font=info_font, bg='black', fg='white')
notes_label1 = tk.Label(root, textvariable=notes1_val, font=info_font, bg='black', fg='white')
notes_label2 = tk.Label(root, textvariable=notes2_val, font=info_font, bg='black', fg='white')
notes_label3 = tk.Label(root, textvariable=notes3_val, font=info_font, bg='black', fg='white')


def change_calendar():
    print("Pobieranie danych o świętach...")
    cal = Calendar()
    temp2 = ""
    holidays = cal.get_holidays()
    for k, v in holidays.items():
        temp2 = temp2 + "{} - {}\n".format(k, v)
    hol_val.set(temp2)
    u_hol_val.set(cal.get_unusual_day())
    day_val.set(cal.get_day())


def change_weather():
    print("Pobieranie danych pogodowych....")
    global weather_icon
    global icons
    global weather_icon
    # pobieram ikonę
    icon_name = weather.get_weather_info('icon')
    weather_icon = icons[icon_name]
    temperature = weather.get_weather_info('temperature')
    humidity = weather.get_weather_info('humidity')
    sunrise = weather.get_weather_info('sunrise')
    sunset = weather.get_weather_info('sunset')
    preasure = weather.get_weather_info('preasure')
    wind = weather.get_weather_info('wind')
    #weather_val.set("t: {}°C\n💧: {}%\n🌀: {} hPa\n💨: {}\n________________\n🌞: {}\n🌚: {}"
                    #.format(round(temperature['temp']), humidity, preasure['press'], wind, sunrise, sunset))
    weather_val.set("\uD83C\uDF21: {}°C\n\ud83d\udca7: {} %\n\ud83d\udcaa: {} hPa\n\ud83d\udca8: {}"
                    "\n________________\n\ud83c\udf1e: {}\n\ud83c\udf1b: {}"
                    .format(round(temperature['temp']), humidity, preasure['press'], wind, sunrise, sunset))
    weather_image = tk.Label(root, image=weather_icon, bg='black').pack()
    weather_label.pack()


def change_news():
    print("Zmiana newsów...")
    global news_counters
    global actual_news
    global info_label
    global news_val
    if news_counters < 18:
        actual_news = news.check_news(news_counters)
        news_counters = news_counters+3
        news_val.set(news_counters)

    elif news_counters == 18:
        news_counters = 0
    news_val.set("{}\n{}\n{}".format(actual_news[0].text, actual_news[1].text, actual_news[2].text))


def change_hour():
    now = datetime.datetime.now()
    temp = "{}:{}:{}".format(now.hour, now.minute, now.second)
    hour_val.set(temp)


def mail_interval():
    print("Pobieranie maili...")
    global mail_val
    mail_val.set(mail.get_mail())


def change_notes(action):
    time.sleep(2)
    print("Generowanie notatek...")
    conn = Connection()
    notes_list = conn.get_notes()
    notes1_val.set(notes_list[0][0])
    notes2_val.set(notes_list[0][1])
    notes3_val.set(notes_list[0][2])
    priority1 = notes_list[0][3]
    priority2 = notes_list[0][4]
    priority3 = notes_list[0][5]

    if action == 0:
        notes_label1.pack()
        notes_label2.pack()
        notes_label3.pack()
    if priority1 == 1:
        notes_label1.configure(fg='white')
    elif priority1 == 2:
        notes_label1.configure(fg='orange')
    elif priority1 == 3:
        notes_label1.configure(fg='red')

    if priority2 == 1:
        notes_label2.configure(fg='white')
    elif priority2 == 2:
        notes_label2.configure(fg='orange')
    elif priority2 == 3:
        notes_label2.configure(fg='red')

    if priority3 == 1:
        notes_label3.configure(fg='white')
    elif priority3 == 2:
        notes_label3.configure(fg='orange')
    elif priority3 == 3:
        notes_label3.configure(fg='red')

    if action == 1:
        print("ACTION 1")


def create_calendar():
    print("Tworzenie nowego kalendarza...")
    tk_cal = T_cal(root, selectmode='none', headersforeground='white', headersbackground='black',
                   normalbackground='black', normalforeground='white', disabledbackground='black',
                   disabledforeground='gray', weekendbackground='black', weekendforeground='gray',
                   othermonthbackground='black', othermonthforeground='gray',
                   othermonthwebackground='black', tooltipforeground='red', tooltipbackground='black',
                   tooltipalpha=float(1), borderwidth=0, showothermonthdays=False, locale='pl_PL',
                   selectbackground='gray')
    from cal import Calendar
    calendar = Calendar()
    for k, v in calendar.get_holidays().items():
        k = k + str(' 10:47:14.489795')
        date = datetime.datetime.strptime(k, '%Y-%m-%d %H:%M:%S.%f')
        if v[0] == '!':
            tk_cal.calevent_create(date, v, 'other')
        else:
            tk_cal.calevent_create(date, v, 'holidays')
    tk_cal.tag_config('holidays', background='red', foreground='white')
    tk_cal.tag_config('other', background='green', foreground='white')

    tk_cal.pack(fill="none", expand=False)
    ttk.Label(root, textvariable=u_hol_val, background='black', foreground='white', justify='center').pack()


def start_server():
    import http.server
    import socketserver
    port = 8080

    class GetHandler(http.server.SimpleHTTPRequestHandler):

        def do_GET(self):
            global handle_counter
            if self.headers.items()[2][1] == 'NOTES':
                change_notes(1)

    handler = GetHandler
    httpd = socketserver.TCPServer(("", port), handler)

    httpd.serve_forever()


def next_day():
    print("Generowanie danych na następny dzień.")
    change_calendar()
    create_calendar()


def sh():
    print("uruchomiono usługę CRON")
    while True:
        schedule.run_pending()
        time.sleep(1)

# cron
print("Ustalam polecenia CRON.")
schedule.every().day.at("00:00").do(next_day)
schedule.every(5).hours.do(change_weather)
schedule.every(600).seconds.do(change_news)
schedule.every(15).minutes.do(mail_interval)
schedule.every(1).seconds.do(change_hour)


#t1 = threading.Timer(1, change_news).start()    # wątek zmiany newsów
#t3 = threading.Timer(1, change_weather).start() # wątek zmiany pogody
#t4 = threading.Timer(1, interval).start()       #mail

print("Wywołuję pierwotne funkcje")
change_news()
change_weather()
change_calendar()
create_calendar()
change_notes(0)
mail_interval()
print("Uruchamiam dodatkowe wątki")
t2 = threading.Timer(1, change_hour).start() # wątek zmiany godziny
t5 = threading.Timer(1, start_server).start() #serwer http
CRON_THREAD = threading.Timer(1, sh).start()
root.mainloop()
while True:
    schedule.run_pending()
    time.sleep(1)


