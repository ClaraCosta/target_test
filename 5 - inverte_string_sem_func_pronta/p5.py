#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------Invertendo os caracteres de uma string----------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------

def inverter_string(s):
    string_invertida = ''
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

string = input("Digite uma frase para ler ao contrário: ")
print(f"Frase invertida: {inverter_string(string)}")
