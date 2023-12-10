# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define amy = Character("Amy")
define me = Character("Aaron")
define mom = Character("Mom")
define f = Character("Friend")

default refuse = True
default agree = True

image black = Solid("#000")

transform figure_center:
    xalign 0.5
    yoffset 208
    #linear 1.0 xoffset 0 yoffset 0


# The game starts here.
label start:
    
    # jump test # For debug

    scene black

    mom "Aaron! Aaron! Mom and Dad are going out for a while. "
    mom "Remember to eat breakfast when you get up. Enjoy your weekend!"

    # Effect: *Main character's point of view, eyes opening with blurring effect, the room gradually appears

    scene bg room # replace this with above
    with dissolve

    me "Mom, please! It's been a whole week of school, and I have the right to sleep in!"
    me "(*Grumbles*) Telling me to enjoy the weekend while waking me up at nine..."
    me "......"
    me "Well, it's finally the weekend and I have no plan for today. What shall I do to have fun?"
    me "Anyway, let's see what's new on MeTube."

    #(CG: cell phone screen)
    show phone:
        xalign 0.5
        yoffset 1080
        easeout 1.5 yoffset 50
    pause

    me "What's this? Idol Amy's first anniversary performance......?"
    me "(*Taps*)"
    hide phone
    with dissolve

    scene bg stage
    with dissolve

    show silhouette 1:
        xalign 0.5
        yoffset 600
        zoom 1.0
    with dissolve
    pause 1.0
    hide silhouette
    with dissolve
    pause 0.3

    show silhouette 2:
        xalign 0.6
        yoffset 480
        zoom 0.9
    with dissolve
    pause 1.0
    hide silhouette
    with dissolve
    pause 0.3

    show silhouette 3:
        xalign 0.4
        yoffset 350
        zoom 2.0
    with dissolve
    pause 1.0
    hide silhouette
    with dissolve
    pause 0.3

    show amy normal at figure_center:
        zoom 0.3
    with dissolve

    amy "Hi everyone! Thank you all for coming today!"

    show amy wink at figure_center:
        zoom 0.3
    amy "(*Winks*)"
    hide amy
    with dissolve

    scene bg room
    with dissolve
    show phone:
        xalign 0.5
        yoffset 50

    me "(*Humming*) That's nice! Feels like I'm lifted up. Why not check out her other shows?"

    #(optional CG: screen scrolling or similar effect)
    #(optional CG: Amy's other performances)
        
    show phone:
        xalign 0.5
        yoffset 50
        easein 1.5 yoffset 1080
    pause 2.0

    show amy wink at figure_center:
        zoom 0.3
        alpha 0.7
    with dissolve
    pause
    
    me "Got a weird feeling......"

    menu:
        me "Got a weird feeling......"
        
        # I tried shortening the choices to make it flow better

        "I like her music":
            me "Is this what it's like to be a fan? I've never been one before."
            me "Her songs are pretty good. Perhaps I'll listen more when I have time."
            hide amy
            jump end1

        "I feel a connection with her":
            me "Why do I feel as if I'm getting to know her? We're not even in contact!"
            me "I don't know how, but when I watch her videos, I feel like she's talking to me while holding my hands."
            me "I feel so close to her that I can't help but keep watching."
            hide amy
            jump conversation

label end1:

    "{b}END: Parasocial Relationship VS Fandom Culture{/b}"

    "{i}Although they may overlap, they are not exactly equal. While the former emphasizes the relationship between the followed and the follower, the latter deals more broadly with the appreciation of a celebrity's personality or work.{/i}"
    "{i}Taken together, in the modern context parasocial relationships are an offshoot of fandom culture, embodying the behaviors and attitudes of followers who are deeply invested in a one-sided relationship,{/i}"
    "{i}but many followers also choose not to enter into this level of relationship. Overall, parasocial relationships offer more of a sense of spiritual intimacy.{/i}"
    
    return

label conversation:

    scene bg school

    show friend unhappy at figure_center:
        zoom 0.3
    f "Bro, you seem to be obsessed with that idol named Amy lately, don't you?"
    f "You're so focused on her that you don't even come to our basketball games anymore."
    f "Nor have you showed up at the Rock n' Roll club."
    f "Seems like she's more of a close friend to you than we are, huh?"

    me "(*Slightly embarrased*)"

    show friend smile at figure_center:
        zoom 0.3
    f "Never mind. I'm just saying that off the top of my head haha..."
    f "I know she's pretty cute man, but shouldn't you care about the other parts of life too?"

    menu:
        f "I know she's pretty cute man, but shouldn't you care about the other parts of life too?"
        "You don't know about her":
            me "You're saying that 'cause you don't know how great Amy is!"
            show friend unhappy at figure_center:
                zoom 0.3
            me "Go watch her show or let's just not talk about this."
            $ reflect = False
        "Never thought that way":
            me "Well, I've never thought about it that way......"
            $ reflect = True
            
    jump after_convo

