# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image tyler happy = im.Scale("tyler happy.png", 1920, 1080) 
image jumpsacre = im.Scale("jumpsacre.jpg", 1920, 1080)
image black = im.Scale("black.png", 1920, 1080)
# image larry = im.Scale("larry.png", 1920, 1080)
image PEC = im.Scale("pec.png", 1920, 1080)
image thevoices = im.Scale("thevoice.png", 1920, 1080)
# image terry = im.Scale("terry.png", 1920, 1080)
# image adolf jackson = im.Scale("adolf jackson.jpg", 1920, 1080)
# image father larry = im.Scale("father larry.gif", 1920, 1080)
# image james = im.Scale("james.jpg", 1920, 1080)
image bg alleyway = im.Scale("bg alleyway.jpg", 1920, 1080)
image bg room = im.Scale("bg room.jpg", 1920, 1080)


# Note: We need Background images. Define above with "= im.Scale("imagefile", 1920, 1080)" as shown.

image larry = "images/sprite/normal_larry.png"
image larry angry = "images/sprite/angry_larry.png"
image father larry = "images/sprite/normal_father_larry.png"
image terry = "images/sprite/normal_terry.png"
image adolf jackson = "images/sprite/normal_adolf.png"
image james = "images/sprite/normal_james.png"
image the creature = "images/sprite/the_creature.png"

transform move_left_and_zoom:
    xalign 0.10
    yalign 0.95
    zoom 0.75

transform move_right_and_zoom:
    xalign 0.90
    yalign 0.95
    zoom 0.75

transform center:
    xalign 0.5
    yalign 0.95
    zoom 0.75


define e = Character("Tyler")
define l = Character("Larry", image="larry", color="#D90000")
define v = Character("The Voices", color="#CFCFCF")
define t = Character("Terry", color="#64C200")  
define a = Character("Adolf Jackson", color="#C7730C")
define f = Character("Father Larry", color="#990000")
define j = Character("James", color="#E6CF00")

define audio.theme = "audio/theme.mp3"
define audio.horn = "audio/Horn.mp3"
define audio.voice = "audio/what.mp3"
define audio.snip = "audio/snip.mp3"
define audio.heehee = "audio/HeeHee.mp3"

label splashscreen :
    scene black
    with Pause(1)
     

    show larry with dissolve
    with Pause(2)
    

    hide larry with dissolve
    with Pause(1)
    
    return

# The game starts here.

