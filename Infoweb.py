#!/usr/bin/python
#Script para coletar informacoes e emails de aplicacoes web
#Desenvolvido por Derick Santos
#Conheca a FSociety Brasil: fsocietybrasil.org
 
import urllib
import re
import sys
import os
import time
import socket
 
try:
    red = '\033[31m'
    yellow = '\033[33m'
    blue = '\033[34m'
    black = '\033[30m'
    green = '\033[32m'
    white = '\033[37m'
    fim = '\033[0;0m'
   
    os.system("clear")
    var = None
    site = sys.argv[1]
   
    time.sleep(3)
    banner = yellow+'''    
                _________ _        _______  _______           _______  ______  
                 \__   __/( (    /|(  ____ \(  ___  )|\    /|(  ____ \(  ___ \
            ) (   |  \ ( || (    \/| (   ) || )   ( || (    \/| (   ) )
            | |   |   \ | || (__    | |   | || | _ | || (__    | (__/ /
                | |   | (\ \) ||  __)   | |   | || |( )| ||  __)   |  __ (  
            | |   | | \  || (      | |   | || || || || (      | (  \ \
         ___) (___| )  \ || )      | (___) || () () || (____/\| )___) )
         \_______/|/    )_)|/       (_______)(_______)(_______/|/\____/ '''+fim
   
    print(banner)
    print green+"============================================="+fim
    print yellow+"FAZENDO REQUISICAO HTTP....................."+fim
    print green+"============================================="+fim
    url = urllib.urlopen("http://"+site)
   
    time.sleep(3)
    print green+"=============================================="+fim
    print yellow+"COLETANDO INFORMACOES DO CODIGO FONTE........"+fim
    print green+"=============================================="+fim
    code = (url.read())    
    url_info = (url.info())
   
    time.sleep(3)
    print green+"=============================================="+fim
    print yellow+"COLETANDO IP................................."+fim
    print green+"=============================================="+fim
    ip = socket.gethostbyname(site)
 
    time.sleep(3)
    print green+"=============================================="+fim
    print yellow+"COLETANDO E-MAILS............................"+fim
    print green+"=============================================="+fim
    email = re.findall(r'[\w_]+[\w.]+[\w-]@[\w_]+[\w.]+[\w-]', code)
   
    time.sleep(3)
    print green+"\n============================================"+fim
    print yellow+"INFORMACOES COLETADAS........................"+fim
    print green+"==============================================\n"+fim
 
    for loop in site:
       time.sleep(4)
       print "SITE: "+"http://"+site
       time.sleep(4)
       print "IP: "+ip
       time.sleep(4)
       print "INFORMACOES: \n", url_info
       time.sleep(4)
       print "E-MAILS: ", email
       exit()
 
except KeyboardInterrupt:
    print red+"\nAte logo!\n"+fim
except IndexError:
        banner = yellow+'''
            _________ _        _______  _______           _______  ______  
            \__   __/( (    /|(  ____ \(  ___  )|\    /|(  ____ \(  ___ \
               ) (   |  \ ( || (    \/| (   ) || )   ( || (    \/| (   ) )
               | |   |   \ | || (__    | |   | || | _ | || (__    | (__/ /
               | |   | (\ \) ||  __)   | |   | || |( )| ||  __)   |  __ (  
               | |   | | \  || (      | |   | || || || || (      | (  \ \
            ___) (___| )  \ || )      | (___) || () () || (____/\| )___) )
            \_______/|/    )_)|/       (_______)(_______)(_______/|/\____/
 
                           COLETOR DE INFORMACOES E EMAILS DE APLICACOES WEB                              
                                  Desenvolvido por Derick Santos
                            Conheca a FSociety Brasil: fsocietybrasil.org
                                  Use: ./infoweb.py www.site.com
                                                                                     '''+fim
    print(banner)
