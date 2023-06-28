import pygame

class Button():
  def __init__(self, image, x, y, text_input, base_color, hovering_color) -> None:
    self.image = image
    self.x = x
    self.y = y
    self.font = pygame.font.SysFont("Arial Narrow", 40)
    self.base_color, self.hovering_color = base_color, hovering_color
    self.text_input = text_input
    self.text = self.font.render(self.text_input, True, self.base_color)
    if self.image is None:
      self.image = self.text
    self.rect = self.image.get_rect(center=(x,y))
    self.text_rect = self.text.get_rect(center=(x,y))

  def update(self, screen):
    if self.image is not None:
      screen.blit(self.image, self.rect)
    screen.blit(self.text, self.text_rect)

  def checkForInput(self, position):
    if self.rect.collidepoint(position):
      return True
    return False

  def changeColor(self, position):
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
      self.text = self.font.render(self.text_input, True, self.hovering_color)
      pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) # Establece el cursor a una mano
    else:
      self.text = self.font.render(self.text_input, True, self.base_color)
      pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Restaura el cursor predeterminado
