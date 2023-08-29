celsius = float(input('Insira a temperatura em °C: '))
fahrenheit = (9 * celsius)/5 + 32
kelvin = celsius + 273
print('A temperatura {:.2f}°C corresponde a {:.2f}°F e a {:.2f}K.'.format(celsius, fahrenheit, kelvin))