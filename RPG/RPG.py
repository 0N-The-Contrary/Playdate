# define all functions 
import random

# MC stats. 
hp = int(100)
max_hp = int(100)
defense = int(0)
attack_dmg = int(0)
item_list = []
lvl = int(1)
#add speed stats, if you're faster, you attack first

#blah blah stats so the program can work 
enemy_atk_dmg = int(0)
enemy_hp = int(1)
enemy_defense = int(0)
current_enemy = ""
enemy_attack = ""
cleave_cooldown = int(0)
choice = ""
kill_count = int(0)
spare_count = int(0)

combat_options = ["attack", "item", "flee"]

# generate random enemy for encounter
def gen_enemy():
    global current_enemy
    global enemy_hp
    global enemy_defense
    current_enemy = random.choice(["Goblin", "Skeleton", "Hermit"])
    print(f"You are fighting a {current_enemy}!")

    #enemy hp's
    if current_enemy == "Goblin":
         enemy_hp = int(50)
         enemy_defense = int(5)
    if current_enemy == "Skeleton":
         enemy_hp = int(30)
         enemy_defense = int(3)
    if current_enemy == "Hermit":
         enemy_hp = int(25)
         enemy_defense = int(10)
    
    return current_enemy


def dmg_given():
     global hp
     global enemy_hp
     global current_enemy
     global attack_dmg
     global enemy_defense
     print(f"It would normally do {attack_dmg} damage!")
     print(f"However, since {current_enemy} has {enemy_defense} defense...")
     attack_dmg = attack_dmg - enemy_defense
     print(f"It does {attack_dmg} damage!")
     enemy_hp -= attack_dmg 
     print(f"the {current_enemy} now has {enemy_hp} hp!")
     if enemy_hp <= int(0):
         print(f"The {current_enemy} has died!")

     print(f"You have {hp} hp!")
     

# enemy attacks
def gen_enemy_attack():
     global enemy_attack
     global enemy_atk_dmg
     if current_enemy == "Goblin":
        Goblin_attacks = ["club_swing", "swipe"]
        enemy_attack = random.choice(Goblin_attacks)
    
        if enemy_attack == "swipe":
           enemy_atk_dmg = int(3)

        if enemy_attack == "club_swing":
            enemy_atk_dmg = int(5)

     if current_enemy == "Skeleton":
         Skeleton_attacks = ["funny_bone", "claw"]
         enemy_attack = random.choice (Skeleton_attacks)
         if enemy_attack == "funny_bone":
              enemy_atk_dmg = int(10)
              
              
         if enemy_attack == "claw":
              enemy_atk_dmg = int(5)
              

     if current_enemy == "Hermit":
         Hermit_attacks = ["shell_shock", "bash"]
         enemy_attack = random.choice (Hermit_attacks)
         if enemy_attack == "shell_shock":
              enemy_atk_dmg = int(3)
         if enemy_attack == "bash":
              enemy_atk_dmg = int(2)
     dmg_taken()
     

# make one overall function for all enemy atacks, optionally. 
     

# receiving dmg from enemies

def dmg_taken():
    global enemy_atk_dmg
    global hp
    global current_enemy
    print(f"{current_enemy} uses {enemy_attack}!")
    print(f"It would normally do {enemy_atk_dmg} damage! However, since your defense is {defense}...")
    print(f"it does {enemy_atk_dmg - defense} damage!") 
    hp = hp - (enemy_atk_dmg - defense)
    print(f"You now have {hp} hp!")
    print(f"{current_enemy} has {enemy_hp} hp!")
    if hp <= int(0):
      print("You lost :(")
      print("Maybe you'll have better luck next time, and take a break if needed!")

    


def combat():
 global attack_dmg
 global cleave_cooldown
 global combat_options
 if cleave_cooldown >= int(1):
     cleave_cooldown -= int(1)
 attack_menu = ["slash", "cleave"]
 action = input(f"What would you like to do? {combat_options} ")

 if action == "attack":
     print(attack_menu)
     attack = input("Here are your attacks, please type which attack you'd like to do: ")
     if attack == "slash":
         attack_dmg = int(15)
         dmg_given()
     if attack == "cleave":
         if cleave_cooldown >= int(1):
             attack_dmg = int(0)
             print("You can't use that move yet")
             cleave_cooldown = int(0)
         if cleave_cooldown <= int(0):
              attack_dmg = int(30)

         print("you must wait one turn before executing that move again")
         dmg_given()


 if action == "item":
     print(f"Here are your items: ", (item_list))
     if item_list == []:
        print("You have no items")


 if action == "flee":
      print("Sorry, no scaredy cats allowed")
      combat_options.remove("flee")
 # remove "flee" as an option lol

 if enemy_hp > int(0):
     gen_enemy_attack()
    
#add item drops and expand on items like health potion for 20hp
def combat_end():
    global current_enemy
    global hp
    print("You won!")
    if current_enemy == "Goblin":
        hp += int(5)
        print("You gained 5hp!")
    if current_enemy == "Skeleton":
        hp += int(10)
        print("You gained 10hp!")
    if current_enemy == "Hermit":
        hp += int(15)
        print("You gained 15hp!")
    if hp > max_hp:
        hp = max_hp
        print("You have exceeded your max hp!")
    print(f"You now have {hp} hp!")

