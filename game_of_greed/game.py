import os
import sys

# from game_of_greed.game_logic import GameLogic
# from game_of_greed.banker import Banker
from game_logic import GameLogic,Banker
# from banker import Banker
# from game_logic import GameLogic,Banker


class Game:
    """Class for Game of Greed application
    """

    def __init__(self, roller=None, num_rounds=20):

        self._roller = roller or GameLogic.roll_dice
        self.banker = Banker()
        self.num_rounds = num_rounds
        self.round_num = 0

    def play(self):
        """
        Entry point for playing (or/not) a game
        """

        print("Welcome to Game of Greed")

        prompt = "Wanna play?"

        self.choice(prompt.strip(), self.start_game, self.decline_game)

    def choice(self, prompt, accept, decline):

        response = input(prompt)

        if response == "y" or response == "yes":

            accept()

        else:

            decline()

    def decline_game(self):
        print("OK. Maybe another time")

    def start_game(self):

        self.round_num = 1

        while self.round_num <= self.num_rounds:

            self.start_round(self.round_num)

            self.round_num += 1

            print(f"Total score is {self.banker.balance} points")

        self.quit_game()

    def quit_game(self):

        print(f"Thanks for playing. You earned {self.banker.balance} points")

        sys.exit()

    def start_round(self, round, num_dice=6):

        print(f"Starting round {round}")

        round_score = 0

        while True:

            roll = self.roll_dice(num_dice)

            if self.got_zilch(roll):
                break

            keepers = self.handle_keepers(roll)

            roll_again_response = input("(r)oll again, (b)ank your points or (q)uit ")

            if roll_again_response == "q":

                self.quit_game()

                return

            elif roll_again_response == "b":

                round_score = self.banker.bank()

                break

            else:

                num_dice -= len(keepers)

                if num_dice == 0:

                    num_dice = 6

        print(f"You banked {str(round_score)} points in round {round}")

    def handle_keepers(self, roll):

        while True:
            keeper_string = input("Enter dice to keep (no spaces), or (q)uit: ")

            if keeper_string.startswith("q"):
                self.quit_game()

            keepers = self.gather_keepers(roll, keeper_string)

            roll_score = self.calculate_score(keepers)

            if roll_score == 0:
                print("Must keep at least one scoring dice")
            else:
                break

        self.banker.shelf(roll_score)

        print(
            f"You have {self.banker.shelved} unbanked points and {len(roll) - len(keepers)} dice remaining"
        )

        return keepers

    def roll_dice(self, num):

        print(f"Rolling {num} dice...")

        roll = self._roller(num)

        print(",".join([str(i) for i in roll]))

        return roll

    def got_zilch(self, roll):

        initial_score = self.calculate_score(roll)

        if initial_score == 0:

            print("Zilch!!! Round over")

            self.banker.clear_shelf()

            return True

        return False

    def calculate_score(self, roll):
        return GameLogic.calculate_score(roll)

    def keep_scorers(self, roll):
        return GameLogic.get_scorers(roll)

    def gather_keepers(self, roll, keeper_string):

        keepers = [int(ch) for ch in keeper_string]

        while not GameLogic.validate_keepers(roll, keepers):
            print("Cheater!!! Or possibly made a typo...")
            print(",".join([str(i) for i in roll]))
            keeper_string = input("Enter dice to keep (no spaces), or (q)uit: ")
            if keeper_string.startswith("q"):
                self.quit_game()

            keepers = [int(ch) for ch in keeper_string]

        return keepers


def clear():
    # stretch goal to allow user to clear terminal mid game

    # os.system("cls" if os.name == "nt" else "clear")
    pass


if __name__ == "__main__":
    game = Game()
    game.play()




















# from game_of_greed.game_logic import GameLogic,Banker
# # from game_logic import GameLogic,Banker
# import sys
# from collections import Counter
# #
# # from tests.flow.flo import roller
# class Game:
#     def __init__(self,roller=None):
#         self.roller = roller or GameLogic.roll_dice
#         self.shelved = 0
#         self.round = 1
#         self.total = 0


