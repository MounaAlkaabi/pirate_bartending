import random


def drink():
    
    
    questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
        
    }
    
    ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
        
    }
    
    


    
    for value in questions.values():
        print(value)
        
        
        answer = bool(raw_input ("> "))
       
       
        if answer in ("y", "yes"):
            answer = True
        else:
            answer = False
        preference=dict()
        preference=(questions[value], answer)
        
    print(preference)
        






if __name__ == '__main__':
    drink()
    