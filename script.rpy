# Declare characters used by this game. The color argument colorizes the
# name of the character.
define MC = Character("[name]")

# Where the pronoun Magic Happens

define fPronouns = 0
define mPronouns = 0
define nbPronouns = 0

default Their = "Their"
default their = "their"
default Theirs = "Theirs"
default theirs = "theirs"
default They = "They"
default they = "they"
default Themself = "Themself"
default themself = "themself"
default Them = "Them"
default them = "them"
default Theyre = "They're"
default theyre = "they're"
default TheyWere = "They were"
default theyWere = "they were"
default Title = "Your Highness"

$ appearance = undefined

image character = ConditionSwitch(
    "appearance == 'female'", "images/female.png",
    "appearance == 'male'", "images/male.png"
    )


screen charaselect():
    imagemap:
        idle "images/charaselect_idle.jpg"
        hover "images/charaselect_hover.jpg"

        hotspot (286, 85, 614, 991) action Jump("male")
        hotspot (1072, 118, 533, 962) action Jump("female")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg
    "INTRO GOES HERE"

    call screen charaselect()

label female:
    hide screen charaselect
    $ appearance = "female"

    show character

    "I'm quite beautiful."
    jump name

label male:
    hide screen charaselect
    $ appearance = "male"

    show character

    "I'm quite handsome."
    jump name


label name:
    "NAME INTRO SCENE GOES HERE"
    python:
        name = renpy.input("What is your name?")
        name = name.strip() or "Maine"

    "Yes, my name is [name]"

    menu:
        "Pronouns?"

        "She/Her":
            jump choice_F

        "He/Him":
            jump choice_M

        "They/Them":
            jump choice_NB

label choice_F:
    $ fPronouns = True

    "I prefer Feminine Pronouns"
    jump Intro

label choice_M:
    $ mPronouns = True

    "I prefer Masculine Pronouns"
    jump Intro

label choice_NB:
    $ nbPronouns = True

    "I prefer Neutral Pronouns"
    jump Intro

label Intro:
    "Scene Intro goes here"

    if fPronouns == True:
        $ Their = "Her"
        $ their = "her"
        $ Theirs = "Her"
        $ theirs = "her"
        $ They = "She"
        $ they = "she"
        $ Themself = "Herself"
        $ themself = "herself"
        $ Them = "Her"
        $ them = "her"
        $ Theyre = "She's"
        $ theyre = "she's"
        $ TheyWere = "She was"
        $ theyWere = "she was"
        $ title = "My Lady"

    else:
            if mPronouns == True:
                $ Their = "His"
                $ their = "his"
                $ Theirs = "His"
                $ theirs = "his"
                $ They = "He"
                $ they = "he"
                $ Themself = "Himself"
                $ themself = "himself"
                $ Them = "Him"
                $ them = "him"
                $ Theyre = "He's"
                $ theyre = "he's"
                $ TheyWere = "He was"
                $ theyWere = "he was"
                $ title = "My Lord"
            else:
                pass




    # This ends the game.

    return
