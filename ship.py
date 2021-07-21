import pygame

class Ship:
  """ 管理飞船的类 """

  def __init__(self, ai_game):
    """ 初始化飞船并设置初始位置 """
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()

    # 加载飞船图像并获取其外接矩形
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()

    # 对于每艘新飞船，都将出现在屏幕底部中央
    self.rect.center = self.screen_rect.center

    self.settings = ai_game.settings

    # 在飞船的属性X中存储小数值
    self.x = float(self.rect.x)
    self.y = float(self.rect.y)

    self.move_right = False
    self.move_left = False
    self.move_up = False
    self.move_down = False



  def update(self):
    """ 根据移动标志，更新飞船的位置 """
    if self.move_right and self.rect.right < self.screen_rect.right:
      self.x += self.settings.ship_speed
    if self.move_left and self.rect.left > 0:
      self.x -= self.settings.ship_speed
    if self.move_up and self.rect.top > 0:
      self.y -= self.settings.ship_speed
    if self.move_down and self.rect.bottom < self.screen_rect.bottom:
      self.y += self.settings.ship_speed

    # 更新位置信息
    self.rect.x = self.x
    self.rect.y = self.y    


  def blitme(self):
    """ 在指定位置绘制飞船 """
    self.screen.blit(self.image, self.rect)