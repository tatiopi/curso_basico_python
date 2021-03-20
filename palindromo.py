# Mi version correcta
def es_palindromo (str):
    if str[::-1].lower() == str.lower():
        return True
    else:
        print(str[::-1].lower())
        print(str.lower)
        return False


def run():
    palindromo = input('Escribe el palindromo: ')
    es = es_palindromo(palindromo)
    if (es == True):
        print('Es un palindromo')
    else:
        print('No es un palindromo')

# seria algo asi como main() en 
if __name__ == '__main__':
    run()