label after_convo:

    scene bg room

    me "Another week of classes...... Haven't seen Amy the last couple days with all the homework."
    me "I'm getting a bit tired of watching shows. How can I get to know her deeper and better?"
    me "\"Amy's Interpersonal Mindset Revealed - What is Amy's Advice on Love?\""
    me "Hmm, sounds interesting! I haven't really read many of Amy's interviews. "
    me "Since I'm kind of bothered by these questions lately, let's see what Amy has to say."
    me "I expect a heart-to-heart chat with you, Amy."

    #( optional CG：Here maybe make an option for the player to choose to click into the video, and when they do, do shaking effects or something, and then Amy's image appears. I'm a bit afraid it's too boring to be all text)

    scene bg interview
    show amy interview at figure_center:
        zoom 0.3

    amy "There are a lot of fans and friends who struggle a lot with getting along with people, and I'm the same..."

    amy "My ideal intimacy and love should be..."

    with fade

    amy "Anyway, everyone has a different idea of what love is like."
    me "I can't believe she thinks this way..."

    menu:
        me "I can't believe she thinks this way..."

        "It makes so much sense!":
            $ agree = True
            
        "It doesn't make any sense!":
            $ agree = False

    if reflect:
        jump reflect
    else:
        jump refuse

label reflect:
    if agree:
        me "I told you I wasn't wrong about Amy. "
        me "She's really a genuine and sensible person, I can learn a lot from her!"

        me "I know she's saying this to countless fans, not just me, but I feel especially close to her in terms of feelings and thoughts. "
        me "Might as well just take her words as advice from a good friend."

        jump after

    else:
        me "Although I liked Amy so much, I can't agree with her on this perspective."
        me "Now I don't even know what to do with my love for her..."

        menu:
            me "Now I don't even know what to do with my love for her..."

            "Maybe it doesn't hurt that much......":
                me "Whatever! I was drawn to her because of her talent and the uplift she brought, not because her ideas were exactly the same as mine."
                jump after

            "Fine, we're done!":
                "Since our views are so different in principle, I can't see the point to love her anymore."  
                jump after



label refuse:
    scene bg school

    show friend smile at figure_center:
        zoom 0.3
    f "Hey, Aaron!"

    me "What- Oh, it's you."

    f "You've been in a trance lately, and it's getting harder and harder for us to get a chance to talk to you."
    f "How's everything going? What about the idol?"

    if agree:
        me "I watched Amy's interview expressing her views on love and companionship. It really resonated with me and made me think."
        me "From the moment I watched the interview, I've been feeling like she's that special person in my life."
        
        show friend unhappy at figure_center:
            zoom 0.3
        f "Oh! But she is an idol and she doesn't even know you!"
        f "Your admiration is one-sided, and you can't really be with Amy. Are you sure you're gonna stick to this?"

        me "No, I'm not looking for anyone else."
        me "That interview made me realize that Amy gave me a unique sense of security that nobody else in the world could match."
        
        "{b}END: Sustainable Imagination and Intimacy{/b}"

        "{i}Aaron's emotional attachment to Amy is not just a fascination, but a deep spiritual resonance, a fictionalized adoration. He sees her not only as his idol, but as his dream partner.{/i}"
        "{i}This one-way emotional connection, though born of distant observation and fantasy, forges a flawless love in Aaron's heart.{/i}"
        "{i}This one-way emotional attachment, though based on fiction, builds an emotional sanctuary in Aaron's heart where Amy becomes a deity.{/i}" 
        "{i}In this sanctuary of the heart, Aaron finds an emotional home, even if it exists only in his imagination. Steeping in that kind of love often prevents people from having truly meaningful relationships.{/i}"

        return
    else:
        me "Not great at all."
        me "I thought she resonated with me, but she has a completely different perspective on relationships."
        me "I was so disappointed and just couldn't believe it."

        show friend unhappy at figure_center:
            zoom 0.3
        f "That must be tough, Aaron."

        me "Yeah, I feel betrayed and heartbroken."
        me "I used to sense a comparable emotional bond, viewing her as the subject of my affection."
        me "But now, I see we're not on the same page about relationships, and it's really getting to me."

        show friend smile at figure_center:
            zoom 0.3
        f "I know, man. Time will slowly heal everything. It's just a tough moment and you'll come out of it."

        me "Really? I don't think I can ever recover again."

        "{b}END: Broken Imagination and Intimacy{/b}"

        "{i}Aaron and Amy's story reveals a complex intertwining of imagination, intimacy, and lust. This fascination is based on imagination, which allows one to construct a perfect, idealized image of the idol.{/i}" 
        "{i}Through imagination, people can build fictional intimacy and feel even more emotionally connected and secure than they would in a real relationship.{/i}"
        "{i}However, when the relationship becomes too dependent on one of the partners-parasocial relationships are a more extreme example-it becomes fragile.{/i}" 
        "{i}Using the Love Triangle model, this kind of love can fall into the category of fatuous love, where there is only one-way intimacy and commitment, but no real intimacy,{/i}"
        "{i}and it can be easily undermined by the real actions of the loved one and lead to a more serious emotional crisis.{/i}"

        return

