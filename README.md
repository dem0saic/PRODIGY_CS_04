## PRODIGY_CS_04
 Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers.

# Simple Keylogger
A basic keylogger program that records and logs keystrokes.

# Table of Contents
- Features
- Installation
- Usage
- Configuration
- Security Considerations
- Creator Information

# Features
- Logs all key presses and releases to a file (`keylog.txt`)
- Stops logging when the 'ESC' key is pressed
- Stops logging after 5 days of inactivity

# Installation
To use this keylogger, you will need to install the following libraries:

- `pyfiglet`
- `termcolor`
- `pynput`
- `logging`
- `threading`
- `time`

You can install these libraries using pip:

bash
```
pip install pyfiglet termcolor pynput
```

# Usage
1. Run the keylogger program.
2. Press any key to start logging.
3. The keylogger will log all key presses and releases to `keylog.txt`.
4. Press the 'ESC' key to stop the keylogger.
5. The keylogger will also stop after 5 days of inactivity.

# Configuration
The keylogger logs all key presses and releases to `keylog.txt`. You can change the log file by modifying the filename parameter in the `logging.basicConfig` function.

# Security Considerations
Please note that this keylogger is for educational purposes only.

- Always obtain permission from users before logging keystrokes.
- Use this knowledge responsibly and only for ethical purposes, such as developing security software or educational projects.

# Creator Information
Created by: Dem0saic
GitHub: https://github.com/dem0saic
LinkedIn: https://www.linkedin.com/in/owusuvincent/
License
This keylogger is licensed under the MIT License. See LICENSE for details.