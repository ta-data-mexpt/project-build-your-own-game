semilleros = 12
semillas = 4
continuar_juego = -2
sin_ganador = -1

# -----------------------------Bases de tablero---------------------------------------


def creaciontab(tab):
    print('------------------------------------------------------------------')
    creaciontab_cad = ''
    mitadsemilleros = 6
    creaciontab_cad += semilleros_sup(tab, mitadsemilleros)
    creaciontab_cad += '\n'
    creaciontab_cad += semilleros_inf(tab, mitadsemilleros)
    return creaciontab_cad
    # Para hacer un recorrido en el sentido de las manecillas de reloj,
    # se toma los primeros seis elementos del arreglo para usarlos como
    # 'semilleros'para el jugardor 2


def semilleros_sup(tab, mitadsemilleros):
    # Semilleros superiores
    # Damos formato y colocamos indices a los semilleros
    mitadsemilleros = 6
    cadsemillero = ''

    for i in range(2*mitadsemilleros-1, mitadsemilleros-1, -1):
        cadsemillero += '\t' + str(i) + ' [' + str(tab[i]) + ']'
    return cadsemillero


def semilleros_inf(tab, mitadsemilleros):
    # Semilleros inferiores
    # Damos formato y colocamos indices a los semilleros
    mitadsemilleros = 6
    cadsemillero = ''

    for i in range(0, mitadsemilleros):
        cadsemillero += '\t' + str(i) + ' [' + str(tab[i]) + ']'
    return cadsemillero


def mostrar_recoleccion(marcador):
    print('------------------------------------------------------------------')
    marcadorcad = "Semillas recogidas:\tJugador 1: {}\tJugador 2: {}\n"
    return marcadorcad.format(marcador[0], marcador[1])

# -----------------------------Funcionalidades y reglas --------------------------------


def selec_mover(tab, semillero):
    # al brindar el tablero y la posición del semillero
    # se recolectaran las semillas existentes
    # además en la posición original habrá '0' semillas
    # no importando si hay 11 semillas
    semillas_recolectar = tab[semillero]
    tab[semillero] = 0
    x = semillero

    while semillas_recolectar > 0:
        x += 1
        if x % semilleros != semillero:
            tab[x % semilleros] += 1
            semillas_recolectar -= 1
    return x % semilleros, tab


def comprobar_posicion(jugador, tab, posicion):
    si_semillero_vacio = (tab[posicion] == 0)
    si_jugador_mueve = (jugador['posicion_min'] <= posicion < jugador['posicion_max'])
    movimiento_posible = si_jugador_mueve and not si_semillero_vacio
    sumar_semillas = sum(tab[jugador['eleccion_min']:jugador['eleccion_max']])

    if sumar_semillas == 0:
        recolec_semilleros = verificar_semilleros_recolectar(jugador, tab, posicion)
        ubicar_semillas = ubicacion_semillas_movidas(jugador, tab)
        return movimiento_posible and (not recolec_semilleros or not ubicar_semillas)
    return movimiento_posible


def recoleccion_semillas(jugador, tab, posicion, marcador):
    posicion_final, tablero_modificado = selec_mover(tab, posicion)

    def recoleccion_dsemilleros(a):
        return (jugador['eleccion_min'] <= posicion_final < jugador['eleccion_max'] and 2 <= tablero_modificado[posicion_final] <= 3)

    while recoleccion_dsemilleros(posicion_final):
        marcador[jugador['numero']] += tablero_modificado[posicion_final]
        tablero_modificado[posicion_final] = 0
        posicion_final -= 1
    return tablero_modificado, marcador


def verificar_semilleros_recolectar(jugador, tab, posicion, marcador = [0, 0]):
    # Esta funcion ubicará los semilleros que se
    # pueden cosechar. Retornando un tablero actualizado
    info_semilleros = tab[:]
    info_marcador = marcador[:]
    semilleros_actualizados, marcador_actualizado = recoleccion_semillas(jugador, info_semilleros, posicion, info_marcador)
    eleccion_min = jugador['eleccion_min']
    eleccion_max = jugador['eleccion_max']
    cosechar_semillas = (sum(semilleros_actualizados[eleccion_min:eleccion_max]) == 0)
    return cosechar_semillas


def ubicacion_semillas_movidas(jugador, tab, marcador = [0, 0]):
    # Esta funcion ubicará la primera posición
    # de la semilla colocada hasta la última
    posicion_min = jugador['posicion_min']
    posicion_max = jugador['posicion_max']
    no_recoger = False

    for i in range(posicion_min, posicion_max):
        posible_cosecha = verificar_semilleros_recolectar(jugador, tab, i, marcador)
        no_recoger = no_recoger and posible_cosecha
    return not no_recoger


def verificar_ganador(jugador, tab, posicion, estado_del_juego, marcador):
    # Esta función nos permitira cortar el juego mediante
    # el cierto número de semillas recolectadas.
    if estado_del_juego == continuar_juego:
        eleccion_min = jugador['eleccion_min']
        elecion_max = jugador['eleccion_max']
        numero_de_jugador = jugador['numero']
        cosechar_semillas = sum(tab[eleccion_min:elecion_max]) == 0
        semillas_para_ganar = int(((semillas * semilleros) / 2))
        pocas_semillas = int(((semillas * semilleros) / 6))

        if cosechar_semillas or marcador[numero_de_jugador] >= semillas_para_ganar or marcador[numero_de_jugador] >= pocas_semillas:
            estado_del_juego = numero_de_jugador
        elif marcador[1 - numero_de_jugador] >= semillas_para_ganar or marcador[numero_de_jugador] >= pocas_semillas:
            estado_del_juego = 1 - numero_de_jugador
        return marcador, estado_del_juego

# ----------------------------------Flujo de juego----------------------------------------------------


def semillero_a_recolectar(tab, jugador_en_turno):
    # Con esta función obtendremos la posición
    # de la cual se recogeran las semillas
    posicion = int(input("Jugador ({}), elije semillero a cosecharas: ".format(jugador_en_turno['numero'] + 1)))

    while not comprobar_posicion(jugador_en_turno, tab, posicion):
        posicion = int(input("No puedes elegir está posición o escribiste una letra. Intenta de nuevo: "))
    return posicion


def caracteristicas_de_jugador(numero, jugador=None):
    # Esta función retornará características del jugador
    # para las funcionalidades del juego
    mitad_semilleros = 6
    return {'numero': numero, 'posicion_min': numero * mitad_semilleros,
        'posicion_max': (1 + numero) * mitad_semilleros, 'eleccion_min': (1 - numero) * mitad_semilleros,
        'eleccion_max': (2 - numero) * mitad_semilleros, 'jugador': jugador,}


def turno_en_juego(jugador_en_turno, tab, posicion, marcador):
    # Esta función nos retornará la información
    # del turno que se esta jugando
    cosechar_semillas = verificar_semilleros_recolectar(jugador_en_turno, tab, posicion, marcador,)

    if cosechar_semillas:
        posicion_final, nuevo_tablero = selec_mover(tab, posicion)
        return nuevo_tablero, marcador
    return recoleccion_semillas(jugador_en_turno, tab, posicion, marcador)


def mostrar_estado_del_juego(estado_del_juego):
    # Esta funcion solo devolverá quien fue el ganador
    if estado_del_juego == sin_ganador:
        return "\nMucho tiempo y no hubo ganador. ¡Echen un volado!"
    return "El ganador fue: {}.".format(estado_del_juego)

