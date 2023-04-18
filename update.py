import json
import os
import re
import requests
import time

BMCLAPI2_VERSION_LIST = 'https://bmclapi2.bangbang93.com/optifine/versionList'
OPTIFINECN_VERSION_LIST = 'https://optifine.cn/api'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

def download_from_bmclapi2():
    response1 = requests.get(BMCLAPI2_VERSION_LIST, headers=headers)
    rjson = json.loads(response1.content)
    for entry in rjson:
        jar_url = f'https://bmclapi2.bangbang93.com/optifine/{entry["mcversion"]}/{entry["type"]}/{entry["patch"]}'
        if not os.path.exists(f'{entry["mcversion"]}'):
            os.makedirs(f'{entry["mcversion"]}')
        file_path = f'{entry["mcversion"]}/{entry["filename"]}'
        if not os.path.isfile(file_path):
            response2 = requests.get(jar_url, headers=headers)
            with open(file_path, 'wb') as f:
                f.write(response2.content)
                print(f'Downloaded {entry["filename"]}')
            time.sleep(5)

def download_from_optifinecn():
    response1 = requests.get(OPTIFINECN_VERSION_LIST, headers=headers)
    rjson = json.loads(response1.content)
    for entry in rjson['files']:
        jar_url = f'https://optifine.cn/download/{entry["name"]}'
        if not os.path.exists(f'{entry["version"]}'):
            os.makedirs(f'{entry["version"]}')
        file_name = str(entry["name"]).replace('legacy_', '')
        file_path = f'{entry["version"]}/{file_name}'
        if not os.path.isfile(file_path):
            response2 = requests.get(jar_url, headers=headers)
            with open(file_path, 'wb') as f:
                f.write(response2.content)
                print(f'Downloaded {file_name}')
            time.sleep(5)

if __name__ == '__main__':
    # download_from_bmclapi2()
    download_from_optifinecn()