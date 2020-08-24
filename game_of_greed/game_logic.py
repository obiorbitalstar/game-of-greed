from collections import Counter
import random

class GameLogic():
    """
    This class is to define the logic of the game of greed for rolling random dice and counting score

    """
    def __init__(self):
        pass

    def calculate_score(self, dice):
        score = 0
        pairs = 0
        coun = Counter(dice)

        if coun[5] == 4 and coun[1] == 2:
            score += 2000
            return score

        if len(coun) == 6:
            score += 1500
            return score

        for i in coun:
            if coun[i] == 2:
                pairs += 1
                if pairs == 3:
                    score = 0
                    score += 1500
                    return score


            if coun[i] < 3 and i == 5:
                score += (coun[i] * 50)


            if coun[i] < 3 and i == 1:
                score += (coun[i] * 100)


            if coun[i] >= 3 and i == 1:
                score += 1000
                coun[i] -= 3
                for i in range(coun[i]):
                    score += 1000
                continue


            if coun[i] >= 3 and i != 1:
                m = i
                score += (i * 100)
                left = coun[i] - 3
                while left > 0:
                    score += (m * 100)
                    left -=1
                continue

        return score

    def roll_dice(self,n):
        list = []
        for i in range(n):
            list.append(random.randint(1, n))
        return(tuple(list))


class Banker():
    """
    The banker class is to keep track of points earned by the player wither he adds them to his balance or shelf them and so on
    """
    def __init__(self):
        self.balance = 0
        self.shelved = 0
    def shelf(self, int):
        self.shelved += int
        return self.shelved
    def bank(self):
        self.balance += self.shelved
        self.clear_shlef()
        return self.balance
    def clear_shlef(self):
        self.shelved = 0
        return self.shelved


if __name__ == "__main__":
    n = GameLogic()
    print(n.roll_dice(6))
    # print(n.calculate_score())
    # print(GameLogic.calculate_score((5,)))
    y = GameLogic()
    print(y.calculate_score((5,)))
