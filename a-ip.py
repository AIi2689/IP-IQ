import requests,re,os,time
from time import sleep as sp
import json
from bs4 import BeautifulSoup as parser



def clear():
	os.system('clear')
def line():
	print (51*'-')
def logo():
	logo =('''
\t \033[1;32m###### ######   
\t   ##   ##   ##  
\t   ##   ##   ##  
\t   ##   ##   ##  
\t   ##   ######   
\t   ##   ##	   
\t ###### ##[ ᏕᏢᎨᎠᏒ ᏉᎨᏢ ] [ IP ]
---------------------------------------------------
ادات فك حظر صيد   : \033[1;96مطور @TTL9T \033[1;97m  ]
\033[1;31m> https://t.me/hackfhg <		 
---------------------------------------------------''')
	print(logo)

class iAmIPClass:
	def __init__(self):
		self.ip_check_url = "http://ip-api.com/json/"
		self.ip_unblock_url= 'https://updraftplus.com/unblock-ip-address/'
	def iAmMenu(self):
		clear();logo()
		print(" [•] \033[1;35mأداة إلغاء حظر IP بواسطة محتوه غير معين ")
		line()
		print(' [1] قم بإلغاء حظر IP الخاص بالجهاز يدويًا \n [2] إلغاء حظر شبكة IP التلقائي')
		line()
		m = input(' [•] حدد الخيار: ')
		if m in ['1','01']:self.manual()
		else:self.iAmIPChecker()
	def manual(self):
		clear();logo()
		print(' [•] \033[1;34mانتقل إلى إعدادات الجهاز/حول الجهاز')
		print(' [•] انتقل إلى إعدادات الجهاز/حول الجهاز ')
		print(' [•] انسخ عنوان IP الخاص بجهازك من About ')
		line ()
		ip = input(' [•] \033[1;33mالصق IP جهازك هنا : ')
		line()
		self.iAmIPUnblocker(ip)
	def iAmIPChecker(self):
		clear();logo()
		print(" [•] \033[1;36mفعل وضع الطيران مده خمس ثواني وارجع شغل وادوس انتر .")
		input(" [•] اضغط على Enter للبدء ...")
		sp(2)
		print(" [•] \033[1;35mالكشف عن عنوان IP الخاص بك ...")
		try:
			getting_network_ip = requests.get(self.ip_check_url).json()
			ip = getting_network_ip["query"]
			print(f" [•] \033[1;32mعنوان IP العام الخاص بك\033[1;31m : {ip}")
			self.iAmIPUnblocker(str(ip))
		except requests.exceptions.ConnectionError:
			print(' [•] \033[1;31mتحقق من فشل الإنترنت الخاص بك في اكتشاف IP ')
		except KeyError:
			print(' [•] الرجاء تغيير الشبكة الخاصة بك !! ..')
		except Exception as e:
			print(e)
				#open("/sdcard/iprespo.txt","w").write(r)
	def iAmIPUnblocker(self,x):
		print(" [•]\033[1;32m محاولة إلغاء حظر عنوان IP الخاص بك ...")
		try:
			r2 = requests.get(self.ip_unblock_url).text
		except requests.exceptions.ConnectionError:
			print(' [•] \033[1;31mتحقق من فشل الإنترنت في إلغاء حظر عنوان IP الخاص بك ')
		data={}
		ud_unblock_ip = x
		nonce= re.search('name="nonce" value="(.*?)"',r2).group(1)
		data.update(
			{
'ud_unblock_ip':ud_unblock_ip,
'nonce':nonce,
			}
			)
		try:
			po = requests.post(self.ip_unblock_url,data=data).text
		except requests.exceptions.ConnectionError:
			print(' [•]\033[1;31m تحقق من فشل الإنترنت في إلغاء حظر عنوان IP الخاص بك ')
		if "لقد تم إلغاء حظر IP الخاص بك بنجاح" in po:
			print(" [•] تم إلغاء حظر IP بنجاح ")
			line()
			exit()
		elif "\033[1;31mتم إلغاء حظر عنوان IP هذا مؤخرًا.  إذا تم حظره مرة أخرى، فيجب عليك تقديم طلب دعم يدوي." in po:
			exit(" [•] تم إلغاء حظر عنوان IP بالفعل ")
		else:
			pass
			#rint(" [•] We are failed to unblock your IP Address")

if __name__=="__main__":
		iAmIPClass().iAmMenu()
		