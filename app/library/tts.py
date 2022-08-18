from gtts import gTTS
import os
# __author__ = 'info-lab'
# imgpath = 'Upload/image.png'
# text = '오마이갓'


def makedirs(path): 
   try: 
        os.makedirs(path) 
   except OSError: 
       if not os.path.isdir(path): 
           raise
       
def save_sound(imgpath:str,text:str):
    tts = gTTS(
        text,
        lang='ko', slow=False
    )
    root_path = 'Upload/sound'
    makedirs(root_path)
    save_path = root_path + '/' + os.path.basename(imgpath).split('.')[0] + '.mp3'
    tts.save(save_path)
    
    return save_path
    
# print(save_sound(imgpath,text))