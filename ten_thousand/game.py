from ten_thousand.game_logic import GameLogic
from collections import Counter

def not_error(input_):
    try:
        input_
        return True
    except Exception:
        return False


def space_remover(choice):
    choice = ''.join(choice)
    while choice.find(' ') != -1:
        num = choice.find(' ')
        choice = list(choice)
        choice.pop(num)
        choice = ''.join(choice)
    return list(map(int, choice))

def counter_reversal(dice_set, choice):
    empty = []
    values = list((Counter(dice_set) - Counter(choice)).items())

    for num in values:
        i = 0
        while i < num[1]:
            empty.append(num[0])
            i += 1

    return empty


def game_stats(not_banked, dice_set):
    print(f'You have {not_banked} unbanked points and {len(dice_set)} dice remaining \n(r)oll again, (b)ank your points or (q)uit:')


def cheat_check(choice, dice_set):
    #typo check
    for num in choice:
        if num != ' ':
            try:
                int(num)
            except Exception:
                return True

    choice = space_remover(choice)

    #cheat check
    if not_error(GameLogic.calculate_score(choice)):
        choice = Counter(choice)
        dice_set = Counter(dice_set)
        for num in choice:
            if choice[num] > dice_set[num]:
                return True
    else:
        return False


def zilch_check(dice_set):
    if len(dice_set) == 0 or GameLogic.calculate_score(dice_set):
        print('****************************************\n**        Zilch!!! Round over         **\n****************************************')



def start_game():
    intro = "Welcome to Ten Thousand \n(y)es to play or (n)o to decline"
    print(intro)
    choice = input('> ')

    if choice == 'y':
        points = 0
        round_ = 1

        #Game
        while round_ != 21:
            dice_set = list(GameLogic.roll_dice(6))
            print(f"Starting round {round_} \nRolling 6 dice...\n*** {' '.join(str(val) for val in dice_set)} ***\nEnter dice to keep, or (q)uit:")
            choice = input('> ')

            if choice == 'q':
                print(f'Thanks for playing. You earned {points} points')
                break

            # cheat and typo checker
            while cheat_check(choice, dice_set):
                print(f"Cheater!!! Or possibly made a typo...\n*** {' '.join(str(val) for val in dice_set)} ***\nEnter dice to keep, or (q)uit:")
                choice = input('> ')

            choice = space_remover(choice)
            not_banked = GameLogic.calculate_score(choice)
            if len(counter_reversal(dice_set, choice)) == 0:
                dice_set = list(GameLogic.roll_dice(6))
            else:
                dice_set = counter_reversal(dice_set, choice)
            game_stats(not_banked,dice_set)
            choice = input('> ')
            if choice == 'b':
                points += not_banked
                print(f'You banked {not_banked} points in round {round_} \nTotal score is {points}')

            if choice == 'r':
                while choice == 'r':
                    prev_dice_set = len(dice_set)
                    if prev_dice_set == 6:
                        dice_set = list(GameLogic.roll_dice(6))
                    else:
                        dice_set = list(GameLogic.roll_dice(len(dice_set)))
                    print(f"Rolling {len(dice_set)} dice...\n*** {' '.join(str(val) for val in dice_set)} ***\nEnter dice to keep, or (q)uit:")
                    if len(dice_set) == 0 or GameLogic.calculate_score(dice_set) == 0:
                        print(
                            '****************************************\n**        Zilch!!! Round over         **\n****************************************')
                        not_banked = 0
                        break
                    choice = input('> ')

                    if choice == 'q':
                        break

                    # cheat and typo checker
                    while cheat_check(choice, dice_set):
                        print(
                            f"Cheater!!! Or possibly made a typo...\n*** {' '.join(str(val) for val in dice_set)} ***\nEnter dice to keep, or (q)uit:")
                        choice = input('> ')

                    choice = space_remover(choice)
                    not_banked += GameLogic.calculate_score(choice)
                    if prev_dice_set == 0:
                        dice_set = list(GameLogic.roll_dice(6))
                    else:
                        dice_set = counter_reversal(dice_set, choice)
                    game_stats(not_banked, dice_set)
                    choice = input('> ')

                    if choice == 'b':
                        points += not_banked
                        print(f'You banked {not_banked} points in round {round_} \nTotal score is {points}')
                        break

            if choice == 'q':
                print(f'Thanks for playing. You earned {points} points')
                break

            round_+=1

    else:
        print("OK. Maybe another time")

if __name__ == '__main__':
    start_game()

# initial dice set could be zilch reroll until points

#python -m ten_thousand.game
