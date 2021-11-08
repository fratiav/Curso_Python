#Tiene arroba

email = input("Email: ")

sw = False

for i in email:
    if i == "@":
        sw = True
        break

print(sw)