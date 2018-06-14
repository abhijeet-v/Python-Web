import webbrowser
import bs4
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as soup

print ("Welcome to my Downloader")
running = True;
while running:
    print("1 = Music Downloader")
    print("2 = TV Show/Series Downloader")

    cmd = int(input("Enter number : "))
    if cmd ==1:
        print ("***mp3 Downloader***")
        Search = input("Enter the name of the song you want to search : ")
        link = 'https://mp3pn.info/song/50094280/'+Search+'/'
        page = urlopen(Request(link, headers={'User-Agent' : 'Mozilla'}))
        page_html = page.read()
        pagen = soup(page_html, "html.parser")
        urla = pagen.findAll("a", {"id" : "SongView"})
        urla
        contb = urla[0]
        contc = contb["href"]
        webbrowser.open_new(contc)
        print ("MESSAGE:	***Thanks for using it.***")
        break

    elif cmd ==2:
        name = input("Enter the name of 'TV SHOW/SERIES' you want to search : ")
        link = 'https://eztv.ag/search/'+name
        page = urlopen(Request(link,headers={'User-Agent' : 'Mozilla'}))
        page_html = page.read()
        pagen = soup(page_html, "html.parser")
        a = pagen.findAll("a", {"class" : "magnet"})
        b = a[0]
        c = b['href']
        c

        webbrowser.open_new(c)
        print ("MESSAGE:	***Thanks for using it.***")
        
        break
    else:
            break
running = False;
