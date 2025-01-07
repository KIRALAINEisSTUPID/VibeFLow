import pygame
import tkinter as tk
from tkinter import filedialog
import os
import sys
import time
from mutagen.mp3 import MP3  # Для работы с MP3
from mutagen.wavpack import WavPack  # Для работы с WAV

def select_file():
    # Используем tkinter для выбора музыкального файла
    file_path = filedialog.askopenfilename(title="Выберите музыкальный файл", filetypes=(("Audio Files", "*.mp3;*.wav"), ("All Files", "*.*")))
    return file_path

def get_audio_length(file_path):
    # Используем mutagen для получения длины аудиофайла
    try:
        if file_path.endswith('.mp3'):
            audio = MP3(file_path)
        elif file_path.endswith('.wav'):
            audio = WavPack(file_path)
        else:
            return 0  # Возвращаем 0, если формат не поддерживается

        return audio.info.length  # Возвращаем длину в секундах
    except Exception as e:
        print(f"Ошибка при получении длины файла: {e}")
        return 0

def play_music(file_path):
    pygame.mixer.init()  # Инициализация mixer
    pygame.mixer.music.load(file_path)  # Загружаем файл
    pygame.mixer.music.play()  # Воспроизводим

def stop_music():
    pygame.mixer.music.stop()  # Останавливаем воспроизведение

def pause_music():
    pygame.mixer.music.pause()  # Ставим на паузу

def unpause_music():
    pygame.mixer.music.unpause()  # Возобновляем воспроизведение

def set_volume(volume):
    pygame.mixer.music.set_volume(volume)  # Устанавливаем громкость (от 0 до 1)

def show_status(file_path):
    # Получаем информацию о музыке
    length = int(get_audio_length(file_path))  # Длительность музыки в секундах
    current_pos = int(pygame.mixer.music.get_pos() / 1000)  # Текущее положение в секундах
    volume = pygame.mixer.music.get_volume()  # Текущая громкость (0.0 до 1.0)

    print(f"Длительность: {length:.2f} секунд")
    print(f"Воспроизведено: {current_pos:.2f} секунд")
    print(f"Громкость: {volume:.2f}")
    print("ocmалось")

def music_control():
    file_path = ""
    while True:
        command = input("Введите команду (play, pause, unpause, stop, volume, status, quit): ").strip().lower()

        if command == 'play':
            file_path = select_file()
            if file_path:
                play_music(file_path)
                print(f"Воспроизведение {file_path} началось.")
                while True:
                    show_status(file_path)
                    time.sleep(1)
                    os.system("cls")
                    
        
        elif command == 'pause':
            pause_music()
            print("Музыка на паузе.")
        
        elif command == 'unpause':
            unpause_music()
            print("Музыка возобновлена.")
        
        elif command == 'stop':
            stop_music()
            print("Музыка остановлена.")
        
        elif command == 'volume':
            volume = float(input("Установите громкость (0.0 до 1.0): ").strip())
            if 0 <= volume <= 1:
                set_volume(volume)
                print(f"Громкость установлена на {volume}.")
            else:
                print("Неверное значение громкости.")
        
        elif command == 'status' and file_path:
            show_status(file_path)
        
        elif command == 'quit':
            stop_music()
            print("Выход из программы.")
            break

        else:
            print("Неизвестная команда, попробуйте снова.")

if __name__ == "__main__":
    pygame.mixer.init()  # Инициализация pygame для музыки
    music_control()
