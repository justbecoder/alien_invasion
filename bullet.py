import pygame
from pygame.sprite import Sprite

class Bullet (Sprite):
  def __init__(self, ai_game):
    """ 在飞船当前位置创建一个字段对象 """
    super().__init__()

    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.color = self.settings.bullet_color

    # 在(0，0)位置创建子弹，在设置其正确位置
    self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

    self.rect.midbottom = ai_game.ship.rect.midtop

    # 存储子弹的位置
    self.y = float(self.rect.y)

  def update(self):
    """ 更新子弹位置信息 """
    self.y -= self.settings.bullet_speed
    self.rect.y = self.y

  def draw_bullet(self):
    """ 屏幕上绘制子弹 """
    pygame.draw.rect(self.screen, self.color, self.rect)