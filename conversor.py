def conversor (tipo_pesos , valor_dolar):
    pesos = input("¿Cuantos pesos "  +  tipo_pesos + "tienes?")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    # redondear valores
    dolares = round(dolares,2)
    # conversion de valorres
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")

menu = """
Bienvenidos al conversor de mondas
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
   conversor('colombianos',3875)
elif opcion == 2:
    conversor('argentinos',65)
elif opcion == 2:
    conversor('mexicanos',24)    
else:
    print('ingresa algo correcto')

