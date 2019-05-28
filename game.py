import random

game_running = True
game_results = []

def calc_random_num(min, max):
    return random.randrange(min, max)


def game_ends(name):
    print(name + " won the game")


while game_running == True:
    new_round = True
    round_counter = 0

    player = {
        'name': 'Todd',
        'attack': [15, 30],
        'heal': [20, 50],
        'health': 100
    }

    monster = {
        'name': 'Hitler',
        'attack': [10, 40],
        'health': 120
    }

    print('---' * 8)
    # print('Enter Player Name')
    player['name'] = raw_input('Enter Player Name \n')

    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

    while new_round == True:
        round_counter = round_counter + 1
        player_won = False
        monster_won = False

        print('---' * 8)
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')
        print('4) Show Results')

        player_choice = input()

        if player_choice == 1:
            monster['health'] = monster['health'] - \
                calc_random_num(player['attack'][0], player['attack'][1])
            if monster['health'] <= 0:
                player_won = True
                print('The monster is dead')
            else:
                player['health'] = player['health'] - \
                    calc_random_num(monster['attack'][0], monster['attack'][1])
                if player['health'] <= 0:
                    monster_won = True
                    print('The player is dead')

        elif player_choice == 2:
            player_heal_amount = calc_random_num(
                player['heal'][0], player['heal'][1])
            print('Player healed for ' + str(player_heal_amount))
            player['health'] = player['health'] + player_heal_amount

            player['health'] = player['health'] - \
                calc_random_num(monster['attack'][0], monster['attack'][1])

        elif player_choice == 3:
            new_round = False
            game_running = False

        elif player_choice == 4:
            for result in game_results:
                print(result)

        else:
            print('Invalid input')
        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' +
                  str(player['health']) + ' health left')
            print(monster['name'] + ' has ' +
                  str(monster['health']) + ' health left')

        elif player_won:
            game_ends(player['name'])
            round_result = {
                'name': player['name'], 'health': player['health'], 'rounds': round_counter}
            game_results.append(round_result)
            new_round = False

        elif monster_won:
            game_ends(monster['name'])
            round_result = {
                'name': player['name'], 'health': player['health'], 'rounds': round_counter}
            game_results.append(round_result)
            new_round = False
