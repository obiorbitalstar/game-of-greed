from game_of_greed.game_logic import GameLogic,Banker
# from game_logic import GameLogic,Banker
import sys
from collections import Counter
#
# from tests.flow.flo import roller
class Game:
    def __init__(self,roller=None):
        self.roller = roller or GameLogic.roll_dice
        self.shelved = 0
        self.round = 1
        self.total = 0


    def play(self):
        num_dice = 6
        self.total = 0
        print('Welcome to Game of Greed')
        start=input('Wanna play?')
        if start =='n':
            print('OK. Maybe another time')
        # x = GameLogic.roll_dice(self,6)
        # print(x)
        elif start == 'y':
            flag = True
            while flag:
                self.shelved = 0 # to be refactored
                print(f"Starting round {self.round}")
                self.play_round(0)


    def quit_game(self):
        # print(f"Total score is {self.total} points")
        print(f"Thanks for playing. You earned {self.total} points")
        sys.exit()


    def play_round(self, rounds_total):
        num_dice = 6

        for i in range(20):

            print(f"Rolling {num_dice} dice...")

            roll = self.roller(num_dice)
            print(roll)

            # For next version, check if ziltch here, if yes then break the round
            # Day 3
            cheack_before=[int(i) for i in roll]
            check_before_start = GameLogic.calculate_score(self,cheack_before)
            # print(check_before_start)
            # if the input is zero its a zilch
            if check_before_start == 0:
                print("Zilch!!! Round over")
                self.total += rounds_total
                print(f"You banked {rounds_total} points in round {self.round}")
                self.round += 1
                num_dice = 6
                print(f"Total score is {self.total} points")
                self.round+=1
                break


            unbanked_score=0
            # Check what user wants to do
            # First input trail
            more =input("Enter dice to keep (no spaces), or (q)uit: ")

            more=list(more)
            input_checkk1=[int(something) for something in tuple(more)]
            input_checkk=Counter(input_checkk1).most_common()

            roll_check=list(roll)
            roll_check=Counter(roll_check).most_common()
            for i in input_checkk:
                for x in roll_check:

                    if int(x[0]) == int(i[0]) and int(x[1]) >= int(i[1]):
                        check_result=True
                        break
                    else:
                        check_result=False

            if check_result:
                splitted_dice=[int(i) for i in more]
                unbanked_score = GameLogic.calculate_score(self,(splitted_dice))
                rounds_total += unbanked_score
                num_dice -= len(splitted_dice)

            elif more == 'q':
                self.quit_game()
            else:
                print("Cheater!!! Or possibly made a typo...")
                # roll = self.roller(num_dice)
                print(','.join([str(i) for i in roll]))
                more =input("Enter dice to keep (no spaces), or (q)uit: ")
                splitted_dice=[str(i) for i in more]
                unbanked_score = GameLogic.calculate_score(self,(splitted_dice))
                rounds_total += unbanked_score
                num_dice -= len(splitted_dice)







            print(f"You have {rounds_total} unbanked points and {num_dice} dice remaining")
            # Second Input trail
            what_next= input("(r)oll again, (b)ank your points or (q)uit ")

            if what_next == 'q' or what_next == 'quit':
                self.quit_game()
            # if what_next == 'r' or what_next =='roll':


            if what_next=='b' or what_next=='bank':
                self.total += rounds_total
                print(f"You banked {rounds_total} points in round {self.round}")
                self.round += 1
                num_dice = 6
                print(f"Total score is {self.total} points")
                break


if __name__ == "__main__":
    game = Game()
    game.play()
