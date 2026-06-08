# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image tyler happy = im.Scale("tyler happy.png", 1920, 1080) 
image jumpsacre = im.Scale("jumpsacre.jpg", 1920, 1080)
image black = im.Scale("black.png", 1920, 1080)
image larry = im.Scale("larry.png", 1920, 1080)
image PEC = im.Scale("pec.png", 1920, 1080)
image thevoices = im.Scale("thevoice.png", 1920, 1080)
image terry = im.Scale("terry.png", 1920, 1080)
image adolf jackson = im.Scale("adolf jackson.jpg", 1920, 1080)
image father larry = im.Scale("father larry.gif", 1920, 1080)
image james = im.Scale("james.jpg", 1920, 1080)

define e = Character("Tyler")
define l = Character("Larry")
define v = Character("The Voices")
define y = Character("Terry")  
define a = Character("Adolf Jackson")
define f = Character("Father Larry")
define j = Character("James")

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

    e "You've opened my game. Prepare for the adventure of a lifetime! And maybe... ballz..."
    e "Once you enter... there's no going back, only larry..."

    show tyler happy
    e "If there was a time where my ballz wouldn't be so unstoppable..."
    e "I'd say you were stoopid!"
    e "Perhapsingly..."

    scene jumpsacre
    e "A JEW!"
    e "Now you know the truth about me, and my ballz. I hope you enjoyed this game, and if you didn't... well, I don't care! I'm Tyler, and I'm unstoppable!"
    
    scene black
    e "..."
    e "......."
    v "*peenar chant*"

    scene larry
    l "Hm... I'm finally here..."
    
    scene thevoices
    v "Welcome, Larry. We've been waiting for you."

    scene larry
    l "Who are you? What is this place?"

    scene thevoices
    v "This is the realm of the voices. We are the ones who guide and influence the minds of those who enter here."

    scene larry
    l "Why am I here? Is there peenar to destory?"

    scene thevoices
    v "Yes... look at them... peenar ready to be destroyed..."

    scene larry
    l "Oh yeah... I see them... I will destroy them all!"
    l "I will be the one to be the peenar menace once and for all!"
    l "I WILL DESTROY ALL PEENAR!!!"
    l "YOU CAN NOT HIDE YOUR PEENAR FROM ME!!!"

    scene terry
    y "Hey Larry, what's going on? Why are you yelling about peenar?"

    scene larry
    l "Terry! I'm trying to destroy all the peenar! They're everywhere, and I can't let them win!" 

    scene terry
    y "I understand that you're upset, but maybe you should take a break and calm down. Yelling won't solve anything."

    scene larry
    l "I know, but I just can't help it! The peenar are so annoying and I want to get rid of them!"

    scene terry
    y "I get it, but maybe we can find a way to deal with the peenar together. Yelling won't make them go away, but maybe we can come up with a plan to handle them."

    scene larry 
    l "I guess you're right, Terry. Maybe we can work together to find a solution to the peenar problem."

    scene thevoices
    v "That's the spirit, Larry. Together, we can find a way to deal with the peenar and restore peace to this realm."
    v "Maybe... just maybe..."
    v "Peenar might not be so bad after all..."

    scene larry
    l "Maybe you're right..."

    scene PEC
    y "PEENAR IS LIFE! PEENAR IS LOVE! PEENAR IS EVERYTHING!"
    y "THERE IS NO ENOUGH PEENAR! I MUST..."
    y "COLLECT..."
    y "ALL... THE..."

    $ renpy.music.set_volume(0.00, delay=2, channel='music')

    play sound horn noloop

    l "PEEENAAARRRRRR"
   
    $renpy.music.set_volume(1.00,delay=0, channel='music')

    scene terry
    y "Woah.... larry..."

    stop music fadeout 2.0

    y "I don't know what to do."

    play sound voice noloop
    scene thevoices

    v "*Muffled signal*"
    
    scene terry
    y "What was that?"

    play music theme fadein 3.0

    y "I need to explore."

    "Terry explores the area to figure out where that noise came from."
    "When suddenly, he hears a..."

    scene adolf jackson
    with dissolve
    play sound heehee noloop

    a "HEEHEE"

    scene terry
    y "OMG! ARE YOU THE INFAMOUS ADOLF JACKSON?!"

    scene adolf jackson
    a "Yes, it is I, Terry there is something I must tell you."

    scene terry
    y "What is it?"

    scene adolf jackson
    a "I know where father larry is hiding..."
    a "if you can find him and catch him, larry will finally be at peace again."
    
    scene terry
    y "But larry said he tried everything and couldn't find him!"
    y "How do you know where he is?!"
 

    scene adolf jackson
    a "Doesn't matter, do you accept my offer?"

    menu:
        "Yes":
            jump findlarry

        "No":
            jump refuse

    label findlarry:
        scene terry
        y "I will find him...and end his terror once and for all!"
        
        scene adolf jackson
        a "Good, now listen intently!"
        a "Father Larry once came to me a long time ago..."

        scene black
        with dissolve
        "About 67 months and 69 days ago..."
        
        scene father larry
        with dissolve
        f "I need your help Adolf..."
        f "With a serious matter..."

        scene adolf jackson
        with dissolve
        play sound heehee noloop

        a "Oh my... HEHE... whatever is troubling you?"

        scene father larry
        with dissolve
        f "It appears my experiments aren't going too well..."
        f "I feared this day would come..."
        f "After all, my son. Larry!-"

        scene adolf jackson
        a "Oh poor little Larry, what a wonderful... child..."

        scene father larry
        with dissolve
        f "Yes... he is..."
        f "Regardless, I need you to help me."

        scene adolf jackson
        with dissolve
        a "Of course! What do you need me to do?"

        scene father larry
        with dissolve
        f "You need to take Larry. Far away."
        f "Far. Far. Away."

        scene adolf jackson
        a "EXCUSE ME?!"
        a "Sorry... I got a bit excited..."
        a "I will do. What are you going to do?"

        scene father larry
        with dissolve
        f "I will tell you this because I trust you, but you mustn't tell a soul!"

        scene adolf jackson
        with dissolve
        a "Okay, I'm all peenar."

        scene father larry
        with dissolve
        f "I'm going to take Larry's peenar."

        scene adolf jackson
        with dissolve
        a "*Gasps like he's found his first kitten.*"
        a "Surely not... don't joke around."

        scene father larry
        with dissolve
        f "I wish I was."
        f "I'll bring him to you."

        scene adolf jackson
        with dissolve
        a "*Shocked... but compliant*"
        a "I'll wait here."

        scene black
        with dissolve
        "A few moments pass."

        scene larry
        with dissolve
        l "*Sleep talking* La la la la la."
        play sound snip noloop
        l "*Sleep talking* Pee... nar...."

        scene black
        with dissolve
        f "Peenar, acquired"

        scene father larry
        with dissolve
        f "Here he is, sleeping soundly. Now go, please."

        scene larry
        with dissolve
        l "*Shmimimimimi.*"

        scene adolf jackson
        with dissolve
        a "Okay, where will you be?"

        scene father larry
        with dissolve 
        f "Taiwan."

        scene black
        with dissolve
        "To the present."

        scene adolf jackson
        with dissolve
        a "Taiwan."

        scene terry
        y "Oh... LADY BOY!"
        "Terry jumps with joy."
        jump after_menu
        

    label refuse:
        scene terry
        y "No, but I will tell Larry and he can take his revenge"

        scene adolf jackson
        with dissolve
        a "Fine, but beware..."
        a "Lady boys are surrounding the area..."

        scene terry
        y "Oh... LADY BOY!"
        jump after_menu


    label after_menu:

    scene adolf jackson
    a "Now I must leave, I can't be seen with young kittens, again."

    scene terry
    y "It has been a pleasure, Adolf Jackson."

    scene black
    play sound heehee noloop
    a "HEHEHE.... HEHE..."
    a "hehe..."

    scene larry with dissolve
    l "*jorking it*"

    scene terry
    y "LARRY THERE IS SOMETHING I MUST TELL YOU!"
    y "Oh my-! Sorry for interrupting."

    scene larry
    l "It's alright, what is it that you want to tell me?"

    scene terry
    y "I met with adolf jackson and he told me where father larry is hiding..."
    y "He said he's in...taiwan..."

    scene larry
    l "WHAT?! I SHOULD HAVE KNOWN!"
    l "When i was a kid, he used to take me to taiwan with adolf jackson...and they would..."

    scene terry
    y "They would ?"

    scene larry
    l "They had a cult there led by...THE CREATURE."
    l "They would steal peenars and conduct sick and twisted experiments on them."
    l "The creature would also host parties where the cult members would all jork their peenars together. Father larry took me to one of those parties once and...they all jorked on me..."

    scene terry
    y "Oh my god, larry...I'm so sorry."
    y "WE HAVE TO GO TO TAIWAN AND TAKE YOUR REVENGE!"

    scene larry
    l "It would be too dangerous with just the two of us, they're too powerfull."

    scene terry
    y "I know the perfect person we can recruit on our journey..."

    scene larry
    l "You don't mean..."

    scene james with fade
    l "JAMES ?!"
    
 



    # This ends the game
    return