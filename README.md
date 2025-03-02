# AIG Model Matching for MSFS 2024

## Introduction

This package provides the latest version of the [Alpha India Group](https://www.alpha-india.net) (AIG) AI traffic models for MSFS 2024. It makes installation quick and easy by removing the need for the AIG installer.

This pack is for use with **VATSIM** but may work with offline traffic (more details below). Only real-world airlines and aircraft are included—no virtual airlines or unrealistic liveries.

> **Note:** This package works only with MSFS 2024 and **will not** work with MSFS 2020, use [this pack](https://github.com/Samueleonard/AIG-ModelMatching-For-MSFS2020) instead.

---

## Installation Instructions

### 1. Download the Package

Download the AIG pack using the link below:

- [Google Drive](https://drive.google.com/file/d/14BiC93-hbCI1-TbAbXbMn0G74AE1SLdc/view?usp=sharing)

The file is a large zip archive (~76.1GB uncompressed, ~3.9GB compressed).

> **Important:** Do not download any GitHub files, as this will not work.

### 2. Remove Previous AIG Installations

Delete any previous AIG files from your Community folder to avoid conflicts.

### 3. Extract the Files

Use an extraction tool (e.g., 7zip or WinRAR) to unzip the downloaded file into your MSFS Community folder.

- [Download 7zip](https://www.7-zip.org/)
- [Download WinRAR](https://www.win-rar.com/)

### 4. Using AIG with VATSIM

To use AIG with VATSIM, nothing extra is required other than vpilot, however some edge cases may lead to liveries being missing. To help with this issue, a VMR file is included to match these liveries to airlines:

- A basic VMR file is included and will be updated in the future.
- For better coverage, use [this third-party file](https://flightsim.to/file/23365/full-vatsim-aig-beta-model-matching). **IMPORTANT** -- this file is outdated and may lead to some vpilot error messages, but overall may help improve coverage.

My recommendation is to only use the included VMR file and not a 3rd party one, but it could be useful if you have specific usage requirements for one.

To set it up:
Open **vPilot settings** > **Model Matching (FS2024)** > **Custom Rules** > **Add Custom Rule Sets**.

---

## Manual Updates

You may need to update your setup manually using the **AIG Manager Tool**:

- Download it [here](https://www.alpha-india.net/software/).

> **Note:** Manual updates are not officially supported, and compatibility is not guaranteed.

---

## Using FSLTL (FS Live Traffic Liveries)

### What is FSLTL?

FSLTL is another model-matching tool that provides models and liveries, and also injects live traffic data from Flightradar24. It is not included in this package.

### Can I Use FSLTL and AIG Together?

Yes, you can use both together:

1. Add the VMR files for FSLTL and AIG to vPilot.
2. Ensure AIG’s VMR file is listed at the top for priority.

Download FSLTL via the [FlyByWire Installer](https://api.flybywiresim.com/installer).

---

## Using AIG on VATSIM

Out of the box, this package covers about 95% of VATSIM traffic.
To improve coverage, you can use a VMR file.

### Included VMR File

- A custom VMR file is included to handle cases like alternate ICAO codes (e.g., Lufthansa Cityline or British Airways Shuttle). However, it does not account for typos, wrong callsigns, or unrealistic livery/aircraft combinations.

### Third-Party VMRs

Alternatively, use a third-party VMR file like [this one](https://flightsim.to/file/23365/full-vatsim-aig-beta-model-matching) by [BritishAvgeek](https://www.youtube.com/@BritishAvgeek). **IMPORTANT** -- this file is outdated and may lead to some vpilot error messages, but overall may help improve coverage.

My recommendation is to only use the included VMR file and not a 3rd party one, but it could be useful if you have specific usage requirements for one.


To add it:
1. Download the file.
2. Open **vPilot settings** > **Model Matching (FS2024)** > **Custom Rules** > **Add Custom Rule Sets**.

---

## Offline Traffic

Offline flight plans are included but untested. Compatibility is not guaranteed, and no support is provided.
MSFS 2024 live traffic may also work but is not tested.

---

## Payware Models

Payware models are supported by aig but not included in this package. Any purchased payware models have been removed.

### Using Payware Models

To use payware models, manually update your setup with the [AIG Manager Tool](https://www.alpha-india.net/software/).

> **Note:** No support is available here for payware models.

