def concatenar(texto1, texto2):
    return texto1 + " " + texto2


def comprobarEmail(email):
    if email.find("@") != -1:
        return True
    else:
        return False


def esTexto(texto):
    return texto.isAlpha()
