"""

@author: mehdi



"""


import os
import time
import urllib.request

import requests
import wget
from bs4 import BeautifulSoup

import Scripts.Core as Core

noex = list()
class WorldSubtitle:

	def __init__ (self , name ,  pf=None):
		self.name = name ;  self.pf = pf

	def main_page (self):
		
		global noex;
		web = "https://worldsubtitle.me/?s="+self.name.replace(" ", "+")
		try :
				req = urllib.request.Request(web, data=None, headers={
						'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
						#'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
						#'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'
						})
				page = urllib.request.urlopen(req)
				ReadingThePage = page.read().decode('utf-8')
				soup = BeautifulSoup(ReadingThePage,  features="lxml")
				div = soup.find_all('div', attrs={'class': 'cat-post-bt'})
				title = list()
				title2 = list() ; t3 = list()
				for a in div:
						resualt = a.find('a')
						title.append(resualt.attrs['title'])
						title2.append(resualt.attrs['href'])
				print (title)
				st=list()
				if len(title)!=0:
					
					for se in title:
							f = Core.final_name(se).lower()
							print ( f + "  "+ self.name)
							if self.name == f :
									con  = title.index(se)
									st.append (title2[con])
									t3.append(f)
									answer = [True , st , t3]
									return answer
							elif title.index(se) == title.index(title[-1]):
									noex.append(self.name)
									answer = [False, noex ]
									return  answer
				else:
					return [False]
		except Exception  :
						pass

	def resualt_page(self ,web2):
		
		try :
			req2 = urllib.request.Request(
			web2,
			data=None,
			headers={
				#'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
						})
			page2 = urllib.request.urlopen(req2)
			ReadingThePage2 = page2.read().decode('utf-8')
			soup2 = BeautifulSoup(ReadingThePage2,  features="lxml")
			div2 = soup2.find_all('div', attrs={'class': 'new-link-3'})
			for a in div2:
				resualt2 = a.find('a')
				link_page2 = resualt2.attrs['href']
				#link_page2 = link_page2.replace("https", "http")
				link_page3 = link_page2.replace("https", "http")
				print (link_page3)
				wget.download(link_page3 , self.pf)
				#wget.download(link_page2 , self.pf)
				return True
		except UnicodeDecodeError :
			return "err"
		except  Exception :
			print (str(Exception))
			print (link_page3)
			search = Core.OsDetection(link_page3)
			os.system(search)
			return False
