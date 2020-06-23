from os import path
import pygame
import random
import pickle
from pygame.math import Vector2
from operator import itemgetter


# Paths to Image Folders
images = path.join(path.dirname(__file__), 'images')
boss = path.join(path.dirname(__file__), 'images/boss')
player = path.join(path.dirname(__file__), 'images/player')
powerups = path.join(path.dirname(__file__), 'images/powerups')

# Paths to Sound Folder
sounds = path.join(path.dirname(__file__), 'sounds')

# Constants
width = 650
height = 650
FPS = 60
POWERUP_TIME = 5000
ULT_TIME = 3000
BOSS1_LASER_TIME = 2000
BOSS1_LASER_WARMING_TIME = 850
BOSS3_LASER_TIME = 500
BOSS5_LASER_TIME = 500
MOB_TIME = 2000

# Define Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(20)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Starship')
clock = pygame.time.Clock()

# Background
background = pygame.image.load(path.join(images, 'SpaceBackground.png')).convert()
scale_background = pygame.transform.scale(background, (650, 650))

# Load Images
level_complete = pygame.image.load(path.join(images, 'level_complete.png')).convert()
level_complete.set_colorkey(black)
paused_img = pygame.image.load(path.join(images, 'paused.png')).convert()
paused_img.set_colorkey(black)
boss1_text = pygame.image.load(path.join(boss, 'boss1_text.png')).convert()
boss1_text.set_colorkey(black)
final_boss_text = pygame.image.load(path.join(boss, 'final_boss_text.png')).convert()
final_boss_text.set_colorkey(black)
boss_defeated_text = pygame.image.load(path.join(boss, 'boss_defeated_text.png')).convert()
boss_defeated_text.set_colorkey(black)
game_complete = pygame.image.load(path.join(images, 'game_complete.png')).convert()
game_complete.set_colorkey(black)
you_win = pygame.image.load(path.join(images, 'you_win.png')).convert()
you_win.set_colorkey(black)
high_scores_text = pygame.image.load(path.join(images, 'high_scores.png')).convert()
high_scores_text.set_colorkey(black)
high_scores_box = pygame.image.load(path.join(images, 'high_scores_box.png')).convert()
high_scores_box.set_colorkey(black)
enter_name_box = pygame.image.load(path.join(images, 'enter_name_box.png')).convert()
enter_name_box.set_colorkey(black)
continue_text = pygame.image.load(path.join(images, 'continue.png')).convert()
continue_text_scale = pygame.transform.scale(continue_text, (360, 30))
continue_text_scale.set_colorkey(black)
boss1_bullet = pygame.image.load(path.join(boss, 'boss1_bullet.png')).convert()
boss1_laser = pygame.image.load(path.join(boss, 'boss1_laser.png')).convert()
boss1_laser.set_colorkey(black)
boss1_laser_warming = pygame.image.load(path.join(boss, 'boss1_laser_warming.png')).convert()
boss1_laser_warming.set_colorkey(black)
boss2_missile = pygame.image.load(path.join(boss, 'boss2_missile.png')).convert()
boss2_missile_scale = pygame.transform.scale(boss2_missile, (45, 45))
boss2_missile_scale.set_colorkey(black)
boss3_exhaust = pygame.image.load(path.join(boss, 'boss3_exhaust.png')).convert()
boss3_exhaust.set_colorkey(black)
boss3_laser = pygame.image.load(path.join(boss, 'boss3_laser.png')).convert()
boss3_laser_warming = pygame.image.load(path.join(boss, 'boss3_laser_warming.png')).convert()
boss5_laser = pygame.image.load(path.join(boss, 'boss5_laser.png')).convert()
boss5_laser_scale = pygame.transform.scale(boss5_laser, (8, 500))
boss5_laser_scale_big = pygame.transform.scale(boss5_laser, (25, 500))
game_over_img = pygame.image.load(path.join(images, 'game_over_img.png')).convert()
scale_game_over_img = pygame.transform.scale(game_over_img, (389, 550))
scale_game_over_img.set_colorkey(black)
player_img = pygame.image.load(path.join(player, 'player.png')).convert()
player_exhaust = pygame.image.load(path.join(player, 'player_exhaust.png')).convert()
boss1_img = pygame.image.load(path.join(boss, 'boss_1.png')).convert()
boss2_img = pygame.image.load(path.join(boss, 'boss_2.png')).convert()
scale_boss2_img = pygame.transform.scale(boss2_img, (517, 293))
boss3_img = pygame.image.load(path.join(boss, 'boss_3.png')).convert()
scale_boss3_img = pygame.transform.scale(boss3_img, (290, 400))
boss4_img = pygame.image.load(path.join(boss, 'boss_4.png')).convert()
scale_boss4_img = pygame.transform.scale(boss4_img, (390, 390))
scale_boss4_img_rotated = pygame.transform.rotate(scale_boss4_img, 10.5)
boss5_img = pygame.image.load(path.join(boss, 'boss_5.png')).convert()
scale_boss5_img = pygame.transform.scale(boss5_img, (575, 800))
scale_boss5_img.set_colorkey(black)
boss5_img_no_right_arm = pygame.image.load(path.join(boss, 'boss5_no_right_arm.png')).convert()
scale_boss5_img_no_right_arm = pygame.transform.scale(boss5_img_no_right_arm, (575, 800))
scale_boss5_img_no_right_arm.set_colorkey(black)
boss5_img_no_arms = pygame.image.load(path.join(boss, 'boss5_no_arms.png')).convert()
scale_boss5_img_no_arms = pygame.transform.scale(boss5_img_no_arms, (575, 800))
scale_boss5_img_no_arms.set_colorkey(black)
boss5_img_no_left_arm1 = pygame.image.load(path.join(boss, 'boss5_no_left_arm1.png')).convert()
scale_boss5_img_no_left_arm1 = pygame.transform.scale(boss5_img_no_left_arm1, (575, 800))
scale_boss5_img_no_left_arm1.set_colorkey(black)
boss5_img_no_arms1 = pygame.image.load(path.join(boss, 'boss5_no_arms1.png')).convert()
scale_boss5_img_no_arms1 = pygame.transform.scale(boss5_img_no_arms1, (575, 800))
scale_boss5_img_no_arms1.set_colorkey(black)
boss5_img_cabin_hitbox = pygame.image.load(path.join(boss, 'boss_5_cabin_hitbox.png')).convert()
scale_boss5_img_cabin_hitbox = pygame.transform.scale(boss5_img_cabin_hitbox, (575, 800))
scale_boss5_img_cabin_hitbox.set_colorkey(black)
boss5_img_left_hitbox = pygame.image.load(path.join(boss, 'boss_5_left_hitbox.png')).convert()
scale_boss5_img_left_hitbox = pygame.transform.scale(boss5_img_left_hitbox, (575, 800))
scale_boss5_img_left_hitbox.set_colorkey(black)
boss5_img_right_hitbox = pygame.image.load(path.join(boss, 'boss_5_right_hitbox.png')).convert()
scale_boss5_img_right_hitbox = pygame.transform.scale(boss5_img_right_hitbox, (575, 800))
scale_boss5_img_right_hitbox.set_colorkey(black)
player_img_mini = pygame.transform.scale(player_img, (25, 19))
player_img_mini.set_colorkey(black)
laser1 = pygame.image.load(path.join(player, 'laser1.png')).convert()
laser1left = pygame.image.load(path.join(player, 'laser1left.png')).convert()
laser1right = pygame.image.load(path.join(player, 'laser1right.png')).convert()
laserult = pygame.image.load(path.join(player, 'laserult.png')).convert()
laserult_scale = pygame.transform.scale(laserult, (10, 500))
boss5_laser_scale_ult = pygame.transform.scale(laserult, (50, 1000))
meteor_images = []
meteor_list = ['meteorBrown_big1.png', 'meteorBrown_big3.png', 'meteorBrown_big4.png', 'meteorBrown_med1.png',
               'meteorBrown_med2.png', 'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
               'meteorBrown_tiny1.png']
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(images, path.join(img))).convert())
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
explosion_anim['boss'] = []
explosion_anim['supersize'] = []
for i in range(9):
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(images, path.join(filename))).convert()
    img.set_colorkey(black)
    explosion_anim['player'].append(img)
for i in range(9):
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(images, path.join(filename))).convert()
    img.set_colorkey(black)
    img_ss = pygame.transform.scale(img, (85, 85))
    explosion_anim['supersize'].append(img_ss)
    img_lg = pygame.transform.scale(img, (65, 65))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (45, 45))
    explosion_anim['sm'].append(img_sm)
    img_boss = pygame.transform.scale(img, (270, 270))
    explosion_anim['boss'].append(img_boss)
powerup_images = {}
powerup_images['shield'] = pygame.image.load(path.join(powerups, 'shield_gold.png')).convert()
powerup_images['gun'] = pygame.image.load(path.join(powerups, 'pill_yellow.png')).convert()
powerup_images['damage'] = pygame.image.load(path.join(powerups, 'pill_red.png')).convert()
powerup_images['ult'] = pygame.image.load(path.join(powerups, 'pill_blue.png')).convert()
heart = pygame.image.load(path.join(powerups, 'heart.png')).convert()
heart.set_colorkey(black)
scale_heart = pygame.transform.scale(heart, (27, 27))

# Load Sounds
background_sound = pygame.mixer.music.load(path.join(sounds, 'background_music.mp3'))
pygame.mixer.music.set_volume(0.15)
level_up_sound = pygame.mixer.Sound(path.join(sounds, 'level_up_sound.wav'))
shoot_sound = pygame.mixer.Sound(path.join(sounds, 'Laser.wav'))
boss_fight_sound = pygame.mixer.Sound(path.join(sounds, 'boss_fight_sound.wav'))
final_boss_fight_sound = pygame.mixer.Sound(path.join(sounds, 'final_boss_fight_sound.wav'))
you_win_sound = pygame.mixer.Sound(path.join(sounds, 'you_win_sound.wav'))
boss1_bullet_sound = pygame.mixer.Sound(path.join(sounds, 'boss1_bullet_sound.wav'))
boss1_bullet_sound.set_volume(0.5)
pygame.mixer.Sound.set_volume(shoot_sound, 0.6)
boss1_warming_sound = pygame.mixer.Sound(path.join(sounds, 'warming_sound.wav'))
boss1_laser_sound = pygame.mixer.Sound(path.join(sounds, 'boss1_laser.wav'))
boss2_missile_sound = pygame.mixer.Sound(path.join(sounds, 'missile.wav'))
boss2_missile_sound.set_volume(0.25)
boss3_thrust = pygame.mixer.Sound(path.join(sounds, 'thrust.wav'))
boss3_laser_sound = pygame.mixer.Sound(path.join(sounds, 'boss3_laser_sound.wav'))
boss4_laser_sound = pygame.mixer.Sound(path.join(sounds, 'boss4_laser_sound.wav'))
boss5_laser_sound = pygame.mixer.Sound(path.join(sounds, 'boss5_laser_sound.wav'))
boss5_ult_sound = pygame.mixer.Sound(path.join(sounds, 'boss5_ult_sound.wav'))
boss_defeated_sound = pygame.mixer.Sound(path.join(sounds, 'boss_defeated.wav'))
boss_defeated_sound.set_volume(0.3)
heart_sound = pygame.mixer.Sound(path.join(sounds, 'jolly_laugh.wav'))
shield_sound = pygame.mixer.Sound(path.join(sounds, 'powerup_shield.wav'))
shield_sound.set_volume(0.75)
damage_sound = pygame.mixer.Sound(path.join(sounds, 'damage_sound.wav'))
ult_powerup_sound = pygame.mixer.Sound(path.join(sounds, 'ult_powerup_sound.wav'))
gun_sound = pygame.mixer.Sound(path.join(sounds, 'powerup_gun.wav'))
explosion_sound = pygame.mixer.Sound(path.join(sounds, 'Explosion.wav'))
pygame.mixer.Sound.set_volume(explosion_sound, 0.7)
player_die_sound = pygame.mixer.Sound(path.join(sounds, 'rumble1.ogg'))
ult_sound = pygame.mixer.Sound(path.join(sounds, 'ult_sound.wav'))

# Add text to the screen
font_name = pygame.font.match_font('arial')  # to make sure python can find the font
user_font = pygame.font.Font(None, 48)


def draw_text(surf, text, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surf.blit(text_surface, text_rect)


def draw_text_centered(surf, text, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surf.blit(text_surface, text_rect)


def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    bar_length = 100
    bar_height = 10
    fill = (pct / 100) * bar_length
    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surf, red, fill_rect)
    pygame.draw.rect(surf, white, outline_rect, 2)


def draw_ult_bar(surf, x, y, pct):
    if pct > 100:
        pct = 100
    bar_length = 100
    bar_height = 10
    fill = (pct / 100) * bar_length
    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surf, (0, 125, 255), fill_rect)
    pygame.draw.rect(surf, white, outline_rect, 2)


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x - 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)


def draw_lvl(surf, x, y, img):
    img_rect = img.get_rect()
    img_rect.center = (x, y)
    surf.blit(img, img_rect)


def pause():
    paused = True
    while paused:
        # Pause music
        pygame.mixer.music.pause()
        draw_lvl(screen, (width / 2), 250, paused_img)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    # Resume music
                    pygame.mixer.music.unpause()
                    # Reset all boss laser timings
                    # Boss 1
                    boss1.last_laser = pygame.time.get_ticks() + 850
                    boss1.last_warming = pygame.time.get_ticks()
                    # Boss2
                    boss2.last_missile = pygame.time.get_ticks()
                    boss2.last_center_missile = pygame.time.get_ticks() + 250
                    # Boss 3
                    boss3.last_laser = pygame.time.get_ticks() + 850
                    boss3.last_warming = pygame.time.get_ticks()
                    # Boss 4
                    # No need to Reset timer for boss 4 because of how lasers are set up
                    # Boss 5
                    boss5.last_laser = pygame.time.get_ticks() + 850
                    boss5.last_laser1 = pygame.time.get_ticks() + 1250
                    boss5.last_laser2 = pygame.time.get_ticks() + 1650
                    boss5.last_laser3 = pygame.time.get_ticks() + 2000
                    boss5.last_laser4 = pygame.time.get_ticks() + 2500
                    boss5.last_laser5 = pygame.time.get_ticks() + 3500
                    boss5.last_laser6 = pygame.time.get_ticks() + 4000
                    boss5.last_laser7 = pygame.time.get_ticks() + 4500
                    boss5.last_laser8 = pygame.time.get_ticks() + 5000
                    boss5.last_laser9 = pygame.time.get_ticks() + 5800
                    boss5.last_warming = pygame.time.get_ticks()
                    boss5.last_warming1 = pygame.time.get_ticks() + 400
                    boss5.last_warming2 = pygame.time.get_ticks() + 800
                    boss5.last_warming3 = pygame.time.get_ticks() + 1150
                    boss5.last_warming4 = pygame.time.get_ticks() + 1650
                    boss5.last_warming5 = pygame.time.get_ticks() + 2650
                    boss5.last_warming6 = pygame.time.get_ticks() + 3150
                    boss5.last_warming7 = pygame.time.get_ticks() + 3650
                    boss5.last_warming8 = pygame.time.get_ticks() + 4150
                    boss5.last_warming9 = pygame.time.get_ticks() + 4950
                    paused = False
        pygame.display.flip()
        clock.tick(FPS)


