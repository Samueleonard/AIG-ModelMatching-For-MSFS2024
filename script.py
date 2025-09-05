import os
import shutil
import subprocess
from pathlib import Path

github_folder = Path("C:/Users/samue/Documents/GitHub/AIG-ModelMatching-For-MSFS2024")
addon_folder = Path("F:/MSFS Addons/Addons/AI Traffic")
move_folders = [
    "aig-aitraffic-effects", 
    "aig-aitraffic-modelbehavior",
    "aig-aitraffic-oci/Sound",
    "aig-aitraffic-oci/Texture",
    "aig-aitraffic-oci/Traffic Files",
    "aig-aitraffic-oci/aig.vmr",
    "aig-aitraffic-oci/layout.json", 
    "aig-aitraffic-oci/manifest.json", 
    "aig-aitraffic-oci/SimObjects",
]
github_community_folder = github_folder / "Community"

def clear_github_folder():
    print("\n" + "="*40)
    print(f'Checking if {github_community_folder} exists...')

    if github_community_folder.exists():
        print(f'{github_community_folder} exists. Clearing contents...')
        for entry in github_community_folder.iterdir():
            try:
                if entry.is_file() or entry.is_symlink():
                    print(f'Deleting file: {entry}')
                    entry.unlink()
                elif entry.is_dir():
                    print(f'Deleting directory: {entry}')
                    shutil.rmtree(entry)
            except Exception as e:
                print(f'Failed to delete {entry}. Reason: {e}')
    else:
        print(f'{github_community_folder} does not exist. Creating directory...')
        github_community_folder.mkdir(parents=True)
    print("Done clearing GitHub Community folder.")
    move_files()

def move_files():
    print("\n" + "="*40)
    src_folder = addon_folder
    dst_folder = github_community_folder

    print(f'Moving files from {src_folder} to {dst_folder}...')
    for item in move_folders:
        src = src_folder / item
        dst = dst_folder / item
        if src.exists():
            print(f'Moving {src} to {dst}')
            if src.is_dir():
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
            print(f'Moved {src} to {dst}')
        else:
            print(f'{src} does not exist. Skipping...')
    print("Done moving files.")
    print("\n" + "="*40)
    try:
        subprocess.run(["C:/Users/samue/AppData/Local/GitHubDesktop/GitHubDesktop.exe"], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Failed to open GitHub Desktop. Reason: {e}')
    zip_choice = input("Do you want to zip the Community folder? (yes/no): ").strip().lower()
    if zip_choice.startswith("y"):
        zip_community_folder()
    input("Press Enter after you have pushed changes to GitHub...")


def zip_community_folder():
    print("\n" + "="*40)
    zip_path = os.path.join(github_folder, "Community.zip")
    print(f'Creating zip file: {zip_path}')
    subprocess.run(["nanazip", "a", zip_path, github_community_folder])
    print("Done creating zip file.")

if __name__ == "__main__":
    clear_github_folder()