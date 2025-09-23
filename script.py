import shutil
import subprocess
from pathlib import Path

GITHUB_FOLDER = Path("C:/Users/samue/Documents/GitHub/AIG-ModelMatching-For-MSFS2024")
ADDON_FOLDER = Path("F:/MSFS Addons/Addons/AI Traffic")
MOVE_FOLDERS = [
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
GITHUB_COMMUNITY_FOLDER = GITHUB_FOLDER / "Community"

def clear_folder(folder: Path):
    if folder.exists():
        for entry in folder.iterdir():
            try:
                if entry.is_file() or entry.is_symlink():
                    entry.unlink()
                elif entry.is_dir():
                    shutil.rmtree(entry)
            except Exception as e:
                print(f'Failed to delete {entry}. Reason: {e}')
    else:
        folder.mkdir(parents=True)

def move_items(src_folder: Path, dst_folder: Path, items: list):
    for item in items:
        src = src_folder / item
        dst = dst_folder / item
        if src.exists():
            if src.is_dir():
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
        else:
            print(f'{src} does not exist. Skipping...')

def open_github_desktop():
    try:
        subprocess.run(
            ["C:/Users/samue/AppData/Local/GitHubDesktop/GitHubDesktop.exe"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f'Failed to open GitHub Desktop. Reason: {e}')

def zip_folder(folder: Path, zip_path: Path):
    print(f'Creating zip file: {zip_path}')
    subprocess.run(["nanazip", "a", str(zip_path), str(folder)])
    print("Done creating zip file.")

def main():
    print("\n" + "="*40)
    print(f'Clearing {GITHUB_COMMUNITY_FOLDER}...')
    clear_folder(GITHUB_COMMUNITY_FOLDER)
    print("Done clearing folder.")

    print("\n" + "="*40)
    print(f'Moving files from {ADDON_FOLDER} to {GITHUB_COMMUNITY_FOLDER}...')
    move_items(ADDON_FOLDER, GITHUB_COMMUNITY_FOLDER, MOVE_FOLDERS)
    print("Done moving files.")

    open_github_desktop()

    zip_choice = input("Do you want to zip the Community folder? (yes/no): ").strip().lower()
    if zip_choice.startswith("y"):
        zip_folder(GITHUB_COMMUNITY_FOLDER, GITHUB_FOLDER / "Community.zip")

    input("Press Enter after you have pushed changes to GitHub...")

if __name__ == "__main__":
    main()