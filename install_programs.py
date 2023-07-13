import secrets
import subprocess
from time import sleep
from helpers import printwc, download_file_with_wget, create_folder, delete_folder_or_file
from GraficInterface.main_window import MainWindow

class InstallPrograms(MainWindow):
    def __init__(self):
        super().__init__()

        self.apt_installed_programs = []
        self.snap_installed_programs = []
        self.flatpak_installed_programs = []
        self.downloaded_programs = []

        self.links_download = {}
        self.links_download["google-chrome"]="https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
        self.links_download["vscode"]="https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"
        self.links_download["discord"]="https://discord.com/api/download?platform=linux&format=deb"
        self.links_download["obsidian"]="https://github.com/obsidianmd/obsidian-releases/releases/download/v1.3.5/obsidian_1.3.5_amd64.deb"

    def separate_programs_by_installation_type(self):
        selected_options = self.get_clicked_options()
        for program in selected_options:
            if program.install_type == "apt":
                self.apt_installed_programs.append(program.option)
            elif program.install_type == "snap":
                self.snap_installed_programs.append(program.option)
            elif program.install_type == "flatpak":
                self.flatpak_installed_programs.append(program.option)
            elif program.install_type == "download":
                self.downloaded_programs.append(program.option)

        print(self.apt_installed_programs)

    def download_all_installers_deb(self):
        for program_name in self.downloaded_programs:
            destination_folder = f"Downloads/{program_name}-{secrets.token_hex(nbytes=8)}.deb"
            download_file_with_wget(self.links_download[program_name], destination_folder)

    def install_program_using_apt_package_manager(self):
        for program_name in self.apt_installed_programs:
            comand = ['sudo', 'apt-get', 'install', program_name]
            printwc(" ".join(comand))
            process = subprocess.Popen(comand, stdout=subprocess.PIPE, universal_newlines=True)

            # Loop para imprimir a saída em tempo real
            while process.poll() is None:
                output = process.stdout.readline()
                if output:
                    print(output.strip())
            
            printwc(f"------------- Fim da instalação [{comand[-1]}] -----------------")

    def install_programs(self):
        delete_folder_or_file("./Downloads")
        self.separate_programs_by_installation_type()
        self.install_program_using_apt_package_manager()
        create_folder("Downloads")
        self.download_all_installers_deb()
        