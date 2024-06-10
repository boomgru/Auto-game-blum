from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller
import colorama
from colorama import Fore

colorama.init(autoreset=True)

mouse = Controller()

def print_intro():
    print(Fore.BLUE + "BMGCLICKER blum")
    print(Fore.RED + "BMGCLICKER blum")
    print(Fore.GREEN + "BMGCLICKER blum")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(Fore.RED + "Nerest - t.me/good2999k")

def print_message(message):
    if "Play" in message:
        print(Fore.MAGENTA + message)
    else:
        print(message)

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

def activate_window(window):
    try:
        if window.isMinimized:
            window.restore()
        window.activate()
        return True
    except Exception:
        return False

def click_play_button(is_first_time):
    try:
        if is_first_time:
            play_button_coords = (telegram_window.left + int(telegram_window.width * 0.75), telegram_window.top + int(telegram_window.height * 0.6))
        else:
            play_button_coords = (telegram_window.left + int(telegram_window.width * 0.5), telegram_window.top + int(telegram_window.height * 0.85) - 10)  # Сместили вверх
        if not activate_window(telegram_window):
            pass
        pyautogui.moveTo(play_button_coords[0], play_button_coords[1])
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(play_button_coords[0], play_button_coords[1])
        time.sleep(0.1)
        pyautogui.moveTo(play_button_coords[0], play_button_coords[1])
        pyautogui.mouseUp(button='left')
        pyautogui.moveTo(play_button_coords[0], play_button_coords[1])
        click(play_button_coords[0], play_button_coords[1])
        print_message('BMG | Кнопка Play нажата.')
        time.sleep(1)
    except Exception as e:
        pass

def find_and_click_bacteria():
    scrn = pyautogui.screenshot(region=(telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height))
    width, height = scrn.size

    bacteria_found = False

    for x in range(0, width, 20):
        for y in range(0, height, 20):
            r, g, b = scrn.getpixel((x, y))

            
            if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                is_bomb = False
                for bx in range(-5, 6):
                    for by in range(-5, 6):
                        if 0 <= x + bx < width and 0 <= y + by < height:
                            br, bg, bb = scrn.getpixel((x + bx, y + by))
                            if br in range(100, 160) and bg in range(100, 160) and bb in range(100, 160):
                                is_bomb = True
                                break
                    if is_bomb:
                        break

                if not is_bomb:
                    screen_x = telegram_window.left + x
                    screen_y = telegram_window.top + y
                    click(screen_x + 4, screen_y)
                    print("◜¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                    print(f" LOG | TAP X - {screen_x} ¦ Y - {screen_y}")
                    print("◟__________________________________________")
                    time.sleep(0.001)
                    bacteria_found = True

    return bacteria_found

def start_game():
    window_name = input('\n BMG | Нажми 1 ')
    num_games = int(input('\n BMG | Сколько игр хотите сыграть: '))

    if window_name == '1':
        window_name = "TelegramDesktop"

    check = gw.getWindowsWithTitle(window_name)
    if not check:
        print(f"BMG | Окно - {window_name} не найдено! Закрытие программы!")
        exit()

    print(f"BMG | Окно найдено - {window_name}\n[☘️] | Нажмите 'q' для паузы.")

    global telegram_window
    telegram_window = check[0]
    paused = False

    games_played = 0
    is_first_time = True

    while games_played < num_games:
        
        click_play_button(is_first_time)
        is_first_time = False

        game_start_time = time.time()
        while time.time() - game_start_time < 31:  
            if keyboard.is_pressed('q'):
                paused = not paused
                if paused:
                    print('BMG | Пауза')
                else:
                    print(' BMG | Возобновление работы')
                time.sleep(1)  

            while paused:
                if keyboard.is_pressed('q'):
                    paused = False
                    print('BMG | Возобновление работы')
                    time.sleep(1)  

            bacteria_found = find_and_click_bacteria()
            if not bacteria_found and not paused:
                time.sleep(0.1)  

        games_played += 1
        print(f"BMG | Игра завершена. Игр сыграно: {games_played}")

        if games_played < num_games:
            is_first_time = False
            time.sleep(2)  

    print(f'BMG | {num_games} билетов потрачено, скрипт приостановлен.')

if __name__ == "__main__":
    print_intro()
    while True:
        start_game()
