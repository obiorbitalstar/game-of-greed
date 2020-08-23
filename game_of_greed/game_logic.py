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
def up_to_six_threes():
    pass
def from_three_fours():
    pass
class GameLogic():
    def __init__(self):
        pass
    def calculate_score(self,dice=(1,1,1,1,1,1)):

        #----------------------------- 1 - 3  Mohmmad
        #----------------------------- 4 -6 saed

        pass
    def roll_dice(self,n):
      list = []
      for i in range(n):
        list.append(random.randint(1,n))
      return(tuple(list))
#------------------------- Basma
class Banker():
    def __init__(self):
        self.balance = 0
        self.shelved = 0
    def shelf(slef, int):
        self.shevled += int
        return self.shelved
    def bank(self, balance):
        self.balanc += self.shelved
        clear_shlef()
        return self.balance
    def clear_shelf(self):
        self.shelved = 0
        return self.shelved

if __name__ == "__main__":
    n=GameLogic()
    print(n.roll_dice(6))