label start:

    stop music fadeout 2.0

    play music theme fadein 3.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "tyler happy.png" to the images
    # directory.

    show tyler happy
    # These display lines of dialogue.

    e "You've opened my game. Prepare for the adventure of a lifetime!{p}And maybe... ballz..."
    e "Once you enter... there's no going back, only larry..."

    show tyler happy
    e "If there was a time where my ballz wouldn't be so unstoppable..."
    e "I'd say you were stoopid!"
    e "Perhapsingly..."

    scene jumpsacre
    e "A JEW!"
    e "Now you know the truth about me, and my ballz. I hope you enjoyed this game, and if you didn't... well, I don't care! I'm Tyler, and I'm unstoppable!"
    
    scene black
    v "..."
    v "......"
    v "{i}*Peenar chant*{/i}"
    v "Rise, my sword."

    scene black with dissolve
    show larry at center
    with dissolve
    l "{i}*Wakes up with an overwhelming sense of peenar*{/i}"
    l "Hm... I'm finally here..."
    
    scene thevoices
    v "Welcome, Larry. We've been waiting for you."

    scene black
    show larry at center
    l "Who are you? What is this place?"

    scene thevoices
    v "This is the realm of the voices.{w} We are the ones who guide and influence the minds of those who enter here."

    scene black 
    show larry at center
    l "Why am I here? Is there peenar to destroy?"

    scene thevoices
    v "Yes... look at them... peenars ready to be destroyed..."

    scene black 
    show larry at center
    l "Oh yeah... I see them... I will destroy them all!"

    show larry angry at center
    l "I will be the one to be the peenar menace once and for all!"
    l "I WILL DESTROY ALL PEENAR!!!"
    l "YOU CAN NOT HIDE YOUR PEENAR FROM ME!!!"

    scene black with dissolve
    show larry angry at move_left_and_zoom
    show terry at move_right_and_zoom with dissolve
    t "Hey Larry, what's going on? Why are you yelling about peenar?"
    l "Terry! I'm trying to destroy all the peenars! They're everywhere, and I can't let them win!" 
    t "I understand that you're upset, but maybe you should take a break and calm down. Yelling won't solve anything."
    l "I know, but I just can't help it! The peenars are so annoying and I want to get rid of them!"
    t "I get it, but maybe we can find a way to deal with the peenar together. Yelling won't make them go away, but maybe we can come up with a plan to handle them." 

    show larry at move_left_and_zoom with dissolve
    l "I guess you're right, Terry. Maybe we can work together to find a solution to the peenar problem."

    scene thevoices with dissolve
    v "That's the spirit, Larry. Together, we can find a way to deal with the peenar and restore peace to this realm."
    v "Maybe... just maybe..."
    v "Peenar might not be so bad after all..."

    scene black 
    show larry at center
    l "Maybe you're right..."

    scene PEC
    "PEENAR IS LIFE! PEENAR IS LOVE! PEENAR IS EVERYTHING!"
    "THERE IS NOT ENOUGH PEENAR! YOU MUST..."
    "COLLECT..."
    "ALL... THE..."

    $ renpy.music.set_volume(0.00, delay=2, channel='music')

    scene black
    play sound horn noloop
    show larry angry at move_left_and_zoom
    show terry at move_right_and_zoom
    l "PEEENAAARRRRRR!!!"
   
    $renpy.music.set_volume(1.00,delay=0, channel='music')
    t "Woah.... Larry..."

    stop music fadeout 2.0
    t "I don't know what to do."

    play sound voice noloop
    scene thevoices
    "{i}*Muffled signal*{/i}"
    
    scene black
    show terry at center
    t "What was that?"

    play music theme fadein 3.0
    t "I need to explore."
    "{i}*Terry explores the area to figure out where that noise came from*{/i}"
    "{i}*When suddenly, he hears a...*{/i}"

    scene black with dissolve
    scene bg alleyway
    show adolf jackson at center
    play sound heehee noloop
    a "HEEHEE"

    show adolf jackson at move_right_and_zoom
    show terry at move_left_and_zoom
    t "OMG! ARE YOU THE INFAMOUS ADOLF JACKSON?!"
    a "Yes, it is I. Terry, there is something I must tell you."
    t "What is it?"
    a "I know where Father Larry is hiding..."
    a "If you can find him and catch him, Larry will finally be at peace again."
    t "But Larry tried everything and couldn't find him!{p} How do you know where he is?!"
    a "Doesn't matter, do you accept my offer?"

    menu:
        a "Doesn't matter, do you accept my offer?"

        "Yes":
            jump findlarry

        "No":
            jump refuse

    label findlarry:
        t "I will find him...and end his terror once and for all!"
        a "Good, now listen intently!"
        a "Father Larry once came to me a long time ago..."

        scene black with dissolve
        "About 67 months and 69 days ago..."
        
        show father larry with dissolve
        f "I need your help, Adolf..."
        f "With a serious matter..."

        show father larry at move_left_and_zoom
        show adolf jackson at move_right_and_zoom
        play sound heehee noloop
        a "Oh my... HEHE...{w} Whatever is troubling you?"
        f "It appears my experiments aren't going too well...{w} I feared this day would come..."
        f "After all, my son. Larry!-"
        a "Oh poor little Larry, what a wonderful... child..."
        f "Yes... he is..."
        f "Regardless, I need you to help me."
        a "Of course! What do you need me to do?"
        f "You need to take Larry. Far away."
        f "Far. Far. Away."
        a "EXCUSE ME?!{p} Sorry... I got a bit excited..."
        a "I will. What are you going to do?"
        f "I will tell you this because I trust you, but you mustn't tell a soul!"
        a "Okay, I'm all peenar."
        f "I'm going to take Larry's peenar."
        a "{i}*Gasps like he's found his first kitten*{/i}"
        a "Surely not... don't joke around lad."
        f "I wish I was."
        f "I'll bring him to you."
        a "{i}*Shocked... but compliant*{/i}"
        a "I'll wait here."

        scene black
        with dissolve
        "{i}A few moments pass.{/i}"

        scene black
        scene bg room
        show larry at center
        with dissolve
        l "{i}*Sleep talking*{/i} La la la la la."

        play sound snip noloop
        l "{i}*Sleep talking*{/i} Pee... nar...."

        scene black
        f "Peenar acquired."

        scene black with dissolve
        show father larry at move_left_and_zoom
        f "Here he is, sleeping soundly.{w} Now go, please."

        show larry at center
        with dissolve
        l "{i}*Sleep talking*{/i} Shmimimimimimi..."

        show adolf jackson at move_right_and_zoom
        with dissolve
        a "Okay, where will you be?"
        f "Taiwan."

        scene black with dissolve
        "{i}*To the present*{/i}"

        scene black
        scene bg alleyway
        show adolf jackson at center
        with dissolve
        a "Taiwan."

        show adolf jackson at move_left_and_zoom
        show terry at move_right_and_zoom
        t "Oh... LADY BOY!{p}{i}*Terry jumps with joy*{/i}"

        jump after_menu
        
    label refuse:
        t "No, but I will tell Larry and he can take his revenge"
        a "Fine, but beware...{w} Lady boys are surrounding the area..."
        t "Oh... LADY BOY!{p}{i}*Terry jumps with joy*{/i}"
        jump after_menu

    label after_menu:

    scene black
    scene bg alleyway
    show adolf jackson at center
    a "Now I must leave, I can't be seen with young kittens, again."

    show adolf jackson at move_left_and_zoom
    show terry at move_right_and_zoom
    t "It has been a pleasure, Adolf Jackson."

    scene black
    play sound heehee noloop
    a "HEHEHE.... HEHE..."
    a "hehe..."
    scene bg room


    show larry at center
    with dissolve
    l "{i}*Jorking it crazy style*{/i}"

    show larry at move_right_and_zoom
    show terry at move_left_and_zoom
    t "LARRY THERE IS SOMETHING I MUST TELL YOU!"
    t "Oh my-! Sorry for interrupting."
    l "It's alright, what is it that you want to tell me?"
    t "I met with Adolf Jackson and he told me where Father Larry is hiding..."
    t "He said he's in... Taiwan..."
    l "WHAT?! I SHOULD HAVE KNOWN!"
    l "When I was a kid, he used to take me to Taiwan with Adolf Jackson... and they would..."
    t "They would?"
    l "They had a cult there led by...{w} {b}THE CREATURE.{/b}"
    l "They would steal peenars and conduct sick, twisted experiments on them."
    l "{b}THE CREATURE{/b} would host parties where the cult members would jork all their peenars together.{w} Father Larry took me to one of those parties once and... they all jorked on me..."
    t "Oh my God, Larry... I'm so sorry."
    t "WE HAVE TO GO TO TAIWAN AND TAKE YOUR REVENGE!"
    l "It would be too dangerous with just the two of us, they're too powerful."
    t "I know the perfect person we can recruit on our journey..."
    l "You don't mean..."

    scene black
    scene bg room 
    show james with fade
    l "JAMES?!"
    j "Hey, kiddo."

    scene black
    scene bg room 
    show larry at center
    l "Where... why... how?"
    l "I saw your... peenar explode."

    show larry at move_left_and_zoom
    show james at move_right_and_zoom
    with dissolve
    j "Yes, it did. Perhance..."
    j "But, when my kohai called me. I couldn't stay away."
    l "You should be....{w} PEENARLESS!"

    show larry angry at move_left_and_zoom
    l "DON'T MESS WITH ME!"
    j "It's okay, Larry. Peenarless isn't the end."
    j "IT'S MERELY THE BEGINNING! FOR I HOLD POWER BEYOND PEENAR! FOR I AM THE PEENARMASTER!"
    j "Now, Terry-chan, what's the plan?"

    show terry at center
    show larry at move_left_and_zoom
    with dissolve
    t "Taiwan."
    "{i}*Crickets*{p}...{p}*More crickets but with a splash of sus*{/i}"
    t "Lady boys."

    scene thevoices with dissolve
    v "I think we need to time skip this."
    v "Terry loves lady boys."

    scene black with dissolve
    scene bg room 
    "{i}*Fast forwarding 6 hours*{/i}"
    "Yes, Terry spoke about lady boys for 6 hours."

    show terry at center with dissolve
    t "And that's how I fell in love with Ching Chong Xiao!"

    show terry at move_left_and_zoom
    show james at center
    j "Right... so how are we getting to Taiwan? I'm hoping Daddy L is expecting us."
    j "Even after all these years..."

    show larry at move_right_and_zoom
    l "James is right. He will want us to come."
    t "This is for your peenar revenge! We have to! It doesn't matter what he will or won't do!"
    l "Yeah... I guess so... Let's go."





    # This ends the game
    return