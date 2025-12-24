import shutil
import subprocess
import os
import sys
import logging
from pathlib import Path

# Import configuration
try:
    import config
except ImportError:
    print("Error: config.py not found. Please ensure it exists in the same directory.")
    sys.exit(1)

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def create_junction(src: Path, dst: Path):
    """
    Creates a Directory Junction (mklink /J) from src to dst.
    """
    if dst.exists():
        if dst.is_dir() and not dst.is_symlink():
            # It's a real directory, we must remove it to replace with junction
            logger.info(f"Removing existing directory to replace with Junction: {dst}")
            shutil.rmtree(dst)
        elif dst.is_file() or dst.is_symlink() or dst.is_mount():
            # It's a file or existing link, unlink it
            dst.unlink()

    # Ensure parent exists
    dst.parent.mkdir(parents=True, exist_ok=True)

    # Command to create junction
    # mklink /J "Link" "Target"
    cmd = ['mklink', '/J', str(dst), str(src)]
    try:
        # shell=True is required for mklink as it's a cmd internal command
        subprocess.run(cmd, check=True, shell=True, stdout=subprocess.DEVNULL)
        logger.info(f"Created Junction: {dst} -> {src}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to create junction for {dst}. Reason: {e}")

def clean_unexpected_items():
    """
    Removes any items in the Community folder that are NOT in config.MOVE_FOLDERS.
    This ensures the folder contains ONLY what is specified.
    """
    folder = config.GITHUB_COMMUNITY_FOLDER
    if not folder.exists():
        return

    logger.info("Cleaning up unexpected items in Community folder...")
    allowed_names = set(config.MOVE_FOLDERS)
    
    # Iterate over top-level items in Community folder
    # Note: MOVE_FOLDERS might contain nested paths like "a/b".
    # But usually, the structure in Community mirrors the structure in ADDON?
    # Wait, the original script flattened them?
    # Original script: move_items(ADDON, COMMUNITY, folders) -> src=ADDON/item, dst=COMMUNITY/item.
    # So if item is "aig-aitraffic-oci/Sound", it copies to "Community/aig-aitraffic-oci/Sound".
    # Wait, looking at original script:
    # dst = dst_folder / item
    # If item is "aig-aitraffic-oci/Sound", dst is "Community/aig-aitraffic-oci/Sound".
    # So the directory structure IS maintained.
    
    # To clean properly, we need to know what top-level folders are allowed.
    # If MOVE_FOLDERS has "A/B", then "A" is a top level folder that must exist.
    # If MOVE_FOLDERS has "C", then "C" is a top level folder.
    
    # Let's extract top-level parts from MOVE_FOLDERS
    allowed_top_level = set()
    for item in config.MOVE_FOLDERS:
        # Get the first part of the path
        parts = Path(item).parts
        if parts:
            allowed_top_level.add(parts[0])
            
    # Now check actual items
    for entry in folder.iterdir():
        if entry.name not in allowed_top_level:
            logger.info(f"Removing stale item: {entry.name}")
            if entry.is_dir() and not entry.is_symlink():
                shutil.rmtree(entry)
            else:
                try:
                    entry.unlink()
                except OSError:
                    # Fallback for safe junction removal if unlink fails (though unlink should work)
                    if entry.is_dir():
                        os.rmdir(entry)
                    else:
                        raise

def process_items():
    """
    Process items defined in config.MOVE_FOLDERS.
    - Directories: Create Junctions (Save space)
    - Files: Copy (Small files)
    """
    logger.info(f"Processing items from {config.ADDON_FOLDER}...")

    if not config.ADDON_FOLDER.exists():
        logger.error(f"Source folder does not exist: {config.ADDON_FOLDER}")
        return

    # First clean up any top-level items that shouldn't be there
    # (Optional, but good for "Sync" behavior)
    clean_unexpected_items()

    for item_path in config.MOVE_FOLDERS:
        src = config.ADDON_FOLDER / item_path
        dst = config.GITHUB_COMMUNITY_FOLDER / item_path

        if not src.exists():
            logger.warning(f"Source item not found, skipping: {src}")
            continue

        if src.is_dir():
            create_junction(src, dst)
        else:
            # File copy
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            logger.info(f"Copied File: {dst}")

def open_github_desktop():
    """Opens GitHub Desktop application."""
    path = config.GITHUB_DESKTOP_BIN
    if path.exists():
        try:
            subprocess.Popen([str(path)])
            logger.info("Launched GitHub Desktop.")
        except Exception as e:
            logger.error(f"Failed to launch GitHub Desktop: {e}")
    else:
        logger.warning(f"GitHub Desktop not found at {path}")

def zip_folder():
    """Zips the community folder using NanaZip."""
    zip_path = config.ZIP_OUTPUT_PATH
    folder = config.GITHUB_COMMUNITY_FOLDER
    
    logger.info(f"Creating zip file with {config.NANAZIP_BIN}...")
    
    # NanaZip command: nanazip a "output.zip" "source_folder"
    # Ensure previous zip is removed if it exists to avoid appending if logic requires (though 'a' usually appends/updates)
    # If we want a fresh zip every time, we should delete the old one.
    if zip_path.exists():
        try:
            zip_path.unlink()
            logger.info("Removed existing zip file.")
        except Exception as e:
            logger.warning(f"Could not remove existing zip file: {e}")

    try:
        subprocess.run(
            [config.NANAZIP_BIN, "a", str(zip_path), str(folder)],
            check=True
        )
        logger.info(f"Successfully created: {zip_path}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to zip folder. Is NanaZip installed and in PATH? Error: {e}")
    except FileNotFoundError:
        logger.error(f"NanaZip executable '{config.NANAZIP_BIN}' not found.")

def main():
    print("\n" + "="*50)
    logger.info("Starting Automation Script")
    print("="*50 + "\n")

    # 1. Clear/Prepare Community Folder
    # With Junction logic, we don't necessarily need to "Clear All" first if we handle overwrites correctly.
    # However, to be clean, let's allow process_items to handle collision or we can clear strictly.
    # Given the previous script cleared everything, let's replicate that safety but smarter?
    # Actually, process_items handles replacement. But if there are *stale* items (items removed from config), they won't be deleted.
    # For now, let's keep it simple: Re-creating junctions is fast.
    
    # 2. Link/Copy Files
    process_items()

    # 3. Open GitHub Desktop
    open_github_desktop()  # Non-blocking usually

    # 4. Zip Prompt
    print("\n" + "-"*30)
    zip_choice = input("Do you want to zip the Community folder? (yes/no): ").strip().lower()
    if zip_choice.startswith("y"):
        zip_folder()

    print("\n" + "="*50)
    input("Script Finished. Press Enter to exit...")

if __name__ == "__main__":
    main()