def post_combat():
    global choice
    global kill_count
    global spare_count
    print("You now have a choice to make...")
    choice = input("What would you like to do? (kill or spare) ")
    if choice == "kill":
        kill_count += int(1)
    if choice == "spare":
        spare_count += int(1)

#Get user name and state it
Name = input("What would you like your name to be? ")
print(Name + ", huh? Alright then, let's get started...")

#intro story
print(" *drip*, *drop*, *drip*, drop*")
print( "A looming silhouette, illuminated by a beam of light behind it, stands in the entrance to a small, shallow, and damp cave.") 
print("Inside the cave, there lay a starving mother, and a young child by the name of " + Name + ".")
print("The mother is begging the silhouette, 'Please, I beg of you, don't take my child away from me. I'll do anything!'")
print("The mother continues, 'You can have all of my money!, all of my food!, Everything! Please, just let me and my child stay together'")
print("The mother asks one final cry, 'Please just let us stay, let just us go.. please.'")
print("The silhouette, unmoving for a moment, its chest heaves, and it takes a step forward, and another, and another.")
print("The silhouette stands in front of the kneeling mother, looks down at her, then at the child just a couple feet away, then back at the mother.")
print("The silhouette lifts a scythe, its arm in front of its face, and at its apex, the blade, seemingly made of shadows, glistens in the light, and the silhouette pauses for a short moment.")
print("Then, the silhouette swings the scythe, the mother shrieks, and as her decapitated body falls onto her side, the child screams, breaking the ice of terror that drowned out the child.")
print("The child begs the silhouette, to be taken with their mother, and the silhouette stares down at the child...")
print("The silhouette stays still for a moment, it looks like he pities the child, but the silhouette doesn't honor the child's request, nor the mother's dying wish.")
print("The silhouette turns around, and walks out of the cave, each step deliberate, and echiong off the cave walls.")
print("The child screams and cries to the silhouette, but it falls on deaf ears, and the silhouete ducks through the archway of the cave, and fades into the light.")
print("The child, " + Name + ", is left alone in the cave, with their mother's body, cold, hungry, scared, and alone.")

#present time 
print("\n")
print(Name + " is now a young adult, and have been given the title of a Death; they now kneel in front of a giant on a pearly white throne with golden accents, in a massive white marble temple")
print(Name + " is presenting to the giant in the throne, known as God, a dark brown burlap sack, filled with the souls of the dead, and the giant God is looking down at " + Name + ", and says, "
"'You have done well, " + Name + ", here's the list of the next souls to be collected and their locations. '")
print(Name + " takes the list, and puts it into their pocket, and says, 'Thank you, God, I will do my best to collect these souls.', and God replies, 'I know you will, " + Name + ",'")
print(Name + " ties the sack around the side of their waist, and leaves the temple to begin their next collection of souls.")
print(Name + " begins to walk across the apocalyptic, decrepit, and desolate land, where ruin surrounds all, and the only thing that can be heard is the occasional wind blowing through the ruins.")
print("Human population is scarce, survival is a struggle for all who remain, the only ones who live are those that are strong enough and lucky enough to have successful scavenges")
print("All except for the Deaths and God, who have been tortured with the curse of immortality, albeit they can only be killed by eachother, they're also the only ones who can interact with the souls of the dead")
print("God judges what to do with a soul based on the kindness of their heart, and when he's not judging souls, he's working on something in an attempt to rebuild humanity; but he needs the souls to do it, " \
"thus, he has Deaths collect them for him.")

#background of Deaths
print("\n")
print("As a Death, " + Name + " has been tasked with killing the people who's hourglasses have run out, collecting their souls in " + Name + "'s bag, and delivering them to God.")
print("The exact number of Deaths is unknown, but they are a small and tortured few.")
print("The duty of Death is given as the ultimate punishment that God gives to exclusively the most horrendous souls, except for " + Name + "...")
print("God was originally going to punish the previous Death, for sparing the life of a soul in a damp cave, however, after the Death had killed himself in grief, " \
"God took his wrath out on the next soul apart of the situation, that being " + Name + ", blaming them for persuading the Death, and thus, made " + Name + " a Death")
print("Deaths have a distinguished look, they are unmistakable, and you can feel the aura of despair around them, even when they simply pass by your neighborhood.")

#first collection
print("\n")
print(Name + " is walking through cobbled ruins, and against a corner of a building, they see a man, tattered and ripped clothes, ungroomed for months") 
print("and as " + Name + " stands in front of the man, he looks up, fearful of whats to come, but willingly not moving, at " + Name + "'s mercy.")
print("You are armed with a scythe of shadows, in a black shadowy cloak, an empty burlap sack of souls, and the knowledge that this man is first on your list of souls to collect.")
print("Your scythe raises, the man winces, and your scythe slices through the air, and the man's chest. ")
print("The man touches his hand to the gash that stretches across his chest, and he looks down at the blood that is now on his hand, and he looks up at you.")
print("He looks like he wants to say something, but the breath leaves him, and the light leaves his eyes, the kind of light that you don't even notice until they're on the brink of death.")
print("He was simply another one towards the  of collected souls, there have been countless before him and there'll be plenty more after him")
print(Name + "collects the soul of the man, puts it into the sack, ties it up again, and journeys to the second soul on the list")

