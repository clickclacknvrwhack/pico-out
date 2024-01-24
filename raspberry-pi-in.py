import RPi.GPIO as GPIO
import time
import threading
import os

STACEY_PIN = 17
BRIAN_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(STACEY_PIN, GPIO.IN)
GPIO.setup(BRIAN_PIN, GPIO.IN)

allowed_to_talk = None

def play_sound():
        print('hey, stop talking')

def check_pico_input():
        global allowed_to_talk
        while True:
                if GPIO.input(STACEY_PIN) and allowed_to_talk != "stacey":
                        play_sound()
                        print('stacey is talking, but shouldnt be talking')
                elif GPIO.input(BRIAN_PIN) and allowed_to_talk != "brian":
                        play_sound()
                        print('brian is talking talking out of turn')
                time.sleep(0.1)


def get_user_input():
        global allowed_to_talk 
        while True:
                user_input = input("Press 1 to allow Stacey to tslk, 2 for Brian or q for quit:")
                if user_input == "1":
                        allowed_to_talk = "stacey"
                        print("Stacey is allowed to talk.")
                elif user_input == "2":
                        allowed_to_talk = "brian"
                        print("Brian is allowed to talk.")
                elif user_input.lower() =="q":
                        print("bye")
                        GPIO.cleanup()
                        os._exit(0)


input_thread = threading.Thread(target=check_pico_input)
input_thread.daemon = True
input_thread.start()

user_input_thread = threading.Thread(target=get_user_input)
user_input_thread.start()