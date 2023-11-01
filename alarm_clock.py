import pygame
import time

def clear_screen():
    print("\n" * 50)  # Print enough newlines to "clear" the screen

def alaram(seconds):
    pygame.init()
    sound = pygame.mixer.Sound("Alarm-Fast-A1-www.fesliyanstudios.com.mp3")
    time_elapsed = 0

    clear_screen()
    
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60

        clear_screen()
        print(f"{time_left:02d}:{minutes_left:02d}")

    sound.play()
    pygame.time.delay(3000)

minutes = (int(input("How many minutes to wait : ")))
seconds = (int(input("How many seconds to wait : ")))
timer = minutes * 60 + seconds

alaram(timer)

