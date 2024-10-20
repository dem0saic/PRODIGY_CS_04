from pyfiglet import figlet_format
from termcolor import colored


# Print the title of the program
title = "Simple Keylogger"
title_ascii = figlet_format(title, font="larry3d", justify="center")

colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
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
creator_colored = colored(creator_info, color="yellow")
print(creator_colored)
