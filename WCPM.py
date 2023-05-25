from os.path import *
import requests
import download
import shutil

while True:
    print()
    cmds = input(">>> ")

    if 'wcpm insert' in cmds:
        command_parts = cmds.split()
        package_name = command_parts[2]
        package_url = f"https://github.com/Windows-1998-Guy/WCPM/raw/main/packages/{package_name}.zip"
        download_location = ".\\packages"

        package_file = join(download_location, f"{package_name}.zip")

        if isfile(package_file):
            print("The requested package exists on your local workspace. The process is aborted.")
        
        else:
            package_download = download.download(package_url, download_location, kind = 'zip', progressbar = True, verbose = True, replace = True)
    
    if 'wcpm outsert' in cmds:
        command_parts = cmds.split()
        package_name = command_parts[2]
        package_folder = f".\\packages\\{package_name}"

        if exists(package_folder):
            shutil.rmtree(package_folder)
            print(f"The requested package - '{package_name}' - was successfully removed from your local workspace.")
        
        else:
            print(f"The requested package does not exist on your local workspace. The process is aborted.")
    
    if 'wcpm find' in cmds:
        command_parts = cmds.split()
        package_name = command_parts[2]

        raw_search_url = f"https://github.com/Windows-1998-Guy/WCPM/tree/main/packages/{package_name}.zip"

        try:
            response = requests.get(raw_search_url)
            if response.status_code == 200:
                print(f"The requested package - '{package_name}' - is found on the WCPM package repository.")
                print(f"Run 'wcpm insert '{package_name}' to install it.")
            else:
                print(f"The requested package - '{package_name}' - is not found on the WCPM package repository.")
            
        except requests.exceptions.RequestException:
            print(f"There was an error while searching for your package.")