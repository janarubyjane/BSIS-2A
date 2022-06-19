# Members: Padasas, Jeannah Jean S. & Porras, Ma. Alexia Louise     Section:  BSIS - 2AB 

import os
from time import sleep

class Character_Class:

    def __init__(self, character: str, weapon: str, ablty1: str, ablty2: str):
        self.character = character
        self.weapon = weapon
        self.ablty1 = ablty1
        self.ablty2 = ablty2

def CharacterChoices():
    print("[1] - Wizard")
    print("[2] - Knight")
    print("[3] - Archer")
    print("[4] - Assassin")

def print_Weapons():
    print("[1] - Wizard Staff")
    print("[2] - Sword")
    print("[3] - Bow & Arrow")
    print("[4] - Katarr")

def print_WizardAbilities():
    print("[1] - Energy Ball")
    print("[2] - Dragons Breath")
    print("[3] - Crown of Flame")
    print("[4] - Hail Storm")

def print_KnightAbilities():
    print("[1] - Fire Slash")
    print("[2] - Power Slash")
    print("[3] - Gigantic Storm")
    print("[4] - Chaotic Disaster")

def print_ArcherAbilities():
    print("[1] - Take Aim")
    print("[2] - Quick Shot")
    print("[3] - Blazing Arrow")
    print("[4] - Frost Arrow")

def print_AssasinAbilities():
    print("[1] - Cloaking")
    print("[2] - Enchant Poison")
    print("[3] - Sonic Acceleration")
    print("[4] - Meteor Assault")


def CharacterType(num: int):

    if num == 1:
        char = "Wizard"
    elif num == 2:
        char = "Knight"
    elif num == 3:
        char = "Archer"
    else:
        char = "Assassin"
    return char

def WeaponType(num: int):

    if num == 1:
        char = "Wizard Staff"
    elif num == 2:
        char = "Sword"
    elif num == 3:
        char = "Bow & Arrow"
    else:
        char = "Katar"
    return char


def WizardAbility(num):

    if num == 1:
        char = "Energy Ball"
    elif num == 2:
        char = "Dragons Breath"
    elif num == 3:
        char = "Crown of Flame"
    else:
        char = "Hail Storm"
    return char

def KnightAbility(num):

    if num == 1:
        char = "Fire Slash"
    elif num == 2:
        char = "Power Slash"
    elif num == 3:
        char = "Gigantic Storm"
    else:
        char = "Chaotic Disaster"
    return char

def ArcherAbility(num):

    if num == 1:
        char = "Take Aim"
    elif num == 2:
        char = "Quick Shot"
    elif num == 3:
        char = "Blazing Arrow"
    else:
        char = "Frost Arrow"
    return char

def AAssassinAbility(num):

    if num == 1:
        char = "Cloaking"
    elif num == 2:
        char = "Enchant Poison"
    elif num == 3:
        char = "Sonic Acceleration"
    else:
        char = "Meteor Assault"
    return char


def SetCharacter():
    i = 1
    
    while i <= 2:
        if i == 1:
            os.system('cls') 
            print("\nPLEASE CUSTOMIZE YOUR FIRST CHARACTER\n")

        else: 
            os.system('cls') 
            print("\nPLEASE CUSTOMIZE YOUR SECOND CHARACTER\n")

        CharacterChoices()
        Character =  int(input("\nSelect your Character: "))
        if Character > 4:
            print("Invalid input")
            sleep(1)
            os.system('cls')
            continue
        Character = CharacterType(Character)
        print(Character + "\n")


        print_Weapons()
        Weapon = int(input("\nSelect your Weapon: "))
        if Weapon > 4:
            print("Invalid input")
            sleep(1)
            os.system('cls')
            continue
        Weapon = WeaponType(Weapon)
        print(Weapon + "\n")
       

        if Character == "Wizard":
            
            print("\nPLEASE CUSTOMIZE YOUR WIZARD ABILITY\n")
            print_WizardAbilities()
            ablty1 = int(input("\nSelect your First Ability: "))
            if ablty1 > 4:
                print("Invalid input")
                sleep(1)
                os.system('cls')
                continue
            ablty1 = WizardAbility(ablty1)
            print(ablty1 + "\n")

            print_WizardAbilities()
            ablty2 = int(input("\nSelect your Second ability: "))
            if ablty2 > 4:
                print("Invalid input")
                sleep(1)
                os.system('cls')
                continue
            ablty2 = WizardAbility(ablty2)
            print(ablty2)
        
        elif Character == "Knight":
            
            print("\nPLEASE CUSTOMIZE YOUR KNIGHT ABILITY\n")
            print_KnightAbilities()
            ablty1 = int(input("\nSelect your First Ability: "))
            if ablty1 > 4:
                print("Invalid input")
                sleep(1)
                os.system('cls')
                continue
            ablty1 = KnightAbility(ablty1)
            print(ablty1 + "\n")
            
            print_KnightAbilities()
            ablty2 = int(input("\nSelect your Second ability: "))
            if ablty2 > 4:
                print("Invalid input")
                sleep(1)
                os.system('cls')
                continue
            ablty2 = KnightAbility(ablty2)
            print(ablty2)
        
        elif Character == "Archer":

            print("\nPLEASE CUSTOMIZE YOUR ARCHER ABILITY\n")
            print_ArcherAbilities()
            ablty1 = int(input("\nSelect your First Ability: "))
            if ablty1 > 4:
                print("Invalid input")
                sleep(1)
                os.system('cls')
                continue
            ablty1 = ArcherAbility(ablty1)
            print(ablty1 + "\n")

            print_ArcherAbilities()
            ablty2 = int(input("\nSelect your Second ability: "))
            if ablty2 > 4:
                print("Invalid input")
                sleep(1)
                os.system('cls')
                continue
            ablty2 = ArcherAbility(ablty2)
            print(ablty2)

        else: 
            print("\nPLEASE CUSTOMIZE YOUR ASSASSIN ABILITY\n")
            print_AssasinAbilities()
            ablty1 = int(input("\nSelect your First Ability: "))
            if ablty1 > 4:
                print("Invalid input")
                sleep(1)
                os.system('cls')
                continue
            ablty1 = AAssassinAbility(ablty1)
            print(ablty1 + "\n")

            print_AssasinAbilities()
            ablty2 = int(input("\nSelect your Second ability: "))
            if ablty2 > 4:
                print("Invalid input")
                sleep(1)
                os.system('cls')
                continue
            ablty2 = AAssassinAbility(ablty2)
            print(ablty2)
    
        if i == 1:
            Character1 = Character_Class(Character, Weapon, ablty1, ablty2)      
        else:
            Character2 = Character_Class(Character, Weapon, ablty1, ablty2)
        i += 1
    
    os.system('cls')
    print("\n\nFIRST CHARACTER ATTRIBUTES\n")
    print("Class: " + Character1.character)
    print("Weapon: " + Character1.weapon)
    print("First Ability: " + Character1.ablty1)
    print("Second Ability: " + Character1.ablty2 + "\n")

    print("\nSECOND CHARACTER ATTRIBUTES\n")
    print("Class: " + Character2.character)
    print("Weapon: " + Character2.weapon)
    print("First Ability: " + Character2.ablty1)
    print("Second Ability: " + Character2.ablty2 + "\n")

SetCharacter()