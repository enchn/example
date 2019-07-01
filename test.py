import bs4, requests, json, pafy, googletrans, datetime

mozhdr,z={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"},{"User-Agent":"Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36"}
class h:
	def shorturl(link):return requests.get("https://api-ssl.bitly.com/v3/shorten?access_token={}&longUrl={}".format(requests.get("https://md5.pinasthika.com/api/decrypt?value=4ad62d27a08d8b794c867408fdfbc5ea").json()["result"],link)).json()["data"]["url"]
	def bsverif(link,hdr):
		if hdr == False:return bs4.BeautifulSoup(requests.get(link,verify=False).content, "html5lib")
		else:return bs4.BeautifulSoup(requests.get(link,verify=False,headers=mozhdr).content, "html5lib")
	def bs(link,hdr=True):
		if hdr == False:return bs4.BeautifulSoup(requests.get(link).content, "html5lib")
		else:return bs4.BeautifulSoup(requests.get(link,headers=z).content, "html5lib")
	def pbs(link):return print(bs4.BeautifulSoup(requests.get(link,headers=mozhdr).content,"html5lib").prettify())
	def pbs2(link):return bs4.BeautifulSoup(requests.get(link).content,"html5lib").prettify()
	def pj(jsonnya):print(json.dumps(jsonnya,indent=4))
	def loadskan(jsonnya):return json.loads(jsonnya)
	def ytmp4(id):return pafy.new(id,basic=False).videostreams[-1].url
	def elist(list,wildanganteng,thisiswrk):
		no,wrk=1,"[ {} ]\n\n".format(wildanganteng)
		for data in list:wrk+="{}. {}\n".format(str(no),data);no+=1
		wrk+="\n[ Finish ]\n\n"+thisiswrk
		return wrk
	def tr(txt,dr,ke):return googletrans.Translator().translate(txt,dest=ke,src=dr).text
	def w(f,t):
		with open (f,"w") as x:x.write(str(t))
		
data,dataa=h.bs("https://www.goal.com/id/berita/jadwal-siaran-langsung-sepakbola/1qomojcjyge9n1nr2voxutdc1n").find("div",class_="body"),[]
hari=["Senin","Selasa","Rabu","Kamis","Jum'at","Sabtu","Minggu"]

def jadwal():
	for kompetisii in data.findAll("a",{"target":"_blank"}):
		info=h.bs(kompetisii.get("href"))
		infox=kompetisii.text.split(" | ")
		jam=infox[0]
		pertandingan=infox[1]
		channel=infox[2]
		infoo=info.title.text.split(",")
		kompetisi=infoo[2].split(" | ")[0][1:]
		try:
			dt=infoo[1][1:].split("/")
			day=hari[datetime.date(int(dt[0]),int(dt[1]),int(dt[2])).weekday()]
			month=h.tr(datetime.date(int(dt[0]),int(dt[1]),int(dt[2])).strftime("%B"),"en","id")
			datee="{}, {} {} 20{}".format(day, dt[0],month,dt[2])
		except:
			dt=info.find("time",{"data-dateformat":"monthDay"}).text[2:].split("/")
			day=hari[datetime.date(int(dt[0]),int(dt[1]),int(dt[2])).weekday()]
			month=h.tr(datetime.date(int(dt[0]),int(dt[1]),int(dt[2])).strftime("%B"),"en","id")
			datee="{}, {} {} 20{}".format(day, dt[0],month,dt[2])
		dataa.append({"pertandingan":pertandingan,"kompetisi":kompetisi,"tanggal":datee,"jam":jam,"channel":channel})
	h.pj(dataa)
jadwal()
	