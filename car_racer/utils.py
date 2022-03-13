import pygame

def scale_image(img, factor):
    """function to scale an image"""
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

def blit_rotate_center(window, image, top_left, angle):
    """function to rotate an image"""
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = top_left).center)
    window.blit(rotated_image, new_rect.topleft)
   

def blit_text_center(window, font, text):
    '''function to center text'''
    render = font.render(text, 1, (255, 255, 255))
    window.blit(render, (window.get_width() / 2 - render.get_width() / 2, 
                        window.get_height() / 2.2 - render.get_height() / 2))
                      
