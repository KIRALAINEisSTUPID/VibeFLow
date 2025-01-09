

# ---------------IMPORTS------------------------- #
import time
from colorama import Fore
import os
from os import system
import msvcrt
import pygame
import requests
import json

from pygame import mixer
from mutagen.mp3 import MP3  # Для работы с MP3
from mutagen.wavpack import WavPack
import tkinter as tk
import re
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


def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', '', filename)           
            
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

def load_api_key(config_file):
    try:
        with open(config_file, "r") as file:
            config = json.load(file)
            return config.get("api_key")
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_file}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{config_file}'.")
        return None

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
    length = int(get_audio_length(file_path)) 
    current_pos = int(pygame.mixer.music.get_pos() / 1000)  
    volume = pygame.mixer.music.get_volume() 
    music_name = os.path.basename(file_path)

    print(f"Music path: {file_path}")
    print(f"Music Name: {music_name}")
    print(f"Length: {length} sec")  
    print(f"Played: {current_pos} sec")
    print("Not played: ", length - current_pos)
    if current_pos == length:
        print("Music has ended")
        time.sleep(1)
        main_menu()

 
def show_status2(file_path):
    length = int(get_audio_length(file_path)) 
    current_pos = int(pygame.mixer.music.get_pos() / 1000)  
    volume = pygame.mixer.music.get_volume()  
    music_name = os.path.basename(file_path)  

    print(f"Music path: {file_path}")
    print(f"Music Name: {music_name}")
    print(f"Length: {length:} sec")  
    print(f"Played: {current_pos} sec")
    print("Not played: ", length - current_pos)
    if current_pos == length:
        print("Music has ended")
        time.sleep(1)
        vibeflow_folder() 
          
def choose_music(files, index):
    try:
        current_directory = os.getcwd()
        music_directory = os.path.join(current_directory, "music")
        file_to_play = os.path.join(music_directory, files[index - 1])
        
        if not os.path.exists(file_to_play):
            print(f"Error: File not found at {file_to_play}")
            return

        play_music(file_to_play)
        print(f"Playing started: {file_to_play}")
        time.sleep(1)
        
        playing = True
        while playing:
            show_status2(file_to_play)
            time.sleep(1)
            os.system("cls") 
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

        
    



def download_with_youtube():
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
    
    # Загружаем API-ключ из config.json
    config_file = "config.json"
    api = load_api_key(config_file)
    if not api:
        print("API key not found. Please check your configuration file.")
        return
    
    video_id = input("Enter the video ID from Youtube: ")
    
    # Определяем фиксированную папку для сохранения
    save_path = os.path.join(os.getcwd(), "music")
    
    # Проверяем и создаём папку, если её нет
    if not os.path.exists(save_path):
        os.makedirs(save_path)  # Создаёт папку, если её нет
    
    try:
        url = "https://youtube-mp36.p.rapidapi.com/dl"
        querystring = {"id": video_id}
        
        headers = {
            "x-rapidapi-key": api,
            "x-rapidapi-host": "youtube-mp36.p.rapidapi.com"
        }
        
        while True:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()
            answer = response.json()
            
            print("API Response:", answer)  # Для отладки
            
            if answer.get("status") == "ok" and "link" in answer:
                # Очистка имени файла
                raw_title = answer["title"]
                sanitized_title = sanitize_filename(f"{raw_title} [{video_id}].mp3")
                
                download_url = answer["link"]
                
                # Формирование полного пути файла
                full_file_path = os.path.join(save_path, sanitized_title)
                
                # Загрузка аудиофайла
                audio_response = requests.get(download_url)
                with open(full_file_path, "wb") as file:
                    file.write(audio_response.content)
                
                print(f"Downloaded successfully as '{full_file_path}'")
                time.sleep(1)
                main_menu()
            elif answer.get("status") == "processing":
                print("File is being processed. Retrying in 5 seconds...")
                time.sleep(5)  # Ожидание перед повторной проверкой
            else:
                print(f"Failed to process the request. Status: {answer.get('status')}")
                time.sleep(5)
                main_menu()
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
        time.sleep(5)
        main_menu()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        time.sleep(5)
























    
    
    

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
    files_in_folder = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

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
        for index, file in enumerate(files_in_folder,start=1):
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
    Vibeflow = Fore.MAGENTA + "✮⋆˙VibeFlow✮⋆˙" + Fore.RESET
    guide = Fore.YELLOW + "ִGuideִ" + Fore.RESET
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
        print("You choosed  'Download Music from Vibeflow-site'")
        
        download_with_youtube()
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
    Vibeflow = Fore.MAGENTA + "✮⋆˙VibeFlow✮⋆˙" + Fore.RESET
    print(f"Welcome to {Vibeflow} - A tiny music player")
    time.sleep(3)
    main_menu()
    
    
#----------------Main-end------------------------- #
if __name__ == "__main__":
    main()
