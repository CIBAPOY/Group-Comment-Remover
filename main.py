import requests
import json
import os
import time

os.system('cls')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

dir = os.path.dirname(os.path.abspath(__file__))
cook = os.path.join(dir, "cookie.txt")

f = open(cook, "r")
cookie = f.read()
f.close()

testing = requests.post('https://auth.roblox.com/v2/logout', cookies = {'.ROBLOSECURITY':cookie})

token = testing.headers['x-csrf-token']

print(f"{bcolors.WARNING}   _____                        _____                                     _   _____                                    ")
print("  / ____|                      / ____|                                   | | |  __ \                                   ")
print(" | |  __ _ __ ___  _   _ _ __ | |     ___  _ __ ___  _ __ ___   ___ _ __ | |_| |__) |___ _ __ ___   _____   _____ _ __ ")
print(" | | |_ | '__/ _ \| | | | '_ \| |    / _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \| __|  _  // _ \ '_ ` _ \ / _ \ \ / / _ \ '__|")
print(" | |__| | | | (_) | |_| | |_) | |___| (_) | | | | | | | | | | |  __/ | | | |_| | \ \  __/ | | | | | (_) \ V /  __/ |   ")
print("  \_____|_|  \___/ \__,_| .__/ \_____\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__|_|  \_\___|_| |_| |_|\___/ \_/ \___|_|   ")
print("                        | |                                                                                            ")
print(f"                        |_|                                                                                            {bcolors.ENDC}")

print("\n")

groupid = input(f'{bcolors.OKGREEN}Enter group id: {bcolors.ENDC}')

header = {
    'cookie': cookie,
    'x-csrf-token': token
}

repeatimes = 1000
while True:

    try:
        r = requests.get(f"https://groups.roblox.com/v1/groups/{groupid}/wall/posts/", headers=header)
        lol = str(r.content)
        lol = lol[2:len(lol)-1]
        lol = lol.encode('unicode_escape')
        print(lol)

        val = json.loads(lol)
        anythingbutboob = {}
        for i in range(0,len(val['data'])):
            anythingbutboob[i] = val['data'][i]['id']
        for v in anythingbutboob:
            r = requests.get(f"https://groups.roblox.com/v1/groups/{groupid}/wall/posts/", headers=header)
            repeatimes = str(r.content)
            repeatimes = repeatimes[11:len(repeatimes)-2]

            b = anythingbutboob[v]
            b = str(b)

            payload = {
                'targetUserId': v
            }
            r = requests.delete(f"https://groups.roblox.com/v1/groups/{groupid}/wall/posts/{anythingbutboob[v]}", data=payload, headers=header)
            debug = str(r.content)
            if debug == "b'{}'":
                print("Successfully removed comment!")
            else:
                print(debug)
    except:
        pass