#First combat encounter buildup
print("\n")
print(Name + " approaches the second on the list, a relatively bulky-looking man by the name of John, John felt the Deaths presence, and turned around to face you as you approach")
print("John stands in front of his relatively well-maintained and pristine barn")
print("However, he doesn't cower like most pepole, he's one of the less common folk who close their hands, put them by their face, and widen their stance")
print("You stop before the man, you and him know what's about to happen.")
print("There is a No Man's Land of sorts between you both, meaning neither of you can reach each other without closing the distance")
print("\n")


# Combat Start 
gen_enemy()
while enemy_hp > int(0):
    combat()
combat_end()

# Post Combat
print("\n")
print("As your latest slice spills the man's blood onto the floor, he falls backwards, following with the motion of your scythe.")
print("He can only lay back, one hand on the ground, the other up to the air, with his open palm facing your head.")
print("He says 'Okay!, okay. You win!")
print("You take a step forward, so now he's back within your range")
print("'Please man, this farms all I got left!'")
print("\n")

post_combat()

print("\n")
if choice == "kill":
    print("Death has no exceptions, and it must come for you all")
    print("You raise your scythe up, and just as quickly slice it through the man, ending him quick")
if choice == "spare":
    print("Death musn't be so cruel")
    print("You continue eye contact for a silent moment")
    print("You outstretch your open hand, to which he takes as you help him up")
    print("The man thanks you and runs into the farm before he can ask any questions, and before you could change your mind.")

print("No matter, time's arrow marches on")
print("You start headed to the next in line")


    
# Notes for future game design ideas:
# Have the player roll different die like DnD for stuff like initiative, and rng will alerady be a thing for loot drop like Skulls 

# notes for art ideas
# pixelated like OG final fantasies
# A future death, burly guy, should have their soul collecting bag be a still person wrapped in burial clothes on their back
# want to change soul collecting sack for MC, could do a glass lantern with a skull in the middle, where the more souls you get, 
    # the more that the eyes and cheeks glow, like there is a fire inside the skull that burns brighter based on your souls. Three sprites, unlit, lit or half lit, fire coming out. 


# notes for future quotes:
# When MC about to kill someone: 'Please, I beg of you, don't take me away from my family. I have a wife and two children, please let me stay with them.'")

# future COMBAT ideas: first action stuff, where like if your first action is attack, you get a 10% bonus dmg if you're going the genocide route

# First_action = input("What would you like to do? (attack, item, flee) ")
# if First_action == "attack":
 #   First_attack = attack = input(print(attack_menu))
 #   if First_attack == attack == "Slash":
 #        dmg_given
# if First_action == "item":
#     print("You have no items")

# Give "attacks" that increase stats to both enemies and player, like you could do a 5 dmg slice that buffs your strength by maybe 10?
# Or an enemy, like the Hermit, to shell up and increase his defense by like 5 or something. 
# if strength >= 5:     attack_dmg = attack_dmg + 5
# if lvl <= int(5):
#     ammend "windmill" into attack_menu
#     windmill = int(20)

# give xp after an encounter, but also want the amount of xp given to scale off how long the combat went on for (How many times combat looped before enemy_hp = int(0)
 # Also scale off how much damage was exchanged between player and enemy
 # Could hardset the numbers, for example - end of the combat function, turn +=1 - then during the combat_end function, if turn >= int(5):    xp = int(15)
 # However this would also make leveling up a linear system, rather than exponential; but you could also have lvl goal posts further away
 # and itd make it easier and simpler for player. So I think it's actually better that way. 

# Give enemies bigger moves that require cooldowns of their own, such as the player' s "Cleave" move.

# could allow for one final attack allowed after you die, so you essentially get one more turn after your hp <= 0
 # call it "One final attack / move, from beyond the grave! (You are a Death, after all.")
 # Could limit it to just one attack, or maybe allow items so they can heal, then get hit, and teeter on the edge of death itself, as one who's job it is to control death. 
 # yk since we called calculators the people who used calculators back in NASA Apollo 1 days, so thus, the people who control death are called Deaths themselves. 

# Have boss enemy make all your abilities have higher cooldowns / take an extra turn before you can use that move again. Would be annoying, but fun to try. 
# Having boss that when you see the horror of God's tortured-soul-powered energy machine, it makes you nauseous, giving you a status debuff for the first section of the fight
 # During this section, your moves may not come out the way you wanted, meaning you may input "Cleave" but you actually end up doing "slash"
 # This is the whole reason behind the test ""...please type which attack YOU'D LIKE to do: ")", and not "...which attack YOU WILL do"
 # Foreshadowing! :D

# if try to run during boss fight, print("you must face your fears eventually")
# if try to flee during God fight, print("It's too late to turn back now") 

