# -*- coding: utf-8 -*-

def run():
    name = str(raw_input('What\'s your name?: '))

    for i in range(10):
        print(name)

    print('I think I can remember it...')

if __name__ == '__main__':
    run()