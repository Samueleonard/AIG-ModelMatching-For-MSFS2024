import os
import shutil
import subprocess
import zipfile

github_folder = "C:\\Users\\samue\\Documents\\GitHub\\AIG-ModelMatching-For-MSFS2024"
addon_folder = "F:\\Flight Sim Addons\\FS2024 Native\\AI Traffic"
move_folders = [
    "aig-aitraffic-oci\\SimObjects", 
    "aig-aitraffic-oci\\Sound", 
    "aig-aitraffic-oci\\layout.json", 
    "aig-aitraffic-oci\\manifest.json", 
    "aig-aitraffic-effects", 
    "aig-aitraffic-modelbehavior"
]
github_community_folder = os.path.join(github_folder, "Community")

def clear_github_folder():
    print(f'Checking if {github_community_folder} exists...')

    if os.path.exists(github_community_folder):
        print(f'{github_community_folder} exists. Clearing contents...')
        for filename in os.listdir(github_community_folder):
            file_path = os.path.join(github_community_folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    print(f'Deleting file: {file_path}')
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    print(f'Deleting directory: {file_path}')
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    else:
        print(f'{github_community_folder} does not exist. Creating directory...')
        os.makedirs(github_community_folder)
    print("Done clearing GitHub Community folder..")
    move_files("to_github")


def move_files(direction):
    print("\n" + "="*40)
    if direction == "to_github":
        src_folder = addon_folder
        dst_folder = github_community_folder
    elif direction == "to_addon":
        src_folder = github_community_folder
        dst_folder = addon_folder
    else:
        print(f'Invalid direction: {direction}')
        return

    print(f'Moving files from {src_folder} to {dst_folder}...')
    for item in move_folders:
        src = os.path.join(src_folder, item)
        dst = os.path.join(dst_folder, item)
        if os.path.exists(src):
            shutil.move(src, dst)
            print(f'Moved {src} to {dst}')
        else:
            print(f'{src} does not exist. Skipping...')
    print("Done moving files...")

    if direction == "to_github":
        zip_choice = input("Do you want to zip the Community folder? (yes/no): ").strip().lower()
        if zip_choice[0] == "y":
            zip_community_folder()
        subprocess.run(["C:\\Users\\samue\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"])
        input("Press Enter after you have pushed changes to GitHub...")
        move_files("to_addon")


def zip_community_folder():
    zip_path = os.path.join(github_folder, "Community.zip")
    print(f'Zipping {github_community_folder} to {zip_path} using NanaZip...')
    subprocess.run(["nanazip", "a", zip_path, github_community_folder])
    print("Done zipping Community folder...")

if __name__ == "__main__":
    clear_github_folder()