#!/usr/bin/python

ver = "v1.2"
print(f"\033[1;91m\n   .   ,    .             .       .   \n    \ /     |   o         |     o |   \n     Y  . . |-  . . , ;-. | ,-. . |-  \n     |  | | |   |  X  | | | | | | |     \033[0;37m{ver}\033[1;91m\n     '  `-` `-' ' ' ` |-' ' `-' ' `-'  \n                      '               \033[0m")
import requests as req
req.urllib3.disable_warnings()
from colorama import Fore,Style
from bs4 import BeautifulSoup as bs

red    = Fore.RED
yellow = Fore.YELLOW
blue   = Fore.BLUE
white  = Fore.WHITE
bold   = Style.BRIGHT
green  = Fore.GREEN
dim    = Style.DIM
purple = Fore.MAGENTA
cyan   = Fore.CYAN
reset  = Style.RESET_ALL+white
mdate  = {}
mpreff = "m"

"""
		DON'T INSULT MY CODE
		I'M JUST NEWBIE CODER
		:)
"""

def main():
	try:
		print(f" {reset}\033[4mCubdomain Scraper{reset}\n https://t.me/yutixverse\n https://github.com/Yutixcode")
		Cubdo().liat()
		for i in range(1,19):
			x = f"    {reset}{i}. {cyan}{mdate[str(i)]}"
			globals()[mpreff + str(i)] = x
			
		print(f"\n{m1}{m11}\n{m2}{m12}\n{m3}{m13}\n{m4}{m14}\n{m5}{m15}\n{m6}{m16}\n{m7}{m17}\n{m8}{m18}\n\n{reset} enter the numbers above or write manual\n format {cyan}year-month-day {reset}example {cyan}2025-05-25{reset}")
		menu = input(f" your mind? > {cyan}")
		if menu:
			outs = input(f" {reset}saved domains to? > {cyan}")
			try: tanggal = mdate[menu]
			except KeyError: tanggal = menu
			print(f"{reset} take your pillow, this process can make you sleep\n")
			Cubdo(tanggal,outs).gasken()
		else:
			print(f"{reset} dumb!\n")
			
	except KeyboardInterrupt:
		print(f"{reset} killed!")
		exit()
		
class Cubdo:
	def __init__(self,tgl=None,out=None):
		self.path = f"domains-registered-by-date/{tgl}/"
		self.outs = open(out,"a") if out else None
		self.tots = 0
	
	def gas(self,path=""):
		respon = req.get(f"https://66.45.226.242/{path}",headers={'Host':'www.cubdomain.com'},verify=False,timeout=30).text
		return respon
	
	def gasken(self):
		try:
			raw = self.gas(self.path+"1")
			self.ambil(raw,"1")
			pages = bs(raw,"html.parser").find("ul",{"class":"pagination-sm pagination mb-0 mt-2"}).findAll("a")[-2].text.strip()
			for i in range(2,int(pages)+1):
				self.ambil(self.gas(self.path+str(i)),i)
			print(f"{reset}\n done, total {cyan}{self.tots}{white} domains, saved to {cyan}{self.outs.name}")
			print(f"{reset} thanks for using this fvcking tools\n")
		except KeyboardInterrupt:
			print(f"{reset} killed!")
			exit()
	
	def ambil(self,raw,hal):
		items = bs(raw,"html.parser").findAll("div",{"class":"col-md-4"})
		print(f"   page {purple}{hal}{reset} found {green}{len(items)}{reset} domains")
		self.tots += len(items)
		for item in items:
			domain = item.a.text.strip()
			self.outs.write(f"{domain}\n")
		
	def liat(self):
		sup = bs(self.gas(),"html.parser").find("ul",{"class":"list-unstyled mb-0 text-center"}).findAll("a")
		for i in range(18):
			tgl = sup[i]["title"].strip()
			mdate.update({str(i+1):tgl})

main()