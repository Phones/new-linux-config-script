import os
import subprocess
from colorama import Fore, Back, Style

color_dict = {
    "black": Fore.BLACK,
    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE,
    "bright_black": Fore.BLACK + Style.BRIGHT,
    "bright_red": Fore.RED + Style.BRIGHT,
    "bright_green": Fore.GREEN + Style.BRIGHT,
    "bright_yellow": Fore.YELLOW + Style.BRIGHT,
    "bright_blue": Fore.BLUE + Style.BRIGHT,
    "bright_magenta": Fore.MAGENTA + Style.BRIGHT,
    "bright_cyan": Fore.CYAN + Style.BRIGHT,
    "bright_white": Fore.WHITE + Style.BRIGHT,
    "bg_black": Back.BLACK,
    "bg_red": Back.RED,
    "bg_green": Back.GREEN,
    "bg_yellow": Back.YELLOW,
    "bg_blue": Back.BLUE,
    "bg_magenta": Back.MAGENTA,
    "bg_cyan": Back.CYAN,
    "bg_white": Back.WHITE,
    "bg_bright_black": Back.BLACK + Style.BRIGHT,
    "bg_bright_red": Back.RED + Style.BRIGHT,
    "bg_bright_green": Back.GREEN + Style.BRIGHT,
    "bg_bright_yellow": Back.YELLOW + Style.BRIGHT,
    "bg_bright_blue": Back.BLUE + Style.BRIGHT,
    "bg_bright_magenta": Back.MAGENTA + Style.BRIGHT,
    "bg_bright_cyan": Back.CYAN + Style.BRIGHT,
    "bg_bright_white": Back.WHITE + Style.BRIGHT
}

def printwc(text, color="bright_green"):
    color_text = color_dict[color]
    print(f"{color_text}{text}{Style.RESET_ALL}")

def download_file_with_wget(url, destination_folder):
    comand = ['wget', '-c', '-q','--show-progress', '-O', destination_folder, url]
    subprocess.run(comand)

def create_folder(folder_name):
    os.mkdir(folder_name)

def delete_folder_or_file(path):
    os.system(f"rm -rf {path}")