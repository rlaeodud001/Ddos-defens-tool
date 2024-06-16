# Copyright © dark_min_. All Rights Reserved.

import os
import subprocess
import time
import urllib.request

print("discord name: dark_min_\nCopyright © dark_min_. All Rights Reserved.\n")

url = "https://api.ip.pe.kr/"

obj = urllib.request.urlopen(url)
ip = obj.read().decode('utf-8')

def menu_en():
    text = """                                                  
                                   ###                        
####                ####          ##                          
## ##   ###   ###   ## ##   ###  #####  ###  # ##   ###  ###  
##  ## ## ## ##     ##  ## ## ##  ##   ## ## ## ## ##   ## ## 
##  ## ## ## ###    ##  ## ## ##  ##   ## ## ## ## ###  ## ## 
##  ## ## ##  ###   ##  ## #####  ##   ##### ## ##  ### ##### 
## ##  ## ##   ##   ## ##  ##     ##   ##    ## ##   ## ##    
####    ###  ###    ####    ####  ##    #### ## ## ###   #### 

        Copyright © dark_min_. All Rights Reserved.
        github: https://github.com/rlaeodud001

[0] 핑 모니터링
    """
    print(text)

def shutdown_system():
    current_os = os.name
    if current_os == "nt": 
        os.system("shutdown /s /t 10")

def check_ping(ip):
    if os.name == 'nt':  
        response = os.popen(f"ping {ip} -n 1").read()

    if "TTL=" in response or "ttl=" in response:
        return True
    elif "요청 시간이 만료되었습니다." in response:
        return False
    elif "리소스가 없습니다." in response:
        return False
    else:
        return None

while True:
    menu_en()
    choice = input("원하는 작업 번호를 입력하세요> ")
    if choice == '0':
        print(f"핑 모니터링을 시작합니다. 보호할 IP: {ip}")
        if os.name == 'nt':  
            subprocess.Popen(["start", "cmd", "/k", f"ping {ip} -t"], shell=True)
        try:
            while True:
                ping_result = check_ping(ip)
                if ping_result is False:
                    print("요청 시간을 만료했습니다. 시스템을 종료합니다.")
                    shutdown_system()
                    break
                time.sleep(1)
        except KeyboardInterrupt:
            print("핑 모니터링을 종료합니다.")
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")

# Copyright © dark_min_. All Rights Reserved.
