import time
import multiprocessing
import keyboard
from sound import sound
import threading

first_row = {'^','1','2','3','4','5','6','7','8','9','0','ß','backspace'}
second_row=['tab','q','w','e','r','t','z','u','i','o','p','ü','+']
third_row={'a','s','d','f','g','h','j','k','l','ö','ä','#'}
fourth_row={'y','x','c','v','b','n','m',',','.','-'}

def kawaii_board():
    print("Redeemed Channel Points, UwU intensifying...")
    t_end =time.time() + 1 * 60
    p = multiprocessing.Process(target=playBoard)
    p.start()

def playBoard():
    t_end =time.time() + 1 * 60
    while time.time() < t_end:
        try:
            if keyboard.read_key() in first_row:
                thread = threading.Thread(target=sound.pitchhighest)
                thread.start()
            if keyboard.read_key() in second_row:
                thread = threading.Thread(target=sound.pitchhigh)
                thread.start()
            if keyboard.read_key() in third_row:
                thread = threading.Thread(target=sound.play)
                thread.start()
            if keyboard.read_key() in fourth_row:
                thread = threading.Thread(target=sound.pitchlow)
                thread.start()
            if keyboard.read_key() == "enter":
                thread = threading.Thread(target=sound.pitch_enter)
                thread.start()
        except:
            break