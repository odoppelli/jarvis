from datetime import datetime, timedelta

import pytz
from pyowm import OWM
from pytz import timezone

API_key = '0aae76c69be7475fdd85253f2bf60ddf'


def round_num_totwo(number):
    rest = number % 0.01
    rounded_number = number - rest
    return rounded_number


def timestamp_to_localtime(timestamp):
    utc = pytz.utc
    aachen_timezone = timezone('Europe/Berlin')
    fmt = '%H:%M'
    utc_dt_rain = utc.localize(datetime.utcfromtimestamp(timestamp))
    local_time = utc_dt_rain.astimezone(aachen_timezone)
    local_time = local_time.strftime(fmt)
    return local_time


def timestamp_to_localtime_v2(timestamp):
    utc = pytz.utc
    aachen_timezone = timezone('Europe/Berlin')
    fmt = '%d.%m. %H:%M'
    utc_dt_rain = utc.localize(datetime.utcfromtimestamp(timestamp))
    local_time = utc_dt_rain.astimezone(aachen_timezone)
    local_time = local_time.strftime(fmt)
    return local_time


def wind_analysieren(wind):
    deg_available = True
    gust_available = True
    if 'deg' not in wind:
        wind_richtung = 666
        deg_available = False
    else:
        wind_richtung = wind.get('deg')

    if 'gust' not in wind:
        gust_available = False
    else:
        wind_boe_kmh = wind.get('gust') * 3.6
        wind_boe_kmh = round_num_totwo(wind_boe_kmh)

    wind_kmh = wind.get('speed') * 3.6
    wind_kmh = round_num_totwo(wind_kmh)

    if (337.5 < wind_richtung <= 360) or (1 <= wind_richtung < 22.5):
        wind_richtung = 'N'
    elif 22.5 < wind_richtung < 67.5:
        wind_richtung = 'NO'
    elif 67.5 < wind_richtung < 112.5:
        wind_richtung = 'O'
    elif 112.5 < wind_richtung < 157.5:
        wind_richtung = 'SO'
    elif 157.5 < wind_richtung < 202.5:
        wind_richtung = 'S'
    elif 202.5 < wind_richtung < 247.5:
        wind_richtung = 'SW'
    elif 247.5 < wind_richtung < 292.5:
        wind_richtung = 'W'
    elif 292.5 < wind_richtung < 337.5:
        wind_richtung = 'NW'
    else:
        wind_richtung = 'error'

    wind['speed'] = wind_kmh
    wind['direction'] = wind_richtung
    if deg_available:
        wind.pop('deg')
    if gust_available:
        wind['gust'] = wind_boe_kmh
    return wind


def current_weather(city_id=6553047):
    # Search for current weather in city(country)
    # Aachen : 3247449
    owm = OWM(API_key)
    observation = owm.weather_at_id(city_id)
    w = observation.get_weather()
    # print(w)

    weather = {}
    # WEATHER DETAILS
    wind = w.get_wind()
    print('wind:',wind)
    # humidity = w.get_humidity()
    temperature = w.get_temperature('celsius')
    clouds = w.get_clouds()
    rain = w.get_rain()
    # pressure = w.get_pressure()
    snow = w.get_snow()
    detailed_weather_status = w.get_detailed_status()
    # weather_status = w.get_status()
    '''
    sunset = w.get_sunset_time()
    ts_sunset = int(sunset)
    sunset = datetime.utcfromtimestamp(ts_sunset).strftime('%Y-%m-%d %H:%M:%S')
    sunrise = w.get_sunrise_time()
    ts_sunrise = int(sunrise)
    sunrise = datetime.utcfromtimestamp(ts_sunrise).strftime('%Y-%m-%d %H:%M:%S')
    '''
    # WIND analysieren
    wind = wind_analysieren(wind)

    # daten einspeichern
    # weather['status'] = weather_status
    weather['detailed_status'] = detailed_weather_status
    weather['temperature'] = temperature.get('temp')
    # weather['humidity'] = humidity
    # weather['pressure'] = pressure.get('press')
    weather['wind'] = wind
    weather['clouds'] = clouds
    weather['rain'] = rain
    weather['snow'] = snow
    # weather['sunrise'] = sunrise
    # weather['sunset'] = sunset

    return weather


