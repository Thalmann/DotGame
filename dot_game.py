
def setup():
    print('Player 1 enter your name: ')
    player_1 = input()
    print('Player 2 enter your name: ')
    player_2 = input()
    return player_1, player_2

def print_dots(dots_count):
    print('Number of dots left: {0}'.format(dots_count))

def read_move(player_name):
    print('{0}, how many dots do you want to remove? (3, 2 or 1)'.format(player_name))
    while(True):
        try:
            move = int(input())
        except Exception:
            move = 0
        if move in range(1, 4):
            return move
        print('You have to choose: 1, 2 or 3')

def lost(player_name):
    print('{0} you have lost.'.format(player_name))

def game():
    player_1, player_2 = setup()
    turn = player_1
    dots_count = 13
    while(True):
        print_dots(dots_count)
        
        move = read_move(turn)
        dots_count -= move

        if dots_count <= 0:
            lost(turn)
            break
        
        if turn is player_1:
            turn = player_2
        elif turn is player_2:
            turn = player_1


game()
        

