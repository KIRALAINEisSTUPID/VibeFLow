

# ---------------IMPORTS------------------------- #
import time
from colorama import Fore
import os
from os import system
import msvcrt
import pygame
from pygame import mixer
from mutagen.mp3 import MP3  # Для работы с MP3
from mutagen.wavpack import WavPack
import tkinter as tk
from tkinter import filedialog
#---------------IMPORTS-end-------------------------- #
# ---------------FUNCTIONS------------------------- #
def get_input():
    pressed = ''
    while True:
        if msvcrt.kbhit():  
            key = msvcrt.getch().decode('utf-8')

            if key in ['1', '2', '3', '4']:
                if pressed == '':
                    pressed = key 
                    return key
            elif key == '\r':  
                continue

def get_letter_input():
    pressed = ''
    while True:
        if msvcrt.kbhit():  
            key = msvcrt.getch().decode('utf-8')

            if key in ['v', 's', 'p', 'u']:
                if pressed == '':
                    pressed = key 
                    return key
            elif key == '\r':  
                continue
            
            
def get_only_1_letter_input():
    pressed = ''
    while True:
        if msvcrt.kbhit():  
            key = msvcrt.getch().decode('utf-8')

            if key in ['s']:
                if pressed == '':
                    pressed = key 
                    return key
            elif key == '\r':  
                continue



def get_audio_length(file_path):
    try:
        if file_path.endswith('.mp3'):
            audio = MP3(file_path)
        elif file_path.endswith('.wav'):
            audio = WavPack(file_path)
        else:
            return 0

        return audio.info.length  
    except Exception as e:
        print(f"Error : {e}")
        return 0
    
    
    

    
    
    
    
def select_file():
    file_path = filedialog.askopenfilename(title="Choose music file", filetypes=(("Audio Files", "*.mp3;*.wav"), ("All Files", "*.*")))
    return file_path    
    
    
    
def play_music(file_path):
    pygame.mixer.init()  
    pygame.mixer.music.load(file_path)  
    pygame.mixer.music.play()      
    
    
    
def pause_music():
    pygame.mixer.music.pause()  
    
def unpause_music():
    pygame.mixer.music.unpause()  # Возобновляем воспроизведение


    
def volume_controling(volume):
    pygame.mixer.music.set_volume(volume)  # Устанавливаем громкость (от 0 до 1)

    
    
    
def show_status(file_path):
    # Получаем информацию о музыке
    length = int(get_audio_length(file_path))  # Длительность музыки в секундах
    current_pos = int(pygame.mixer.music.get_pos() / 1000)  # Текущее положение в секундах
    volume = pygame.mixer.music.get_volume()  # Текущая громкость (0.0 до 1.0)

    print(f"Length: {length:.2f} секунд")
    print(f"Played: {current_pos:.2f} секунд")
    print(f"VOlume: {volume:.2f}")
    print("Not played: ", length - current_pos)
    
    
# ---------------FUNCTIONS-ends------------------------- #
#----------------Modes------------------------- #
def choosen_music():
    time.sleep(1)
    os.system("cls")
    file_path = ""
    print("Which music file do you want to play?")
    first_time = get_only_1_letter_input()
    if first_time == 's':
        file_path=select_file()
        if file_path:
            play_music(file_path)
            print(f"Воспроизведение {file_path} началось.")
            while True:
                show_status(file_path)
                time.sleep(1)
                os.system("cls")
    
        
    
        
    




    
    
    

def vibeflow_folder():
    time.sleep(1)
    os.system("cls") 
    path = "music"
    music_extensions = {".mp3", ".wav",}

    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Folder '{path}' was created, because it didn't exist.")
        return  

    only_music = True
    files_in_folder = os.listdir(path) 

    if not files_in_folder:  
        only_music = False
    else:
        for file in files_in_folder:
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path): 
                _, ext = os.path.splitext(file)
                if ext.lower() not in music_extensions:  
                    only_music = False
                    break

    if only_music and files_in_folder: 
        print("Music is running")
    else:
        print(f"There are no music files in the folder '{path}'")
        print(Fore.MAGENTA + "`✦ 1.Return to the main menu?"+Fore.RESET, Fore.RED + "exit any other key to stop program`✦"+Fore.RESET)
        choice = get_input()
        if choice == '1':   
            main_menu()


def main_menu():
    system("cls")
    Vibeflow = Fore.MAGENTA + "VibeFlow" + Fore.RESET
    print(f"             Welcome to {Vibeflow} - A tiny music player")
    print(Fore.GREEN + "----------------------------------------------------------------"+Fore.RESET)
    print("1.                Play Choosen Music             ")
    print("2.                Open Vibeflow music folder")
    print("3.                Download Music from Vibeflow-site")
    print("4.                Exit")
    print(Fore.GREEN + "----------------------------------------------------------------"+Fore.RESET)
    print(Fore.GREEN + "----------------------------------------------------------------"+Fore.RESET)
    print(Fore.GREEN + "  `✦ ˑ ִֶ 𓂃⊹ ----------------------------------`✦ ˑ ִֶ 𓂃⊹    "+Fore.RESET)
    choice = get_input() 
    if choice == '1':
        system("cls")
        print("You choosed 'Play Choosen Music'")
        choosen_music()
        
    elif choice == '2':
        system("cls")
        print("You choosed  'Open Vibeflow music folder'")
        vibeflow_folder()
    elif choice == '3':
        system("cls")
        print("You choosed  'Download Music from Vibeflow-server'")
    elif choice == '4':
        system("cls")
        print("You choosed  'Exit'")
        exit()


    
    
    
    
    
    
#----------------Modes-end------------------------- #
#----------------Main------------------------- #
    
def main():
    os.system("cls")
    Vibeflow = Fore.MAGENTA + "VibeFlow" + Fore.RESET
    print(f"Welcome to {Vibeflow} - A tiny music player")
    time.sleep(3)
    main_menu()
    
    
#----------------Main-end------------------------- #
if __name__ == "__main__":
    main()
