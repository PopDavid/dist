from classes import *
import pygame
pygame.init()
player = characters() 

if 'objects' == 'objects':
    fakard = weapon('fakard (1)', 1, 10)
    marvanykard = weapon(name='márványkard (3)', damage = 3, price=35)
    vaskard = weapon(name='vaskard (6)', damage=6, price=55)
    obszidianel = weapon(name='obszidiánél (11)', damage=11, price=170)

    fapancel = armor(name='fapáncél (1)', shield=1, price=55)
    marvanypancel = armor(name='marvanypáncél (2)', shield=2, price=105)
    vaspancel = armor(name='vaspáncél (5)', shield = 5, price=210)
    obszidianpancel = armor(name='obszidianpáncél (11)', shield = 11, price=320)

    fapajzs = shield(name='fapáncél (1)', shield=1, price=25)
    marvanypajzs = shield(name='marvanypáncél (2)', shield=2, price=55)
    vaspajzs = shield(name='vaspáncél (5)', shield = 5, price=105)
    obszidianpajzs = shield(name='vaspáncél (11)', shield = 11, price=210)

    goblin = Enemies(name='goblin', hp = 5, strength = 4,speed=2,  shield=5)
    ogre = Enemies(name='ogre', hp = 10, strength=7,speed=4,  shield=10)
    bandit = Enemies(name='bandit', hp = 7, strength= 11, speed = 5, shield=12)
    cerberus = Enemies(name='cerberus', hp = 15, strength=16, speed=3, shield=8)
    vampir = Enemies(name='vampir', hp = 20, strength=14, speed=2, shield=11)

WEAPON = [
    fakard,
    marvanykard,
    vaskard,
    obszidianel
]

ARMOR = [
    fapancel,
    marvanypancel,
    vaspancel,
    obszidianpancel
]

SHIELD = [
    fapajzs,
    marvanypajzs,
    vaspajzs,
    obszidianpajzs,
]

Cshield = [
    
]

Cweapon = [
    fakard
]

Carmor = [

]

inv = [

]

bosses = [
    'mineBoss', 
    'forestboss',
    'kazamatboss',
    'dragonlayerboss',
    'fieldboss',
    'dragon'
]

QUESTS = [
    'pénzgyűjtés fegyverre',
    'vadászat',
    'gyűjtőgetés',
    'ogrevadászat',
    'király kísérés'
]

universialquest = [
    'özvegy néni férje',
    'lovagi torna',
    'kard a kőben',
    'elaltatni a sárkányt',
    'meglopni a sárkányt'
]

Dquest = [

]

PAL = [
    'opál',
    'kapál',
    'kalimpál',
    'kalapál',
    'gyepál',
    'pálca',
    'pálinka',
    'pálma',
    'pálmafa',
    'pálfordulás',
    'pumpál',
    'nepál',
    'bepáll',
    'pipál',
    'kupál',
    'bekrepál',
    'strapál',
    'rúgkapál'
]

pal = [
    'opál',
    'kapál',
    'kalimpál',
    'kalapál',
    'gyepál',
    'pálca',
    'pálinka',
    'pálma',
    'pálmafa',
    'pálfordulás',
    'pumpál',
    'nepál',
    'bepáll',
    'pipál',
    'kupál',
    'bekrepál',
    'strapál',
    'rúgkapál'
]

OTHER = [
    'kapáll',
    'Kalmipál',
    'ordipál',
    'Páli-fordulat',
    'bekerpál',
    'cseszernyepálinka',
    'pállinka',
    'pályaudvar',
    'VONAT pályaudvar',
    'paálma',
    'pálink@',
    'kalappál'
]

other = [
    'kapáll',
    'Kalmipál',
    'ordipál',
    'Páli-fordulat',
    'bekerpál',
    'cseszernyepálinka',
    'pállinka',
    'pályaudvar',
    'VONAT pályaudvar',
    'paálma',
    'pálink@',
    'kalappál'
]

PLACE = [
    'mine',
    'mountain'
    'forest',
    'kazamata',
    'dragonlayel',
    'field',
    'city'
]

