player_1 = input('Introduzca el nombre del primer jugador: ').title()
player_2 = input('Introduzca el nombre del segundo jugador: ').title()

person_1 = input(f'¡{player_1}! piedra, papel, tijeras saca lo que quieras: ').lower()
person_2 = input(f'¡{player_2}! piedra, papel, tijeras saca lo que quieras: ').lower()

if person_1 == person_2:
    winner = None
    print('Empate, preparados para otra ronda')
elif (
    (person_1 == 'piedra' and person_2 == 'tijeras')
    or (person_1 == 'tijeras' and person_2 == 'papel')
    or (person_1 == 'papel' and person_2 == 'piedra')
):
    winner = player_1
else:
    winner = player_2

win_condition = person_1 if winner == player_1 else person_2 if winner == player_2 else None
rock_win = 'La piedra rompe las tijeras'
scissors_win = 'Las tijeras cortan el papel'
paper_win = 'El papel envuelve la piedra'

if win_condition == 'piedra':
    print(f'Gana {winner}, {rock_win}')
elif win_condition == 'tijeras':
    print(f'Gana {winner}, {scissors_win}')
elif win_condition == 'papel':
    print(f'Gana {winner}, {paper_win}')

if winner is None:
    print('Vuelva a ejecutar el programa.')
elif winner == player_1 or player_2:
    print('Felicidades')
