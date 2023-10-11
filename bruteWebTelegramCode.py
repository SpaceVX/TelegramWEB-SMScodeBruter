import pyautogui
import time
import keyboard

cursor_position = None
input_field_detected = True  


def enter_number(number):
    pyautogui.typewrite(str(number))

def save_cursor_position():
    global cursor_position
    cursor_position = pyautogui.position()

def restore_cursor_position():
    if cursor_position:
        pyautogui.moveTo(cursor_position[0], cursor_position[1])

def main():
    global input_field_detected

    start_number = 10000
    end_number = 99999
    current_number = start_number

    input_coords = pyautogui.locateOnScreen('input_locator.png')  # Замените 'input_locator.png' на скриншот поля ввода
    if not input_coords:
        input_field_detected = False
        print('Либо я слепой и не вижу поля для брута либо ты тупой и я не вижу пнгшки ')

    while current_number <= end_number:
        if keyboard.is_pressed('F6'):
            print('Process stopped.')
            break

        if input_field_detected:
            
            save_cursor_position()

            pyautogui.press('backspace', presses=5)

            enter_number(current_number)
            print('Entered number:', current_number)

            pyautogui.press('enter')

            current_number += 1
            time.sleep(1.0)

            pyautogui.press('backspace', presses=5)
            restore_cursor_position()

if __name__ == "__main__":
    main()
