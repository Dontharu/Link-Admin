import requests
import argparse
import pyfiglet
import os.path
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

print(f'''{Re}DISCLAIMER!{cl}\n {Wh}This tool is only for educational purposes\n I am not Responsible for any damage for a website
{cl}\n''')

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

# admin panels
try:
    user = input(f"{Mage}Do you want to put your own paths?(y/default(n)):{cl} ")
    if user == "n":
        print("")
        print(f"{Cy}[+]{cl} Default paths using")
        default = open("paths.txt", "r")
        pass

    elif user == "y":
        admin_panel = input("Enter file of paths path: ")
        try:
            admin = open(admin_panel, "r")
            print("")
            print(f"{Cy}[+]{cl} File is available for use")
        except IOError:
            print("")
            print(f"{Ye}[-]{cl} File is not accessible. {Re}Wrong Path!{cl}") 
            print("")
            quit()

    else:
        print("Type Error: "+user)
        print("")
        print(f"{Blu}Exiting the program! Goodbye{cl}")
        quit()
        print("")

except Exception as e:
    print(e)
    quit()

try:
    re = requests.get(target + '/robots.txt')
    if '<html>' in re.text:
        print(f'{Re}[-]{cl} Robots.txt not found\n')
        breakpoint()
    else:
        print("\n")
        print(f'{Gr}[+]{cl} Robots.txt found')
        print("")
        file = open("data.html", "w")
        file.write(re.text)
        print(f"{Gr}[+]{cl} Open the file 'data.html' to find what is written in it.\n")
except:
    print(f'{Re}[-]{cl} Robots.txt not found\n')


def link():
    if user == "n":
        for each in default:
            if not each[0] == "/":
                each = "/"+each
            try:
                combine = target+each
                requests.get(combine)
            except:
                break
            else:
                combine = target+each
                r = requests.get(combine)
                if r.status_code == 200:
                    print(f"{Gr}[+] Admin Panel: {combine}{cl}")             
                    file = open("admin_panels.txt", "a")
                    file.write(combine)
                elif r.status_code == 404:
                    print(f"{Re}[-]{cl}",combine)
                elif r.status_code == 302:
                    print(f"{Re}[-]{cl}",combine)
                else:
                    print(f"{Re}[-]{cl}",combine)

    elif user == "y":
        for each in admin:
            if not each[0] == "/":
                each = "/"+each
            try:
                combine = target+each
                requests.get(combine)
            except:
                break
            else:
                combine = target+each
                r = requests.get(combine)
                if r.status_code == 200:
                    print(f"{Gr}[+] Admin Panel: {combine}{cl}")
                    file = open("admin_panels.txt", "a")
                    file.write("")
                    file.write(combine)
                elif r.status_code == 404:
                    print(f"{Re}[-]{cl}",combine)
                elif r.status_code == 302:
                    print(f"{Re}[-]{cl}",combine)
                else:
                    print(f"{Re}[-]{cl}",combine)

    else:
        print(f"{Re}Wrong input!{cl}")

if __name__ == "__main__":

    link()
    path = "admin_panels.txt"
    check_file = os.path.exists(path)

    if check_file == True:
        with open(r"admin_panels.txt", 'r') as fp:
            for count, line in enumerate(fp):
               pass
        total = count + 1
        print(f"{Bl}[++]{cl} {Cy}{total}{cl} {Blu}Admin Panels Found . Go Check Out 'admin_panels.txt' To See The Admin Panels{cl}")

    else:
        print(f"{Ye}[--] Every SORRY We Couldn't Find And Admin Panel{cl}")
        print("")
