password = input("Password: ")

sw = True

for i in password:
    if i == " ":
        sw = False

if(len(password)>8):
    sw = False

if sw is False:
    print("Contraseña no permitida")
else:
    print("Contraseña correcta")

