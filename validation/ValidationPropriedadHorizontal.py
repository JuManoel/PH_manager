from Validation import Validation

class ValidationPropriedadHorizontal(Validation):
    def __init__(self):
        letters = "qwertyuiopasdfghjklçñzxcvbnm"
        upperLetters = letters.upper()
        number = "1234567890"
        self.specialCharacter = "!@#$%¨&*()_=/*-+"
        self.passWord = letters+upperLetters+number+specialCharacter
    def validar(self, obj):
        if(len(obj.senha)<5):
            raise Exception("Contraseña muy corta")
        has_numbers = False
        has_special = false
        for l in obj.senha:
            if (has_special and has_numbers):
                break
            if(l.isdecimal()):
                has_numbers = True
                continue
            if(l in self.specialCharacter):
                has_special = True
                continue
        if(not has_numbers):
            raise Exception("Tiene que tener al menos 1 numero")
        if(not has_special):
            raise Exception("Tiene que tener al menos 1 caracter especial")