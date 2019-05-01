import dns.resolver
from colorama import *
import time
import os

os.system("clear")


print(Style.BRIGHT + "___________              .__         .__  __            __________                    ")
print(Style.BRIGHT + "\_   _____/__  _________ |  |   ____ |__|/  |_          \____    /____   ____   ____  ")
print(Style.BRIGHT + " |    __)_\  \/  /\____ \|  |  /  _ \|  \   __\  ______   /     //  _ \ /    \_/ __ \ ")
print(Style.BRIGHT + " |        \>    < |  |_> >  |_(  <_> )  ||  |   /_____/  /     /(  <_> )   |  \  ___/ ")
print(Style.BRIGHT + "/_______  /__/\_ \|   __/|____/\____/|__||__|           /_______ \____/|___|  /\___  >")
print(Style.BRIGHT + "        \/      \/|__|                                          \/          \/     \/ ")

print(Style.BRIGHT + """
 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
 #				User It Responsibly				    #
 #				Made By Antoine Zayat				    #
 #                              Github: hacker900123				    #
 ####################################################################################
 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")
domain = input(Fore.CYAN + "[?] Enter Website To Resolve Its Name Servers: ")
nameservers = dns.resolver.query(domain,'NS')
print("[*] Extracting Name Servers....")
time.sleep(4)
for data in nameservers:
    print ("[+] " + str(data))