def level_up(start_time, stop_time, stage_num):
    global lvl_up
    if start_time <= stage_num <= stop_time:
        draw_lvl(screen, (width / 2), (height / 4), level_complete)
        lvl_up = True
    if lvl_up:
        for mob in mobs:
            expl = Explosion(mob.rect.center, 'lg')
            all_sprites.add(expl)
    if stage_num >= stop_time:
        lvl_up = False


def show_go_screen():
    waiting = True
    z = 0
    while waiting:
        # Scrolling Background
        rel_z = z % scale_background.get_rect().height
        screen.blit(scale_background, (0, rel_z - scale_background.get_rect().height))
        if rel_z < height:
            screen.blit(scale_background, (0, rel_z))
        z += 2
        img_rect = scale_game_over_img.get_rect(center=(width / 2, height / 2))
        screen.blit(scale_game_over_img, img_rect)
        pygame.display.flip()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                waiting = False


def show_user_name_screen():
    waiting = True
    global user_name
    z = 0
    user_name = ''
    while waiting:
        pygame.display.flip()
        clock.tick(FPS)
        # Scrolling Background
        rel_z = z % scale_background.get_rect().height
        screen.blit(scale_background, (0, rel_z - scale_background.get_rect().height))
        if rel_z < height:
            screen.blit(scale_background, (0, rel_z))
        z += 2
        draw_lvl(screen, (width / 2), (height / 2), enter_name_box)
        if len(user_name) < 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_name = user_name[:-1]
                    else:
                        user_name += event.unicode.upper()
        draw_text_centered(screen, user_name, 135, (width / 2), (height / 2 - 65), black)
        if len(user_name) == 3:
            draw_lvl(screen, (width / 2), (height - 150), continue_text_scale)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_name = user_name[:-1]
                    else:
                        waiting = False


