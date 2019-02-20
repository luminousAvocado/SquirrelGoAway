import sys
import pygame
from pygame import *
from PestSound import s_dict
from motion import motionDetect as testObject

class menu_manager():
    def __init__(self):
        self.main_menu = True
        self.audio_menu = False
        self.user_manual_menu = False
        self.sounds = s_dict()

width = 720
height = 600
screen_size = (width, height)

pygame.init()

background_color = (0, 0, 0)

screen = pygame.display.set_mode(screen_size)

# *************************** Variables that determine what page is currently active ****************************
manager = menu_manager()

# ************************************* Load Images **************************************
# main menu buttons
night_mode_button = pygame.image.load("../img/NightModeButton.png")
audio_button = pygame.image.load("../img/AudioSettingsButton.png")
user_manual = pygame.image.load("../img/UserManualButton.png")
start = pygame.image.load("../img/START.png")

# audio settings buttons
checkbox = pygame.image.load("../img/checkboxICON.png")
checkbox = pygame.transform.scale(checkbox, (150, 150))
uncheckedbox = pygame.image.load("../img/uncheckedBoxICON.png")
uncheckedbox = pygame.transform.scale(uncheckedbox, (150, 150))
animal_label = pygame.image.load("../img/Anml_label.png")
chaos_label = pygame.image.load("../img/Chaos_label.png")
freq_label = pygame.image.load("../img/Freq_label.png")

# user manual images/buttons
manual_text = pygame.image.load("../img/UserManual.png")
manual_text = pygame.transform.scale(manual_text, (600, 1000))
up_arrow = pygame.image.load("../img/upArrow.png")
up_arrow = pygame.transform.scale(up_arrow, (30, 30))
down_arrow = pygame.image.load("../img/downArrow.png")
down_arrow = pygame.transform.scale(down_arrow, (30, 30))
back_arrow = pygame.image.load("../img/backArrow.png")
back_arrow = pygame.transform.scale(back_arrow, (75, 50))

# ********************************** create rectangle objects to control images *********************************
# main menu buttons
night_m_b_rect = night_mode_button.get_rect()
audio_b_rect = audio_button.get_rect()
user_m_rect = user_manual.get_rect()
start_button = start.get_rect()

# user manual images/buttons
manual_text_rect = manual_text.get_rect()
up_arrow_rect = up_arrow.get_rect()
down_arrow_rect = down_arrow.get_rect()
back_arrow_rect = back_arrow.get_rect()

# audio checkboxes/labels
animals_checkbox = checkbox.get_rect()
frequencies_checkbox = checkbox.get_rect()
chaos_checkbox = checkbox.get_rect()
# a_label_rect = animal_label.get_rect()
# f_label_rect = freq_label.get_rect()
# c_label_rect = chaos_label.get_rect()

# **************************************** Set Button Locations ***********************************************
# main menu buttons
night_m_b_rect.midtop = (360, 50)
audio_b_rect.midtop = (360, 200)
user_m_rect.midtop = (360, 350)
start_button.midbottom = (360, 550)

# user manual images/buttons
down_arrow_rect.bottomright = (700, 580)
up_arrow_rect.topright = (700, 0)
back_arrow_rect.topleft = (10, 10)

# audio buttons
back_arrow_rect.topleft = (10, 10)
animals_checkbox.topleft = (150, 100)
frequencies_checkbox.topleft = (150, 275)
chaos_checkbox.topleft = (150, 450)


def main_menu_options(x, y):
    if night_m_b_rect.right >= x >= night_m_b_rect.left and night_m_b_rect.top <= y <= night_m_b_rect.bottom:
        manager.sounds.use_animal = False
        manager.sounds.use_chaos = False
        manager.sounds.use_frequencies = True
        testObject.start(manager.sounds)
        print("nightmode")

    if audio_b_rect.right >= x >= audio_b_rect.left and audio_b_rect.top <= y <= audio_b_rect.bottom:
        print("Audio Button")
        manager.audio_menu = True
        manager.main_menu = False

    if user_m_rect.right >= x >= user_m_rect.left and user_m_rect.top <= y <= user_m_rect.bottom:
        print("User Manual")
        manager.user_manual_menu = True
        manager.main_menu = False
        manual_text_rect.midtop = (360, 50)

    if start_button.right >= x >= start_button.left and start_button.top <= y <= start_button.bottom:
        testObject.start(manager.sounds)
        print("START")



