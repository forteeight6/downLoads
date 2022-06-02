import logging as log
from downloader_youtube import *

def test_downloadVideoFromYoutube():
    """ Entry-str-url, Expect-None
    
    I hope it's not returning anything.
    """
    entry_1 = "www.youtube.com/watch?v=1mq7GD-rCVg&t=7s"
    entry_2 = "./midia/video/"
    
    expect = None
    result = downloadVideoFromYoutube(entry_1, entry_2)
    assert result == expect
    log.warning(result)
    

def test_downloadAudioFromYoutube():
    """ Entry-str-url, Expect-None
    
    I hope it's not returning anything.
    """
    entry_1 = "https://www.youtube.com/watch?v=XK3Pb6BMxkY"
    entry_2 = "./midia/audio/"
    
    expect = None
    result = downloadAudioFromYoutube(entry_1, entry_2)
    assert result == expect
    log.warning(result)
    
if __name__ == "__main__":
    test_downloadVideoFromYoutube()
    test_downloadAudioFromYoutube()