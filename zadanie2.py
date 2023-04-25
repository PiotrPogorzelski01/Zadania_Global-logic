zdanie=input("Wpisz zdanie: ")


result=""

for i in zdanie.split()[::-1]:
    result+=i+" "


print(result)


