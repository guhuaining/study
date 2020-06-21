import sys
import pygame


'''游戏开始界面'''
def startInterface(screen, begin_image_paths,begin_button_path):
    begin_image=pygame.image.load(begin_image_paths)
    begin_image=pygame.transform.scale(begin_image, (993,480))
    #对图片进行缩放，使适应窗口大小
    button_image=pygame.image.load(begin_button_path)
    button_image=pygame.transform.scale(button_image,(300,180))
    while True:
        for event in pygame.event.get():#获取键盘事件，通过遍历从而实现对对应事件进行响应
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()#获取鼠标的位置
                #判断鼠标点击的位置是否处于开始游戏对应按钮的位置
                if mouse_pos[0] in list(range(200, 500)) and mouse_pos[1] in list(range(300, 480)):
                   return True
        screen.blit(begin_image, (0, 0))
        screen.blit(button_image,(200,300))
        #使开始按钮处于居中位置
        pygame.display.update()