allboundle = ['gold', 'gold', 'gold', 'gold', 'gold', 'iron', 'iron', 'iron', 'iron','iron', 'coal', 'coal', 'coal', 'coal', 'coal']

goldboundle = []

ironboundle = []

coalboundle = []

if 'var' == 'var':
    indit = True
    startTime = 0
    money = 0
    endminigameplace = ''
    firstboundle = False
    firstindex = False
    secondboundle = False
    secondindex = False
    helyes = False

    nowplace = 'fightgoblin'
    destination = ' '
    hour = 6
    minute = 0
    day = 0
    Palvolt = False
    currentquest = 'király kísérés'
    lo = False
    paltovabb = True
    szorzo = 4
    WIDTH, HEIGHT = 1200, 720
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    score = 0
    orientacion = 'left'
    textFont30 = pygame.font.SysFont('Arial', 30)
    textFont20 = pygame.font.SysFont('Arial', 20)
    textFont50 = pygame.font.SysFont('Arial', 50)
    textFont100 = pygame.font.SysFont('Arial', 100)
    textFont75 = pygame.font.SysFont('Arial', 75)
    userText = ''
    meret = 1
    canmove = True
    FPS = 60
    displaystat = True
    word = ''
    mousePos = [0, 0]
    palscore = 0
    ismousepressed = False
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    rosszans = pygame.Rect(WIDTH/2, 0, WIDTH/2, HEIGHT)

    events = []

