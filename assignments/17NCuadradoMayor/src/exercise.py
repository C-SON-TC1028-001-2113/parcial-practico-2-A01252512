def cuadrado_mayor(n):
    i = 0

    while True:
        if i**2 > n:
            return i
        else:
            i += 1

def main():
    numero = int(input("Escribe un numero : "))
    #escribe tu código abajo de esta línea
    print(cuadrado_mayor(numero))

if __name__=='__main__':
    main()