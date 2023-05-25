from CupOfCoffee import CupOfCoffee
from CupOfTea import CupOfTea

def processcup(drink):
    drink.Milk(6)
    drink.Sugar(10)
    drink.Volume = 0.3
    drink.Type = 'glass'
    drink.AddMilk()
    drink.AddSugar()
    drink.Drink()
    drink.Wash()
    drink.Refill()

if __name__ == '__main__':
    x = int(input('choose your drink: 1 - Coffee, 2 - Tea '))
    if(x==1):
        c = CupOfCoffee('robusta')
        processcup(c)
    elif (x==2):
        t = CupOfTea('test leaf')
        processcup(t)
    else:
        print('there is no such drink')