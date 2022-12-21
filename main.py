from pytube import YouTube


def Download(link):
    YouTubeObject = YouTube(link)
    YouTubeObject = YouTubeObject.streams.get_highest_resolution()
    try:
        YouTubeObject.download()
    except:
        print("Il tuo video non è stato scaricato")
    print("Il tuo video è stato scaricato")


link = input("Inserisci il link del tuo video ")
Download(link)
