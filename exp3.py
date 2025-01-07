import time
import msvcrt  # Для работы с клавишами без задержки на Windows

def get_input():
    pressed = ''
    while True:
        if msvcrt.kbhit():  # Проверка, была ли нажата клавиша
            key = msvcrt.getch().decode('utf-8')  # Получаем символ, нажатый пользователем

            if key in ['1', '2', '3', '4']:
                if pressed == '':
                    pressed = key  # Устанавливаем цифру, если она ещё не была нажата
                    # print(f"Вы нажали {key}. Для продолжения удалите {key}.")
                    return key
            elif key == '\r':  # Если нажата клавиша Enter, ничего не делаем
                continue
            # Если нажата любая другая клавиша, ничего не происходит
            # Просто игнорируем её

def main_menu():
    while True:
        print("1. Play Choosen Music")
        print("2. Open Vibeflow music folder")
        print("3. Download Music from Vibeflow-server")
        print("4. Exit")
        time.sleep(1)
        choice = get_input()  # Получаем выбор пользователя
        if choice == '1':
            print("Вы выбрали 'Play Choosen Music'")
        elif choice == '2':
            print("Вы выбрали 'Open Vibeflow music folder'")
        elif choice == '3':
            print("Вы выбрали 'Download Music from Vibeflow-server'")
        elif choice == '4':
            print("Вы выбрали 'Exit'")
            break

# Вызов главного меню
main_menu()
