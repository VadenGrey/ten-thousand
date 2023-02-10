from ten_thousand.game_logic import GameLogic
from collections import Counter

def not_error(input_):
    try:
        input_
        return True
    except Exception:
        return False

def counter_reversal(dice_set, choice):
    empty = []
    values = list((Counter(dice_set) - Counter(choice)).items())

    for num in values:
        i = 0
        while i < num[1]:
            empty.append(num[0])
            i += 1

    return empty


def start_game():
    intro = "Welcome to Ten Thousand \n(y)es to play or (n)o to decline"
    print(intro)
    choice = input('> ')

    if choice == 'y':
        points = 0
        round_ = 1

        while round_ != 21:
            dice_set = list(GameLogic.roll_dice(6))
            print(f'''Starting round {round_} \nRolling 6 dice...''')
            print(f"*** {' '.join(str(val) for val in dice_set)} ***")
            print('Enter dice to keep, or (q)uit:')
            choice = input('> ')

            if choice == 'q':
                print(f'Thanks for playing. You earned {points} points')
                break

            choice = list(map(int, choice))

            if not_error(GameLogic.calculate_score(choice)):
                unbanked = GameLogic.calculate_score(choice)
                dice_set = counter_reversal(dice_set,choice)
                print(f'You have {unbanked} unbanked points and {len(dice_set)} dice remaining \n(r)oll again, (b)ank your points or (q)uit:')
                choice = input('> ')
                if choice == 'b':
                    points += unbanked
                    print(f'You banked {unbanked} points in round {round_} \nTotal score is {points}')
                elif choice == 'q':
                    print(f'Thanks for playing. You earned {points} points')
                    break
            round_+=1





    else:
        print("OK. Maybe another time")

if __name__ == '__main__':
    start_game()



#python -m ten_thousand.game
