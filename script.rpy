# define images at the top of script.rpy
image kael = "images/kael.png"
image luma = "images/luma.png"
image maw = "images/maw.png"
image dungeon_bg = "images/dungeon_bg.png"
image maw_bg = "images/maw_bg.png"
image maw_final_bg = "images/maw_final_bg.png"
image red_flash = "images/red_flash.png"
image void_bg = "images/void_bg.png"
image white_fade = "images/white_fade.png"
image shiny = "images/shiny.png"
image god = "images/god.png"

transform fit_height:
    ysize config.screen_height




# Characters
define k = Character("Kael")
define l = Character("Luma")
define m = Character("The Black Maw", what_color="#990000")

# Fragmented narration function
init python:
    def fragmented(text):
        # loss_count_tracker is normal variable
        loss_count = loss_count_tracker  

        if loss_count == 0:
            return text  # normal text
        elif loss_count > 0 and loss_count <= 1:
            # Mild fragmentation
            return text.replace("the dungeon","the... dungeon").replace("Shiny","S...")
        elif loss_count > 1 and loss_count <= 2:
            # Moderate fragmentation
            return text.replace("you find","find...").replace("Kael","...").replace("glimmers","g...")
        elif loss_count > 2:
            # Severe fragmentation
            return "...shadows...lost...feathers...dark...Shinies"

# Start of game
label start:

    # Normal variables (reset every new game)
    $ day_count = 1
    $ shiny_chance = 70
    $ feathers_left = 3
    $ items_left = 2
    $ items_lost = 0
    $ loss_count_tracker = 0  # tracks items lost + feathers lost
    $ has_shiny = False

    scene black
    play sound "crow_caw.mp3"
    pause 0.5
    play sound "crow_caw.mp3"
    show shiny with fade
    "Long ago, the sun shattered, scattering its fragments - known as \"Shinies\" - across the world. These radiant shards were more than treasure: they were the lifeblood of existence, keeping the light burning and the skies alive."
    play sound "crow_caw.mp3"
    pause 0.5
    play sound "crow_caw.mp3"
    hide shiny
    "The gods decreed a cruel law:"
    play sound "crow_caw.mp3"
    pause 0.5
    play sound "crow_caw.mp3"
    show god at left with fade
    "\"{color=#999900}To preserve the light, sacrifice must be made{/color}.\""
    play sound "crow_caw.mp3"
    pause 0.5
    play sound "crow_caw.mp3"
    hide god at left
    "The Crow race was chosen as the keepers of this law, sworn to gather Shinies and offer feathers, blood, and their lives in tribute. Their wings were symbols of duty - carrying light back to the sky, but also carrying the burden of loss."
    play sound "crow_caw.mp3"
    pause 0.5
    play sound "crow_caw.mp3"
    "For centuries, the gods ruled the cycle of sacrifice, demanding offerings in exchange for the rising of the sun."
    play sound "crow_caw.mp3"
    pause 0.5
    play sound "crow_caw.mp3"
    show god at left with fade
    ""
    hide god at left
    "Among the Crows was one unlike the rest - a great collector, a Crow who had gathered more Shinies than any other. Ambitious, cunning, and relentless, he devoured Shinies meant for the gods. With each fragment he consumed, he grew stronger, darker until his body twisted into an abyssal monstrosity: {b}{color=#990000}The Black Maw{/color}{/b}."
    play sound "crow_caw.mp3"
    pause 0.5
    play sound "crow_caw.mp3"
    show maw with fade
    "When his hunger could no longer be sated, he turned his wings against the heavens. Legends say he overthrew the gods, tearing them from their thrones, feather by feather. With their power stolen, he bound the law of sacrifice to himself. From then on, every offering, every tribute, every Shiny belonged to him."
    play sound "crow_caw.mp3"
    pause 0.5
    play sound "crow_caw.mp3"
    hide maw
    show maw with fade
    "Now, it is the Black Maw - not the gods - who keeps the sun chained in shadows. And it is he who whispers the eternal command:"
    play sound "crow_caw.mp3"
    pause 0.5
    play sound "crow_caw.mp3"
    m "Sacrifices must be made… to me"
    play sound "crow_caw.mp3"
    pause 0.5
    play sound "crow_caw.mp3"
    hide maw
    show kael with fade
    "You are Kael, a survivor. Once a proud Crow, now broken. Your wings are torn, your feathers fall faster with each passing day."
    play sound "crow_caw.mp3"
    pause 0.5
    play sound "crow_caw.mp3"
    hide kael
    show luma with fade
    "Your only light is Luma, the last innocent Crow-child. His laughter reminds you of a world before shadows."
    play sound "crow_caw.mp3"
    pause 0.5
    play sound "crow_caw.mp3"
    hide luma
    "But you carry a dangerous secret. Long ago, you escaped the cult of the Black Maw, stealing a fragment of Shiny - one of the treasures that once fueled his ascension. That fragment has kept you and your son alive, but it also binds the Black Maw’s gaze to you. He will never stop hunting you until you have nothing left."
    ""
    "Welcome to the land of Noctyra."
    play sound "crow_caw.mp3"
    pause 0.5
    play sound "crow_caw.mp3"
    jump dungeon_cycle

