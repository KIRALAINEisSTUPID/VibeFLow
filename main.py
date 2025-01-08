

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
pygame.init()
#---------------IMPORTS-end-------------------------- #
# ---------------FUNCTIONS------------------------- #
def get_input():
    pressed = ''
    while True:
        if msvcrt.kbhit():  
            key = msvcrt.getch().decode('utf-8')

            if key in ['1', '2', '3', '4', '5']:
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
    
    

    

def show_status(file_path):
    # Получаем информацию о музыке
    length = int(get_audio_length(file_path))  # Длительность музыки в секундах
    current_pos = int(pygame.mixer.music.get_pos() / 1000)  # Текущее положение в секундах
    volume = pygame.mixer.music.get_volume()  # Текущая громкость (0.0 до 1.0)
    music_name = os.path.basename(file_path)  # Получаем имя файла музыки

    print(f"Music path: {file_path}")
    print(f"Music Name: {music_name}")
    print(f"Length: {length:.2f} sec")  
    print(f"Played: {current_pos:.2f} sec")
    print("Not played: ", length - current_pos)
    if current_pos == length:
        print("Music has ended")
        time.sleep(1)
        main_menu()

 
def show_status2(file_path):
    # Получаем информацию о музыке
    length = int(get_audio_length(file_path))  # Длительность музыки в секундах
    current_pos = int(pygame.mixer.music.get_pos() / 1000)  # Текущее положение в секундах
    volume = pygame.mixer.music.get_volume()  # Текущая громкость (0.0 до 1.0)
    music_name = os.path.basename(file_path)  # Получаем имя файла музыки

    print(f"Music path: {file_path}")
    print(f"Music Name: {music_name}")
    print(f"Length: {length:.2f} sec")  
    print(f"Played: {current_pos:.2f} sec")
    print("Not played: ", length - current_pos)
    if current_pos == length:
        print("Music has ended")
        time.sleep(1)
        vibeflow_folder() 
          
