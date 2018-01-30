# -*- coding: utf-8 -*-

def run ():
    countdown = int(raw_input('Set the countdown (seconds)... '))

    for countdown in range(countdown, -1, -1):
        if countdown != 0:
            print(countdown)
        elif countdown == 0:
            print(countdown)
            print('BLAST OFF!')

if __name__ == '__main__':
    run()