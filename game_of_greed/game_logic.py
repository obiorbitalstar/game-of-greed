from collections import Counter
import random
"""
score_ calculator

points = 0
if 1 :
    return 100
if 5
    return 50
if counter(dice).most_common(1)[0][0] == 1
    if Counter(dice).most_common(1)[0][1]) == 3
           point+=1000
    elif Counter(dice).most_common(1)[0][1]) ==4
           100000
    elif Counter(dice).most_common(1)[0][1]) == 5
            50000
    elif Counter(dice).most_common(1)[0][1]) ==6
            4000
elif counter(dice).most_common(1)[0][0] == 2

(Counter(data).most_common(1)[0][0])
(1,3)

----------------------------
def roll_dice(n):
  list = []
  for i in range(n):
    list.append(random.randint(1,n))
  return(tuple(list))
--------------------------------------
Banker():
def __init__(self,balance,shelved):
    self.balance=0
    self.shelved =0

def shelf(int,self):
  self.shevled+=int

  return self.shelved


def bank(self):
   self.balanc+=self.shelved
   clear_shlef()
   return balance


def clear_shelf(self):
    self.shelved =0
    return self.shelved

"""


def up_to_six_threes(dice):
    score = 0
    coun = Counter(dice).most_common  # aliase for Counter of dice
    if dice == 1:
        score+= 100
    if dice ==5:
        score+= 50

    elif coun(1)[0][0] == 1:
        if coun(1)[0][1] == 1:
            score+= 100
        elif coun(1)[0][1] == 2:
            score+= 200
        elif coun(1)[0][1] == 3:
            score+= 1000
        elif coun(1)[0][1] == 4:
            score+= 2000
        elif coun(1)[0][1] == 5:
            score+= 3000
        elif coun(1)[0][1] == 6:
            score+= 4000
    elif coun(1)[0][0] == 2:
        if coun(1)[0][1] == 3:
            score+= 200
        elif coun(1)[0][1] == 4:
            score+= 400
        elif coun(1)[0][1] == 5:
            score+= 600
        elif coun(1)[0][1] == 6:
            score+= 800
    elif coun(1)[0][0] == 3:
        if coun(1)[0][1] == 3:
            score+= 300
        elif coun(1)[0][1] == 4:
            score+= 600
        elif coun(1)[0][1] == 5:
            score+= 900
        elif coun(1)[0][1] == 6:
            score+= 1200
    elif coun(1)[0][0] == 4:
        if coun(1)[0][1] == 3:
            score+= 400
        elif coun(1)[0][1] == 4:
            score+= 800
        elif coun(1)[0][1] == 5:
            score+= 1400
        elif coun(1)[0][1] == 6:
            score+= 1600
    elif coun(1)[0][0] == 5:
        if coun(1)[0][1] == 1:
            score+= 50
        elif coun(1)[0][1] == 2:
            score+= 100
        elif coun(1)[0][1] == 3:
            score+= 500
        elif coun(1)[0][1] == 4:
            score+= 1000
        elif coun(1)[0][1] == 5:
            score+= 1500
        elif coun(1)[0][1] == 6:
            score+= 2000
    elif coun(1)[0][0] == 6:
        if coun(1)[0][1] == 3:
            score+= 600
        elif coun(1)[0][1] == 4:
            score+= 1200
        elif coun(1)[0][1] == 5:
            score+= 1800
        elif coun(1)[0][1] == 6:
            score+= 2400
    elif coun(1)[0][0] == 1:
        score+= 1500
    elif coun(1)[0][1] == 2:
        score+= 750
    else:
        score+= 0
    return score

class GameLogic():
    def __init__(self):
        pass

    def calculate_score(self, dice):
        x = up_to_six_threes(dice)
        if x:
            return x
        else:
            return 0

    def roll_dice(self, n):
        list = []
        for i in range(n):
            list.append(random.randint(1, n))
        return(tuple(list))
#------------------------- Basma


class Banker():
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
