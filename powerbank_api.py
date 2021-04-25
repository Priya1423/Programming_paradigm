import requests
api_key = "import requests"
api_key = "f1b4ab880558b6036471c79f5e3abd12"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print(" Temperature (in kelvin unit) = " +
     str(current_temperature) + 
     "\n atmospheric pressure (in hPa unit) = " +
     str(current_pressure) +
     "\n humidity (in percentage) = " +
     str(current_humidity) +
     "\n description = " +
     str(weather_description))
else:
    print(" City Not Found ")

f=open("Weather_report.txt","a+")
f.write(f"{city_name:-^30}" '\n')
f.write(f"Temperature: {current_temperature}" '\n')
f.write(f"Humidity: {current_humidity}" '\n')
f.write(f"Pressure: {current_pressure}" '\n')
f.write(f"Weather Report: {weather_description}")
f.read()
f.close()
