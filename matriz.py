# Matriz de assentos do cinema
assentos = [
    [0, 0, 0, 0, 0, 0, 0, 0],  # Fileira 1
    [0, 0, 0, 0, 0, 0, 0, 0],  # Fileira 2
    [0, 0, 0, 0, 0, 0, 0, 0],  # Fileira 3
    [0, 0, 0, 0, 0, 0, 0, 0],  # Fileira 4
    [0, 0, 0, 0, 0, 0, 0, 0]   # Fileira 5
]

def reservar_assentos(assentos, coordenadas):
    #Y coluna
    #X fileira
    for Y, X in coordenadas:
        # Verifica se os índices estão dentro dos limites
        if 0 <= Y < len(assentos) and 0 <= X < len(assentos[0]):
            if assentos[Y][X] == 0:  # Verifica se o assento está livre
                assentos[Y][X] = 1  # Marca o assento como ocupado
            else:
                print(f"Assento ({Y}, {X}) já está ocupado.")
        else:
            print(f"Coordenadas ({Y}, {X}) são inválidas.")

#assentos a serem reservados
coordenadas_para_reservar = [ (1,3), (2,5),(4,7)]  # Lista de coordenadas para reserva

# Reservando os assentos
reservar_assentos(assentos, coordenadas_para_reservar)

print("\n-assentos apos reserva- \n")
# Exibindo a matriz após a reserva
for linha in assentos:
    print(linha)


def Cancelar_assentos(assentos, coordenadas):
    for Y, X in coordenadas:
        # Verifica se os índices estão dentro dos limites
        if 0 <= Y < len(assentos) and 0 <= X < len(assentos[0]):
            if assentos[Y][X] == 1:  # Verifica se o assento está ocupado
                assentos[Y][X] = 0  # Marca o assento como livre
            else:
                print(f"Assento ({Y}, {X}) já está desocupado.")
        else:
            print(f"Coordenadas ({Y}, {X}) são inválidas.")

#assentos a serem cancelados
coordenadas_para_Cancelar = [(2,5)]  # Lista de coordenadas para Cancelar

# Cancelando os assentos
Cancelar_assentos(assentos, coordenadas_para_Cancelar)

print("\n-assentos apos cancelamento- \n")
#Exibindo a matriz após a Cancelamento
for linha in assentos:
    print(linha)
