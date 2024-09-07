import os
import shutil

# List of tags
tags = [
    "AB5", "AB4", "AB3", "AB2", "AB1", "AB0",
    "KHL", "KND", "KSN",
    "L3Z", "L2Z", "L1Z", "L0Z",
    "BZD",
    "C9R", "C8R", "C7R", "C6R", "C4R", "C3R", "C2R", "C1R", "C10", "C0R",
    "DA8", "DA7", "DA6", "DA5", "DA4", "DA3", "DA2", "DA0",
    "DG4", "DG3", "DG2", "DG1", "DG0",
    "DRV", "DUB",
    "FUJ",
    "MKU", "MLN", "RAS", "REG","SHD", "SIS", "SRG", "SV0", "SWA", "TAU","UMM","WKH","ZOU",
    "AB5", "AB4", "AB3", "AB2", "AB1", "AB0",
    "AJM", "AZ9", "AZ8", "AZ7", "AZ6", "AZ5", "AZ4", "AZ3", "AZ2", "AZ1", "AZ0",
    "BGP", "BKU", "BRC", "BSR", "BZD", "CLB",
    "C9R", "C8R", "C7R", "C6R", "C5R", "C4R", "C3R", "C2R", "C1R", "C10", "C0R",
    "DA8", "DA7", "DA6", "DA5", "DA4", "DA3", "DA2", "DA1", "DA0",
    "DBT", "DG4", "DG3", "DG2", "DG1", "DG0",
    "DRV", "DUB", "FUJ", "GUR", "IME", "JBJ",
    "KGH", "KGN", "KHL", "KKX", "KND", "KSN",
    "LEZ", "L3Z", "L2Z", "L1Z", "L0Z",
    "MAN", "ME5", "MKU", "MLN", "NAR",
    "RAS", "REG", "RNC", "SHD", "SHN", "SIS",
    "SMK", "SRJ", "SV0", "TAU", "TLY", "TTN",
    "UMM", "WKH"
]

# Create the "moved files" folder if it doesn't exist
moved_files_folder = "moved files"
if not os.path.exists(moved_files_folder):
    os.makedirs(moved_files_folder)

# Move files starting with the tag names
for tag in tags:
    for filename in os.listdir("."):
        if filename.startswith(tag):
            shutil.move(filename, moved_files_folder)
            print(f"Moved {filename} to {moved_files_folder}")