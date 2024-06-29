import threading
import pyautogui
from win32gui import GetWindowText, GetForegroundWindow

print('WARNING: Running too many threads can slow down or freeze your system.')


def get_threads_count():
    while True:
        threads_count = input('\nEnter the number of threads (default=100, max=500)\nValue: ').strip()
        if not threads_count:
            return 100
        try:
            threads_count = int(threads_count)
        except ValueError:
            print('Invalid input.')
            continue
        if 1 <= threads_count <= 500:
            return threads_count
        print('Invalid input.')

threads_count = get_threads_count()    
    
def spam_backspace():
    while True:
        if GetWindowText(GetForegroundWindow()) == 'ClickToEleven':
            pyautogui.press('backspace')

print('RESULT:',threads_count)
threads = []
for _ in range(threads_count):
    thread = threading.Thread(target=spam_backspace)
    thread.start()
    threads.append(thread)
