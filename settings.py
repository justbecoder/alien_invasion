class Settings:
  def __init__(self):
    """ 初始化游戏设置 """
    
    # 屏幕设置
    self.screen_width = 800
    self.screen_height = 600
    self.bg_color = (230, 230, 230)
    self.caption_title = '外星人入侵'

    # 飞船飞行速度
    self.ship_speed = 1.5

    # 子弹设置
    self.bullet_speed = 1.0
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (255, 0, 0)