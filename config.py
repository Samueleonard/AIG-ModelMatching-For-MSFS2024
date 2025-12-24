import os
from pathlib import Path

# ==========================================
# CONFIGURATION
# ==========================================

# Base directory for the GitHub repository
GITHUB_FOLDER = Path(r"C:\Users\samue\Documents\GitHub\AIG-ModelMatching-For-MSFS2024")

# Source directory for the Addons
ADDON_FOLDER = Path(r"F:\MSFS Addons\Addons\AI Traffic")

# List of files/folders to process relative to ADDON_FOLDER
# These will be linked (folders) or copied (files) to GITHUB_FOLDER/Community
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

# ==========================================
# TOOLS
# ==========================================

# Path to NanaZip executable (or just "nanazip" if in PATH)
NANAZIP_BIN = "nanazip"

# GitHub Desktop Executable
# Using standard global path or local appdata if not found
GITHUB_DESKTOP_BIN = Path(os.path.expandvars(r"%LOCALAPPDATA%\GitHubDesktop\GitHubDesktop.exe"))

# ==========================================
# COMPUTED PATHS
# ==========================================
GITHUB_COMMUNITY_FOLDER = GITHUB_FOLDER / "Community"
ZIP_OUTPUT_PATH = GITHUB_FOLDER / "Community.zip"
