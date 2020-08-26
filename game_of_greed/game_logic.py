from collections import Counter
from random import randint


class GameLogic:
    @staticmethod
    def roll_dice(num=6):
        return tuple([randint(1, 6) for _ in range(num)])

    @staticmethod
    def calculate_score(dice):
        """
        dice is a tuple of integers represent the user's selected dice pulled out from current roll
        """

        if len(dice) > 6:
            raise Exception("Cheating Cheater!")

        counts = Counter(dice)

        if len(counts) == 6:
            return 1500

        if len(counts) == 3 and all(val == 2 for val in counts.values()):
            return 1500

        score = 0

        ones_used = fives_used = False

        for num in range(1, 6 + 1):

            pip_count = counts[num]

            if pip_count >= 3:

                if num == 1:

                    ones_used = True

                elif num == 5:

                    fives_used = True

                score += num * 100

                # handle 4,5,6 of a kind
                score += score * (pip_count - 3)

                # 1s are worth 10x
                if num == 1:
                    score *= 10

        if not ones_used:
            score += counts.get(1, 0) * 100

        if not fives_used:
            score += counts.get(5, 0) * 50

        return score

    @staticmethod
    def validate_keepers(roll, keepers):
        return not Counter(keepers) - Counter(roll)

    @staticmethod
    def get_scorers(dice):
        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        scorers = []

        for i in range(len(dice)):
            sub_roll = dice[:i] + dice[i + 1 :]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                scorers.append(dice[i])

        return tuple(scorers)




















# from collections import Counter
# import random
# # from abc import staticmethod

# class GameLogic():
#     """
#     This class is to define the logic of the game of greed for rolling random dice and counting score

#     """
#     def __init__(self):
#         pass

#     def calculate_score(self, dice):
#         score = 0
#         pairs = 0
#         coun = Counter(dice)

#         if coun[5] == 4 and coun[1] == 2:
#             score += 2000
#             return score

#         if len(coun) == 6:
#             score += 1500
#             return score

#         for i in coun:
#             if coun[i] == 2:
#                 pairs += 1
#                 if pairs == 3:
#                     score = 0
#                     score += 1500
#                     return score


#             if coun[i] < 3 and i == 5:
#                 score += (coun[i] * 50)


#             if coun[i] < 3 and i == 1:
#                 score += (coun[i] * 100)


#             if coun[i] >= 3 and i == 1:
#                 score += 1000
#                 coun[i] -= 3
#                 for i in range(coun[i]):
#                     score += 1000
#                 continue


#             if coun[i] >= 3 and i != 1:
#                 m = i
#                 score += (i * 100)
#                 left = coun[i] - 3
#                 while left > 0:
#                     score += (m * 100)
#                     left -=1
#                 continue

#         return score

#     @staticmethod
#     def roll_dice(n):
#         list = []
#         for i in range(n):
#             list.append(random.randint(1, n))
#         return(tuple(list))


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
        self.clear_shelf()
        return self.balance
    def clear_shelf(self):
        self.shelved = 0
        return self.shelved


# if __name__ == "__main__":
#     n = GameLogic()
#     print(n.roll_dice(6))
#     # print(n.calculate_score())
#     # print(GameLogic.calculate_score((5,)))
#     y = GameLogic()
#     print(y.calculate_score((5,)))
