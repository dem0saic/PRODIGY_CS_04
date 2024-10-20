# PRODIGY_CS_04
 Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers.

# Explanation of the Code:
Imports:

pynput.keyboard is used to listen to keyboard events.
logging is used to log the keystrokes into a file.

# Logging Configuration:
The basicConfig function sets up logging, specifying the filename (keylog.txt), the logging level (DEBUG), and the log message format.
Key Press Function:

on_press(key) logs the character of the key pressed. If it’s a special key (like Shift, Ctrl, etc.), it logs the key name instead.
Key Release Function:

on_release(key) checks if the Escape key is pressed, which stops the listener.
Listener:

The keyboard.Listener collects keyboard events and runs until the Escape key is pressed.

# Important Considerations:
Permissions: Always obtain permission from users before logging keystrokes.
Ethical Use: Use this knowledge responsibly and only for ethical purposes, such as developing security software or educational projects.
