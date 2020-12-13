# For test_madlib.py
#################################################################
import re

def read_template(x):
    with open(x) as text:
        text_read = text.read()
        return text_read

def parse_template(txt):
    result = tuple(re.findall(r"\{([A-Za-z0-9 '_]+)\}", txt))
    new_txt = txt.replace(result[0], "")
    new_txt = new_txt.replace(result[2], "")
    return(new_txt, result)

def merge(one, two):
    new_str = one.format(two[0], two[1], two[2])
    print(new_str)
    return new_str
#################################################################

print("***********************************************************************************")
print('Welcome to my madlib game! Follow the prompts and enter what you\'d like to enter')
print("***********************************************************************************")

adj1 = input('give me an adjective ')
adj2 = input('give me another adjective ')
first_name = input('what is your name? ')
past_tense = input('give me a past tense verb ')
adj3 = input('another adjective please ')
adj4 = input('more adjectives! ')
noun1 = input('and a plural noun ')
ani1 = input('your favorite large animal is... ')
ani2 = input('your favorite small animal is... ')
girl = input('enter a girl\'s name ')
adj5 = input('you guessed it, another adjective please! ')
noun2 = input('let\'s get another plural noun ')
adj6 = input('adjective please! ')
noun3 = input('one more plural noun ')
num50 = input('select a number 1 - 50 ')
num = input('enter any number ')
noun4 = input('another plural noun ')
num2 = input('enter any number ')
noun5 = input('last plural noun ')

with open('../assets/madlib.txt', 'r') as madlib:
    updated = madlib.read() 

    # updated = updated[22:]
    updated = updated.replace('{Adjective}', adj1, 1)
    updated = updated.replace('{Adjective}', adj2, 1)
    updated = updated.replace('{A First Name}', first_name)
    updated = updated.replace('{Past Tense Verb}', past_tense)
    updated = updated.replace('{Adjective}', adj3, 1)
    updated = updated.replace('{Adjective}', adj4, 1)
    updated = updated.replace('{Plural Noun}', noun1, 1)
    updated = updated.replace('{Large Animal}', ani1)
    updated = updated.replace('{Small Animal}', ani2)
    updated = updated.replace("{A Girl's Name}", girl)
    updated = updated.replace('{Adjective}', adj5, 1)
    updated = updated.replace('{Plural Noun}', noun2, 1)
    updated = updated.replace('{Adjective}', adj6, 1)
    updated = updated.replace('{Plural Noun}', noun3, 1)
    updated = updated.replace('{Number 1-50}', num50)
    updated = updated.replace("{First Name's}", f"{first_name}'s")
    updated = updated.replace('{Number}', num, 1)
    updated = updated.replace('{Plural Noun}', noun4, 1)
    updated = updated.replace('{Number}', num2, 1)
    updated = updated.replace('{Plural Noun}', noun5, 1)
    print("***********************************************************************************")
    print(updated)
    print("***********************************************************************************")
    
with open('../assets/madlib1.txt', 'wt') as madlib1:
    madlib1.write(updated)