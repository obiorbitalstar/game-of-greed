from game_of_greed.game_logic import GameLogic,Banker
# from tests.flow.flo import roller
class Game:
    def __init__(self,roller=None):
        self.roller=roller or GameLogic.roll_dice
        self.shelved=0
    def play(self):
        round = 1
        num_dice = 6
        total =0
        print('Welcome to Game of Greed')
        start=input('Wanna play?')
        if start =='n':
            print('OK. Maybe another time')
        # x = GameLogic.roll_dice(self,6)
        # print(x)
        elif start == 'y':
            print(f"Starting round {round}")
            print("Rolling 6 dice...")
            roll = self.roller(num_dice)
            print(','.join([str(i) for i in roll]))
            more =int(input("Enter dice to keep (no spaces), or (q)uit: "))
            please_work=[int(i) for i in str(more)]
            bank = GameLogic.calculate_score(self,(please_work))
            print(f"You have {bank} unbanked points and {num_dice-1} dice remaining")
            what_next= input("(r)oll again, (b)ank your points or (q)uit ")

            if what_next=='b' or what_next=='bank':
                total+=bank
                print(f"You banked {total} points in round {round}")
                round+=1
                num_dice =6
            print(f"Total score is {total} points")
            print(f"Starting round {round}")
            print(f"Rolling {num_dice} dice...")
            roll = self.roller(num_dice)
            print(','.join([str(i) for i in roll]))
            end = input("Enter dice to keep (no spaces), or (q)uit: ")
            if end =='q' or end =='quit':
                print(f"Total score is {total} points")
                print(f"Thanks for playing. You earned {total} points")


if __name__ == "__main__":
    game = Game()
    game.play()
