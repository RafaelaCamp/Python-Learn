x = int(input("Por favor, entre com o número de segundos que deseja converter:"))

a = x//60//60//24
b = (x//60//60)%24
c = (x//60)%60
d = x%60

print(a, "dias,", b, "horas,", c, "minutos e", d, "segundos.")