from GraficInterface.main_window import MainWindow

class InstallPrograms(MainWindow):
    def __init__(self):
        super().__init__()

        self.apt_installed_programs = []
        self.snap_installed_programs = []
        self.flatpak_installed_programs = []
        self.downloaded_programs = []
    
    def install_program_using_apt_package_manager(self, list_programs):
        pass

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