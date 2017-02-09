import time

print "nathan garces"
time.sleep(1)
print
print "a game of meddling with the laws of physics and magic:"
time.sleep(1)
print
print "the wizard's cauldron"

result = []

#first layer

def main():
    print "you are a apprentice of the arcane arts"
    time.sleep(1)
    print
    print "customer arrives"
    time.sleep(1)
    print
    print "make something using the cauldron"
    print "cauldron is full of boiling elemental water from the well"
    choice_1 = first_ingredient()
    print
    if choice_1 == 1:
        print "souls of the dead can be faintly heard"
        dead_mans_tooth()
    elif choice_1 == 2:
        print "blue arcane runes are clustering in the cauldron"
        runic_iron()
    else:
        print "smells like nice forest and weed"
    
def first_ingredient():
    first_choice = int(input("""the ingredients are stored on various shelves
                           1:dead man's tooth
                           2:runic iron
                           3:pure leaf"""))
    return first_choice

#second layer

def dead_mans_tooth():
    choice_2 = int(input("""
                             1:void horn
                             2:emberstone
                             3:lightroot"""))
    if choice_2 == 1:
        print "cauldron groans with the darkness of the lowest depths of the underworld"
    elif choice_2 == 2:
        print "cauldron blazes brightly, strange formations resembling claws form and liquify"
    else:
        print "golden wave of energy bursts forth and shines from within the depths"
    return second_choice

def runic_iron():
    choice_2 = int(input("""
                             1:imp blood
                             2:arskarel's arcane dust
                             3:chronal etherfluid"""))
    if choice_2 == 1:
        print "blood begins to clot in lumps"
    elif choice_2 == 2:
        print "runes swirl and knit themselves into a shining cloth"
    else:
        print "strange unearthly ripples form in the cauldron"
    return second_choice

def pure_leaf():
    choice_2 = int(input("""
                             1:sickly moss
                             2:true ice
                             3:golden heart"""))
    if choice_2 == 1:
        print "mixture begins to bubble and shake violently, black veins crawl across the surface"
    elif choice_2 == 2:
        print "refreshing scent pours from the cauldron and delicate ice crystals form on the rim"
    else:
        print "a feeling of comfort and total benevolence bursts from the shining cauldron"
    return second_choice

#item chooser

def item_output():
    if choice_1 == 1:
        #dead man's tooth
        if choice_2 == 1:
            print "you douse a quartz sphere in the evil-looking fluid"
            print
            print "you made: Sphere of Evil Detection"
        elif choice_2 == 2:
            print "you dip a granite stone in and string it up with cord"
            print 
            print "you made: Amulet of Soulfire"
        else:
            print "you scoop up some of the liquid in a glass bottle"
            print
            print "you made: Vial of Undead Repellent"
            
    elif choice_1 == 2:
        #runic iron
        if choice_2 == 1:
            print "the blood forms a crimson ingot engraved with demonic swirls"
            print
            print "you made: Demon Crimsteel"
        elif choice_2 == 2:
            print "the mixture settles into a comfy, strong, and potentially powerful fabric"
            print
            print "you made: Arcanist's Weave"
        else:
            print "the cauldron spits out a strange humming bronze orb with circle markings"
            print
            print "you made: Timetinkerer's Bauble"

    else:
        #pure leaf
        if choice_2 == 1:
            print "you scoop the mixture up carefully into a ceramic bottle"
            print
            print "you made: Potion of Countercure"
        elif choice_2 == 2:
            print "A strange light blue seed floats to the top"
            print
            print "you made: Cryoflower Seed"
        else:
            print "a shining speck of light rises out of the cauldron and you catch it in a glass bottle"
            print
            print "you made: Spark of True Good"