def audio_menu_options(x, y):
    if animals_checkbox.right >= x >= animals_checkbox.left and animals_checkbox.top <= y <= animals_checkbox.bottom:
        if manager.sounds.use_animal:
            manager.sounds.use_animal = False
        else:
            manager.sounds.use_animal = True

    if frequencies_checkbox.right >= x >= frequencies_checkbox.left and frequencies_checkbox.top <= y <= frequencies_checkbox.bottom:
        if manager.sounds.use_frequencies:
            manager.sounds.use_frequencies = False
        else:
            manager.sounds.use_frequencies = True

    if chaos_checkbox.right >= x >= chaos_checkbox.left and chaos_checkbox.top <= y <= chaos_checkbox.bottom:
        if manager.sounds.use_chaos:
            manager.sounds.use_chaos = False
        else:
            manager.sounds.use_chaos = True

    if back_arrow_rect.right >= x >= back_arrow_rect.left and back_arrow_rect.top <= y <= back_arrow_rect.bottom:
        print("back arrow")
        manager.audio_menu = False
        manager.main_menu = True


def user_manual_options(x, y):
    # if .right >= x >= .left and .top <= y <= .bottom:
    if up_arrow_rect.right >= x >= up_arrow_rect.left and up_arrow_rect.top <= y <= up_arrow_rect.bottom:
        manual_text_rect.top -= 5
        print("up arrow")

    if down_arrow_rect.right >= x >= down_arrow_rect.left and down_arrow_rect.top <= y <= down_arrow_rect.bottom:
        manual_text_rect.top += 5
        print("down arrow")

    if back_arrow_rect.right >= x >= back_arrow_rect.left and back_arrow_rect.top <= y <= back_arrow_rect.bottom:
        print("back arrow")
        manager.user_manual_menu = False
        manager.main_menu = True


# def night_mode_menu(x, y):

key.set_repeat(1, 1)

# ********************************* START LOOP ************************************
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # *** If on user manuel page, enable arrow keys
        if manager.user_manual_menu:
            if event.type == KEYDOWN:
                if event.key == K_DOWN and manual_text_rect.top < 580:
                    manual_text_rect.top += 5
                if event.key == K_UP and manual_text_rect.bottom > 20:
                    manual_text_rect.top -= 5

        if mouse.get_pressed() == (1, 0, 0):
            x = mouse.get_pos()[0]
            y = mouse.get_pos()[1]

            if manager.main_menu:
                main_menu_options(x, y)

            if manager.audio_menu:
                audio_menu_options(x, y)

            if manager.user_manual_menu:
                user_manual_options(x, y)

    screen.fill(background_color)

    if manager.main_menu:
        screen.blit(night_mode_button, night_m_b_rect)
        screen.blit(audio_button, audio_b_rect)
        screen.blit(user_manual, user_m_rect)
        screen.blit(start, start_button)

    if manager.audio_menu:
        screen.blit(back_arrow, back_arrow_rect)
        screen.blit(animal_label, (350, 100))
        screen.blit(freq_label, (350, 275))
        screen.blit(chaos_label, (350, 450))

        if manager.sounds.use_animal:
            screen.blit(checkbox, animals_checkbox)
        else:
            screen.blit(uncheckedbox, animals_checkbox)

        if manager.sounds.use_chaos:
            screen.blit(checkbox, chaos_checkbox)

        else:
            screen.blit(uncheckedbox, chaos_checkbox)

        if manager.sounds.use_frequencies:
            screen.blit(checkbox, frequencies_checkbox)
        else:
            screen.blit(uncheckedbox, frequencies_checkbox)

    if manager.user_manual_menu:
        screen.blit(manual_text, manual_text_rect)
        screen.blit(up_arrow, up_arrow_rect)
        screen.blit(down_arrow, down_arrow_rect)
        screen.blit(back_arrow, back_arrow_rect)

    pygame.display.flip()

# **************************************** END LOOP ****************************************
