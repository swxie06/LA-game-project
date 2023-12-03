# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define amy = Character("Amy")
define me = Character("Me")

transform figure_center:
    xoffset 680
    yoffset 205
    #linear 1.0 xoffset 0 yoffset 0


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg stage

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show amy wink at figure_center

    # These display lines of dialogue.

    amy "Hi."

    me "This is me."

    # This ends the game.

    return
