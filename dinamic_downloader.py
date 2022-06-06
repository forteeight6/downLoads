from downloader_youtube import *

def options(op, title, url):
    match op:
        case 1:
            if title:
                downloadVideoFromYoutube(title,url, './')
            else:
                downloadVideoFromYoutube(url, './')
        case 2:
            if title:
                downloadAudioFromYoutube(title,url, './')
            else:
                downloadAudioFromYoutube(url, './')
        case _:
            return "Falhou"
    

def main():
    url = str(input("URL < "))
    title = str(input('TITLE (opcional) < '))
    print(type(title), len(title))
    op = int(input(" 1 to mp4, 2 to mp3 < "))
    options(op, title, url)
                
if __name__ == "__main__":
    main()