# Juego en rayas
# Grupo (Marc, Cristian, Carlo, Hugo, Alexander)


# Info del Jugador
def jugador_info():
    nombre1 = input("Introduce un nombre para el Jugador 1: ")
    ficha1 = ""
    while ficha1 not in ["X", "O"]:
        ficha1 = input("Escoge entre X o O: ").upper()  
    nombre2 = input("Introduce un nombre para el Jugador 2: ")
    if ficha1 == "X":
        ficha2 = "O"
    else:
        ficha2 = "X"
    return nombre1, ficha1, nombre2, ficha2

# Dibuja la tabla de tres en rayas y se los junta y se los multiplica los por 3
def tabla_juego_en_rayas(tabla):
    for row in tabla:
        print(" | ".join(row))
        print(" - " * 3)

# Verificacion de la tabla y el del jugador
def verificar(tabla, jugador):
    for i in range(3):
        if (tabla[i][0] == tabla[i][1] == tabla[i][2] == jugador) or (tabla[0][i] == tabla[1][i] == tabla[2][i] == jugador):
            return True
       
    if (tabla[0][0] == tabla[1][1] == tabla[2][2] == jugador) or (tabla[0][2] == tabla[1][1] == tabla[2][0] == jugador):
        return True
    return False

# Comprobacion del ganador
def comprobar_ganador():
    rondas = 0
    victorias = {nombre1: 0, nombre2: 0} 
    max_victorias = 3 

    while True:
        tabla = [[" " for _ in range(3)] for _ in range(3)]
        print("\nTabla juego en rayas: ")
        tabla_juego_en_rayas(tabla)

        for num_rondas in range(1, 9):  
            jugador_actual = nombre1 if num_rondas % 2 == 1 else nombre2
            ficha_actual = ficha1 if num_rondas % 2 == 1 else ficha2
            print(f"\nRonda {rondas + 1}")
            print(f"Turno de {jugador_actual} ({ficha_actual})")
            position = int(input("Introduce la posicion (1 a 9): ")) - 1
            row = position // 3
            col = position % 3

            while tabla[row][col] != " ":
                print("Posicion invalido. prueba otra vez")
                position = int(input("Introduce la posicion (1 a 9): ")) - 1
                row = position // 3
                col = position % 3

            tabla[row][col] = ficha_actual
            print("\nTabla juego en rayas: ")
            tabla_juego_en_rayas(tabla)
           
            if verificar(tabla, ficha_actual):
                print(f"\nLa ronda {rondas + 1} gano {jugador_actual}!")
                victorias[jugador_actual] += 1
                rondas += 1
                break
   
        if victorias[nombre1] == max_victorias or victorias[nombre2] == max_victorias:
            ganador = nombre1 if victorias[nombre1] > victorias[nombre2] else nombre2
            print(f"\nFin de partida! {ganador} gano {max_victorias} veces!")
            break

if __name__ == "__main__":
    nombre1, ficha1, nombre2, ficha2 = jugador_info()
    comprobar_ganador()