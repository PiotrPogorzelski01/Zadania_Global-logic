imie=input("Podaj imie: ")

result=""
x=len(imie)-1

while len(imie)>len(result):
    for i in range(len(imie)):
        while i==x:
            x=x-1
            result=result+imie[i]


print(result)