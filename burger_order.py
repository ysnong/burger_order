#This is a program that simulates an online order system for a burger restaurant called Grillby's
#Author: Yun Shan Nong


#Global variables
bun_options = ['regular', 'gluten-free', 'veggie', 'sesame', 'french', 'italian', 'potato',
               'multigrain', 'golden', 'cold', 'icing', 'baguette']

topping_options = ['cheddar', 'feta', 'swiss', 'tomato', 'cucumbers', 'green olives',
                   'lettuce', 'red onions', 'kimchi', 'boba','jelly grass',
                   'pineapple','poutine', 'mango', 'chocolat']

base_cost = [5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 7.0, 6.0, 6.6, 5.59] #cost of the bun

toppings_list = []

bun_choice = [] 

def greet():
    """() - NoneType
    Displays a greeting message to the users
    
    >>> greet()
    Welcome to Grillby's! Are you hungry? Then start your order ASAP!
    """
    print("Welcome to Grillby's! Are you hungry? Then start your order ASAP!")
    
def burger_choice():
    """() - NoneType
    Asks the users what kind of bun do they want. The functions keeps asking the user
    until they enter a valid option.
    
    >>> burger_choice()
    What kind of burger do you want?: regular
    >>> print(bun_choice)
    ['regular']
    
    >>> burger_choice()
    What kind of burger do you want?: vegetarian
    What kind of burger do you want?: multigrain
    >>> print(bun_choice)
    ['multigrain']
    """
    
    bun = ''
    
    while bun not in bun_options:
        if bun in bun_options:
            break
        bun = input('What kind of burger do you want?: ')
      
    bun_choice.append(bun)
        
def toppings():
    """() - NoneType
    Asks the users what toppings they want. Do not allow duplicate toppings.
    Keep track of toppings entered by the user by storing them into a list
    
    >>> toppings()
    Enter a topping: cheddar
    Enter a topping: tomato
    Enter a topping: tomato
    Enter a topping: done
    >>> print(toppings_list)
    ['cheddar', 'tomato']
    
    >>> toppings()
    Enter a topping: cheese
    Enter a topping: boba
    Enter a topping: tomato
    Enter a topping: pineapple
    Enter a topping: done
    >>> print(toppings_list)
    ['boba', 'tomato','pineapple']
    
    """
    
    topping = ''
    
    while topping != 'done':
        topping = input('Enter a topping: ')
        if topping not in toppings_list and topping in topping_options:
            if topping != 'done':
                toppings_list.append(topping)
                

def price_cal():
    """() - float
    Returns the total price of the order according to user's previous choice
    
    >>> toppings_list = ['feta','swiss','cucumber']
    >>> bun_choice = ['golden']
    >>> price_cal()
    8.25
    
    >>> toppings_list = ['kimchi','tomato','lettuce','cucumber','green olives']
    >>> bun_choice = ['veggie']
    >>> price_cal()
    12.7
    
    >>> toppings_list = ['boba','pineapple','mango','poutine']
    >>> bun_choice = ['icing']
    >>> price_cal()
    8.5
    
    """
    #bun price (base price)
    i = 0 #number of position in the list
    
    for opt in bun_options:
        if opt == bun_choice[0]:
            break
        i += 1 #i represents the position in the list
        
    bun_price = base_cost[i] #get the correspond price
    
    #toppings price
    extra_toppings = []
    toppings_price = 0.0
    
    if len(toppings_list) > 1:
        
        if toppings_list[0] == 'kimchi':
            toppings_price += 5.0
            extra_toppings = toppings_list[3:]
        elif toppings_list[1] == 'kimchi':
            toppings_price += 5.0
            extra_toppings = toppings_list[3:]
        elif len(toppings_list) > 2:
            extra_toppings = toppings_list[2:]
        
    for i in range(len(extra_toppings)):
        
        if extra_toppings[i] == 'kimchi':
            toppings_price += 5.0
        else:
            toppings_price += 1.25
            
    total_price = bun_price + toppings_price
    
    return total_price
    
    
def main():
    """() --> NoneType
    Outputs the receipt of the order, including the choices of bun and toppins and
    the total price
    
    >>> What kind of burger do you want?: french
    >>> Enter a topping: kimchi
    >>> Enter a topping: feta
    >>> Enter a topping: green olives
    >>> Enter a topping: done
    You ordered:  french
    with these toppings: 
    kimchi
    feta
    green olives
    Your total price is:  10.0 $    
    """
    greet()
    burger_choice()
    toppings()
    
    print('You ordered: ', bun_choice[0])
    
    print('with these toppings: ')
    
    for choice in toppings_list:
        print('\t', choice)
    print('Your total price is: ', price_cal(), '$')
    
main()