from game_of_greed.game_logic import GameLogic,Banker
# from game_logic import GameLogic,Banker
import sys

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
            while True:
                self.shelved = 0 # to be refactored
                print(f"Starting round {self.round}")
                self.play_round(0)


    def quit_game(self):
        print(f"Total score is {self.total} points")
        print(f"Thanks for playing. You earned {self.total} points")
        sys.exit()


    def play_round(self, rounds_total):
        num_dice = 6
        while True:
            # Rolling dice
            print(f"Rolling {num_dice} dice...")
            # roll = self.roller(num_dice)
            roll = self.roller(num_dice)
            print(','.join([str(i) for i in roll]))

            # For next version, check if ziltch here, if yes then break the round
            # Day 3

            # Check what user wants to do
            more =input("Enter dice to keep (no spaces), or (q)uit: ")

            # Check if player wants to quit
            if more == 'q':
                self.quit_game()

            # Split "dice to keep" into list of integers
            splitted_dice=[int(i) for i in more]
            unbanked_score = GameLogic.calculate_score(self,(splitted_dice))
            rounds_total += unbanked_score

            # Subtract from num_dice
            num_dice -= len(splitted_dice)

            print(f"You have {unbanked_score} unbanked points and {num_dice} dice remaining")
            what_next= input("(r)oll again, (b)ank your points or (q)uit ")
            if more == 'q':
                self.quit_game()

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
