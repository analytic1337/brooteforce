#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
  ██████╗██╗   ██╗██████╗ ███████╗██████╗ ██╗  ██╗ █████╗ ██████╗ ███╗   ███╗
 ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██║  ██║██╔══██╗██╔══██╗████╗ ████║
 ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝███████║███████║██████╔╝██╔████╔██║
 ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██╔══██║██╔══██║██╔══██╗██║╚██╔╝██║
 ╚██████╗   ██║   ██████╔╝███████╗██║  ██║██║  ██║██║  ██║██║  ██║██║ ╚═╝ ██║
  ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
                            t.me/CyberHarm
'''

from os import system, name
def clr():
  '''
  Clears console
  '''
  
  _=system('cls' if name in ('nt', 'dos') else 'clear')

clr()



"""
from pyfiglet import Figlet # Ascii-Text
def fg(txt, size):
  '''
  Prints ASCII text
  '''

  if size is None or len(size) <= 1:
    size = 'small'
  
  return Figlet(font=size).renderText(txt)
"""



cf_ips = [ # Cloudflare IP's
    '103.21.244',
    '103.22.200',
    '103.31.4',
    '104.16',
    '104.24',
    '108.162.192',
    '131.0.72',
    '141.101.64',
    '162.158',
    '172.64',
    '173.245.48',
    '188.114.96',
    '190.93.240',
    '197.234.240',
    '198.41.128',
    '172.67',
    '104.21',
    '104.18',
]

#from colorama import Fore
from socket import gethostbyname, gethostbyname_ex
def getip(host, realurl, realip): # Get IP from website
  try:
    ip = str(gethostbyname_ex(host)) # From Tuple to String
    ip = ip.replace('[],', '').replace('[]', '').replace(',', ' &').replace('[],', '').replace('[]', '').replace('(', '').replace(')', '').strip().replace('\'', '').replace('[', '').replace(']', '').replace('  ', ' ')#.replace(realip, '').replace(realurl, '') # Clean some shit
  
    if not 'cloudflare' in ip:
      for cf_ip in cf_ips:
        if ip.startswith(cf_ip):
          return # If it's cloudflare IP then skip it
    
      return ip

  except:
    return