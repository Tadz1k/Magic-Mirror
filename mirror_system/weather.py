class Weather:

    def get_weather_info(self, item):
        import pyowm
        import geocoder
        import socket
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        g = geocoder.ip(IPAddr)
        g = geocoder.ip('me')
        owm_api = pyowm.OWM('KLUCZ API@@@@@')
        city = owm_api.three_hours_forecast(g.city + ', PL')
        city2 = owm_api.weather_at_place(g.city + ', PL')
        weather = city2.get_weather()
        output = ""
        if item == 'icon':
            output = weather.get_weather_icon_name()
        elif item == 'temperature':
            output = weather.get_temperature('celsius')
        elif item == 'humidity':
            output = weather.get_humidity()
        elif item == 'sunrise':
            output = weather.get_sunrise_time(timeformat='iso')
        elif item == 'sunset':
            output = weather.get_sunset_time(timeformat='iso')
        elif item == 'preasure':
            output = weather.get_pressure()
        elif item == 'wind':
            wind = weather.get_wind()
            #deg = int(wind['deg'])
            deg = 0  #Prawdopodobnie nastąpiła jakaś zmiana w API
            speed = round(wind['speed'])
            direction = ""
            if 0 < deg <= 30:
                direction = "⬇️."
            elif 30 < deg <= 70:
                direction = "↘️."
            elif 70 < deg <= 110:
                direction = "➡️ ."
            elif 110 < deg <= 160:
                direction = "↗️ "
            elif 160 < deg <= 210:
                direction = "⬆️."
            elif 210 < deg <= 250:
                direction = "↖️ "
            elif 250 < deg <= 290:
                direction = "⬇️."
            elif 290 < deg <= 330:
                direction = "↘️"
            elif 330 < deg <= 360:
                direction = "⬇️"
            output = '{} km/h {}'.format(speed, direction)
        else:
            output = None

        return output