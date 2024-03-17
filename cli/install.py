import subprocess
import os

def install_common_requirements():
    """
    Install common Python packages required by both tools.
    """
    packages = [
        "Pillow",
        "tqdm",
        "requests",
        "tqdm",
        "beautifulsoup4",  # Note: bs4 is an import name, the package is beautifulsoup4
        "html5lib",
        "phonenumbers",
        "argparse",
        "urllib3",
        "colorama>=0.4.1",
        "certifi>=2019.6.16",
        "PySocks>=1.7.0",
        "requests-futures>=1.0.0",
        "stem>=1.8.0",
        "torrequest>=0.1.0",
        "pandas>=1.0.0",
        "openpyxl<=3.0.10"
    ]
    subprocess.run(["python3", "-m", "pip", "install"] + packages, check=True)

def clone_and_install_requirements(git_url, dir_name):
    """
    Clone the git repository into the specified directory and install the Python requirements from its requirements.txt file.
    """
    if not os.path.exists(dir_name):
        print(f"{dir_name} not found. Cloning repository...")
        subprocess.run(["git", "clone", git_url, dir_name], check=True)
        
        print(f"Installing requirements for {dir_name}...")
        requirements_path = os.path.join(dir_name, "requirements.txt")
        subprocess.run(["python3", "-m", "pip", "install", "-r", requirements_path], check=True)
    else:
        print(f"{dir_name} is already installed.")

def main():
    # Install common requirements first
    install_common_requirements()

    # Configuration for Sherlock
    sherlock_git_url = "https://github.com/sherlock-project/sherlock.git"
    sherlock_dir_name = "sherlock"

    # Configuration for PhoneInfoga
    phoneinfoga_git_url = "https://github.com/wingerbijay/PhoneInfoga.git"
    phoneinfoga_dir_name = "PhoneInfoga"

    # Install Sherlock
    clone_and_install_requirements(sherlock_git_url, sherlock_dir_name)

    # Install PhoneInfoga
    clone_and_install_requirements(phoneinfoga_git_url, phoneinfoga_dir_name)

if __name__ == "__main__":
    main()
