# I LOVE SCLUXWARE !!!1!1   1!
import pydirectinput as pdi
import pywinusb.hid as hid
import pygame
import time
import random

pygame.init()
pygame.joystick.init()

screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.image.save(screen, "testscreenshot.jpg")
screen.fill((92, 16, 199))
pygame.display.set_caption("etchersketcher")

draw_speed_max = 10 # this will change depending on how far the stick is moved
draw_colour = pygame.Color(215, 186, 255) # (123, 199, 16)
draw_position = [600, 400]
draw_dir = ''
draw_change_dir = draw_dir
draw_size = 10
conch_dead_zone = 0.1

fps = pygame.time.Clock()

remove_mode = False

if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print("Controller detected: ", joystick.get_name())

else:
    print("Please plug in a controller")
    pygame.quit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

        elif event.type == pygame.JOYAXISMOTION:
            # Get the axis values (ranging from -1 to 1 for each axis)
            x_axis = joystick.get_axis(0)  # Left/Right
            y_axis = joystick.get_axis(1)  # Up/Down

            if abs(x_axis) < conch_dead_zone:
                x_axis = 0
            if abs(y_axis) < conch_dead_zone:
                y_axis = 0
             
            draw_position[0] += x_axis * draw_speed_max
            draw_position[1] += y_axis * draw_speed_max

            draw_position[0] = max(0, min(screen_width - draw_size, draw_position[0]))
            draw_position[1] = max(0, min(screen_height - draw_size, draw_position[1]))

            print(f"X-Axis: {x_axis:.2f}, Y-Axis: {y_axis:.2f}, draw direction: {draw_change_dir}")
            if draw_change_dir == 'left':
                draw_position[0] -= 1
            if draw_change_dir == 'right':
                draw_position[0] += 1

            pygame.draw.rect(screen, draw_colour, (draw_position[0], draw_position[1], draw_size, draw_size))

        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                pygame.image.save(screen, "testscreenshot.jpg") #x button on my conch
            if event.button == 1:
                remove_mode = True
                print("b down")
                def remove_random():
                    allpixels = screen_width * screen_height
                    randompixels10 = allpixels // 10
                    randompixels = set()
                    while len(randompixels) < randompixels10:
                        x = random.randint(0, screen_width - 1)
                        y = random.randint(0, screen_height - 1)
                        randompixels.add((x, y))
                    return randompixels

                randompixels = remove_random()
                for pixel in randompixels:
                    screen.set_at(pixel, (92, 16, 199))
        elif event.type == pygame.JOYBUTTONUP:
            if event.button == 1:
                remove_mode = False
                print("b up")

    pygame.display.flip()