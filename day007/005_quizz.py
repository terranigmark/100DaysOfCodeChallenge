# -*- coding: utf-8 -*-

def run():
    print('##### QUIZZ GAME #####')
    
    correct_answers = 0
    answer = raw_input('1. How many primary colors are there?: ')
    if answer == '3':
        print('Right answer!')
        correct_answers += 1
    else:
        print('Too bad, wrong answer...')
    
    answer = raw_input('2. Who is Harry Potter\'s rival?:')
    if answer.lower() == 'draco' or answer.lower() == 'draco malfoy' or answer.lower() == 'malfoy':
        print('Right answer!')
        correct_answers += 1
    else:
        print('Too bad, wrong answer...')

    answer = raw_input('3. What animal has 9 lives?: ')
    if answer.lower() == 'cat' or answer.lower() == 'a cat' or answer.lower() == 'cats':
        print('Right answer!')
        correct_answers += 1
    else:
        print('Too bad, wrong answer...')

    answer = raw_input('4. How many Ninja Turtles are?: ')
    if answer == '4':
        print('Right answer!')
        correct_answers += 1
    else:
        print('Too bad, wrong answer...')

    answer = raw_input('5. What\'s the name for Japanese comics?: ')
    if answer.lower() == 'manga':
        print('Right answer!')
        correct_answers += 1
    else:
        print('Too bad, wrong answer...')
    
    print('You had {} correct answers out of 5'.format(correct_answers))
    print('That\'s {}% correct answers'.format(percentage))

if __name__ == '__main__':
    run()