# Dungeon Cycle
label dungeon_cycle:
    scene dungeon_bg

    play sound "dungeon_theme.mp3" loop

    $ narration = fragmented(f"Day {day_count} begins. You enter the dungeon once more...")
    "[narration]"
    $ narration = fragmented("Shadows coil, distant whispers echo, and the glow of Shinies glimmers faintly")
    "[narration]"
    ""

    $ import random
    $ shiny_found = random.randint(1,100) <= shiny_chance

    if shiny_found:
        $ has_shiny = True
        $ narration = fragmented("Luck favours you today; you find a Shiny in the depths of the dungeon.")
        "[narration]"
    else:
        $ has_shiny = False
        $ narration = fragmented("The dungeon yields nothing today; The Shinies elude you.")
        "[narration]"

        # If no shiny, 30% chance for treasure
        $ treasure_found = random.randint(1,100) <= 30
        if treasure_found:
            $ items_left += 1
            $ narration = fragmented("Among the shadows, you discover a treasure item - perhaps a fragment of old memories.")
            "[narration]"

    jump tribute_phase

# Tribute Phase
label tribute_phase:    
    scene maw_bg
    play sound "whisper.mp3" loop
    
    m "Tribute. Now."
    play sound "boss.mp3" loop
    menu:
        "Offer Shinies":
            if has_shiny:
                "You hand over the Shiny. The Maw's whispers soften, approving your offering."
                # Reduce fragmentation if possible
                if loss_count_tracker >= 1:
                    $ loss_count_tracker -= 1
                jump next_day
            else:
                "You have no Shiny to offer. Pick a different option."
                jump tribute_phase

        "Offer a Treasured Item":
            if items_left > 0:
                $ items_left -= 1
                $ items_lost += 1
                $ loss_count_tracker = items_lost + (3 - feathers_left)
                $ narration = fragmented("You drop a treasured item into the abyss. A memory fades, leaving a hollow ache.")
                "[narration]"
                jump next_day
            else:
                $ narration = fragmented("You have no items left")
                "[narration]"
                jump tribute_phase

        "Pluck Feathers":
            if feathers_left > 0:
                $ feathers_left -= 1
                $ shiny_chance = max(0, shiny_chance - 10)
                $ loss_count_tracker = items_lost + (3 - feathers_left)
                $ narration = fragmented("You pluck a feather from your wing. Pain sears through you, but the Maw is pleased.")
                "[narration]"
                jump next_day
            else:
                $ narration = fragmented("No feathers remain to sacrifice.")
                "[narration]"
                jump tribute_phase

        "Refuse the Maw":
            $ narration = fragmented("Defying the Maw is deadly...")
            "[narration]"
            jump bad_end

# Next Day Loop
label next_day:
    $ day_count += 1
    $ shiny_chance = max(0, shiny_chance - 10)

    if feathers_left == 0 and items_left == 0 and not has_shiny:
        jump major_branch
    else:
        jump dungeon_cycle

# Major Branches and Endings
label major_branch:
    scene maw_final_bg
    m "The tribute has run dry. Choose..."
    
    menu:
        "Hoard Shinies for Yourself":
            stop music
            stop sound
            jump bad_end
        "Ask Luma to Sacrifice":
            stop music
            stop sound
            jump dark_end
        "Offer Yourself Fully":
            stop music
            stop sound
            jump true_end
    
# Endings
label bad_end:
    scene red_flash
    play music "scream.mp3" loop
    "The Maw devours both you and your son. The shadows consume all."
    return

label dark_end:
    scene void_bg
    play music "darkness.mp3" loop
    l "Father... I'll do it. For you."
    "Luma fades away as the ultimate tribute. You scream, but the Maw only laughs."
    return

label true_end:
    scene white_fade
    play music "angel.mp3" loop
    "You kneel before the Maw. Feather by feather, you dissolve into nothing."
    "A single shiny drifts upward... your son's soul, freed from the Maw's grasp."
    return