import requests
import argparse
import pyfiglet
from termcolor import colored

# open
Bl='\033[30m'
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

# close
cl='\033[0m'

# banner
banner = pyfiglet.figlet_format("Link Admin")
text = colored(banner, "red")
print(text)

print(f'''{Re}DISCLAIMER!{cl}\n {Wh}This tool is only for educational purposes, I am not Responsible for any damage for a website
{cl}\n''')

# admin panels
admin_panel = open("paths.txt", "r")

# defines the parser
parser = argparse.ArgumentParser() 

# Arguements that can be supplied
parser.add_argument("-u", help="target url", dest='target')
args = parser.parse_args()

# input of the site
target = args.target
try:
    target = target.replace('https://', '')
except:
    print(f'\n{Re}[-] -u argument is not supplied. Enter python main.py -h/--help for help{cl}\n')
    quit()
target = target.replace('http://', '')
target = target.replace('/', '')
target = 'http://' + target

try:
    re = requests.get(target + '/robots.txt')
    if '<html>' in re.text:
        print ('  \033[1;31m[-]\033[1;m Robots.txt not found\n')
    else:
        print ('  \033[1;32m[+]\033[0m Robots.txt found\n')
        file = open("data.html", "w")
        file.write(re.text)
        print("\033[1;32m[+]\033[0m Open the file 'data.html' to find what is written in it.\n")
except:
    print ('  \033[1;31m[-]\033[1;m Robots.txt not found\n')

for each in admin_panel:
    if not each[0] == "/":
        each = "/"+each
    try:
        requests.get(target+each)
    except:
        print(f"{Cy}Could not find{cl}")
    else:
        r = requests.get(target+each)
        if r.status_code == 200:
            if len(r.history) == 0:
                print(f"{Gr}[+]",target+each,{cl})
                break
            else:
                print(f"{Ye}[-] redirected{cl}")
        else:
            print(f"{Re}[-]{cl}",target+each)