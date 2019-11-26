from CupOfCoffee import CupOfCoffee
from CupOfTea import CupOfTea

def processcup(drink):
    #c.type("gla")
    drink.Milk(6)
    drink.Sugar(10)
    drink.AddMilk()
    drink.AddSugar()
    drink.Drink()
    drink.Wash()
    drink.Refill()

if __name__ == '__main__':
    x = int(input("choose your drink: 1 - Coffee, 2 - Tea "))
    if(x==1):
        c = CupOfCoffee('robusta')
        print(c._bean)
        processcup(c)
    elif (x==2):
        t = CupOfTea('green')
        print(t._leaf)
        processcup(t)
    else:
        print("there is no such drink")
