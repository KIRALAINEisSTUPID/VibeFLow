import time
from colorama import Fore
import os
from os import system
import msvcrt



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




def vibeflow_folder():
    os.system("cls") 
    path = "music"
    music_extensions = {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"}

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


    
    
    
    
    
    
    
    
    
def main():
    os.system("cls")
    Vibeflow = Fore.MAGENTA + "VibeFlow" + Fore.RESET
    print(f"Welcome to {Vibeflow} - A tiny music player")
    time.sleep(3)
    main_menu()
if __name__ == "__main__":
    main()