def choose_music(files, index):
    try:
        # Получаем текущую директорию
        current_directory = os.getcwd()
        # Формируем путь к файлу
        music_directory = os.path.join(current_directory, "music")
        file_to_play = os.path.join(music_directory, files[index - 1])
        
        # Проверяем, существует ли файл
        if not os.path.exists(file_to_play):
            print(f"Error: File not found at {file_to_play}")
            return

        # Проигрываем файл
        play_music(file_to_play)
        print(f"Playing started: {file_to_play}")
        time.sleep(1)
        
        # Имитация процесса воспроизведения
        playing = True
        while playing:
            show_status2(file_to_play)
            time.sleep(1)
            os.system("cls")  # Очистка экрана
    except IndexError:
        print("Invalid index. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
  
    
# ---------------FUNCTIONS-ends------------------------- #
#----------------Modes------------------------- #
def choosen_music():
    time.sleep(1)
    os.system("cls")
    file_path = ""
    print("S.Choose music to play:")
    first_time = get_only_1_letter_input()
    if first_time == 's':
        file_path=select_file()
        if file_path:
            print(f"Playing started {file_path} .")
            time.sleep(1)
            play_music(file_path)
            
            playing = True
            while playing:
                show_status(file_path)
                time.sleep(1)
                os.system("cls")
                




        
def guide_mode():
    time.sleep(1)
    system("cls")
    print(Fore.YELLOW + "Welcome to the guide mode" + Fore.RESET)
    print(Fore.MAGENTA+"""⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢋⣩⣉⢻
⣿⣿⣿⠀⣿⣶⣕⣈⠹⠿⠿⠿⠿⠟⠛⣛⢋⣰⠣⣿⣿⠀⣿
⣿⣿⣿⡀⣿⣿⣿⣧⢻⣿⣶⣷⣿⣿⣿⣿⣿⣿⠿⠶⡝⠀⣿
⣿⣿⣿⣷⠘⣿⣿⣿⢏⣿⣿⣋⣀⣈⣻⣿⣿⣷⣤⣤⣿⡐⢿
⣿⣿⣿⣿⣆⢩⣝⣫⣾⣿⣿⣿⣿⡟⠿⠿⠦⠀⠸⠿⣻⣿⡄⢻
⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⠇⣼
⣿⣿⣿⣿⣿⣿⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰
⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣿
⣿⣿⣿⣿⣿⠏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿
⣿⣿⣿⣿⠟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿
⣿⣿⣿⠋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣿
⣿⣿⠋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸"""+Fore.RESET)
    print(Fore.YELLOW + "Here you can learn how to use the player" + Fore.RESET)
    time.sleep(2)
    system("cls")
    print(Fore.YELLOW + "How to  choose?" + Fore.RESET)
    time.sleep(3)
    print(Fore.YELLOW + "To choose options or files you need enter that sysbols near them for example:" + Fore.RESET)
    print(Fore.YELLOW + "345.My old piano album.mp3  <--- you need write 345 to play it on player" + Fore.RESET)
    time.sleep(3)
    print(Fore.YELLOW + "s.Choose music to play <--- you need write s to choose music to play" + Fore.RESET)
    print(Fore.RED +"You will returned to main menu in 5 seconds"+Fore.RESET)
    time.sleep(3)
    print(Fore.RED + "5..."+Fore.RESET)
    time.sleep(1)
    print(Fore.RED + "4..."+Fore.RESET)
    time.sleep(1)
    print(Fore.RED + "3..."+Fore.RESET)
    time.sleep(1)
    print(Fore.RED + "2..."+Fore.RESET)
    time.sleep(1)
    print(Fore.RED + "1..."+Fore.RESET)
    time.sleep(1)
    main_menu()

        
    



    
    
    

def vibeflow_folder():
    time.sleep(1)
    os.system("cls") 
    path = "music"
    music_extensions = {".mp3", ".wav",}

    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Folder '{path}' was created, because it didn't exist.")
        time.sleep(1)
        main_menu()

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
        print(f"Folder '{path}' contains only music files:")
        for index, file in enumerate(files_in_folder, start=1):
             print(f"{index}. {file}")
             choice = int(input("Choose music to play (by index,write 0 to return): "))
             if choice == 0:
                    main_menu()
             else:
                choose_music(files_in_folder, choice)            
             
    else:
        print(f"There are not only music files in the folder or they dont exist'{path}'")
        print(Fore.MAGENTA + "`✦ 1.Return to the main menu?"+Fore.RESET, Fore.RED + "exit any other key to stop program`✦"+Fore.RESET)
        choice = get_input()
        if choice == '1':   
            main_menu()


def main_menu():
    system("cls")
    Vibeflow = Fore.MAGENTA + "VibeFlow" + Fore.RESET
    guide = Fore.YELLOW + "Guide" + Fore.RESET
    print(f"             Welcome to {Vibeflow} - A tiny music player")
    print(Fore.GREEN+f"                           Main Menu                     "+Fore.RESET)
    print(Fore.GREEN + "----------------------------------------------------------------"+Fore.RESET)
    print("1.                Play Choosen Music             ")
    print("2.                Open Vibeflow music folder")
    print("3.                Download Music from Vibeflow-site")
    print("4.                Exit")
    print(Fore.GREEN + "----------------------------------------------------------------"+Fore.RESET)
    print(Fore.GREEN + "----------------------------------------------------------------"+Fore.RESET)
    print(Fore.GREEN + "  `✦ ˑ ִֶ 𓂃⊹ --------credits by Kiralaine-----------------`✦ ˑ ִֶ 𓂃⊹    "+Fore.RESET)
    print(f"              ------Touch 5 to open {guide}------   ")
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
        print("Coming soon")
        time.sleep(1)
        main_menu()
    elif choice == '4':
        system("cls")
        print("You choosed  'Exit'")
        exit()
        
    elif choice == '5':
        system("cls")
        print("You choosed  'Guide'")
        guide_mode()


    
    
    
    
    
    
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
