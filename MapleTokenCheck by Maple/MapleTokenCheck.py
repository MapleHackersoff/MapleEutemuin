import pyfiglet
import requests
from colorama import Fore,Back,Style,init
init(autoreset=True)
#
ascii_banner0 = pyfiglet.figlet_format("Enter  code  :")
print(ascii_banner0)

question = input("Enter activation code: ")
start_over = 10
if question == "ABC-ILOVEMAPLE2020":
    start_over -= 1
    print("")
else:
    raise SystemExit
# activated
print('Contact: invite.gg/Maple')
print('Contact: invite.gg/MapleDev')

ascii_banner1 = pyfiglet.figlet_format("Maple  Token  Checker")
print(ascii_banner1)

print("Enter file name: ")
inp = input()

with open(inp + ".txt") as f:
    for line in f:
        token = line.strip("\n")
        headers = {'Content-Type': 'application/json', 'authorization': token}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            print(Fore.LIGHTGREEN_EX + "{} is valid.".format(token))
        else:
            print(Fore.LIGHTRED_EX + "{} is invalid.".format(token))