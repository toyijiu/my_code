import pygame

def main():
    pygame.init()
    #初始化窗口
    screen = pygame.display.set_mode((800,600))
    #标题
    pygame.display.set_caption("大球吃小球")
    #设置窗口背景色
    screen.fill((242,242,242))
    #设置一个园，入参分别是屏幕，颜色 圆心位置 半径 0表示填充
    pygame.draw.circle(screen,(255,0,0),(100,100),30,0)
    #刷新窗口
    pygame.display.flip()
    running = True

    while running:
        #从消息队列中获取事件并处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



if __name__ == "__main__":
    main()