#     def play(self):
#         num_dice = 6
#         self.total = 0
#         print('Welcome to Game of Greed')
#         start=input('Wanna play?')
#         if start =='n':
#             print('OK. Maybe another time')
#         # x = GameLogic.roll_dice(self,6)
#         # print(x)
#         elif start == 'y':
#             flag = True
#             while flag:
#                 self.shelved = 0 # to be refactored
#                 print(f"Starting round {self.round}")
#                 self.play_round(0)


#     def quit_game(self):
#         # print(f"Total score is {self.total} points")
#         print(f"Thanks for playing. You earned {self.total} points")
#         sys.exit()
#     def zilch(self,rounds_total):
#         print("Zilch!!! Round over")
#         rounds_total=0
#         print(f"You banked {rounds_total} points in round {self.round}")
#         print(f"Total score is {self.total} points")
#         self.round += 1
#         num_dice = 6

#     def cheater_or_typo(self,roll):
#         print("Cheater!!! Or possibly made a typo...")
#         print(','.join([str(i) for i in roll]))
#         more =input("Enter dice to keep (no spaces), or (q)uit: ")



#     def play_round(self, rounds_total):
#         num_dice = 6

#         for i in range(20):

#             print(f"Rolling {num_dice} dice...")

#             roll = self.roller(num_dice)
#             print(','.join([str(i) for i in roll]))

#             # For next version, check if ziltch here, if yes then break the round
#             # Day 3
#             cheack_before=[int(i) for i in roll]
#             check_before_start = GameLogic.calculate_score(self,cheack_before)
#             # print(check_before_start)
#             # if the input is zero its a zilch

#             if check_before_start == 0:
#                 self.zilch(rounds_total)
#                 break
#             # unbanked_score=0
#             # Check what user wants to do
#             # First input trail
#             more =input("Enter dice to keep (no spaces), or (q)uit: ")
#             if more == 'q' or more =='quit':
#                 print(f"Total score is {self.total} points")
#                 self.quit_game()
#                 sys.exit()
#             more=list(more)
#             input_checkk1=[int(i) for i in tuple(more)]
#             input_checkk=Counter(input_checkk1).most_common()

#             roll_check=list(roll)
#             roll_check=Counter(roll_check).most_common()
#             for i in input_checkk:
#                 for x in roll_check:

#                     if int(x[0]) == int(i[0]) and int(x[1]) >= int(i[1]):
#                         check_result=True
#                         break
#                     else:
#                         check_result=False
#             if not check_result:
#                 self.cheater_or_typo(roll)
#                 splitted_dice=[int(i) for i in more]
#                 unbanked_score = GameLogic.calculate_score(self,(splitted_dice))
#                 rounds_total += unbanked_score
#                 num_dice -= len(splitted_dice)

#             elif check_result:
#                 splitted_dice=[int(i) for i in more]
#                 unbanked_score = GameLogic.calculate_score(self,(splitted_dice))
#                 rounds_total += unbanked_score
#                 num_dice -= len(splitted_dice)
#                 # print(f"You have {rounds_total} unbanked points and {num_dice} dice remaining")
#                 # what_next= input("(r)oll again, (b)ank your points or (q)uit ")
#             elif more == 'q':
#                 self.quit_game()
#             # else:

#             print(f"You have {rounds_total} unbanked points and {num_dice} dice remaining")
#             # Second Input trail
#             what_next= input("(r)oll again, (b)ank your points or (q)uit ")

#             if what_next == 'q' or what_next == 'quit':
#                 self.quit_game()
#             # if what_next == 'r' or what_next =='roll':


#             if what_next=='b' or what_next=='bank':
#                 self.total += rounds_total
#                 print(f"You banked {rounds_total} points in round {self.round}")
#                 print(f"Total score is {self.total} points")
#                 self.round += 1
#                 num_dice = 6
#                 break


# if __name__ == "__main__":
#     game = Game()
#     game.play()
