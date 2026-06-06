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
define f = Character("father larry")
define j = Character("james")


define audio.theme = "audio/theme.mp3"
define audio.horn = "audio/Horn.mp3"
define audio.voice = "what.mp3"

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

    # This ends the game.

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

    l "maybe you're right..."

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


    return