def show_high_scores():
    waiting = True
    global high_scores_test
    global high_scores
    global game_over
    z = 0
    while waiting:
        pygame.display.flip()
        clock.tick(FPS)
        # Scrolling Background
        rel_z = z % scale_background.get_rect().height
        screen.blit(scale_background, (0, rel_z - scale_background.get_rect().height))
        if rel_z < height:
            screen.blit(scale_background, (0, rel_z))
        z += 2
        if high_scores_test == 0:
            high_scores = []

            with open('highscores.txt', 'rb') as f:
                high_scores = pickle.load(f)

            high_scores.append((user_name, score))
            high_scores = sorted(high_scores, key=itemgetter(1), reverse=True)[:10]

            with open('highscores.txt', 'wb') as f:
                pickle.dump(high_scores, f)

            high_scores = []

            with open('highscores.txt', 'rb') as f:
                high_scores = pickle.load(f)

            name_only_list = [x[0] for x in high_scores]

            score_only_list = [x[1] for x in high_scores]

            high_scores_test = 1

        draw_lvl(screen, (width / 2), (height / 2), high_scores_box)

        for i in range(0, 10):
            draw_text(screen, str(name_only_list[i]), 36, 150, (height / 4) - 25 + 45 * i, black)
            draw_text(screen, '-', 36, 240, (height / 4) - 25 + 45 * i, black)
            draw_text(screen, str(score_only_list[i]), 36, 265, (height / 4) - 25 + 45 * i, black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                game_over = True
                waiting = False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius = 25
        self.rect.center = (width / 2, 700)
        self.speedx = 0
        self.speedy = 0
        self.shield = 100
        self.ult = 0
        self.shoot_delay = 240
        self.last_shot = pygame.time.get_ticks()
        self.lives = 5
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()
        self.invincible = 0
        self.fly_in = True
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # timeout for powerups
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1500:
            self.hidden = False
            self.rect.center = (width / 2, 575)
            self.invincible = 60

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if not self.fly_in:
            self.speedx = 0
            self.speedy = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speedx = -8
            if keystate[pygame.K_RIGHT]:
                self.speedx = 8
            if keystate[pygame.K_UP]:
                self.speedy = -8
            if keystate[pygame.K_DOWN]:
                self.speedy = 8
            if keystate[pygame.K_SPACE] and not self.hidden and not lvl_up:
                self.shoot()
            if keystate[pygame.K_f] and self.ult >= 100:
                self.fireult()
                self.ult = 0

            if self.rect.right > width:
                self.rect.right = width
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > height and not self.hidden:
                self.rect.bottom = height

        if self.speedy < 0:
            self.player_exhaust()

    def player_exhaust(self):
        exh = PlayerExhaust(self.rect.left + 10, self.rect.top - 4)
        exh1 = PlayerExhaust(self.rect.right - 10, self.rect.top - 4)
        all_sprites.add(exh)
        all_sprites.add(exh1)

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def fireult(self):
        ult = Ultimate(self.rect.centerx, self.rect.top)
        all_sprites.add(ult)
        ults.add(ult)
        ult_sound.play()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            if self.power == 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()
            if self.power == 3:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()
            if self.power >= 4:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                bullet3 = AngledBulletRight(self.rect.right, self.rect.centery)
                bullet4 = AngledBulletLeft(self.rect.left, self.rect.centery)
                all_sprites.add(bullet)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                all_sprites.add(bullet3)
                all_sprites.add(bullet4)
                bullets.add(bullet)
                bullets.add(bullet1)
                bullets.add(bullet2)
                bullets.add(bullet3)
                bullets.add(bullet4)
                shoot_sound.play()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (1000, 3000)


class PlayerExhaust(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_exhaust
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        self.speedy = player.speedy
        self.speedx = player.speedx

    def update(self):
        self.rect.x += player.speedx
        self.rect.y += player.speedy
        self.kill()
        if player.hidden:
            self.kill()


class Ultimate(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.ult_time = pygame.time.get_ticks()
        self.image = laserult
        self.image = pygame.transform.scale(laserult, (64, 1000))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = player.speedy
        self.speedx = player.speedx

    def update(self):
        self.rect.x += player.speedx
        self.rect.y += player.speedy
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.bottom > height - 64:
            self.rect.bottom = height - 64
        if self.rect.bottom < 0:
            self.rect.bottom = 0
        if pygame.time.get_ticks() - self.ult_time > ULT_TIME:
            self.kill()
        if player.hidden:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser1
        self.image = pygame.transform.scale(laser1, (7, 35))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += self.speedy
        # Kill it if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
        # Kill it during Level Up Announcements
        if lvl_up:
            self.kill()


class AngledBulletRight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser1right
        self.image = pygame.transform.scale(laser1right, (7, 35))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.speedx = 5

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # Kill it if it moves off the top or side of the screen
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.left > width:
            self.kill()
        # Kill it during Level Up Announcements
        if lvl_up:
            self.kill()


class AngledBulletLeft(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser1left
        self.image = pygame.transform.scale(laser1left, (7, 35))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.speedx = -5

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # Kill it if it moves off the top or side of the screen
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.right < 0:
            self.kill()
        # Kill it during Level Up Announcements
        if lvl_up:
            self.kill()


class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun', 'damage', 'ult'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 9
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += self.speedy
        # Kill it if it moves off the bottom of the screen
        if self.rect.top > height:
            self.kill()


class ExtraLifePow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'heart'
        self.image = scale_heart
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 11
        self.speedx = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += self.speedy
        # Kill it if it moves off the bottom of the screen
        if self.rect.top > height:
            self.kill()


class FinalHeart(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'bigheart'
        self.image = heart
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 1
        self.speedx = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += self.speedy
        # Stop it before it goes off the screen
        if self.rect.bottom >= 600:
            self.rect.bottom = 600


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(black)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .9 / 2)
        self.rect.x = random.randrange(0, width - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(3, 10)
        self.speedx = random.randrange(-4, 4)
        self.rot = 0
        self.rot_speed = random.randrange(-10, 10)
        self.last_update = pygame.time.get_ticks()
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 25:
            self.rect.x = random.randrange(0, width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 10)
            self.speedx = random.randrange(-4, 4)
        if lvl_up:
            self.rect.x = 1200
            self.rect.y = 1200
            self.speedy = 0
            self.speedx = 0
        if boss_fight:
            self.rect.x = 1200
            self.rect.y = 1200
            self.speedy = 0
            self.speedx = 0


class Boss1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss1_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, -300)
        self.speedx = 0
        self.speedy = 0
        self.shield = 1000
        self.shoot_delay = 500
        self.laser_delay = 8000
        self.warming_delay = 8000
        self.wait = 0
        self.last_shot = pygame.time.get_ticks()
        self.last_laser = pygame.time.get_ticks()
        self.last_warming = pygame.time.get_ticks()
        self.alive = True
        self.boss_defeated_sound = pygame.mixer.Sound(path.join(sounds, 'boss_defeated.wav'))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.speedy = 1.5
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right >= width + 75:
            self.rect.right = width + 75
            self.speedx = 0
        if self.rect.left <= -75:
            self.rect.left = -75
            self.speedx = 0
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            self.boss_shoot()
            self.boss_laser_warming()
            self.boss_laser()
            self.boss_dying()
        if self.rect.bottom == 300 and self.speedx != -1 and self.rect.right != width + 75:
            self.speedx = 1
        if self.rect.bottom == 300 and self.speedx != 1 and self.rect.left != -75:
            self.speedx = -1
        if self.shield <= 0:
            self.kill()
            self.rect.center = (width / 2, 1500)
            self.boss_defeated_sound.play(0)
            self.boss_defeated_sound.play(0)
            self.boss_defeated_sound.play(0)
            self.alive = False

    def boss_shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.shield >= 800:
                boss1_bullet = Boss1Bullet(self.rect.centerx, self.rect.bottom - 42)
                all_sprites.add(boss1_bullet)
                boss1_bullets.add(boss1_bullet)
                boss1_bullet_sound.play()
            if 800 > self.shield >= 500:
                boss1_bullet = Boss1Bullet(self.rect.centerx, self.rect.bottom - 42)
                boss1_bullet1 = VariableBoss1Bullet(self.rect.left + 55, self.rect.bottom)
                boss1_bullet2 = VariableBoss1Bullet(self.rect.right - 55, self.rect.bottom)
                all_sprites.add(boss1_bullet)
                boss1_bullets.add(boss1_bullet)
                boss1_bullet_sound.play()
                if random.random() > 0.8:
                    all_sprites.add(boss1_bullet1)
                    boss1_bullets.add(boss1_bullet1)
                    boss1_bullet_sound.play()
                if random.random() > 0.8:
                    all_sprites.add(boss1_bullet2)
                    boss1_bullets.add(boss1_bullet2)
                    boss1_bullet_sound.play()
            if 500 > self.shield >= 200:
                boss1_bullet = Boss1Bullet(self.rect.centerx, self.rect.bottom - 42)
                boss1_bullet1 = VariableBoss1Bullet(self.rect.left + 55, self.rect.bottom)
                boss1_bullet2 = VariableBoss1Bullet(self.rect.right - 55, self.rect.bottom)
                all_sprites.add(boss1_bullet)
                boss1_bullets.add(boss1_bullet)
                boss1_bullet_sound.play()
                if random.random() > 0.5:
                    all_sprites.add(boss1_bullet1)
                    boss1_bullets.add(boss1_bullet1)
                    boss1_bullet_sound.play()
                if random.random() > 0.5:
                    all_sprites.add(boss1_bullet2)
                    boss1_bullets.add(boss1_bullet2)
                    boss1_bullet_sound.play()
            if 200 > self.shield >= 0:
                boss1_bullet = Boss1Bullet(self.rect.centerx, self.rect.bottom - 42)
                boss1_bullet1 = Boss1Bullet(self.rect.left + 55, self.rect.bottom)
                boss1_bullet2 = Boss1Bullet(self.rect.right - 55, self.rect.bottom)
                all_sprites.add(boss1_bullet)
                boss1_bullets.add(boss1_bullet)
                all_sprites.add(boss1_bullet1)
                boss1_bullets.add(boss1_bullet1)
                all_sprites.add(boss1_bullet2)
                boss1_bullets.add(boss1_bullet2)
                boss1_bullet_sound.play()

    def boss_laser(self):
        self.wait += clock.get_rawtime()
        if self.wait >= 850:
            now = pygame.time.get_ticks()
            if now - self.last_laser > self.laser_delay:
                self.last_laser = now
                boss1_laser = Boss1Laser(self.rect.centerx - 53, self.rect.bottom - 83)
                boss1_laser1 = Boss1Laser(self.rect.centerx + 53, self.rect.bottom - 83)
                all_sprites.add(boss1_laser)
                boss1_lasers.add(boss1_laser)
                all_sprites.add(boss1_laser1)
                boss1_lasers.add(boss1_laser1)
                boss1_laser_sound.play()
        if boss1.shield <= 0:
            self.kill()

    def boss_laser_warming(self):
        now = pygame.time.get_ticks()
        if now - self.last_warming > self.warming_delay:
            self.last_warming = now
            boss1_laser_warming = Boss1Warming(self.rect.centerx - 53, self.rect.bottom - 83)
            boss1_laser_warming1 = Boss1Warming(self.rect.centerx + 53, self.rect.bottom - 83)
            all_sprites.add(boss1_laser_warming)
            boss1_bullets.add(boss1_laser_warming)
            all_sprites.add(boss1_laser_warming1)
            boss1_bullets.add(boss1_laser_warming1)
            boss1_warming_sound.play()
        if boss1.shield <= 0:
            self.kill()

    def boss_dying(self):
        if self.shield == 250:
            explo = Explosion((self.rect.centerx, self.rect.bottom - 55), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 245
        if self.shield == 225:
            explo = Explosion((self.rect.centerx + 135, self.rect.bottom - 200), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 220
        if self.shield == 200:
            explo = Explosion((self.rect.centerx - 150, self.rect.bottom - 150), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 195
        if self.shield == 175:
            explo = Explosion((self.rect.centerx + 160, self.rect.bottom - 100), 'supersize')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 170
        if self.shield == 150:
            explo = Explosion((self.rect.centerx + 125, self.rect.bottom - 40), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 145
        if self.shield == 115:
            explo = Explosion((self.rect.centerx - 150, self.rect.bottom - 170), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 110
        if self.shield == 100:
            explo = Explosion((self.rect.centerx - 130, self.rect.bottom - 115), 'supersize')
            explo1 = Explosion((self.rect.centerx + 180, self.rect.bottom - 75), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 95
        if self.shield == 85:
            explo = Explosion((self.rect.centerx - 170, self.rect.bottom - 80), 'lg')
            explo1 = Explosion((self.rect.centerx + 160, self.rect.bottom - 180), 'supersize')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 80
        if self.shield == 75:
            explo = Explosion((self.rect.centerx + 180, self.rect.bottom - 90), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 70
        if self.shield == 65:
            explo = Explosion((self.rect.centerx + 170, self.rect.bottom - 170), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 60
        if self.shield == 55:
            explo = Explosion((self.rect.centerx + 110, self.rect.bottom - 50), 'supersize')
            explo1 = Explosion((self.rect.centerx - 125, self.rect.bottom - 95), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 50
        if self.shield == 45:
            explo = Explosion((self.rect.centerx - 150, self.rect.bottom - 150), 'lg')
            explo1 = Explosion((self.rect.centerx + 170, self.rect.bottom - 105), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 40
        if self.shield == 35:
            explo = Explosion((self.rect.centerx + 130, self.rect.bottom - 30), 'supersize')
            explo1 = Explosion((self.rect.centerx - 20, self.rect.bottom - 25), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 30
        if self.shield == 25:
            explo = Explosion((self.rect.centerx - 140, self.rect.bottom - 190), 'lg')
            explo1 = Explosion((self.rect.centerx - 180, self.rect.bottom - 50), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 20
        if self.shield == 15:
            explo = Explosion((self.rect.centerx - 180, self.rect.bottom - 190), 'lg')
            explo1 = Explosion((self.rect.centerx + 190, self.rect.bottom - 175), 'supersize')
            explo2 = Explosion((self.rect.centerx + 30, self.rect.bottom - 220), 'lg')
            explo3 = Explosion((self.rect.centerx + 10, self.rect.bottom - 100), 'lg')
            explo4 = Explosion((self.rect.centerx - 150, self.rect.bottom - 110), 'supersize')
            explo5 = Explosion((self.rect.centerx - 140, self.rect.bottom - 140), 'lg')
            explo6 = Explosion((self.rect.centerx, self.rect.bottom - 110), 'boss')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            all_sprites.add(explo2)
            all_sprites.add(explo3)
            all_sprites.add(explo4)
            all_sprites.add(explo5)
            all_sprites.add(explo6)
            explosion_sound.play()
            self.shield = 10
        if self.shield == 5:
            explo = Explosion((self.rect.centerx - 180, self.rect.bottom - 190), 'supersize')
            explo1 = Explosion((self.rect.centerx + 190, self.rect.bottom - 175), 'supersize')
            explo2 = Explosion((self.rect.centerx + 125, self.rect.bottom - 220), 'boss')
            explo3 = Explosion((self.rect.centerx + 150, self.rect.bottom - 100), 'boss')
            explo4 = Explosion((self.rect.centerx - 150, self.rect.bottom - 200), 'boss')
            explo5 = Explosion((self.rect.centerx - 125, self.rect.bottom - 100), 'boss')
            explo6 = Explosion((self.rect.centerx, self.rect.bottom - 110), 'boss')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            all_sprites.add(explo2)
            all_sprites.add(explo3)
            all_sprites.add(explo4)
            all_sprites.add(explo5)
            all_sprites.add(explo6)
            explosion_sound.play()
            lifepow = ExtraLifePow(boss1.rect.center)
            all_sprites.add(lifepow)
            powerups.add(lifepow)
            self.shield = 0


class Boss1Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.boss_laser_time = pygame.time.get_ticks()
        self.image = boss1_laser
        self.image = pygame.transform.scale(laserult, (13, 500))
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x

    def update(self):
        self.rect.x += boss1.speedx
        if pygame.time.get_ticks() - self.boss_laser_time > BOSS1_LASER_TIME:
            self.kill()
        if boss1.shield <= 0:
            self.kill()


class Boss1Warming(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.boss_laser_time = pygame.time.get_ticks()
        self.image = boss1_laser_warming
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x

    def update(self):
        self.rect.x += boss1.speedx
        if pygame.time.get_ticks() - self.boss_laser_time > BOSS1_LASER_WARMING_TIME:
            self.kill()
        if boss1.shield <= 0:
            self.kill()


class Boss1Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss1_bullet
        self.image = pygame.transform.scale(boss1_bullet, (13, 13))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        self.speedx = random.randrange(-5, 5)
        self.speedy = 10

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Kill it if it moves off the bottom of the screen
        if self.rect.top > height:
            self.kill()


class VariableBoss1Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss1_bullet
        self.image = pygame.transform.scale(boss1_bullet, (13, 13))
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        self.speedx = random.randrange(-7, 7)
        self.speedy = random.randrange(7, 13)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Kill it if it moves off the bottom of the screen
        if self.rect.top > height:
            self.kill()


class Boss2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scale_boss2_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, -300)
        self.speedx = 0
        self.speedy = 0
        self.shield = 1000
        self.shoot_delay = 700
        self.missile_delay = 4500
        self.center_missile_delay = 9500
        self.last_shot = pygame.time.get_ticks()
        self.last_missile = pygame.time.get_ticks()
        self.last_center_missile = pygame.time.get_ticks()
        self.alive = True
        self.boss_defeated_sound = pygame.mixer.Sound(path.join(sounds, 'boss_defeated.wav'))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.speedy = 1.5
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right >= width + 50:
            self.rect.right = width + 50
            self.speedx = 0
        if self.rect.left <= -50:
            self.rect.left = -50
            self.speedx = 0
        if self.rect.bottom >= 275:
            self.rect.bottom = 275
            self.boss_shoot()
            self.boss_missile()
            self.boss_dying()
            self.boss_missile_center()
        if self.rect.bottom == 275 and self.speedx != -1.5 and self.rect.right != width + 50:
            self.speedx = 1.5
        if self.rect.bottom == 275 and self.speedx != 1.5 and self.rect.left != -50:
            self.speedx = -1.5
        if self.shield <= 0:
            self.kill()
            self.rect.center = (width / 2, 1500)
            self.boss_defeated_sound.play(0)
            self.boss_defeated_sound.play(0)
            self.boss_defeated_sound.play(0)
            self.alive = False

    def boss_shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.shield >= 800:
                boss1_bullet = Boss1Bullet(self.rect.centerx - 12, self.rect.bottom - 42)
                boss1_bullet1 = Boss1Bullet(self.rect.centerx + 12, self.rect.bottom - 42)
                all_sprites.add(boss1_bullet)
                all_sprites.add(boss1_bullet1)
                boss1_bullets.add(boss1_bullet)
                boss1_bullets.add(boss1_bullet1)
                boss1_bullet_sound.play()
            if 800 > self.shield >= 500:
                boss1_bullet = Boss1Bullet(self.rect.centerx - 12, self.rect.bottom - 42)
                boss1_bullet1 = Boss1Bullet(self.rect.centerx + 12, self.rect.bottom - 42)
                boss1_bullet2 = VariableBoss1Bullet(self.rect.centerx + 89, self.rect.bottom - 77)
                boss1_bullet3 = VariableBoss1Bullet(self.rect.centerx - 89, self.rect.bottom - 77)
                all_sprites.add(boss1_bullet)
                all_sprites.add(boss1_bullet1)
                boss1_bullets.add(boss1_bullet)
                boss1_bullets.add(boss1_bullet1)
                boss1_bullet_sound.play()
                if random.random() > 0.8:
                    all_sprites.add(boss1_bullet2)
                    boss1_bullets.add(boss1_bullet2)
                    boss1_bullet_sound.play()
                if random.random() > 0.8:
                    all_sprites.add(boss1_bullet3)
                    boss1_bullets.add(boss1_bullet3)
                    boss1_bullet_sound.play()
            if 500 > self.shield >= 200:
                boss1_bullet = Boss1Bullet(self.rect.centerx - 12, self.rect.bottom - 42)
                boss1_bullet1 = Boss1Bullet(self.rect.centerx + 12, self.rect.bottom - 42)
                boss1_bullet2 = VariableBoss1Bullet(self.rect.centerx + 89, self.rect.bottom - 77)
                boss1_bullet3 = VariableBoss1Bullet(self.rect.centerx - 89, self.rect.bottom - 77)
                all_sprites.add(boss1_bullet)
                all_sprites.add(boss1_bullet1)
                boss1_bullets.add(boss1_bullet)
                boss1_bullets.add(boss1_bullet1)
                boss1_bullet_sound.play()
                if random.random() > 0.5:
                    all_sprites.add(boss1_bullet2)
                    boss1_bullets.add(boss1_bullet2)
                    boss1_bullet_sound.play()
                if random.random() > 0.5:
                    all_sprites.add(boss1_bullet3)
                    boss1_bullets.add(boss1_bullet3)
                    boss1_bullet_sound.play()
            if 200 > self.shield >= 0:
                boss1_bullet = Boss1Bullet(self.rect.centerx - 12, self.rect.bottom - 42)
                boss1_bullet1 = Boss1Bullet(self.rect.centerx + 12, self.rect.bottom - 42)
                boss1_bullet2 = VariableBoss1Bullet(self.rect.centerx + 89, self.rect.bottom - 77)
                boss1_bullet3 = VariableBoss1Bullet(self.rect.centerx - 89, self.rect.bottom - 77)
                all_sprites.add(boss1_bullet)
                boss1_bullets.add(boss1_bullet)
                all_sprites.add(boss1_bullet1)
                boss1_bullets.add(boss1_bullet1)
                all_sprites.add(boss1_bullet2)
                boss1_bullets.add(boss1_bullet2)
                all_sprites.add(boss1_bullet3)
                boss1_bullets.add(boss1_bullet3)
                boss1_bullet_sound.play()

    def boss_missile(self):
        now = pygame.time.get_ticks()
        if now - self.last_missile > self.missile_delay:
            self.last_missile = now
            if self.shield >= 600:
                boss1_missile = Boss2Missile(self.rect.centerx - 130, self.rect.bottom - 95)
                boss1_missile1 = Boss2Missile(self.rect.centerx - 156, self.rect.bottom - 90)
                boss1_missile2 = Boss2Missile(self.rect.centerx + 130, self.rect.bottom - 95)
                boss1_missile3 = Boss2Missile(self.rect.centerx + 156, self.rect.bottom - 90)
                all_sprites.add(boss1_missile)
                boss2_missiles.add(boss1_missile)
                all_sprites.add(boss1_missile1)
                boss2_missiles.add(boss1_missile1)
                all_sprites.add(boss1_missile2)
                boss2_missiles.add(boss1_missile2)
                all_sprites.add(boss1_missile3)
                boss2_missiles.add(boss1_missile3)
                boss2_missile_sound.play()
            if 600 > self.shield > 0:
                boss1_missile = Boss2Missile(self.rect.centerx - 130, self.rect.bottom - 95)
                boss1_missile1 = Boss2Missile(self.rect.centerx - 156, self.rect.bottom - 90)
                boss1_missile2 = Boss2Missile(self.rect.centerx + 130, self.rect.bottom - 95)
                boss1_missile3 = Boss2Missile(self.rect.centerx + 156, self.rect.bottom - 90)
                boss1_missile4 = Boss2Missile(self.rect.centerx - 89, self.rect.bottom - 77)
                boss1_missile5 = Boss2Missile(self.rect.centerx + 89, self.rect.bottom - 77)
                all_sprites.add(boss1_missile)
                boss2_missiles.add(boss1_missile)
                all_sprites.add(boss1_missile1)
                boss2_missiles.add(boss1_missile1)
                all_sprites.add(boss1_missile2)
                boss2_missiles.add(boss1_missile2)
                all_sprites.add(boss1_missile3)
                boss2_missiles.add(boss1_missile3)
                all_sprites.add(boss1_missile4)
                boss2_missiles.add(boss1_missile4)
                all_sprites.add(boss1_missile5)
                boss2_missiles.add(boss1_missile5)
                boss2_missile_sound.play()

    def boss_missile_center(self):
        now = pygame.time.get_ticks()
        if now - self.last_center_missile > self.center_missile_delay:
            self.last_center_missile = now
            if 650 > self.shield > 0:
                boss1_missile = Boss2Missile(self.rect.centerx - 14, self.rect.bottom - 42)
                boss1_missile1 = Boss2Missile(self.rect.centerx + 14, self.rect.bottom - 42)
                all_sprites.add(boss1_missile)
                boss2_missiles.add(boss1_missile)
                all_sprites.add(boss1_missile1)
                boss2_missiles.add(boss1_missile1)
                boss2_missile_sound.play()

    def boss_dying(self):
        if self.shield == 250:
            explo = Explosion((self.rect.centerx, self.rect.bottom - 55), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 245
        if self.shield == 225:
            explo = Explosion((self.rect.centerx + 135, self.rect.bottom - 200), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 220
        if self.shield == 200:
            explo = Explosion((self.rect.centerx - 150, self.rect.bottom - 150), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 195
        if self.shield == 175:
            explo = Explosion((self.rect.centerx + 160, self.rect.bottom - 100), 'supersize')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 170
        if self.shield == 150:
            explo = Explosion((self.rect.centerx + 125, self.rect.bottom - 40), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 145
        if self.shield == 115:
            explo = Explosion((self.rect.centerx - 150, self.rect.bottom - 170), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 110
        if self.shield == 100:
            explo = Explosion((self.rect.centerx - 130, self.rect.bottom - 115), 'supersize')
            explo1 = Explosion((self.rect.centerx + 180, self.rect.bottom - 75), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 95
        if self.shield == 85:
            explo = Explosion((self.rect.centerx - 170, self.rect.bottom - 80), 'lg')
            explo1 = Explosion((self.rect.centerx + 160, self.rect.bottom - 180), 'supersize')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 80
        if self.shield == 75:
            explo = Explosion((self.rect.centerx + 180, self.rect.bottom - 90), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 70
        if self.shield == 65:
            explo = Explosion((self.rect.centerx + 170, self.rect.bottom - 170), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 60
        if self.shield == 55:
            explo = Explosion((self.rect.centerx + 110, self.rect.bottom - 50), 'supersize')
            explo1 = Explosion((self.rect.centerx - 125, self.rect.bottom - 95), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 50
        if self.shield == 45:
            explo = Explosion((self.rect.centerx - 150, self.rect.bottom - 150), 'lg')
            explo1 = Explosion((self.rect.centerx + 170, self.rect.bottom - 105), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 40
        if self.shield == 35:
            explo = Explosion((self.rect.centerx + 130, self.rect.bottom - 30), 'supersize')
            explo1 = Explosion((self.rect.centerx - 20, self.rect.bottom - 25), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 30
        if self.shield == 25:
            explo = Explosion((self.rect.centerx - 140, self.rect.bottom - 190), 'lg')
            explo1 = Explosion((self.rect.centerx - 180, self.rect.bottom - 50), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 20
        if self.shield == 15:
            explo = Explosion((self.rect.centerx - 180, self.rect.bottom - 190), 'lg')
            explo1 = Explosion((self.rect.centerx + 190, self.rect.bottom - 175), 'supersize')
            explo2 = Explosion((self.rect.centerx + 30, self.rect.bottom - 220), 'lg')
            explo3 = Explosion((self.rect.centerx + 10, self.rect.bottom - 100), 'lg')
            explo4 = Explosion((self.rect.centerx - 150, self.rect.bottom - 110), 'supersize')
            explo5 = Explosion((self.rect.centerx - 140, self.rect.bottom - 140), 'lg')
            explo6 = Explosion((self.rect.centerx, self.rect.bottom - 110), 'boss')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            all_sprites.add(explo2)
            all_sprites.add(explo3)
            all_sprites.add(explo4)
            all_sprites.add(explo5)
            all_sprites.add(explo6)
            explosion_sound.play()
            self.shield = 10
        if self.shield == 5:
            explo = Explosion((self.rect.centerx - 180, self.rect.bottom - 190), 'supersize')
            explo1 = Explosion((self.rect.centerx + 190, self.rect.bottom - 175), 'supersize')
            explo2 = Explosion((self.rect.centerx + 125, self.rect.bottom - 220), 'boss')
            explo3 = Explosion((self.rect.centerx + 150, self.rect.bottom - 100), 'boss')
            explo4 = Explosion((self.rect.centerx - 150, self.rect.bottom - 200), 'boss')
            explo5 = Explosion((self.rect.centerx - 125, self.rect.bottom - 100), 'boss')
            explo6 = Explosion((self.rect.centerx, self.rect.bottom - 110), 'boss')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            all_sprites.add(explo2)
            all_sprites.add(explo3)
            all_sprites.add(explo4)
            all_sprites.add(explo5)
            all_sprites.add(explo6)
            explosion_sound.play()
            lifepow = ExtraLifePow(boss2.rect.center)
            all_sprites.add(lifepow)
            powerups.add(lifepow)
            self.shield = 0


class Boss2Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        boss2_missile_scale.set_colorkey(black)
        self.image = boss2_missile_scale
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        self.speedy = 0

    def update(self):
        self.speedy += 2
        self.rect.y += self.speedy
        # Kill it if it moves off the bottom of the screen
        if self.rect.top > height:
            self.kill()


class Boss3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scale_boss3_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, -300)
        self.speedx = 0
        self.speedy = 1.5
        self.shield = 1000
        self.shoot_delay = 500
        self.laser_delay = 8000
        self.warming_delay = 8000
        self.wait = 0
        self.last_shot = pygame.time.get_ticks()
        self.last_laser = pygame.time.get_ticks()
        self.last_warming = pygame.time.get_ticks()
        self.alive = True
        self.boss_defeated_sound = pygame.mixer.Sound(path.join(sounds, 'boss_defeated.wav'))
        self.boss_thrust_sound = pygame.mixer.Sound(path.join(sounds, 'thrust.wav'))
        self.boss_thrust_sound.set_volume(0.25)
        self.draw_arms = 1
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.boss_dying()
        if self.rect.right >= width - 20:
            self.rect.right = width - 20
            self.speedx = 0
        if self.rect.left <= 20:
            self.rect.left = 20
            self.speedx = 0
        if self.rect.bottom >= 300:
            self.boss_shoot()
            self.boss_laser_warming()
            self.boss_laser()
        if self.rect.bottom == 300 and self.speedx != -2 and \
                self.rect.right != width - 20 and self.speedy != 20 and self.speedy != -5:
            self.speedx = 2
            self.speedy = 0
        if self.rect.bottom == 300 and self.speedx != 2 and \
                self.rect.left != 20 and self.speedy != 20 and self.speedy != -5:
            self.speedx = -2
            self.speedy = 0
        if self.rect.bottom == 300 and random.random() > 0.995:
            self.boss_exhaust()
            self.speedy = 20
            self.speedx = 0
            self.boss_thrust_sound.play()
        if self.rect.bottom == 680:
            self.speedy = -5
            self.speedx = 0
        if self.speedy == -5 and self.rect.bottom == 300:
            if random.random() > 0.5:
                self.speedy = 0
                self.speedx = 2
            else:
                self.speedy = 0
                self.speedx = -2
        if self.shield <= 0:
            self.kill()
            self.rect.center = (width / 2, 1500)
            self.boss_defeated_sound.play(0)
            self.boss_defeated_sound.play(0)
            self.boss_defeated_sound.play(0)
            self.alive = False

    def boss_shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.shield >= 700:
                boss3_bullet = Boss1Bullet(self.rect.centerx, self.rect.bottom - 112)
                all_sprites.add(boss3_bullet)
                boss1_bullets.add(boss3_bullet)
                boss1_bullet_sound.play()
            if 700 > self.shield >= 300:
                boss3_bullet = Boss1Bullet(self.rect.centerx, self.rect.bottom - 112)
                all_sprites.add(boss3_bullet)
                boss1_bullets.add(boss3_bullet)
                boss1_bullet_sound.play()
                if random.random() > 0.7:
                    boss3_bullet1 = Boss1Bullet(self.rect.centerx, self.rect.bottom - 112)
                    all_sprites.add(boss3_bullet1)
                    boss1_bullets.add(boss3_bullet1)
            if 300 > self.shield > 0:
                boss3_bullet = Boss1Bullet(self.rect.centerx, self.rect.bottom - 112)
                all_sprites.add(boss3_bullet)
                boss1_bullets.add(boss3_bullet)
                boss1_bullet_sound.play()
                if random.random() > 0.5:
                    boss3_bullet1 = Boss1Bullet(self.rect.centerx, self.rect.bottom - 112)
                    all_sprites.add(boss3_bullet1)
                    boss1_bullets.add(boss3_bullet1)
                if random.random() > 0.5:
                    boss3_bullet2 = Boss1Bullet(self.rect.centerx, self.rect.bottom - 112)
                    all_sprites.add(boss3_bullet2)
                    boss1_bullets.add(boss3_bullet2)

    def boss_laser(self):
        self.wait += clock.get_rawtime()
        if self.wait >= 850:
            now = pygame.time.get_ticks()
            if now - self.last_laser > self.laser_delay:
                self.last_laser = now
                boss3_laser = Boss3Laser(self.rect.centerx - 48, self.rect.bottom - 155)
                boss3_laser1 = Boss3Laser(self.rect.centerx + 48, self.rect.bottom - 155)
                boss3_laser2 = Boss3Laser(self.rect.centerx - 66, self.rect.bottom - 148)
                boss3_laser3 = Boss3Laser(self.rect.centerx + 66, self.rect.bottom - 148)
                boss3_laser4 = Boss3Laser(self.rect.centerx - 86, self.rect.bottom - 127)
                boss3_laser5 = Boss3Laser(self.rect.centerx + 86, self.rect.bottom - 127)
                all_sprites.add(boss3_laser)
                boss3_lasers.add(boss3_laser)
                all_sprites.add(boss3_laser1)
                boss3_lasers.add(boss3_laser1)
                all_sprites.add(boss3_laser2)
                boss3_lasers.add(boss3_laser2)
                all_sprites.add(boss3_laser3)
                boss3_lasers.add(boss3_laser3)
                all_sprites.add(boss3_laser4)
                boss3_lasers.add(boss3_laser4)
                all_sprites.add(boss3_laser5)
                boss3_lasers.add(boss3_laser5)
                boss3_laser_sound.play()

    def boss_laser_warming(self):
        now = pygame.time.get_ticks()
        if now - self.last_warming > self.warming_delay:
            self.last_warming = now
            boss1_laser_warming = Boss3Warming(self.rect.centerx - 48, self.rect.bottom - 155)
            boss1_laser_warming1 = Boss3Warming(self.rect.centerx + 48, self.rect.bottom - 155)
            boss1_laser_warming2 = Boss3Warming(self.rect.centerx - 66, self.rect.bottom - 148)
            boss1_laser_warming3 = Boss3Warming(self.rect.centerx + 66, self.rect.bottom - 148)
            boss1_laser_warming4 = Boss3Warming(self.rect.centerx - 86, self.rect.bottom - 127)
            boss1_laser_warming5 = Boss3Warming(self.rect.centerx + 86, self.rect.bottom - 127)
            all_sprites.add(boss1_laser_warming)
            boss1_bullets.add(boss1_laser_warming)
            all_sprites.add(boss1_laser_warming1)
            boss1_bullets.add(boss1_laser_warming1)
            all_sprites.add(boss1_laser_warming2)
            boss1_bullets.add(boss1_laser_warming2)
            all_sprites.add(boss1_laser_warming3)
            boss1_bullets.add(boss1_laser_warming3)
            all_sprites.add(boss1_laser_warming4)
            boss1_bullets.add(boss1_laser_warming4)
            all_sprites.add(boss1_laser_warming5)
            boss1_bullets.add(boss1_laser_warming5)
            boss1_warming_sound.play()

    def boss_exhaust(self):
        boss3_exhaust = BossExhaust(self.rect.centerx - 97, self.rect.centery - 87)
        boss3_exhaust1 = BossExhaust(self.rect.centerx + 97, self.rect.centery - 87)
        all_sprites.add(boss3_exhaust)
        all_sprites.add(boss3_exhaust1)

    def boss_dying(self):
        if self.shield == 250:
            explo = Explosion((self.rect.centerx, self.rect.bottom - 55), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 245
        if self.shield == 225:
            explo = Explosion((self.rect.centerx + 135, self.rect.bottom - 200), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 220
        if self.shield == 200:
            explo = Explosion((self.rect.centerx - 150, self.rect.bottom - 150), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 195
        if self.shield == 175:
            explo = Explosion((self.rect.centerx + 160, self.rect.bottom - 100), 'supersize')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 170
        if self.shield == 150:
            explo = Explosion((self.rect.centerx + 125, self.rect.bottom - 40), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 145
        if self.shield == 115:
            explo = Explosion((self.rect.centerx - 150, self.rect.bottom - 170), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 110
        if self.shield == 100:
            explo = Explosion((self.rect.centerx - 130, self.rect.bottom - 115), 'supersize')
            explo1 = Explosion((self.rect.centerx + 180, self.rect.bottom - 75), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 95
        if self.shield == 85:
            explo = Explosion((self.rect.centerx - 170, self.rect.bottom - 80), 'lg')
            explo1 = Explosion((self.rect.centerx + 160, self.rect.bottom - 180), 'supersize')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 80
        if self.shield == 75:
            explo = Explosion((self.rect.centerx + 180, self.rect.bottom - 90), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 70
        if self.shield == 65:
            explo = Explosion((self.rect.centerx + 170, self.rect.bottom - 170), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 60
        if self.shield == 55:
            explo = Explosion((self.rect.centerx + 110, self.rect.bottom - 50), 'supersize')
            explo1 = Explosion((self.rect.centerx - 125, self.rect.bottom - 95), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 50
        if self.shield == 45:
            explo = Explosion((self.rect.centerx - 150, self.rect.bottom - 150), 'lg')
            explo1 = Explosion((self.rect.centerx + 170, self.rect.bottom - 105), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 40
        if self.shield == 35:
            explo = Explosion((self.rect.centerx + 130, self.rect.bottom - 30), 'supersize')
            explo1 = Explosion((self.rect.centerx - 20, self.rect.bottom - 25), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 30
        if self.shield == 25:
            explo = Explosion((self.rect.centerx - 140, self.rect.bottom - 190), 'lg')
            explo1 = Explosion((self.rect.centerx - 180, self.rect.bottom - 50), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 20
        if self.shield == 15:
            explo = Explosion((self.rect.centerx - 180, self.rect.bottom - 190), 'lg')
            explo1 = Explosion((self.rect.centerx + 190, self.rect.bottom - 175), 'supersize')
            explo2 = Explosion((self.rect.centerx + 30, self.rect.bottom - 220), 'lg')
            explo3 = Explosion((self.rect.centerx + 10, self.rect.bottom - 100), 'lg')
            explo4 = Explosion((self.rect.centerx - 150, self.rect.bottom - 110), 'supersize')
            explo5 = Explosion((self.rect.centerx - 140, self.rect.bottom - 140), 'lg')
            explo6 = Explosion((self.rect.centerx, self.rect.bottom - 110), 'boss')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            all_sprites.add(explo2)
            all_sprites.add(explo3)
            all_sprites.add(explo4)
            all_sprites.add(explo5)
            all_sprites.add(explo6)
            explosion_sound.play()
            self.shield = 10
        if self.shield == 5:
            explo = Explosion((self.rect.centerx - 130, self.rect.bottom - 190), 'supersize')
            explo1 = Explosion((self.rect.centerx + 140, self.rect.bottom - 175), 'supersize')
            explo2 = Explosion((self.rect.centerx + 95, self.rect.bottom - 220), 'boss')
            explo3 = Explosion((self.rect.centerx + 120, self.rect.bottom - 100), 'boss')
            explo4 = Explosion((self.rect.centerx - 120, self.rect.bottom - 200), 'boss')
            explo5 = Explosion((self.rect.centerx - 105, self.rect.bottom - 100), 'boss')
            explo6 = Explosion((self.rect.centerx, self.rect.bottom - 110), 'boss')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            all_sprites.add(explo2)
            all_sprites.add(explo3)
            all_sprites.add(explo4)
            all_sprites.add(explo5)
            all_sprites.add(explo6)
            explosion_sound.play()
            lifepow = ExtraLifePow(boss3.rect.center)
            all_sprites.add(lifepow)
            powerups.add(lifepow)
            self.shield = 0


class BossExhaust(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss3_exhaust
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y += boss3.speedy
        self.rect.x += boss3.speedx
        if boss3.speedy == -5:
            self.kill()
        if boss3.shield <= 0:
            self.kill()


class Boss3Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.boss_laser_time = pygame.time.get_ticks()
        self.image = boss3_laser
        self.image = pygame.transform.scale(boss3_laser, (5, 500))
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x

    def update(self):
        self.rect.x += boss3.speedx
        self.rect.y += boss3.speedy
        if pygame.time.get_ticks() - self.boss_laser_time > BOSS3_LASER_TIME:
            self.kill()
        if boss3.shield <= 0:
            self.kill()


class Boss3Warming(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.boss_laser_time = pygame.time.get_ticks()
        self.image = boss3_laser_warming
        self.image = pygame.transform.scale(boss3_laser_warming, (5, 10))
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x

    def update(self):
        self.rect.x += boss3.speedx
        self.rect.y += boss3.speedy
        if pygame.time.get_ticks() - self.boss_laser_time > BOSS1_LASER_WARMING_TIME:
            self.kill()
        if boss3.shield <= 0:
            self.kill()


class Boss4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = scale_boss4_img_rotated
        self.image_orig.set_colorkey(black)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, -300)
        self.speedx = 0
        self.speedy = 0
        self.shield = 1000
        self.shoot_delay = 500
        self.laser_delay = 6000
        self.warming_delay = 6000
        self.last_shot = pygame.time.get_ticks()
        self.last_laser = pygame.time.get_ticks()
        self.last_warming = pygame.time.get_ticks()
        self.alive = True
        self.boss_defeated_sound = pygame.mixer.Sound(path.join(sounds, 'boss_defeated.wav'))
        self.angle = 0
        self.offset = Vector2(0, 0)
        self.laser = True
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.speedy = 1.5
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.mask = pygame.mask.from_surface(self.image)
        if self.rect.centery == 150:
            boss1_warming_sound.play()
        if self.rect.centery >= 200:
            self.rect.centery = 200
            self.angle += 1
            self.rotate()
            self.boss4_laser()
            self.boss_shoot()
            self.boss_dying()
        if self.shield <= 0:
            self.kill()
            self.rect.center = (width / 2, 1500)
            self.boss_defeated_sound.play(0)
            self.boss_defeated_sound.play(0)
            self.boss_defeated_sound.play(0)
            self.alive = False
        if self.shield < 750:
            self.shoot_delay = 350
            self.angle += 0.35
        if self.shield < 500:
            self.shoot_delay = 250
            self.angle += 0.35
        if self.shield < 250:
            self.shoot_delay = 150
            self.angle += 0.35

    def rotate(self):
        self.image = pygame.transform.rotate(self.image_orig, -self.angle)
        offset_rotated = self.offset.rotate(self.angle)
        self.rect = self.image.get_rect(center=self.rect.center + offset_rotated)

    def boss4_laser(self):
        if self.laser:
            boss4_laser = Boss4Laser(0, 435, 0, boss4.rect.center)
            boss4_laser1 = Boss4Laser1(-375, -218, -120, boss4.rect.center)
            boss4_laser2 = Boss4Laser2(378, -218, 120, boss4.rect.center)
            all_sprites.add(boss4_laser)
            boss4_lasers.add(boss4_laser)
            all_sprites.add(boss4_laser1)
            boss4_lasers.add(boss4_laser1)
            all_sprites.add(boss4_laser2)
            boss4_lasers.add(boss4_laser2)
            boss4_laser_sound.play()
            self.laser = False
        # now = pygame.time.get_ticks()
        # if now - self.last_laser > self.laser_delay:
        #     self.last_laser = now
        #     boss4_laser_sound.play()

    def boss_shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.shield > 0:
                boss4_bullet = Boss4Bullet(self.rect.centerx, self.rect.centery)
                all_sprites.add(boss4_bullet)
                boss1_bullets.add(boss4_bullet)
                boss1_bullet_sound.play()

    def boss_dying(self):
        if self.shield == 250:
            explo = Explosion((self.rect.centerx, self.rect.centery - 55), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 245
        if self.shield == 225:
            explo = Explosion((self.rect.centerx + 35, self.rect.centery), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 220
        if self.shield == 200:
            explo = Explosion((self.rect.centerx - 50, self.rect.centery - 50), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 195
        if self.shield == 175:
            explo = Explosion((self.rect.centerx + 60, self.rect.centery + 100), 'supersize')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 170
        if self.shield == 150:
            explo = Explosion((self.rect.centerx + 25, self.rect.centery - 40), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 145
        if self.shield == 115:
            explo = Explosion((self.rect.centerx - 50, self.rect.centery - 70), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 110
        if self.shield == 100:
            explo = Explosion((self.rect.centerx - 30, self.rect.centery + 15), 'supersize')
            explo1 = Explosion((self.rect.centerx + 80, self.rect.centery - 75), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 95
        if self.shield == 85:
            explo = Explosion((self.rect.centerx - 70, self.rect.centery + 10), 'lg')
            explo1 = Explosion((self.rect.centerx + 60, self.rect.centery - 80), 'supersize')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 80
        if self.shield == 75:
            explo = Explosion((self.rect.centerx + 80, self.rect.centery - 90), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 70
        if self.shield == 65:
            explo = Explosion((self.rect.centerx + 70, self.rect.centery + 70), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 60
        if self.shield == 55:
            explo = Explosion((self.rect.centerx + 10, self.rect.centery - 50), 'supersize')
            explo1 = Explosion((self.rect.centerx - 25, self.rect.centery + 95), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 50
        if self.shield == 45:
            explo = Explosion((self.rect.centerx - 50, self.rect.centery - 50), 'lg')
            explo1 = Explosion((self.rect.centerx + 70, self.rect.centery + 5), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 40
        if self.shield == 35:
            explo = Explosion((self.rect.centerx + 30, self.rect.centery - 30), 'supersize')
            explo1 = Explosion((self.rect.centerx - 20, self.rect.centery + 25), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 30
        if self.shield == 25:
            explo = Explosion((self.rect.centerx - 40, self.rect.centery - 90), 'lg')
            explo1 = Explosion((self.rect.centerx - 80, self.rect.centery + 50), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 20
        if self.shield == 15:
            explo = Explosion((self.rect.centerx - 80, self.rect.centery - 90), 'lg')
            explo1 = Explosion((self.rect.centerx + 90, self.rect.centery + 75), 'supersize')
            explo2 = Explosion((self.rect.centerx + 30, self.rect.centery - 20), 'lg')
            explo3 = Explosion((self.rect.centerx + 10, self.rect.centery), 'lg')
            explo4 = Explosion((self.rect.centerx - 50, self.rect.centery - 10), 'supersize')
            explo5 = Explosion((self.rect.centerx - 40, self.rect.centery + 40), 'lg')
            explo6 = Explosion((self.rect.centerx, self.rect.centery), 'boss')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            all_sprites.add(explo2)
            all_sprites.add(explo3)
            all_sprites.add(explo4)
            all_sprites.add(explo5)
            all_sprites.add(explo6)
            explosion_sound.play()
            self.shield = 10
        if self.shield == 5:
            explo = Explosion((self.rect.centerx - 80, self.rect.centery + 90), 'supersize')
            explo1 = Explosion((self.rect.centerx + 90, self.rect.centery - 75), 'supersize')
            explo2 = Explosion((self.rect.centerx + 25, self.rect.centery + 120), 'boss')
            explo3 = Explosion((self.rect.centerx + 150, self.rect.centery - 50), 'boss')
            explo4 = Explosion((self.rect.centerx - 150, self.rect.centery + 100), 'boss')
            explo5 = Explosion((self.rect.centerx - 25, self.rect.centery - 50), 'boss')
            explo6 = Explosion((self.rect.centerx, self.rect.centery), 'boss')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            all_sprites.add(explo2)
            all_sprites.add(explo3)
            all_sprites.add(explo4)
            all_sprites.add(explo5)
            all_sprites.add(explo6)
            explosion_sound.play()
            lifepow = ExtraLifePow(boss4.rect.center)
            all_sprites.add(lifepow)
            powerups.add(lifepow)
            self.shield = 0


class Boss4Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, rot, pos):
        super().__init__()
        self.image = pygame.transform.rotate(laserult_scale, rot)
        self.image.set_colorkey(black)
        self.orig_image = self.image
        self.rect = self.image.get_rect(topleft=(10000, 10000))  # Use topleft starting position to keep lasers from flashing around (0,0)
        self.pos = Vector2(pos)
        self.offset = Vector2(x, y)
        self.angle = 0
        self.hidden = False
        self.hide_clock = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.angle += 1
        self.rotate()
        self.hide_clock += clock.get_rawtime()
        self.mask = pygame.mask.from_surface(self.image)
        if boss4.shield < 750:
            self.angle += 0.35
        if boss4.shield < 500:
            self.angle += 0.35
        if boss4.shield < 250:
            self.angle += 0.35
        if boss4.shield <= 0:
            self.kill()

        if self.hide_clock > 3000:
            self.hidden = True
            self.rect.center = (3000, 0)
            if self.hide_clock > 6000:
                self.hide_clock = 0
                self.hidden = False

        if self.hide_clock == 0:
            boss4_laser_sound.play()

    def rotate(self):
        self.image = pygame.transform.rotate(self.orig_image, -self.angle)
        offset_rotated = self.offset.rotate(self.angle)
        self.rect = self.image.get_rect(center=self.pos + offset_rotated)


class Boss4Laser1(pygame.sprite.Sprite):
    def __init__(self, x, y, rot, pos):
        super().__init__()
        self.image = pygame.transform.rotate(laserult_scale, rot)
        self.image.set_colorkey(black)
        self.orig_image = self.image
        self.rect = self.image.get_rect(topleft=(10000, 10000))  # Use topleft starting position to keep lasers from flashing around (0,0)
        self.pos = Vector2(pos)
        self.offset = Vector2(x, y)
        self.angle = 0
        self.hidden = False
        self.warming_once = True
        self.hide_clock = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.angle += 1
        self.rotate()
        self.hide_clock += clock.get_rawtime()
        self.mask = pygame.mask.from_surface(self.image)
        if boss4.shield < 750:
            self.angle += 0.35
        if boss4.shield < 500:
            self.angle += 0.35
        if boss4.shield < 250:
            self.angle += 0.35
        if boss4.shield <= 0:
            self.kill()

        if self.hide_clock > 3000:
            self.hidden = True
            self.rect.center = (3000, 0)
            if self.hide_clock > 6000:
                self.hide_clock = 0
                self.hidden = False

        if 5025 < self.hide_clock < 5060:
            boss1_warming_sound.play()

    def rotate(self):
        self.image = pygame.transform.rotate(self.orig_image, -self.angle)
        offset_rotated = self.offset.rotate(self.angle)
        self.rect = self.image.get_rect(center=self.pos + offset_rotated)


class Boss4Laser2(pygame.sprite.Sprite):
    def __init__(self, x, y, rot, pos):
        super().__init__()
        self.image = pygame.transform.rotate(laserult_scale, rot)
        self.image.set_colorkey(black)
        self.orig_image = self.image
        self.rect = self.image.get_rect(topleft=(10000, 10000))  # Use topleft starting position to keep lasers from flashing around (0,0)
        self.pos = Vector2(pos)
        self.offset = Vector2(x, y)
        self.angle = 0
        self.hidden = False
        self.hide_clock = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.angle += 1
        self.rotate()
        self.hide_clock += clock.get_rawtime()
        self.mask = pygame.mask.from_surface(self.image)
        if boss4.shield < 750:
            self.angle += 0.35
        if boss4.shield < 500:
            self.angle += 0.35
        if boss4.shield < 250:
            self.angle += 0.35
        if boss4.shield <= 0:
            self.kill()

        if self.hide_clock > 3000:
            self.hidden = True
            self.rect.center = (3000, 0)
            if self.hide_clock > 6000:
                self.hide_clock = 0
                self.hidden = False

    def rotate(self):
        self.image = pygame.transform.rotate(self.orig_image, -self.angle)
        offset_rotated = self.offset.rotate(self.angle)
        self.rect = self.image.get_rect(center=self.pos + offset_rotated)


class Boss4Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss1_bullet
        self.image = pygame.transform.scale(boss1_bullet, (13, 13))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speedx = random.randrange(-10, 10)
        if random.random() > 0.7:
            self.speedy = random.randrange(-10, -6)
        else:
            self.speedy = random.randrange(6, 10)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Kill it if it moves off the screen
        if self.rect.top > height or self.rect.bottom < 0 or self.rect.left > width or self.rect.right < 0:
            self.kill()


class Boss5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scale_boss5_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = (width / 2)
        self.rect.bottom = -102
        self.speedy = 0
        self.shield = 1000
        self.shoot_delay = 800
        self.laser_delay = 8000
        self.warming_delay = 8000
        self.wait = 0
        self.last_shot = pygame.time.get_ticks()
        self.last_shot1 = pygame.time.get_ticks()
        self.last_shot2 = pygame.time.get_ticks()
        self.last_laser = pygame.time.get_ticks()
        self.last_laser1 = pygame.time.get_ticks()
        self.last_laser2 = pygame.time.get_ticks()
        self.last_laser3 = pygame.time.get_ticks()
        self.last_laser4 = pygame.time.get_ticks()
        self.last_laser5 = pygame.time.get_ticks()
        self.last_laser6 = pygame.time.get_ticks()
        self.last_laser7 = pygame.time.get_ticks()
        self.last_laser8 = pygame.time.get_ticks()
        self.last_laser9 = pygame.time.get_ticks()
        self.last_warming = pygame.time.get_ticks()
        self.last_warming1 = pygame.time.get_ticks()
        self.last_warming2 = pygame.time.get_ticks()
        self.last_warming3 = pygame.time.get_ticks()
        self.last_warming4 = pygame.time.get_ticks()
        self.last_warming5 = pygame.time.get_ticks()
        self.last_warming6 = pygame.time.get_ticks()
        self.last_warming7 = pygame.time.get_ticks()
        self.last_warming8 = pygame.time.get_ticks()
        self.last_warming9 = pygame.time.get_ticks()
        self.alive = True
        self.boss_defeated_sound = pygame.mixer.Sound(path.join(sounds, 'boss_defeated.wav'))
        self.you_win_sound = pygame.mixer.Sound(path.join(sounds, 'you_win_sound.wav'))
        self.mask = pygame.mask.from_surface(self.image)
        self.change_image_right_first = 0
        self.change_image_left_first = 0

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 300:
            self.speedy = 1.5
        if self.rect.bottom == 300:
            self.speedy = 0
        if self.rect.bottom >= 300:
            self.boss_shoot()
            self.boss_laser_warming()
            self.boss_laser()
            self.boss_dying()

        # Make the boss move down randomly and then back up
        if self.rect.bottom == 300:
            if random.random() > 0.997:
                self.speedy = 1
        if self.rect.bottom == 550:
            self.speedy = -1
        if self.speedy == -1 and self.rect.bottom == 300:
            self.speedy = 0

        # If shield = 0, kill the boss
        if self.shield <= 0:
            self.kill()
            self.rect.center = (width / 2, 3500)
            self.boss_defeated_sound.play(0)
            self.boss_defeated_sound.play(0)
            self.boss_defeated_sound.play(0)
            self.alive = False

        # Updating Image depending on what gets destroyed (right arm destroyed first)
        if not boss5_right_hitbox.alive and boss5_left_hitbox.alive and self.change_image_right_first == 0:
            self.image = scale_boss5_img_no_right_arm
            self.change_image_right_first = 1
        if not boss5_right_hitbox.alive and not boss5_left_hitbox.alive and self.change_image_right_first == 1:
            self.image = scale_boss5_img_no_arms
            self.change_image_right_first = 2

        # Updating Image depending on what gets destroyed (left arm destroyed first)
        if not boss5_left_hitbox.alive and boss5_right_hitbox.alive and self.change_image_left_first == 0:
            self.image = scale_boss5_img_no_left_arm1
            self.change_image_left_first = 1
        if not boss5_left_hitbox.alive and not boss5_right_hitbox.alive and self.change_image_left_first == 1:
            self.image = scale_boss5_img_no_arms1
            self.change_image_left_first = 2

    def boss_shoot(self):
        if self.shield >= 1:
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                self.last_shot = now
                boss5_bullet = Boss1Bullet(self.rect.centerx, self.rect.bottom - 20)
                all_sprites.add(boss5_bullet)
                boss1_bullets.add(boss5_bullet)
                boss1_bullet_sound.play()
            if self.wait >= 266:
                now1 = pygame.time.get_ticks()
                if now1 - self.last_shot1 > self.shoot_delay:
                    self.last_shot1 = now1
                    boss5_bullet1 = Boss1Bullet(self.rect.centerx - 114, self.rect.bottom - 385)
                    all_sprites.add(boss5_bullet1)
                    boss1_bullets.add(boss5_bullet1)
                    boss1_bullet_sound.play()
            if self.wait >= 533:
                now2 = pygame.time.get_ticks()
                if now2 - self.last_shot2 > self.shoot_delay:
                    self.last_shot2 = now2
                    boss5_bullet2 = Boss1Bullet(self.rect.centerx + 114, self.rect.bottom - 385)
                    all_sprites.add(boss5_bullet2)
                    boss1_bullets.add(boss5_bullet2)
                    boss1_bullet_sound.play()

    def boss_laser(self):
        self.wait += clock.get_rawtime()
        if self.wait >= 850:
            now = pygame.time.get_ticks()
            if now - self.last_laser > self.laser_delay:
                self.last_laser = now
                boss5_laser = Boss5Laser(self.rect.centerx - 50, self.rect.bottom - 107)
                boss5_laser1 = Boss5Laser(self.rect.centerx + 50, self.rect.bottom - 107)
                all_sprites.add(boss5_laser)
                boss5_lasers.add(boss5_laser)
                all_sprites.add(boss5_laser1)
                boss5_lasers.add(boss5_laser1)
                boss5_laser_sound.play()
        if self.wait >= 1250:
            now1 = pygame.time.get_ticks()
            if now1 - self.last_laser1 > self.laser_delay:
                self.last_laser1 = now1
                boss5_laser2 = Boss5Laser(self.rect.centerx - 33, self.rect.bottom - 33)
                boss5_laser3 = Boss5Laser(self.rect.centerx + 33, self.rect.bottom - 33)
                all_sprites.add(boss5_laser2)
                boss5_lasers.add(boss5_laser2)
                all_sprites.add(boss5_laser3)
                boss5_lasers.add(boss5_laser3)
                boss5_laser_sound.play()
        if self.wait >= 1650:
            now2 = pygame.time.get_ticks()
            if now2 - self.last_laser2 > self.laser_delay:
                self.last_laser2 = now2
                boss5_laser4 = Boss5Laser(self.rect.centerx - 20, self.rect.bottom)
                boss5_laser5 = Boss5Laser(self.rect.centerx + 20, self.rect.bottom)
                all_sprites.add(boss5_laser4)
                boss5_lasers.add(boss5_laser4)
                all_sprites.add(boss5_laser5)
                boss5_lasers.add(boss5_laser5)
                boss5_laser_sound.play()
        if self.wait >= 2000:
            now3 = pygame.time.get_ticks()
            if now3 - self.last_laser3 > self.laser_delay and boss5_left_hitbox.alive and boss5_right_hitbox.alive:
                self.last_laser3 = now3
                boss5_laser7 = Boss5Laser(self.rect.centerx - 196, self.rect.bottom - 89)
                boss5_laser8 = Boss5Laser(self.rect.centerx + 196, self.rect.bottom - 89)
                all_sprites.add(boss5_laser7)
                boss5_lasers.add(boss5_laser7)
                all_sprites.add(boss5_laser8)
                boss5_lasers.add(boss5_laser8)
                boss5_laser_sound.play()
            elif now3 - self.last_laser3 > self.laser_delay and not boss5_left_hitbox.alive and boss5_right_hitbox.alive:
                self.last_laser3 = now3
                boss5_laser8 = Boss5Laser(self.rect.centerx + 196, self.rect.bottom - 89)
                all_sprites.add(boss5_laser8)
                boss5_lasers.add(boss5_laser8)
                boss5_laser_sound.play()
            elif now3 - self.last_laser3 > self.laser_delay and boss5_left_hitbox.alive and not boss5_right_hitbox.alive:
                self.last_laser3 = now3
                boss5_laser7 = Boss5Laser(self.rect.centerx - 196, self.rect.bottom - 89)
                all_sprites.add(boss5_laser7)
                boss5_lasers.add(boss5_laser7)
                boss5_laser_sound.play()
        if self.wait >= 2500:
            now4 = pygame.time.get_ticks()
            if now4 - self.last_laser4 > self.laser_delay and boss5_left_hitbox.alive and boss5_right_hitbox.alive:
                self.last_laser4 = now4
                boss5_laser9 = Boss5Laser(self.rect.centerx - 216, self.rect.bottom - 101)
                boss5_laser10 = Boss5Laser(self.rect.centerx + 216, self.rect.bottom - 101)
                all_sprites.add(boss5_laser9)
                boss5_lasers.add(boss5_laser9)
                all_sprites.add(boss5_laser10)
                boss5_lasers.add(boss5_laser10)
                boss5_laser_sound.play()
            elif now4 - self.last_laser4 > self.laser_delay and not boss5_left_hitbox.alive and boss5_right_hitbox.alive:
                self.last_laser4 = now4
                boss5_laser10 = Boss5Laser(self.rect.centerx + 216, self.rect.bottom - 101)
                all_sprites.add(boss5_laser10)
                boss5_lasers.add(boss5_laser10)
                boss5_laser_sound.play()
            elif now4 - self.last_laser4 > self.laser_delay and boss5_left_hitbox.alive and not boss5_right_hitbox.alive:
                self.last_laser4 = now4
                boss5_laser9 = Boss5Laser(self.rect.centerx - 216, self.rect.bottom - 101)
                all_sprites.add(boss5_laser9)
                boss5_lasers.add(boss5_laser9)
                boss5_laser_sound.play()
        if self.wait >= 3500:
            now5 = pygame.time.get_ticks()
            if now5 - self.last_laser5 > self.laser_delay and boss5_left_hitbox.alive:
                self.last_laser5 = now5
                boss5_laser11 = Boss5Laser(self.rect.centerx - 196, self.rect.bottom - 89)
                all_sprites.add(boss5_laser11)
                boss5_lasers.add(boss5_laser11)
                boss5_laser_sound.play()
        if self.wait >= 4000:
            now6 = pygame.time.get_ticks()
            if now6 - self.last_laser6 > self.laser_delay and boss5_right_hitbox.alive:
                self.last_laser6 = now6
                boss5_laser12 = Boss5Laser(self.rect.centerx + 196, self.rect.bottom - 89)
                all_sprites.add(boss5_laser12)
                boss5_lasers.add(boss5_laser12)
                boss5_laser_sound.play()
        if self.wait >= 4500:
            now7 = pygame.time.get_ticks()
            if now7 - self.last_laser7 > self.laser_delay and boss5_left_hitbox.alive:
                self.last_laser7 = now7
                boss5_laser13 = Boss5Laser(self.rect.centerx - 216, self.rect.bottom - 101)
                all_sprites.add(boss5_laser13)
                boss5_lasers.add(boss5_laser13)
                boss5_laser_sound.play()
        if self.wait >= 5000:
            now8 = pygame.time.get_ticks()
            if now8 - self.last_laser8 > self.laser_delay and boss5_right_hitbox.alive:
                self.last_laser8 = now8
                boss5_laser14 = Boss5Laser(self.rect.centerx + 216, self.rect.bottom - 101)
                all_sprites.add(boss5_laser14)
                boss5_lasers.add(boss5_laser14)
                boss5_laser_sound.play()
        if self.wait >= 5800:
            now9 = pygame.time.get_ticks()
            if now9 - self.last_laser9 > self.laser_delay:
                self.last_laser9 = now9
                boss5_laser15 = Boss5LaserUlt(self.rect.centerx + 105, self.rect.bottom - 115)
                boss5_laser16 = Boss5LaserUlt(self.rect.centerx - 105, self.rect.bottom - 115)
                all_sprites.add(boss5_laser15)
                boss5_lasers.add(boss5_laser15)
                all_sprites.add(boss5_laser16)
                boss5_lasers.add(boss5_laser16)
                boss5_ult_sound.play()
        if boss5.shield <= 0:
            self.kill()

    def boss_laser_warming(self):
        if self.wait >= 0:
            now = pygame.time.get_ticks()
            if now - self.last_warming > self.warming_delay:
                self.last_warming = now
                boss5_laser_warming = Boss5Warming(self.rect.centerx - 50, self.rect.bottom - 107)
                boss5_laser_warming1 = Boss5Warming(self.rect.centerx + 50, self.rect.bottom - 107)
                all_sprites.add(boss5_laser_warming)
                boss1_bullets.add(boss5_laser_warming)
                all_sprites.add(boss5_laser_warming1)
                boss1_bullets.add(boss5_laser_warming1)
                boss1_warming_sound.play()
        if self.wait >= 400:
            now1 = pygame.time.get_ticks()
            if now1 - self.last_warming1 > self.warming_delay:
                self.last_warming1 = now1
                boss5_laser_warming2 = Boss5Warming(self.rect.centerx - 33, self.rect.bottom - 33)
                boss5_laser_warming3 = Boss5Warming(self.rect.centerx + 33, self.rect.bottom - 33)
                all_sprites.add(boss5_laser_warming2)
                boss1_bullets.add(boss5_laser_warming2)
                all_sprites.add(boss5_laser_warming3)
                boss1_bullets.add(boss5_laser_warming3)
                boss1_warming_sound.play()
        if self.wait >= 800:
            now2 = pygame.time.get_ticks()
            if now2 - self.last_warming2 > self.warming_delay:
                self.last_warming2 = now2
                boss5_laser_warming4 = Boss5Warming(self.rect.centerx - 20, self.rect.bottom)
                boss5_laser_warming5 = Boss5Warming(self.rect.centerx + 20, self.rect.bottom)
                all_sprites.add(boss5_laser_warming4)
                boss1_bullets.add(boss5_laser_warming4)
                all_sprites.add(boss5_laser_warming5)
                boss1_bullets.add(boss5_laser_warming5)
                boss1_warming_sound.play()
        if self.wait >= 1150:
            now3 = pygame.time.get_ticks()
            if now3 - self.last_warming3 > self.warming_delay and boss5_left_hitbox.alive and boss5_right_hitbox.alive:
                self.last_warming3 = now3
                boss5_laser_warming7 = Boss5Warming(self.rect.centerx - 196, self.rect.bottom - 89)
                boss5_laser_warming8 = Boss5Warming(self.rect.centerx + 196, self.rect.bottom - 89)
                all_sprites.add(boss5_laser_warming7)
                boss1_bullets.add(boss5_laser_warming7)
                all_sprites.add(boss5_laser_warming8)
                boss1_bullets.add(boss5_laser_warming8)
                boss1_warming_sound.play()
            elif now3 - self.last_warming3 > self.warming_delay and not boss5_left_hitbox.alive and boss5_right_hitbox.alive:
                self.last_warming3 = now3
                boss5_laser_warming8 = Boss5Warming(self.rect.centerx + 196, self.rect.bottom - 89)
                all_sprites.add(boss5_laser_warming8)
                boss1_bullets.add(boss5_laser_warming8)
                boss1_warming_sound.play()
            elif now3 - self.last_warming3 > self.warming_delay and boss5_left_hitbox.alive and not boss5_right_hitbox.alive:
                self.last_warming3 = now3
                boss5_laser_warming7 = Boss5Warming(self.rect.centerx - 196, self.rect.bottom - 89)
                all_sprites.add(boss5_laser_warming7)
                boss1_bullets.add(boss5_laser_warming7)
                boss1_warming_sound.play()
        if self.wait >= 1650:
            now4 = pygame.time.get_ticks()
            if now4 - self.last_warming4 > self.warming_delay and boss5_left_hitbox.alive and boss5_right_hitbox.alive:
                self.last_warming4 = now4
                boss5_laser_warming8 = Boss5Warming(self.rect.centerx - 216, self.rect.bottom - 101)
                boss5_laser_warming9 = Boss5Warming(self.rect.centerx + 216, self.rect.bottom - 101)
                all_sprites.add(boss5_laser_warming8)
                boss1_bullets.add(boss5_laser_warming8)
                all_sprites.add(boss5_laser_warming9)
                boss1_bullets.add(boss5_laser_warming9)
                boss1_warming_sound.play()
            elif now4 - self.last_warming4 > self.warming_delay and not boss5_left_hitbox.alive and boss5_right_hitbox.alive:
                self.last_warming4 = now4
                boss5_laser_warming9 = Boss5Warming(self.rect.centerx + 216, self.rect.bottom - 101)
                all_sprites.add(boss5_laser_warming9)
                boss1_bullets.add(boss5_laser_warming9)
                boss1_warming_sound.play()
            elif now4 - self.last_warming4 > self.warming_delay and boss5_left_hitbox.alive and not boss5_right_hitbox.alive:
                self.last_warming4 = now4
                boss5_laser_warming8 = Boss5Warming(self.rect.centerx - 216, self.rect.bottom - 101)
                all_sprites.add(boss5_laser_warming8)
                boss1_bullets.add(boss5_laser_warming8)
                boss1_warming_sound.play()
        if self.wait >= 2650:
            now5 = pygame.time.get_ticks()
            if now5 - self.last_warming5 > self.warming_delay and boss5_left_hitbox.alive:
                self.last_warming5 = now5
                boss5_laser_warming10 = Boss5Warming(self.rect.centerx - 196, self.rect.bottom - 89)
                all_sprites.add(boss5_laser_warming10)
                boss1_bullets.add(boss5_laser_warming10)
                boss1_warming_sound.play()
        if self.wait >= 3150:
            now6 = pygame.time.get_ticks()
            if now6 - self.last_warming6 > self.warming_delay and boss5_right_hitbox.alive:
                self.last_warming6 = now6
                boss5_laser_warming11 = Boss5Warming(self.rect.centerx + 196, self.rect.bottom - 89)
                all_sprites.add(boss5_laser_warming11)
                boss1_bullets.add(boss5_laser_warming11)
                boss1_warming_sound.play()
        if self.wait >= 3650:
            now7 = pygame.time.get_ticks()
            if now7 - self.last_warming7 > self.warming_delay and boss5_left_hitbox.alive:
                self.last_warming7 = now7
                boss5_laser_warming12 = Boss5Warming(self.rect.centerx - 216, self.rect.bottom - 101)
                all_sprites.add(boss5_laser_warming12)
                boss1_bullets.add(boss5_laser_warming12)
                boss1_warming_sound.play()
        if self.wait >= 4150:
            now8 = pygame.time.get_ticks()
            if now8 - self.last_warming8 > self.warming_delay and boss5_right_hitbox.alive:
                self.last_warming8 = now8
                boss5_laser_warming13 = Boss5Warming(self.rect.centerx + 216, self.rect.bottom - 101)
                all_sprites.add(boss5_laser_warming13)
                boss1_bullets.add(boss5_laser_warming13)
                boss1_warming_sound.play()
        if self.wait >= 4950:
            now9 = pygame.time.get_ticks()
            if now9 - self.last_warming9 > self.warming_delay:
                self.last_warming9 = now9
                boss5_laser_warming14 = Boss5UltWarming(self.rect.centerx - 105, self.rect.bottom - 115)
                boss5_laser_warming15 = Boss5UltWarming(self.rect.centerx + 105, self.rect.bottom - 115)
                all_sprites.add(boss5_laser_warming14)
                boss1_bullets.add(boss5_laser_warming14)
                all_sprites.add(boss5_laser_warming15)
                boss1_bullets.add(boss5_laser_warming15)
                boss1_warming_sound.play()
        if boss5.shield <= 0:
            self.kill()

    def boss_dying(self):
        if self.shield == 250:
            explo = Explosion((self.rect.centerx, self.rect.bottom - 55), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 245
        if self.shield == 225:
            explo = Explosion((self.rect.centerx + 135, self.rect.bottom - 200), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 220
        if self.shield == 200:
            explo = Explosion((self.rect.centerx - 150, self.rect.bottom - 150), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 195
        if self.shield == 175:
            explo = Explosion((self.rect.centerx + 160, self.rect.bottom - 100), 'supersize')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 170
        if self.shield == 150:
            explo = Explosion((self.rect.centerx + 125, self.rect.bottom - 40), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 145
        if self.shield == 115:
            explo = Explosion((self.rect.centerx - 150, self.rect.bottom - 170), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 110
        if self.shield == 100:
            explo = Explosion((self.rect.centerx - 130, self.rect.bottom - 115), 'supersize')
            explo1 = Explosion((self.rect.centerx + 180, self.rect.bottom - 75), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 95
        if self.shield == 85:
            explo = Explosion((self.rect.centerx - 170, self.rect.bottom - 80), 'lg')
            explo1 = Explosion((self.rect.centerx + 160, self.rect.bottom - 180), 'supersize')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 80
        if self.shield == 75:
            explo = Explosion((self.rect.centerx + 180, self.rect.bottom - 90), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 70
        if self.shield == 65:
            explo = Explosion((self.rect.centerx + 170, self.rect.bottom - 170), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 60
        if self.shield == 55:
            explo = Explosion((self.rect.centerx + 110, self.rect.bottom - 50), 'supersize')
            explo1 = Explosion((self.rect.centerx - 125, self.rect.bottom - 95), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 50
        if self.shield == 45:
            explo = Explosion((self.rect.centerx - 150, self.rect.bottom - 150), 'lg')
            explo1 = Explosion((self.rect.centerx + 170, self.rect.bottom - 105), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 40
        if self.shield == 35:
            explo = Explosion((self.rect.centerx + 130, self.rect.bottom - 30), 'supersize')
            explo1 = Explosion((self.rect.centerx - 20, self.rect.bottom - 25), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 30
        if self.shield == 25:
            explo = Explosion((self.rect.centerx - 140, self.rect.bottom - 190), 'lg')
            explo1 = Explosion((self.rect.centerx - 180, self.rect.bottom - 50), 'lg')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            explosion_sound.play()
            self.shield = 20
        if self.shield == 15:
            explo = Explosion((self.rect.centerx - 180, self.rect.bottom - 190), 'lg')
            explo1 = Explosion((self.rect.centerx + 190, self.rect.bottom - 175), 'supersize')
            explo2 = Explosion((self.rect.centerx + 30, self.rect.bottom - 220), 'lg')
            explo3 = Explosion((self.rect.centerx + 10, self.rect.bottom - 100), 'lg')
            explo4 = Explosion((self.rect.centerx - 150, self.rect.bottom - 110), 'supersize')
            explo5 = Explosion((self.rect.centerx - 140, self.rect.bottom - 140), 'lg')
            explo6 = Explosion((self.rect.centerx, self.rect.bottom - 110), 'boss')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            all_sprites.add(explo2)
            all_sprites.add(explo3)
            all_sprites.add(explo4)
            all_sprites.add(explo5)
            all_sprites.add(explo6)
            explosion_sound.play()
            self.shield = 10
        if self.shield == 5:
            explo = Explosion((self.rect.centerx - 180, self.rect.bottom - 190), 'supersize')
            explo1 = Explosion((self.rect.centerx + 190, self.rect.bottom - 175), 'supersize')
            explo2 = Explosion((self.rect.centerx + 125, self.rect.bottom - 220), 'boss')
            explo3 = Explosion((self.rect.centerx + 150, self.rect.bottom - 100), 'boss')
            explo4 = Explosion((self.rect.centerx - 150, self.rect.bottom - 200), 'boss')
            explo5 = Explosion((self.rect.centerx - 125, self.rect.bottom - 100), 'boss')
            explo6 = Explosion((self.rect.centerx, self.rect.bottom - 110), 'boss')
            explo7 = Explosion((self.rect.centerx - 280, self.rect.bottom - 290), 'supersize')
            explo8 = Explosion((self.rect.centerx + 290, self.rect.bottom - 275), 'supersize')
            explo9 = Explosion((self.rect.centerx + 225, self.rect.bottom - 320), 'boss')
            explo10 = Explosion((self.rect.centerx + 250, self.rect.bottom - 200), 'boss')
            explo11 = Explosion((self.rect.centerx - 250, self.rect.bottom - 300), 'boss')
            explo12 = Explosion((self.rect.centerx - 225, self.rect.bottom - 200), 'boss')
            explo13 = Explosion((self.rect.centerx, self.rect.bottom - 210), 'boss')
            all_sprites.add(explo)
            all_sprites.add(explo1)
            all_sprites.add(explo2)
            all_sprites.add(explo3)
            all_sprites.add(explo4)
            all_sprites.add(explo5)
            all_sprites.add(explo6)
            all_sprites.add(explo7)
            all_sprites.add(explo8)
            all_sprites.add(explo9)
            all_sprites.add(explo10)
            all_sprites.add(explo11)
            all_sprites.add(explo12)
            all_sprites.add(explo13)
            explosion_sound.play()
            lifepow = FinalHeart(boss5.rect.center)
            all_sprites.add(lifepow)
            powerups.add(lifepow)
            self.shield = 0
            boss5_hitbox.shield = 0


class Boss5HitBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scale_boss5_img_cabin_hitbox
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = boss5.rect.center
        self.mask = pygame.mask.from_surface(self.image)
        self.shield = 1000
        self.alive = True

    def update(self):
        if self.shield > 0:
            self.rect.center = boss5.rect.center
        if self.shield <= 0:
            self.kill()
            self.alive = False
            self.rect.center = (10000, 10000)
        self.dying()

    def dying(self):
        if self.shield == 100:
            explo = Explosion((self.rect.centerx, self.rect.bottom - 120), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 95
        if self.shield == 75:
            explo = Explosion((self.rect.centerx + 25, self.rect.bottom - 140), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 70
        if self.shield == 55:
            explo = Explosion((self.rect.centerx - 20, self.rect.bottom - 130), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 50
        if self.shield == 25:
            explo = Explosion((self.rect.centerx + 10, self.rect.bottom - 120), 'supersize')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 20
        if self.shield == 15:
            explo = Explosion((self.rect.centerx - 15, self.rect.bottom - 150), 'supersize')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 10
        if self.shield == 5:
            explo = Explosion((self.rect.centerx, self.rect.bottom - 140), 'boss')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 0


class Boss5LeftHitBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scale_boss5_img_left_hitbox
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = boss5.rect.center
        self.mask = pygame.mask.from_surface(self.image)
        self.shield = 500
        self.alive = True

    def update(self):
        if self.shield > 0:
            self.rect.center = boss5.rect.center
        if self.shield <= 0:
            self.kill()
            self.alive = False
            self.rect.center = (10000, 10000)
        self.dying()

    def dying(self):
        if self.shield == 100:
            explo = Explosion((self.rect.left + 80, self.rect.bottom - 120), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 95
        if self.shield == 75:
            explo = Explosion((self.rect.left + 105, self.rect.bottom - 140), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 70
        if self.shield == 55:
            explo = Explosion((self.rect.left + 80, self.rect.bottom - 130), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 50
        if self.shield == 25:
            explo = Explosion((self.rect.left + 90, self.rect.bottom - 120), 'supersize')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 20
        if self.shield == 15:
            explo = Explosion((self.rect.left + 75, self.rect.bottom - 150), 'supersize')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 10
        if self.shield == 5:
            explo = Explosion((self.rect.left + 85, self.rect.bottom - 140), 'boss')
            all_sprites.add(explo)
            explosion_sound.play()
            explosion_sound.play()
            self.shield = 0


class Boss5RightHitBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scale_boss5_img_right_hitbox
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = boss5.rect.center
        self.mask = pygame.mask.from_surface(self.image)
        self.shield = 500
        self.alive = True

    def update(self):
        if self.shield > 0:
            self.rect.center = boss5.rect.center
        if self.shield <= 0:
            self.kill()
            self.alive = False
            self.rect.center = (10000, 10000)
        self.dying()

    def dying(self):
        if self.shield == 100:
            explo = Explosion((self.rect.right - 80, self.rect.bottom - 120), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 95
        if self.shield == 75:
            explo = Explosion((self.rect.right - 105, self.rect.bottom - 140), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 70
        if self.shield == 55:
            explo = Explosion((self.rect.right - 80, self.rect.bottom - 130), 'lg')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 50
        if self.shield == 25:
            explo = Explosion((self.rect.right - 90, self.rect.bottom - 120), 'supersize')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 20
        if self.shield == 15:
            explo = Explosion((self.rect.right - 75, self.rect.bottom - 150), 'supersize')
            all_sprites.add(explo)
            explosion_sound.play()
            self.shield = 10
        if self.shield == 5:
            explo = Explosion((self.rect.right - 85, self.rect.bottom - 140), 'boss')
            all_sprites.add(explo)
            explosion_sound.play()
            explosion_sound.play()
            self.shield = 0


class Boss5Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.boss_laser_time = pygame.time.get_ticks()
        self.image = boss5_laser_scale
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x

    def update(self):
        self.rect.y += boss5.speedy
        if pygame.time.get_ticks() - self.boss_laser_time > BOSS5_LASER_TIME:
            self.kill()
        if boss5.shield <= 0:
            self.kill()


class Boss5LaserUlt(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.boss_laser_time = pygame.time.get_ticks()
        self.image = pygame.transform.rotate(boss5_laser_scale_ult, 180)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x

    def update(self):
        self.rect.y += boss5.speedy
        if pygame.time.get_ticks() - self.boss_laser_time > 2000:
            self.kill()
        if boss5.shield <= 0:
            self.kill()


class Boss5Warming(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.boss_laser_time = pygame.time.get_ticks()
        self.image = boss3_laser_warming
        self.image = pygame.transform.scale(boss3_laser_warming, (5, 10))
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x

    def update(self):
        self.rect.y += boss5.speedy
        if pygame.time.get_ticks() - self.boss_laser_time > BOSS1_LASER_WARMING_TIME:
            self.kill()
        if boss5.shield <= 0:
            self.kill()


class Boss5UltWarming(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.boss_laser_time = pygame.time.get_ticks()
        self.image = boss1_laser_warming
        self.image = pygame.transform.scale(boss1_laser_warming, (40, 70))
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x

    def update(self):
        self.rect.y += boss5.speedy
        if pygame.time.get_ticks() - self.boss_laser_time > BOSS1_LASER_WARMING_TIME:
            self.kill()
        if boss5.shield <= 0:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# Game Loop
# Timers
y = 0
total_level_time = 0
level_time = 0
level_up_sound_time = 0
boss1_time = 0
boss2_time = 0
boss3_time = 0
boss4_time = 0
boss5_time = 0
stage1_time = 0
stage2_time = 0
stage3_time = 0
stage4_time = 0
stage5_time = 0
boss1_death_delay_time = 0
boss2_death_delay_time = 0
boss3_death_delay_time = 0
boss4_death_delay_time = 0
boss5_death_delay_time = 0
stage2_display_delay_time = 0
stage2_level_up_sound_time = 0
stage3_display_delay_time = 0
stage3_level_up_sound_time = 0
stage4_display_delay_time = 0
stage4_level_up_sound_time = 0
stage5_display_delay_time = 0
stage5_level_up_sound_time = 0
you_win_sound_one_time = 0
arm = 0
high_scores_test = 0
game_over = True
running = True
while running:
    if game_over:
        show_go_screen()
        show_user_name_screen()
        game_over = False
        lvl_up = False
        boss_fight = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        boss1_bullets = pygame.sprite.Group()
        boss1_lasers = pygame.sprite.Group()
        boss2_missiles = pygame.sprite.Group()
        boss3_lasers = pygame.sprite.Group()
        boss4_lasers = pygame.sprite.Group()
        boss5_lasers = pygame.sprite.Group()
        boss_arms = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        shields = pygame.sprite.Group()
        ults = pygame.sprite.Group()
        levels = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        boss1 = Boss1()
        boss1_group = pygame.sprite.Group()
        boss2 = Boss2()
        boss2_group = pygame.sprite.Group()
        boss3 = Boss3()
        boss3_group = pygame.sprite.Group()
        boss4 = Boss4()
        boss4_group = pygame.sprite.Group()
        boss5 = Boss5()
        boss5_group = pygame.sprite.Group()
        boss5_hitbox = Boss5HitBox()
        boss5_left_hitbox = Boss5LeftHitBox()
        boss5_right_hitbox = Boss5RightHitBox()
        score = 0
        for i in range(5):
            newmob()
        # Background Music
        pygame.mixer.music.play(-1)

    # keep loop running at the right speed
    clock.tick(FPS)

    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_p:
                pause()
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYUP and player.rect.bottom <= -100:
            game_over = True

    # Restart the game if player died and explosion finished playing
    if player.lives == 0 and not death_explosion.alive():
        total_level_time = 0
        level_time = 0
        level_up_sound_time = 0
        boss1_time = 0
        boss2_time = 0
        boss3_time = 0
        boss4_time = 0
        boss5_time = 0
        stage1_time = 0
        stage2_time = 0
        stage3_time = 0
        stage4_time = 0
        stage5_time = 0
        boss1_death_delay_time = 0
        boss2_death_delay_time = 0
        boss3_death_delay_time = 0
        boss4_death_delay_time = 0
        boss5_death_delay_time = 0
        stage2_display_delay_time = 0
        stage2_level_up_sound_time = 0
        stage3_display_delay_time = 0
        stage3_level_up_sound_time = 0
        stage4_display_delay_time = 0
        stage4_level_up_sound_time = 0
        stage5_display_delay_time = 0
        stage5_level_up_sound_time = 0
        you_win_sound_one_time = 0
        arm = 0
        high_scores_test = 0
        # game_over = True
        show_high_scores()

    # Update
    all_sprites.update()

    # Total Level Time
    total_level_time += clock.get_rawtime()

    # Add Enemies as time passes
    level_time += clock.get_rawtime()
    if level_time > 10000:
        for i in range(3):
            newmob()
        level_time = 0

    # Fly In
    if player.fly_in:
        player.invincible = 60
        player.speedy = -5
        if player.rect.center == (width / 2, 575):
            player.fly_in = False

    # Player invincible after respawn
    if player.invincible > 0:
        player.invincible -= 1

    # Spawn Boss1 at a certain time
    if boss1_time != -1:
        # Boss 1 times starts when stage_1_time starts
        if boss1_time >= 60000:
            all_sprites.add(boss1)
            boss1_group.add(boss1)
            boss_fight_sound.play()
            boss1_time = -1
            boss_fight = True

    # Spawn Boss2 at a certain time
    if boss2_time != -1:
        # Boss2_time starts when stage2_time starts
        if boss2_time >= 60000:
            all_sprites.add(boss2)
            boss2_group.add(boss2)
            boss_fight_sound.play()
            boss2_time = -1
            boss_fight = True

    # Spawn Boss3 at a certain time
    if boss3_time != -1:
        # Boss3_time starts when stage3_time starts
        if boss3_time >= 60000:
            all_sprites.add(boss3)
            boss3_group.add(boss3)
            boss_fight_sound.play()
            boss3_time = -1
            boss_fight = True

    # Spawn Boss4 at a certain time
    if boss4_time != -1:
        # Boss4_time starts when stage4_time starts
        if boss4_time >= 60000:
            all_sprites.add(boss4)
            boss4_group.add(boss4)
            boss_fight_sound.play()
            boss4_time = -1
            boss_fight = True

    # Spawn Boss5 at a certain time
    if boss5_time != -1:
        # Boss 5 times starts when stage 5 times starts
        if boss5_time >= 60000:
            all_sprites.add(boss5_hitbox)
            all_sprites.add(boss5_left_hitbox)
            all_sprites.add(boss5_right_hitbox)
            all_sprites.add(boss5)
            boss5_group.add(boss5)
            final_boss_fight_sound.play()
            final_boss_fight_sound.play()
            final_boss_fight_sound.play()
            boss5_time = -1
            boss_fight = True

    # Play Level Up Sound every level
    level_up_sound_time += clock.get_rawtime()
    if level_up_sound_time >= 20000 and total_level_time < 59000:
        level_up_sound.play()
        level_up_sound.play()
        level_up_sound.play()
        explosion_sound.play()
        level_up_sound_time = 0

    if total_level_time >= 60500 and not boss1.alive:
        stage2_display_delay_time += clock.get_rawtime()
        if stage2_display_delay_time >= 5000:
            stage2_level_up_sound_time += clock.get_rawtime()
            if stage2_level_up_sound_time >= 20000 and stage2_time < 59000:
                level_up_sound.play()
                level_up_sound.play()
                level_up_sound.play()
                explosion_sound.play()
                stage2_level_up_sound_time = 0

    if total_level_time >= 120500 and not boss2.alive:
        stage3_display_delay_time += clock.get_rawtime()
        if stage3_display_delay_time >= 5000:
            stage3_level_up_sound_time += clock.get_rawtime()
            if stage3_level_up_sound_time >= 20000 and stage3_time < 59000:
                level_up_sound.play()
                level_up_sound.play()
                level_up_sound.play()
                explosion_sound.play()
                stage3_level_up_sound_time = 0

    if total_level_time >= 180500 and not boss3.alive:
        stage4_display_delay_time += clock.get_rawtime()
        if stage4_display_delay_time >= 5000:
            stage4_level_up_sound_time += clock.get_rawtime()
            if stage4_level_up_sound_time >= 20000 and stage4_time < 59000:
                level_up_sound.play()
                level_up_sound.play()
                level_up_sound.play()
                explosion_sound.play()
                stage4_level_up_sound_time = 0

    if total_level_time >= 250500 and not boss4.alive:
        stage5_display_delay_time += clock.get_rawtime()
        if stage5_display_delay_time >= 5000:
            stage5_level_up_sound_time += clock.get_rawtime()
            if stage5_level_up_sound_time >= 20000 and stage5_time < 59000:
                level_up_sound.play()
                level_up_sound.play()
                level_up_sound.play()
                explosion_sound.play()
                stage5_level_up_sound_time = 0

    # Check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 50 - hit.radius
        player.ult += 0.25
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.92:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        if random.random() > 0.996:
            lifepow = ExtraLifePow(hit.rect.center)
            all_sprites.add(lifepow)
            powerups.add(lifepow)
        newmob()
        explosion_sound.play()

    # Check to see if a bullet hit Boss1
    hits = pygame.sprite.spritecollide(boss1, bullets, True, pygame.sprite.collide_circle_ratio(0.54))
    for hit in hits:
        boss1.shield -= 5
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        explosion_sound.play()

    # Check to see if a bullet hit Boss2
    hits = pygame.sprite.spritecollide(boss2, bullets, True, pygame.sprite.collide_circle_ratio(0.65))
    for hit in hits:
        boss2.shield -= 5
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        explosion_sound.play()

    # Check to see if a bullet hit Boss3
    hits = pygame.sprite.spritecollide(boss3, bullets, True, pygame.sprite.collide_circle_ratio(0.55))
    for hit in hits:
        boss3.shield -= 5
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        explosion_sound.play()

    # Check to see if a bullet hit Boss4
    hits = pygame.sprite.spritecollide(boss4, bullets, True, pygame.sprite.collide_circle_ratio(0.38))
    for hit in hits:
        boss4.shield -= 5
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        explosion_sound.play()

    # Check to see if a bullet hit Boss5 Cabin
    if not boss5_right_hitbox.alive and not boss5_left_hitbox.alive:
        hits = pygame.sprite.spritecollide(boss5_hitbox, bullets, True, pygame.sprite.collide_mask)
        for hit in hits:
            boss5.shield -= 5
            boss5_hitbox.shield -= 5
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
            explosion_sound.play()

    # Check to see if a bullet hit Boss5 left
    hits = pygame.sprite.spritecollide(boss5_left_hitbox, bullets, True, pygame.sprite.collide_mask)
    for hit in hits:
        boss5_left_hitbox.shield -= 5
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        explosion_sound.play()

    # Check to see if a bullet hit Boss5 Right
    hits = pygame.sprite.spritecollide(boss5_right_hitbox, bullets, True, pygame.sprite.collide_mask)
    for hit in hits:
        boss5_right_hitbox.shield -= 5
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        explosion_sound.play()

    # Check to see if a boss1_bullet hit the player
    if player.invincible == 0:
        hits = pygame.sprite.spritecollide(player, boss1_bullets, True)
        for hit in hits:
            player.shield -= 8
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
            explosion_sound.play()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -= 1
                player.shield = 100

    # Check to see if a Boss1 Laser hit the player
    if player.invincible == 0:
        hits = pygame.sprite.spritecollide(player, boss1_lasers, False)
        for hit in hits[0:1]:
            player.shield -= 100
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            explosion_sound.play()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.shield = 100
                player.lives -= 1

    # Check to see if a Boss3 Laser hit the player
    if player.invincible == 0:
        hits = pygame.sprite.spritecollide(player, boss3_lasers, False)
        for hit in hits[0:1]:
            player.shield -= 100
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            explosion_sound.play()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.shield = 100
                player.lives -= 1

    # Check to see if a Boss4 Laser hit the player
    if player.invincible == 0:
        hits = pygame.sprite.spritecollide(player, boss4_lasers, False, pygame.sprite.collide_mask)
        for hit in hits[0:1]:
            player.shield -= 100
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            explosion_sound.play()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.shield = 100
                player.lives -= 1

    # Check to see if a Boss5 Laser hit the player
    if player.invincible == 0:
        hits = pygame.sprite.spritecollide(player, boss5_lasers, False)
        for hit in hits[0:1]:
            player.shield -= 100
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            explosion_sound.play()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.shield = 100
                player.lives -= 1

    # Check to see if Boss1 hit the player
    if player.invincible == 0:
        hits = pygame.sprite.spritecollide(player, boss1_group, False, pygame.sprite.collide_mask)
        for hit in hits:
            player.shield -= 100
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            explosion_sound.play()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -= 1
                player.shield = 100

    # Check to see if Boss2 hit the player
    if player.invincible == 0:
        hits = pygame.sprite.spritecollide(player, boss2_group, False, pygame.sprite.collide_mask)
        for hit in hits:
            player.shield -= 100
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            explosion_sound.play()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -= 1
                player.shield = 100

    # Check to see if Boss3 hit the player
    if player.invincible == 0:
        hits = pygame.sprite.spritecollide(player, boss3_group, False, pygame.sprite.collide_mask)
        for hit in hits:
            player.shield -= 100
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            explosion_sound.play()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -= 1
                player.shield = 100

    # Check to see if Boss4 hit the player
    if player.invincible == 0:
        hits = pygame.sprite.spritecollide(player, boss4_group, False, pygame.sprite.collide_mask)
        for hit in hits:
            player.shield -= 100
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            explosion_sound.play()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -= 1
                player.shield = 100

    # Check to see if Boss5 hit the player
    if player.invincible == 0:
        hits = pygame.sprite.spritecollide(player, boss5_group, False, pygame.sprite.collide_mask)
        for hit in hits:
            player.shield -= 100
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            explosion_sound.play()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -= 1
                player.shield = 100

    # Check to see if a boss2_missile hit the player
    if player.invincible == 0:
        hits = pygame.sprite.spritecollide(player, boss2_missiles, True, pygame.sprite.collide_circle_ratio(0.75))
        for hit in hits:
            player.shield -= 50
            expl = Explosion(hit.rect.center, 'supersize')
            all_sprites.add(expl)
            explosion_sound.play()
            explosion_sound.play()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -= 1
                player.shield = 100

    # Check to see if the ult hit a mob
    hits = pygame.sprite.groupcollide(mobs, ults, True, False)
    for hit in hits:
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.8:
            explosion_sound.play()
        if random.random() > 0.15:
            newmob()

    # Check to see if a mob hit the player
    if player.invincible == 0:
        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
        for hit in hits:
            explosion_sound.play()
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
            player.shield -= hit.radius * 2
            newmob()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -= 1
                player.shield = 100

    # check to see if the player hit a powerup
    hits = pygame.sprite.spritecollide(player, powerups, True, pygame.sprite.collide_mask)
    for hit in hits:
        if hit.type == 'shield':
            player.shield += random.randrange(20, 30)
            if player.shield >= 100:
                player.shield = 100
            shield_sound.play()
        if hit.type == 'gun':
            if player.power < 4:
                player.powerup()
            gun_sound.play()
        if hit.type == 'damage':
            player.shield -= random.randrange(25, 35)
            damage_sound.play()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -= 1
                player.shield = 100
        if hit.type == 'ult':
            player.ult += random.randrange(10, 15)
            if player.ult >= 100:
                player.ult = 100
            ult_powerup_sound.play()
        if hit.type == 'heart':
            player.lives += 1
            heart_sound.play()
        if hit.type == 'bigheart':
            heart_sound.play()
            heart_sound.play()
            heart_sound.play()

    # Draw / Render
    screen.fill(black)

    # Scrolling Background
    rel_y = y % scale_background.get_rect().height
    screen.blit(scale_background, (0, rel_y - scale_background.get_rect().height))
    if rel_y < height:
        screen.blit(scale_background, (0, rel_y))
    y += 2

    all_sprites.draw(screen)

    # Levels and Bosses
    # Stage 1
    stage1_time += clock.get_rawtime()
    if boss1_time != -1:
        boss1_time += clock.get_rawtime()

    level_up(20000, 23000, stage1_time)
    level_up(40000, 43000, stage1_time)

    if 60000 <= stage1_time <= 63000:
        draw_lvl(screen, (width / 2), (height / 4), boss1_text)
        lvl_up = True

    if stage1_time >= 63500 and not boss1.alive:
        boss1_death_delay_time += clock.get_rawtime()
        if 1 < boss1_death_delay_time < 3500:
            draw_lvl(screen, (width / 2), (height / 4), boss_defeated_text)
            lvl_up = True
            player.power = 4
        if boss1_death_delay_time >= 5000:
            lvl_up = False
            boss_fight = False

            # Stage 2
            stage2_time += clock.get_rawtime()
            if boss2_time != -1:
                boss2_time += clock.get_rawtime()
            level_up(20000, 23000, stage2_time)
            level_up(40000, 43000, stage2_time)

            if 60000 <= stage2_time <= 63000:
                draw_lvl(screen, (width / 2), (height / 4), boss1_text)
                lvl_up = True

            if stage2_time > 63000 and boss2.alive:
                boss_fight = True

            if stage2_time >= 63500 and not boss2.alive:
                boss2_death_delay_time += clock.get_rawtime()
                if 1 < boss2_death_delay_time < 3500:
                    draw_lvl(screen, (width / 2), (height / 4), boss_defeated_text)
                    lvl_up = True
                    player.power = 4
                if boss2_death_delay_time >= 5000:
                    lvl_up = False
                    boss_fight = False

                    # Stage 3
                    stage3_time += clock.get_rawtime()
                    if boss3_time != -1:
                        boss3_time += clock.get_rawtime()
                    level_up(20000, 23000, stage3_time)
                    level_up(40000, 43000, stage3_time)

                    if 60000 <= stage3_time <= 63000:
                        draw_lvl(screen, (width / 2), (height / 4), boss1_text)
                        lvl_up = True

                    if stage3_time > 63000 and boss3.alive:
                        boss_fight = True

                    if stage3_time >= 63500 and not boss3.alive:
                        boss3_death_delay_time += clock.get_rawtime()
                        if 1 < boss3_death_delay_time < 3500:
                            draw_lvl(screen, (width / 2), (height / 4), boss_defeated_text)
                            lvl_up = True
                            player.power = 4
                        if boss3_death_delay_time >= 5000:
                            lvl_up = False
                            boss_fight = False

                            # Stage 4
                            stage4_time += clock.get_rawtime()
                            if boss4_time != -1:
                                boss4_time += clock.get_rawtime()
                            level_up(20000, 23000, stage4_time)
                            level_up(40000, 43000, stage4_time)

                            if 60000 <= stage4_time <= 63000:
                                draw_lvl(screen, (width / 2), (height / 4), boss1_text)
                                lvl_up = True

                            if stage4_time > 63000 and boss4.alive:
                                boss_fight = True

                            if stage4_time >= 63500 and not boss4.alive:
                                boss4_death_delay_time += clock.get_rawtime()
                                if 1 < boss4_death_delay_time < 3500:
                                    draw_lvl(screen, (width / 2), (height / 4), boss_defeated_text)
                                    lvl_up = True
                                    player.power = 4
                                if boss4_death_delay_time >= 5000:
                                    lvl_up = False
                                    boss_fight = False

                                    # Stage 5
                                    stage5_time += clock.get_rawtime()
                                    if boss5_time != -1:
                                        boss5_time += clock.get_rawtime()
                                    level_up(20000, 23000, stage5_time)
                                    level_up(40000, 43000, stage5_time)

                                    if 60000 <= stage5_time <= 63000:
                                        draw_lvl(screen, (width / 2), (height / 4), final_boss_text)
                                        lvl_up = True

                                    if stage5_time > 60000 and boss5.alive:
                                        boss_fight = True

                                    if stage5_time >= 63500 and not boss5.alive:
                                        lvl_up = True
                                        boss5_death_delay_time += clock.get_rawtime()
                                        if 1 < boss5_death_delay_time < 3500:
                                            draw_lvl(screen, (width / 2), (height / 4), boss_defeated_text)
                                        if 4000 <= boss5_death_delay_time <= 9000:
                                            draw_lvl(screen, (width / 2), (height / 4), game_complete)
                                            if you_win_sound_one_time == 0:
                                                you_win_sound.play()
                                                you_win_sound.play()
                                                you_win_sound.play()
                                                you_win_sound_one_time = -1
                                        if 5000 <= boss5_death_delay_time <= 9000:
                                            draw_lvl(screen, (width / 2), (height / 2), you_win)

                                        if boss5_death_delay_time >= 9500:
                                            player.fly_in = True
                                            if player.rect.bottom <= -100:
                                                player.rect.bottom = -100

                                                # Display High Scores
                                                lvl_up = True

                                                if high_scores_test == 0:
                                                    high_scores = []

                                                    with open('highscores.txt', 'rb') as f:
                                                        high_scores = pickle.load(f)

                                                    high_scores.append((user_name, score))
                                                    high_scores = sorted(high_scores, key=itemgetter(1), reverse=True)[:10]

                                                    with open('highscores.txt', 'wb') as f:
                                                        pickle.dump(high_scores, f)

                                                    high_scores = []

                                                    with open('highscores.txt', 'rb') as f:
                                                        high_scores = pickle.load(f)

                                                    name_only_list = [x[0] for x in high_scores]

                                                    score_only_list = [x[1] for x in high_scores]

                                                    high_scores_test = 1

                                                draw_lvl(screen, (width / 2), (height / 2), high_scores_box)

                                                for i in range(0, 10):
                                                    draw_text(screen, str(name_only_list[i]), 36, 150, (height / 4) - 25 + 45 * i, black)
                                                    draw_text(screen, '-', 36, 240, (height / 4) - 25 + 45 * i, black)
                                                    draw_text(screen, str(score_only_list[i]), 36, 265, (height / 4) - 25 + 45 * i, black)

    # Draw to Screen
    draw_text(screen, 'Score: ' + str(score), 18, 5, 5, white)
    draw_shield_bar(screen, 120, 10, player.shield)
    if player.lives < 15:
        draw_lives(screen, width - 30, 8, player.lives, player_img_mini)
    if player.lives >= 15:
        draw_lives(screen, width - 30, 8, 1, player_img_mini)
        draw_text(screen, str(player.lives) + 'x', 16, width - 60, 8, white)
    draw_text(screen, 'Ultimate: ', 18, 5, height - 26, white)
    draw_ult_bar(screen, 80, height - 19, player.ult)
    # after drawing everything flip the display
    pygame.display.flip()

pygame.quit()
