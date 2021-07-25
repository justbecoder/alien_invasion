import sys
import pygame
from pygame.constants import KEYUP, K_RIGHT

from settings import Settings
from ship import Ship

class AlientInvasion:
  """ 管理游戏资源和行为的类 """
  def __init__ (self):
    pygame.init()

    # 获取游戏配置
    self.settings = Settings()

    # 设置屏幕大小 - 全屏

    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    self.settings.screen_width = self.screen.get_rect().width
    self.settings.screen_height = self.screen.get_rect().height

    # 飞船
    self.ship = Ship(self)

    # 设置屏幕背景色
    pygame.display.set_caption(self.settings.caption_title)

  def _check_events(self):
    """ 响应按键和鼠标事件 """
    for event in pygame.event.get():
      
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)

      if event.type == pygame.KEYUP:
        self._check_keyup_events(event)

  def _check_keydown_events (self, event):
    """ 响应按键 """
    if event.key == pygame.K_RIGHT:
      self.ship.move_right = True
    if event.key == pygame.K_LEFT:
      # 向左移动飞船
      self.ship.move_left = True
    if event.key == pygame.K_UP:
      self.ship.move_up = True
    if event.key == pygame.K_DOWN:
      self.ship.move_down = True

    if event.key == pygame.K_q:
        pygame.quit()
        sys.exit()

  def _check_keyup_events (self, event):
    """ 响应松开 """
    if event.key == pygame.K_RIGHT:
      self.ship.move_right = False
    if event.key == pygame.K_LEFT:
      self.ship.move_left = False
    if event.key == pygame.K_UP:
      self.ship.move_up = False
    if event.key == pygame.K_DOWN:
      self.ship.move_down = False

  def _update_screen(self):
    # 填充背景色
    self.screen.fill(self.settings.bg_color)

    # 渲染飞船
    self.ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

  def run_game (self):
    """ 开始游戏主循环 """
    while True:
      # 键盘、鼠标事件
      self._check_events()

      self.ship.update()

      # 更新屏幕
      self._update_screen()
    
if __name__ == '__main__':
  # 创建游戏实例，并运行
  ai = AlientInvasion()
  ai.run_game()