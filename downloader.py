import json
import subprocess
import os
import configparser

mister_path = "/media/fat/"
default_curl_args = ["--cacert", "/etc/ssl/certs/cacert.pem"]

def main():
    db = get_database()
    ia_config = get_config()

    for path, file in db['files'].items():
        download(file['url'], path.replace("|", mister_path), ia_config['cookies'])

def get_database():
    result = subprocess.run(["curl", *default_curl_args, "-LOs", "https://raw.githubusercontent.com/zakk4223/ArcadeROMsDB_MiSTer/db/arcade_roms_db.json.zip"], stderr=subprocess.STDOUT)
    if result.returncode != 0:
        print("Failed to download arcade database")
        exit(-1)
    
    result = subprocess.run(["unzip", "-u", "arcade_roms_db.json.zip"], stderr=subprocess.STDOUT)
    if result.returncode != 0:
        print("Failed to unzip arcade database")
        exit(-1)
    
    with open("arcade_roms_db.json", "r") as f:
        return json.load(f)

def get_config():
    try:
        xdg_config_home = os.path.join(os.path.expanduser('~'), '.config')
        xdg_config_file = os.path.join(xdg_config_home, 'internetarchive', 'ia.ini')
        config = configparser.RawConfigParser()
        config.read(xdg_config_file)
        return config
    except:
        print("Failed to locate ia config file. Did you forget to run `ia configure`?")
        exit(-1)
    
def download(url, output_path, cookies = []):
    args = ["curl", *default_curl_args, "-Ls", "--create-dirs", "-o", output_path]
    for key in cookies:
        args.append("--cookie")
        args.append(f'{key}={cookies[key]}')
    args.append(url)
    print(output_path)
    result = subprocess.run(args, stderr=subprocess.STDOUT)
    if result.returncode != 0:
        print("Failed to download file")

if __name__ == "__main__":
    main()
