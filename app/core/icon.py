import os
from PIL import Image

assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets')
icons_dir = os.path.join(assets_dir, 'icons')

class BoxImages:
    main_info_box = Image.open(os.path.join(icons_dir, 'main_info_box.png'))
    sub_info_box = Image.open(os.path.join(icons_dir, 'sub_info_box.png'))
    hour_info_box = Image.open(os.path.join(icons_dir, 'hour_info_box.png'))
    day_info_box = Image.open(os.path.join(icons_dir, 'day_info_box.png'))

class SubInfoIcons:
    sunrise = Image.open(os.path.join(icons_dir, 'sunrise.png'))
    sunset = Image.open(os.path.join(icons_dir, 'sunset.png'))
    uv = Image.open(os.path.join(icons_dir, 'uv.png'))
    moonrise = Image.open(os.path.join(icons_dir, 'moonrise.png'))
    moonset = Image.open(os.path.join(icons_dir, 'moonset.png'))
    humidity = Image.open(os.path.join(icons_dir, 'humidity.png'))
    pm10 = Image.open(os.path.join(icons_dir, 'pm10.png'))
    pm25 = Image.open(os.path.join(icons_dir, 'pm25.png'))
    windy = Image.open(os.path.join(icons_dir, 'windy.png'))
    

class Icons:
    umbrella = Image.open(os.path.join(icons_dir, 'umbrella.png'))
    sunny = Image.open(os.path.join(icons_dir, 'sunny.png'))
    moon = Image.open(os.path.join(icons_dir, 'moon.png'))
    sun_cloud = Image.open(os.path.join(icons_dir, 'sun-cloud.png'))
    moon_cloud = Image.open(os.path.join(icons_dir, 'moon-cloud.png'))
    day_cloud = Image.open(os.path.join(icons_dir, 'day-cloud.png'))
    night_cloud = Image.open(os.path.join(icons_dir, 'night-cloud.png'))
    rain = Image.open(os.path.join(icons_dir, 'rain.png'))
    snow = Image.open(os.path.join(icons_dir, 'snow.png'))
    rain_snow = Image.open(os.path.join(icons_dir, 'rain-snow.png'))
    sun_rain = Image.open(os.path.join(icons_dir, 'sun-rain.png'))
    moon_rain = Image.open(os.path.join(icons_dir, 'moon-rain.png'))
    sun_cloud_and_rain = Image.open(os.path.join(icons_dir, 'sun-cloud-and-rain.png'))
    moon_cloud_and_rain = Image.open(os.path.join(icons_dir, 'moon-cloud-and-rain.png'))
    day_cloud_and_rain = Image.open(os.path.join(icons_dir, 'day-cloud-and-rain.png'))
    night_cloud_and_rain = Image.open(os.path.join(icons_dir, 'night-cloud-and-rain.png'))
    sun_cloud_and_snow = Image.open(os.path.join(icons_dir, 'sun-cloud-and-snow.png'))
    moon_cloud_and_snow = Image.open(os.path.join(icons_dir, 'moon-cloud-and-snow.png'))
    day_cloud_and_snow = Image.open(os.path.join(icons_dir, 'day-cloud-and-snow.png'))
    night_cloud_and_snow = Image.open(os.path.join(icons_dir, 'night-cloud-and-snow.png'))
    sun_cloud_and_rain_snow = Image.open(os.path.join(icons_dir, 'sun-cloud-and-rain-snow.png'))
    moon_cloud_and_rain_snow = Image.open(os.path.join(icons_dir, 'moon-cloud-and-rain-snow.png'))
    day_cloud_and_rain_snow = Image.open(os.path.join(icons_dir, 'day-cloud-and-rain-snow.png'))
    night_cloud_and_rain_snow = Image.open(os.path.join(icons_dir, 'night-cloud-and-rain-snow.png'))
    sun_cloud_and_sun_rain = Image.open(os.path.join(icons_dir, 'sun-cloud-and-sun-rain.png'))
    moon_cloud_and_moon_rain = Image.open(os.path.join(icons_dir, 'moon-cloud-and-moon-rain.png'))
    day_cloud_and_sun_rain = Image.open(os.path.join(icons_dir, 'day-cloud-and-sun-rain.png'))
    night_cloud_and_moon_rain = Image.open(os.path.join(icons_dir, 'night-cloud-and-moon-rain.png'))