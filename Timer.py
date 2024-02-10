
import time
import pygame
def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
try:
    x = float(input('enter the time in seconds'))
except ValueError:
        print('Please enter a valid number.')
while x > 0 :
    time.sleep(1)
    x -=1
    print('========================================================================')
    print('time remaining')
    print(x)
if x == 0 :
    audio_file_path = "MV27TES-alarm.mp3"
    play_audio(audio_file_path)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        print('time is over')
        time.sleep(10)
        break
        
        

               


        

               
