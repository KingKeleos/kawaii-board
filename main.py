import keyboard
from sound import sound
import multiprocessing

first_row = {'^','1','2','3','4','5','6','7','8','9','0','ß','backspace'}
second_row=['tab','q','w','e','r','t','z','u','i','o','p','ü','+']
third_row={'a','s','d','f','g','h','j','k','l','ö','ä','#'}
fourht_row={'y','x','c','v','b','n','m',',','.','-'}

def kawaii_board():
    while True:
        try:
            if keyboard.read_key() in first_row:
                p = multiprocessing.Process(target=sound.pitchhighest)
                p.start()
            if keyboard.read_key() in second_row:
                p = multiprocessing.Process(target=sound.pitchhigh)
                p.start()
            if keyboard.read_key() in third_row:
                p = multiprocessing.Process(target=sound.play)
                p.start()
            if keyboard.read_key() in third_row:
                p = multiprocessing.Process(target=sound.pitchlow)
                p.start()
            if keyboard.read_key() == "enter":
                p = multiprocessing.Process(target=sound.pitch_enter)
                p.start()
        except:
            break

if __name__ == '__main__':
    kawaii_board()
