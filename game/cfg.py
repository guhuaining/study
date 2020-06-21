'''配置文件'''
import os


CURPATH = os.getcwd()#用于返回目标的当前工作目录
SCREENSIZE = (993, 477)
HAMMER_IMAGEPATHS = [os.path.join(CURPATH, 'resources/images/hammer0.png'), os.path.join(CURPATH, 'resources/images/hammer1.png')]
GAME_BEGIN_IMAGEPATHS = os.path.join(CURPATH, 'resources/images/begin0.jpg')
GAME_BUTTON_IMAGEPATH = os.path.join(CURPATH, 'resources/images/button.png')
GAME_AGAIN_IMAGEPATHS = [os.path.join(CURPATH, 'resources/images/again1.png'), os.path.join(CURPATH, 'resources/images/again2.png')]
GAME_BG_IMAGEPATH = os.path.join(CURPATH, 'resources/images/background.png')
GAME_END_IMAGEPATH = os.path.join(CURPATH, 'resources/images/end.jpg')
MOLE_IMAGEPATHS = [os.path.join(CURPATH, 'resources/images/Tom&Jerry-01.png'), os.path.join(CURPATH, 'resources/images/Tom&Jerry-02.png'),
                   os.path.join(CURPATH, 'resources/images/Tom&Jerry-03.png'), os.path.join(CURPATH, 'resources/images/Tom&Jerry-04.png')]
HOLE_POSITIONS = [(90, -20), (405, -20), (720, -20), (90, 140), (405, 140), (720, 140), (90, 290), (405, 290), (720, 290)]
BGM_PATH = 'resources/audios/bgm.mp3'
COUNT_DOWN_SOUND_PATH = 'resources/audios/count_down.wav'
HAMMERING_SOUND_PATH = 'resources/audios/count_down.wav'
FONT_PATH = 'resources/font/PAPYRUS.ttf'
WHITE = (255, 255, 255)
RED = (255, 0, 0)
RECORD_PATH = 'score.rec'#用于存储最佳成绩