
import os

def copyFiles(audioFile, videoFile, textFile, newDir):
    success = False
    if copy(audioFile,'b',newDir):
        print('audioCopied')
        if copy(videoFile, 'b',newDir):
            print('videoCopied')
            if copy(textFile,'',newDir):
                success = Trlue
    return success

def copy(file, t, newDir):
    success = False
    readType = ''.join(['r',t])
    writeType = ''.join(['w',t])
    try:
        f = open(file,readType)
        newFile = ''.join([newDir,r'/',os.path.basename(file)])
        print(newFile)
        newF = open(newFile,writeType)
        newF.write(f.read())
    except Exception as e:
        raise e
        return False
    return success


success = copyFiles(r'C:/Users/Hp/Desktop/old dir/t8_l_q19_audio.mp3',
          r'C:/Users/Hp/Desktop/old dir/VID-20170107-WA0022.mp4',
          r'C:/Users/Hp/Desktop/old dir/randomFile.txt',
          r'C:/Users/Hp/Desktop/new dir')
print(success)

import shutil
try:
    shutil.copyfile(r'C:\Users\Hp\Desktop\old dir\t8_l_q19_audio.mp3',r'C:\Users\Hp\Desktop\new dir\t8_l_q19_audio.mp3')
    shutil.copyfile(r'C:\Users\Hp\Desktop\old dir\randomfile.txt',r'C:\Users\Hp\Desktop\new dir\randomfile.txt')
    shutil.copyfile(r'C:\Users\Hp\Desktop\old dir\VID-20170107-WA0022.mp4',r'C:\Users\Hp\Desktop\new dir\VID-20170107-WA0022.mp4')
except Exception as e:
    raise e
