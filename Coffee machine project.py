menu={
    'Expresso':{
        'ingredients':{
            'water':50,
            'coffee':18
        },
        'cost':1.5
    },

    'latte':{
        'ingredients':{
            'water':200,
            'milk':150,
            'coffee':24
        },
        'cost':2.5
    },

    'Cappuccino':{
        'ingredients':{
            'water':250,
            'milk':100,
            'coffee':24
        },
        'cost':3.0
    }
}
profit=0
resources = {
    'water':300,
    'milk':200,
    'coffee':100
}

def is_resource_sufficient(order_ingredients):
    for i in order_ingredients:
        if order_ingredients[i]>=resources[i]:
            print(f'sry not enough ingredients {i}')
            return False
        return True
    
def process_coins():
    print('enter coins')
    t=int(input('No. of quaters: '))*0.25
    t+=int(input('No. of dims: '))*0.10
    t+=int(input('No. of nickels: '))*0.05
    t+=int(input('No. of pennies: '))*0.01
    return t

def is_tansiction_comp(mon_rece,drink_cos):
    if mon_rece>=drink_cos:
        change=round(mon_rece-drink_cos,2)
        print(f'Here is your change {change}')
        global profit
        profit+=drink_cos
        return True
    else:
        print(f'Sry thats not enough money there mate, u broke as hell damn,, heres you money back {mon_rece}')
        return False

def make_coffee(drink_name,order_ingredients):
    for i in order_ingredients:
        resources[i]-=order_ingredients[i]
    print(f'here is you {drink_name}☕')

is_on=True

while is_on:
    ch=input('What would you like?(Expresso/latte/cappuccino): ')
    if ch=='off':
        is_on=False
    elif ch=='report':
        print(resources)
        print(profit)
    else:
        drink=menu[ch]
        if is_resource_sufficient(drink['ingredients']):
            pay=process_coins()
            if is_tansiction_comp(pay,drink['cost']):
                make_coffee(ch,drink['ingredients'])