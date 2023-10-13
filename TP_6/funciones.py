# 6 funciones
def repeated_name(e_set, h_set):
    repeated_names = set()
    for student in e_set:
        if student in h_set:
            repeated_names.add(student)
    return repeated_names

# 8 funciones
# Mostrar partidos ganados, empatados y perdidos
def games_results(goals,col,team):
    tied_counter = 0
    won_counter = 0
    lost_counter = 0
    print()
    for j in range(1,col):
        if team != j:
            print(f'{team} vs. {j} = {goals[team][j]} - {goals[j][team]}')
            if goals[team][j] > goals[j][team]:
                won_counter+=1
                print("Ganó.")
            elif goals[team][j] == goals[j][team]:
                tied_counter += 1
                print("Empató.")
            else:
                lost_counter+=1
                print("Perdió.")
    return (won_counter,tied_counter,lost_counter)

# Diferencia entre el total de goles marcados y el total de goles recibidos
def goals_dif(goals,col,row,team):
    goals_in_favor = 0
    goals_against = 0
    if team in (1,2,3,4,5,6,7,8,9,10):
        for j in range(1,col):
            goals_in_favor += goals[team][j]
        for i in range(1,row):
            goals_against += goals[i][team] 
    return (goals_in_favor,goals_against)

# Puntos obtenidos por cada equipo
def points(results):
    print("\nLos equipos obtienen tres puntos por partido ganado, uno por empatado y cero por perdido. ")
    total = (results[0] * 3) + results[1] 
    return total