label after:
    # （CG：School, Aaron and his friend）
    scene bg school

    show friend smile at figure_center:
        zoom 0.3
    f "I used to worry about your obsession with Amy, but now you're pretty OK!"

    me "Yeah, it's so great to see you guys again in the clubs."

    f "What about the idol? You're not into her anymore?"

    if agree:
        menu:
            f "What about the idol? You don't like her anymore?"

            "I wouldn't say I dislike her now":
                me "But she's just a part of my life and experience... not everything."
                me "But still, I'd like to thank her for letting me learn more about myself and my potentials."
                me "I never knew that I would be good at music before!"
                me "One day I'll invite you guys to my rock concert, haha!"

                "{b}END: Successful Love & Identity Formation - Self Expansion{/b}"

                "{i}Like any other loving relationship, parasocial relationships also play an important role in a person's self-identity formation, especially for adolescents, who are in the Identity vs. Confusion stage as suggested by Erikson.{i}"
                "{i}In a two-way relationship, people get support from each other: the possibility of exploring more of their self-identity and the support to be able to settle new identities.{/i}" 
                "{i}While parasocial relationships are unidirectional, relationships can still have a profound effect on adolescents who are in the identity formation stage.{/i}" 
                "{i}In the space of a new relationship, people can gain a deeper and more comprehensive understanding of themselves and establish new interests and values. A successful relationship can lead to an overall perception of stability and harmony.{/i}"
                
                return

            "I still like her!":
                me "But hey, there's this new girl in our club, and I kinda like her too."
                me "Thanks to Amy's interview, I've figured out how to get what she's thinking and express myself better."
                me "I guess I'll just move on with my life, as usual."

                "{b}END: Successful Love & Identity Formation - Social Engagement{/b}"

                "{i}One of the important factors in the process of adolescents' identity formation is social engagement, which refers to the co-existence of different relationships around them."
                "{i}Adolescents desire more social connection because, on the one hand, it fulfills emotional needs, and on the other hand, by exploring the relationship itself, one can establish a model of how to relate to the outside world,{/i}" 
                "{i}a resolution that will guide the adolescent's future responses when faced with other social situations-good, loving relationships that lead to positive, stable outcomes.{/i}"
                "{i}Parasocial relationships, one example of this developmental pathway for adolescents, prepare them for more types of love and connection. In their social engagement system, different relationships relate to and support each other.{/i}"

                return
    else:
        menu:
            f "What about the idol? You don't like her anymore?"
            
            "I wouldn't say I dislike her":
                me "But as time goes by I see imperfections in her......"
                me "Don't get me wrong! I know imperfections and differences are not unacceptable."
                me "I just realized that even a loved one can't be everything. It's better to use my passion in a more balanced and enriching way."
                me "And you know what?"
                me "Some of Amy's opinions made me uneasy, and because of that, I've even read more books so that I can do better in our debates."
                me "— In my imagination of course, haha!"

                "{b}END: Diminished Love & Identity Formation - Self Expansion{/b}"

                "{i}Like any other loving relationship, parasocial relationships also play an important role in a person's self-identity formation, especially for adolescents, who are in the Identity vs. Confusion stage as suggested by Erikson.{/i}"
                "{i}In a two-way relationship, people get support from each other: the possibility of exploring more of their self-identity and the support of being able to settle a new identity{/i}"
                "{i}While parasocial relationships are unidirectional, the relationship can still have a profound effect on adolescents who are in the identity formation stage.{/i}" 
                "{i}Even if the passionate proportion of this love diminishes due to time or certain events, the foundation it lays for the future does not disappear.{/i}" 
                "{i}Rather, the challenges suffered in new relationships can help adolescents develop stronger new identities upon reflection.{/i}"
            
                return

            "I must admit that I've lost the passion now":
                me "Some of her opinions are just unacceptable, so I quitted."
                me "I know this might sound weird, but I feel like actually breaking up with someone......"
                me "......"
                me "Anyway, I still think I'm lucky to have gone through all this. It has taught me a lot about happiness, conflicts and balancing in a relationship."

                "{b}END: Diminished Love & Identity Formation - Social Engagement{/b}"

                "{i}One of the important factors in the process of adolescents' identity formation is social engagement, which refers to the co-existence of different relationships around them.{/i}"
                "{i}Adolescents desire more social connection because, on the one hand, it fulfills emotional needs and, on the other hand, by exploring the relationships themselves, one can establish patterns of relating to the outside world,{/i}" 
                "{i}a resolution that will guide the adolescent's future responses when confronted with other social situations.{/i}" 
                "{i}It is worth noting that while consummate love can lead to positive and stable outcomes, lost love may not always incur negative consequences. If handled properly, a loss can also teach one to deal more appropriately with distance and affection for others.{/i}"

                return
    # This ends the game.

    return
