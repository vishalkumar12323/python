"""
Use Dictionary Comprehension to create a dictionary called weather_f that takes
each temperature in degrees Celsius and converts it into degrees Fahrenheit. 
"""

def weather_converter(celsius_temp: float):
    """weather_converter take celsius_temperature and convert it to fahrenheit."""
    return (celsius_temp * 9/5) + 32


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: weather_converter(temp) for (day, temp) in weather_c.items()}

print(weather_f)