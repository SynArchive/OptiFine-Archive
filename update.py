import json
import os
import re
import requests

BMCLAPI2_VERSION_LIST = 'https://bmclapi2.bangbang93.com/optifine/versionList'

def download_from_bmclapi2():
    response1 = requests.get(BMCLAPI2_VERSION_LIST)
    rjson = json.loads(response1.content)
    for entry in rjson:
        jar_url = f'https://bmclapi2.bangbang93.com/optifine/{entry["mcversion"]}/{entry["type"]}/{entry["patch"]}'
        if not os.path.exists(f'{entry["mcversion"]}'):
            os.makedirs(f'{entry["mcversion"]}')
        file_path = f'{entry["mcversion"]}/{entry["filename"]}'
        if not os.path.isfile(file_path):
            response2 = requests.get(jar_url)
            with open(file_path, 'wb') as f:
                f.write(response2.content)
                print(f'Downloaded {entry["filename"]}')

if __name__ == '__main__':
    download_from_bmclapi2()