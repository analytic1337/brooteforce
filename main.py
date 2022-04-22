#!/usr/bin/python
# -*- coding: utf-8 -*-

# don't skid :)

from colorama import Fore # Colored text
#from simple_colors import * # I added it for bold text (And now I don't use it)
from __tools__ import clr, getip # My own library that can clear console and get IP of domain


clr() # Colorama doesn't work sometimes on Windows without clearing the window



class Style: # Some styles for text
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m' # \033[0;0m


print(f'''{Fore.RED}{Style.BOLD}
   ___     _             _  _
  / __|  _| |__  ___ _ _| || |__ _ _ _ _ __
 | (_| || | '_ \\/ -_) '_| __ / _` | '_| '  \\
  \\___\\_, |_.__/\\___|_| |_||_\\__,_|_| |_|_|_|
      |__/
                         {Fore.CYAN} cloudflare bypass
''')#, Style.END) # Watermark 
url = input(f' {Fore.YELLOW}url {Fore.RED}> {Fore.BLUE}') # Ask for a web-site
url = url.replace('https://', '').replace('http://', '').replace('www.', '').replace('ww1.', '').replace('ww2.', '').replace('ww3.', '') # Remove prefixes (subdomain and http(-s) prefix)

print(f" {Fore.GREEN}please{Fore.WHITE}, {Fore.GREEN}wait\n")


realip = getip(url, '', '')
if realip:
  realip = realip.replace(' &', f' {Fore.WHITE}|{Fore.BLUE}')

  print(f' {Fore.WHITE}[{Fore.BLUE}i{Fore.WHITE}] {Fore.BLUE}{url} {Fore.WHITE}: {Fore.BLUE}{realip}')


subdomains = open("dom.txt","r") # Open a file

checked = []

for sub in subdomains:
  sub = sub.strip()  # Remove spaces

  try:

    if sub in checked:
      sub = '[-] Already checked.';pass;getip('', '', '')
    else:
      checked.append(sub)


    # Check the subdomain
    if sub.endswith('.'):
      site = f'{sub}{url}'
    else:
      site = f'{sub}.{url}' # Subdomain + URL


    ip = getip(site, url, realip)
    
    if ip:
      ip = ip.replace(' &', f' {Fore.WHITE}|{Fore.GREEN}') # Get the IP of subdomain

      print(f' {Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}{site} {Fore.WHITE}: {Fore.GREEN}{ip}')


  except:


    
    try:

      if f'www.{sub}' in checked:
        sub = '[-] Already checked.';pass;getip('', '', '')
      else:
        checked.append(f'www.{sub}')

      # Try to use www. with subdomain
      site2 = f'www.{sub}.{url}' # www + Subdomain + URL
      ip2 = getip(site2, url, realip).replace(' &', f' {Fore.WHITE}|{Fore.GREEN}')
  
      print(f' {Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}{site2} {Fore.WHITE}: {Fore.GREEN}{ip2}')

    except:
      pass


    pass



print(f'\n {Fore.WHITE}[{Fore.ORANGE}!{Fore.WHITE}] {Fore.ORANGE}work finished{Style.END}')

input()
