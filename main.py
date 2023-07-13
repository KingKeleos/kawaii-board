import keyboard
from sound import sound
import multiprocessing
from threading import Thread
from pynput.keyboard import Key, Listener

first_row = {'^','1','2','3','4','5','6','7','8','9','0','ß','backspace'}
second_row=['tab','q','w','e','r','t','z','u','i','o','p','ü','+']
third_row={'a','s','d','f','g','h','j','k','l','ö','ä','#'}
fourth_row={'y','x','c','v','b','n','m',',','.','-'}

def kawaii_board(key):
        try:
            if key.char in first_row:
                sound.pitchhighest()
            elif key.char in second_row:
                sound.pitchhigh()
            elif key.char in third_row:
                sound.play()
            elif key.char in fourth_row:
                sound.pitchlow()
            elif key == Key.enter:
                sound.pitch_enter()
        except:
            return

def stop(key):
    if key == Key.esc:
        sound.pitch_enter()
        return False

if __name__ == '__main__':
    print("Initiating UwU...")
    with Listener(
        on_press=kawaii_board,
        on_release=stop) as listener:
        listener.join()
