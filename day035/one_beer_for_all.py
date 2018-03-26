# -*- coding: utf-8 -*-

from matches import matches
from read_profiles import PROFILES, BEER_PROFILES

def title():
    print('''
    /\|\ |[~  |)[~[~|)  [~/\|)   /|| | 
    \/| \|[_  |)[_[_|\  | \/|\  /-||_|_
        ''')

def about():
    print('')
    print('My name is Hector, I\'m passionate to technology/videogames, martial arts and craft beer of course!')
    print('Even though my coding skills aren\'t that great I won\'t surrender')
    print('This project was made for the mere purpose of having fun and shouldn\'t be taken seriously')
    print('By the way, if you read until this part, now you owe me a beer ;)')

def questions(adjectives_list, answer_most, answer_least, square, zeth, star, triangle):
    for i in range(3): #27
        print('''
            Question #{}
            [1]{}
            [2]{}
            [3]{}
            [4]{}
        '''.format(i + 1, adjectives_list[i][0], adjectives_list[i][1], adjectives_list[i][2], adjectives_list[i][3]))
        
        answer_most = int(raw_input('You\'re MOST inditified with the number: '))
        if answer_most == 1:
            square += 1
        elif answer_most == 2:
            zeth += 1
        elif answer_most == 3:
            star +=1
        elif answer_most == 4:
            triangle += 1
        else:
            while answer_most < 0 or answer_most > 4:
                print('Invalid option, try again')
                answer_most = int(raw_input('You\'re MOST inditified with the number: '))
        

        answer_least = int(raw_input('You\'re LEAST inditified with the number: '))
        if answer_least == 1:
            square -= 1
        elif answer_least == 2:
            zeth -= 1
        elif answer_least == 3:
            star -=1
        elif answer_least == 4:
            triangle -= 1
        else:
            while answer_least < 0 or answer_least > 4:
                print('\nInvalid option, try again')
                answer_least = int(raw_input('You\'re LEAST inditified with the number: '))

        while answer_least == answer_most:
            print('\nLEAST value can\'t be the same as MOST!!')
            answer_least = int(raw_input('You\'re LEAST inditified with the number: '))

        #print(square, zeth, star, triangle)
        
        #print(result)

    return matches([square, zeth, star, triangle])

def final_result(result):
    final_number = int(''.join(str(x) for x in result))

    for prof in PROFILES:
        if prof['number'] == final_number:
            profile = prof
    
    return BEER_PROFILES[profile['profile']], profile['profile']
    

def run():
    #Variables declaration
    # - Variables for test
    square = 0
    triangle = 0
    star = 0
    zeth = 0
    answer_most = 0
    answer_least = 0
    # --
    square_result = 0
    zeth_result = 0
    star_result = 0
    triangle_result =0
    

    #List declarations
    adjectives_numbers = [1, 2, 3, 4]
    adjectives_list = [
        # SQUARE - ZETH - STAR - TRIANGLE
        ['Enthusiastic', 'Daring', 'Diplomatic', 'Satisfied'],
        ['Convincing', 'Determined', 'Cautious', 'Good-Natured'],
        ['Friendly', 'Outspoken', 'Accurate', 'Calm'],
        ['Talkative', 'Decisive', 'Controlled', 'Conventional'],
        ['Outgoing', 'Adventurous', 'Insightful', 'Moderate'],
        ['Persuasive', 'Original', 'Humble', 'Gentle'],
        ['Expressive', 'Dominant', 'Conscientious', 'Responsive'],
        ['Poised', 'Impatient', 'Observant', 'Modest'],
        ['Magnetic', 'Insistent', 'Tactful', 'Agreeable'],
        ['Inspiring', 'Brave', 'Timid', 'Submissive'],
        ['Cheerful', 'Strong-Willed', 'Reserved', 'Obliging'],
        ['Stimulating', 'Independent', 'Perceptive', 'Kind'],
        ['Playful', 'Firm', 'Fussy', 'Obedient'],
        ['Attractive', 'Stubborn', 'Introspective', 'Predictable'],
        ['Charming', 'Bold', 'Logical', 'Loyal'],
        ['Sociable', 'Self-Reliant', 'Soft-Spoken', 'Patient'],
        ['High-Spirited', 'Eager', 'Thorough', 'Willing'],
        ['Extroverted', 'Agressive', 'Fearful', 'Amiable'],
        ['Condifendt', 'Assertive', 'Impartial', 'Sympathetic'],
        ['Animated', 'Persistent', 'Well-Disciplined', 'Generous'],
        ['Impulsive', 'Forceful', 'Introverted', 'Easygoing'],
        ['Good mixer', 'Vigorous', 'Refined', 'Lenient'],
        ['Captivating', 'Demanding', 'Compliant', 'Contended'],
        ['Light-Hearted', 'Argumentative', 'Systematic', 'Cooperative'],
        ['Jovial', 'Direct', 'Precise', 'Even-Tempered'],
        ['Appealing', 'Restless', 'Careful', 'Neighbourly'],
        ['Optimistic', 'Pionering', 'Respectful', 'Helpful'],

        ]
    
    option = 0
    valid = False
    
    #Welcome title and directions
    print('Because there\'s a CHELA for everyone!\n')
    print('Always wondered which beer style is suited for you?\nGuess no more!')
    print('Based in your personality we\'ll discover the right style for you ;)')

    #Validation to choose an option
    while valid == False:
        title()
        option = int((raw_input('''
            Choose an option and press ENTER:
            [1] Instructions
            [2] DO the test!
            [3] How does this work?
            [4] About
        ''')))

        if option == 1:
            print('\nYou will answer 28 questions where you\'ll pick 2 adjectives out of 4')
            print('Choose the one that suits you MOST and LEAST')
        elif option == 2:
            valid = True
            print('\nLet\'s dri... Begin! ')
            print('')
            result = questions(adjectives_list, answer_most, answer_least, square, zeth, star, triangle)
            user_profile, user_beer_style = final_result(result)
            print(user_profile, str(user_beer_style))

        elif option == 3:
            print('\nThat\'s actually a good question!...\nGood enough that I don\'t have the answer\nWhy not try it by yourself?')
        elif option == 4:
            about()
        else:
            print('\nNot a valid option... Or you\'re too drunk\nTry again')
    
            



if __name__ == '__main__':
    run()