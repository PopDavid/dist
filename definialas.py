from variables import *


Eweapon = ['', 0]
EShield = ['', 0]
Earmor = ['', 0]

def getItem(type, item):
    global Eweapon, EShield, Earmor, money

    match type:
        case 'weapon':
            if item in Cweapon:
                money += item.price
            else:
                Cweapon.append(item)

        case 'armor':
            if item in Carmor:
                money += item.price
            else:

                Carmor.append(item)
        case 'shield':
            if item in Cshield:
                money += item.price
            else:
                Cshield.append(item)

def DrawText(text, font, color, x, y):
    img = font.render(text, True, color)
    WIN.blit(img, (x, y))

