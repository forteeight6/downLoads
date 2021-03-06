from pytube import YouTube, streams
import re
# !pip install pytube
"""
    O pytube cria o diretorio para você. Exemplo:
    Execute as funções com a local ainda não existente,
    o pytube ira criar a pasta e as subspastas referente ao valor
    inserido no parametro 'output_path'.
    
    Pytube creates the directory for you. Example:
    Execute the functions with the location not yet existent,
    pytube will create the folder and subfolders referring to the value
    entered in the parameter.
"""

def downloadAudioFromYoutube(*args) -> None:
    """ Download de Audio do Youtube / Youtube Audio download.
    
    Função que possibilita o download de Audio do Youtube.
    Function that allows you to download audio from Youtube.
    
    :param - args[0]: Url of the audio you want to download.
    :param - args[1]: Location where you want to save the audio.
    :return - None
    """
    
    youtube = YouTube(args[0])
    
    if (title is False) | (len(title) == 0):
        title = re.sub(r"[/:,.?]","-", youtube.title)
    
    title = youtube.title + ".mp3"
    stream = youtube.streams.get_audio_only()
    stream.download(output_path=args[1], filename=title + ".mp3")
    print('Download completed successfully!')
    return None

def downloadVideoFromYoutube(title=None, *args) -> None:
    """ Download de video do Youtube / Youtube video download.
    
    Função que possibilita o download de video do Youtube.
    Function that allows you to download video from Youtube.
    
    :param - title: Denined title to save the video.
    :param - args[0]: Url of the video you want to download.
    :param - args[1]: Location where you want to save the video.
    :return - None
    """

    youtube = YouTube(args[0])
    if (title is False) | (len(title) == 0):
        title = re.sub(r"[/:,.?]","-", youtube.title)
        
    print('Estou tentando baixar o seguinte video:\n', title)
    stream = youtube.streams.get_highest_resolution()
    
    stream.download(output_path=args[1], filename=title+".mp4")
    print('Download completed successfully!')
    return None

if __name__ == "__main__":
    
    url = "https://www.youtube.com/watch?v=jq6C3aIDkKI"
    location = "./"
    downloadVideoFromYoutube("teste",url, location)