if 'pic' == 'pic':
    HERO = pygame.image.load('imgs\\hero másolata.jpg')
    BANDIT = pygame.image.load('imgs\\bandit.png')
    CERBERUS = pygame.image.load('imgs\\cerberus.png')
    DRAGON = pygame.image.load('imgs\\dragon.png')
    GOBLIN = pygame.image.load('imgs\\goblin.png')
    OGRE = pygame.image.load('imgs\\ogre.png')
    VAMPIR = pygame.image.load('imgs\\vampir.png')
    CITY = pygame.image.load('imgs\\city.png')
    SHOP = pygame.image.load('imgs\\shop.png')
    HOSPITAL = pygame.image.load('imgs\\hospital.png')
    GYM = pygame.image.load('imgs\\gym.png')
    QUESTBOARD = pygame.image.load('imgs\\questboard.png')
    GATE = pygame.image.load('imgs\\gate.png')

    HERO = pygame.transform.scale(HERO, (50, 50))
    BANDIT = pygame.transform.scale(BANDIT, (100, 100))
    CERBERUS = pygame.transform.scale(CERBERUS, (100, 100))
    DRAGON = pygame.transform.scale(DRAGON, (100, 100))
    GOBLIN = pygame.transform.scale(GOBLIN, (100, 100))
    OGRE = pygame.transform.scale(OGRE, (100, 100))
    VAMPIR = pygame.transform.scale(VAMPIR, (100, 100))
    CITY = pygame.transform.scale(CITY, (WIDTH, 720))
    SHOP = pygame.transform.scale(SHOP, (100, 75))
    SHOP.set_colorkey((255, 255 ,255))
    HOSPITAL = pygame.transform.scale(HOSPITAL, (75, 75))
    HOSPITAL.set_colorkey((254, 254 ,254))
    GYM = pygame.transform.scale(GYM, (150, 75))
    GYM.set_colorkey((255, 255, 255))
    QUESTBOARD = pygame.transform.scale(QUESTBOARD, (150, 75))
    STRENGTHPNG = pygame.transform.scale(pygame.image.load('imgs\\edzsőterem.png'), (400, 400))
    STRENGTHPNG.set_colorkey((255, 255, 255))
    AGILITYPNG = pygame.transform.scale(pygame.image.load('imgs\\traps.png'), (250, 250))
    AGILITYPNG.set_colorkey((255, 255, 255))
    SPEEDPNG = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('imgs\\track.png'), (300, 250)), 90)
    SPEEDPNG.set_colorkey((255, 255, 255))
    OLDLADY = pygame.transform.scale(pygame.image.load('imgs\\oldLady.png'), (400, 400))
    OLDLADY.set_colorkey((255, 255, 255))
    SWORDINSTONE = pygame.transform.scale(pygame.image.load('imgs\\swordInStone.png'), (400, 400))
    SWORDINSTONE.set_colorkey((255, 255, 255))
    GATE = pygame.transform.scale(GATE, (100, 100))
    GATE.set_colorkey((255, 255, 255))
    MAP = pygame.transform.scale(pygame.image.load('imgs\\map.png'), (WIDTH, HEIGHT))
    MAP.set_colorkey((255, 255, 255))
    FORESTGUI = pygame.transform.scale(pygame.image.load('imgs\\forestlogo.png'), (75, 100))
    FORESTGUI.set_colorkey((255, 255, 255))
    FIELDGUI = pygame.transform.scale(pygame.image.load('imgs\\field.png'), (150, 100))
    MINEGUI = pygame.transform.scale(pygame.image.load('imgs\\minelogo.png'), (80, 80))
    MINEGUI.set_colorkey((255, 255, 255))

    GOLD = pygame.transform.scale(pygame.image.load('imgs\\gold.png'), (150, 150))
    GOLD.set_colorkey((255, 255, 255))
    IRON = pygame.transform.scale(pygame.image.load('imgs\\iron.png'), (125, 125))
    IRON.set_colorkey((255, 255, 255))
    COAL = pygame.transform.scale(pygame.image.load('imgs\\coal.png'), (125, 125))
    COAL.set_colorkey((255, 255, 255))

    SPEAR = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('imgs\\spear.png'), (175, 175)), -45)
    SPEAR.set_colorkey((255, 255, 255))
    SPEARRECT = pygame.Rect(WIDTH-400, HEIGHT-500, 75, 75)

    FAKARD = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('imgs\\fakard.png'), (35, 140)), -140)
    MARVANYKARD = pygame.transform.scale(pygame.image.load('imgs\\marvanykard.png'), (120, 120))
    VASKARD = pygame.transform.scale(pygame.image.load('imgs\\vaskard.png'), (120, 120))
    OBOSZIDIANEL = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('imgs\\obszidianel.png'), (120, 120)), -90)
    
    FAPANCEL = pygame.transform.scale(pygame.image.load('imgs\\fapancel.png'), (125, 130))
    MARVANYPANCEL = pygame.transform.scale(pygame.image.load('imgs\\marvanypancel.png'), (125, 130))
    VASPANCEL = pygame.transform.scale(pygame.image.load('imgs\\vaspancel.png'), (125, 130))
    OBOSZIDIANPANCEL = pygame.transform.scale(pygame.image.load('imgs\\obszidianpancel.png'), (125, 130))

    FAPAJZS = pygame.transform.scale(pygame.image.load('imgs\\fapajzs.png'), (125, 130))
    MARVANYPAJZS = pygame.transform.scale(pygame.image.load('imgs\\marvanypajzs.png'), (125, 130))
    VASPAJZS = pygame.transform.scale(pygame.image.load('imgs\\vaspajzs.png'), (125, 130))
    OBOSZIDIANPAJZS = pygame.transform.scale(pygame.image.load('imgs\\obszidianpajzs.png'), (125, 130))

    GUISHOP = pygame.Rect(895, 475, 100, 75)
    GUIGYM = pygame.Rect(155, 260, 150, 75)
    GUIQUESTBOARD = pygame.Rect(155, 475, 150, 75)
    GUIGATE = pygame.Rect(WIDTH-150, (HEIGHT-75)/2, 100, 75)
    GUIHOSPITAL = pygame.Rect(800, 140, 75, 75)
    GUICITY = pygame.Rect(210/2*5, 210/2*3, 150, 90)
    GUIFOREST = pygame.Rect(100, 200, 75, 100)
    GUIFIELD = pygame.Rect(650, 600, 150, 100)
    GUIMINE = pygame.Rect(1000, 150, 80, 80)
