slowo=input("Podaj słowo: ")
x=0
result=""
for i in slowo:
    if i==slowo[x]:
        result=result+i.upper()
    else:
        result=result+i.lower()

print(result)