def x_hours_weather(hours, city_id=6553047):
    speicher = {}
    # timezones
    # Search for current weather in city(country)
    # Aachen : 3247449
    owm = OWM(API_key)
    fc = owm.three_hours_forecast_at_id(city_id)
    f = fc.get_forecast()
    fc_lst = f.get_weathers()
    # kommende 21h analysieren
    fc_lst = fc_lst[:(hours // 3)]

    # maximale und minimale Temperatur mit Zeitangabe
    max_temp = {}
    min_temp = {}
    max_temperature = fc_lst[0].get_temperature('celsius')['temp']
    min_temperature = fc_lst[0].get_temperature('celsius')['temp']
    max_temp_time = fc_lst[0].get_reference_time()
    min_temp_time = fc_lst[0].get_reference_time()
    for fc_weather in fc_lst:
        temperature = fc_weather.get_temperature('celsius')['temp']
        timestamp = fc_weather.get_reference_time()
        if temperature > max_temperature:
            max_temperature = temperature
            max_temp_time = timestamp
        elif temperature < min_temperature:
            min_temperature = temperature
            min_temp_time = timestamp

    min_aachen_time = timestamp_to_localtime(min_temp_time)
    max_aachen_time = timestamp_to_localtime(max_temp_time)

    max_temp['temp'] = max_temperature
    max_temp['time'] = max_aachen_time
    min_temp['temp'] = min_temperature
    min_temp['time'] = min_aachen_time

    # Temperaturen --> SPEICHER
    speicher['max_temp'] = max_temp
    speicher['min_temp'] = min_temp

    # Regen analysieren
    rain_all = {}
    rain_time = []
    rain_summ = 0
    for fc_weather in fc_lst:
        fc_rain = fc_weather.get_rain()
        if len(fc_rain) != 0:
            timestamp = fc_weather.get_reference_time()
            local_time = timestamp_to_localtime(timestamp)
            rain_time.append(local_time)
            rain_summ += fc_rain.get('3h')
            rain_all[local_time] = fc_rain.get('3h')
    # print('\nraining time: ', rain_time, '\nrain summ: ', rain_summ)

    # Regen --> SPEICHER
    speicher['rain_all'] = rain_all
    speicher['rain_time'] = rain_time
    speicher['rain_summ'] = rain_summ

    # return SPEICHER
    return speicher
    # SPEICHER untersuchen
    # for key, value in speicher.items():
    # print(key, ':', value)


def wind_six_hours(city_id=6553047):
    # WIND analyisieren (6h)
    speicher = {}
    owm = OWM(API_key)
    fc = owm.three_hours_forecast_at_id(city_id)
    # f = fc.get_forecast()
    # fc_lst = f.get_weathers()
    time_six_hours = datetime.now() + timedelta(hours=6)
    weather_six_hours = fc.get_weather_at(time_six_hours)
    wind_six_hours = weather_six_hours.get_wind()
    wind_six_hours = wind_analysieren(wind_six_hours)
    time_six_hours = weather_six_hours.get_reference_time()
    time_six_hours = timestamp_to_localtime(time_six_hours)

    # WIND (6h) --> SPEICHER
    speicher['wind_six_hours'] = wind_six_hours
    speicher['time_six_hours'] = time_six_hours
    speicher['detailed_status'] = weather_six_hours.get_detailed_status()
    return speicher

    # DETAILED STATUS (6h)
    detailed_status_six_hours = weather_six_hours.get_detailed_status()

    # DETAILED STATUS (6h) --> SPEICHER
    speicher['detailed_status_six_hours'] = detailed_status_six_hours


def uvi_three_days(city_id=6553047):
    days = []
    owm = OWM(API_key)
    obs = owm.weather_at_id(city_id)
    l = obs.get_location()
    lon_aachen = l.get_lon()
    lat_aachen = l.get_lat()

    uvi_fc = owm.uvindex_forecast_around_coords(lat_aachen, lon_aachen)
    uvi_fc = uvi_fc[:3]
    for uvi in uvi_fc:
        value = uvi.get_value()
        reference_time = uvi.get_reference_time()
        exposure_risk = uvi.get_exposure_risk()
        reference_time = timestamp_to_localtime_v2(reference_time)

        uvi_day_dict = {
            'reference_time': reference_time,
            'value': value,
            'exposure_risk': exposure_risk
        }
        days.append(uvi_day_dict)
    return days


# Requests
aachen = current_weather(6553047)
print('\ncurrent Weather:')
for x, y in aachen.items():
    print(x, ':', y)

print('\nweather forecast (next 6h):')
next_six_hours = x_hours_weather(6)
for x, y in next_six_hours.items():
    print(x, ':', y)

print('\nweather forecast (next 21h):')
next_twentyone_hours = x_hours_weather(21)
for x, y in next_twentyone_hours.items():
    print(x, ':', y)

print('\nwind & weather in 6 hours:')
wind_six_hours = wind_six_hours()
for x, y in wind_six_hours.items():
    print(x, ':', y)

print('\nUV Index forecast (next 3d):')
uvi = uvi_three_days()
for day in uvi:
    for x, y in day.items():
        print(x, ':', y)
    print()

'''
{
    "id": 3247449,
    "name": "Aachen",
    "state": "",
    "country": "DE",
    "coord": {
      "lon": 6.08342,
      "lat": 50.776642
    }
'''
