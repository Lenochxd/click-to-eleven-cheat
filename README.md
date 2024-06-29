# Click To Eleven Achievement Unlocker

<p align="center">
    <a href="https://store.steampowered.com/app/1586220/Click_To_Eleven/" target="_blank">
        <img src="https://i.imgur.com/DouauOb.png" alt="Achievement">
    </a>
</p>

This Python script is designed to help you unlock the achievement in the Steam game "Click To Eleven" by spamming the backspace key.

Consider checking out this awesome and highly addictive game on [Steam](https://store.steampowered.com/app/1586220/Click_To_Eleven/)!

## How it Works

The script uses the `pyautogui` library to simulate keyboard input and the `win32gui` library to detect the active window. It creates multiple threads (up to 200) that continuously press the backspace key when the game window is in focus.

## Usage

1. Install the required libraries:

    `pip install pyautogui pywin32`

2. Run the script:

    `python main.py`


3. When prompted, enter the number of threads you want to run (default is 50, maximum is 200).

4. Switch to the game window, and the script will start spamming the backspace key.

**Note:** Running too many threads can potentially slow down or freeze your system. Use caution when increasing the number of threads.

## Disclaimer

This script is provided for fun and convenience. Enjoy the game!
