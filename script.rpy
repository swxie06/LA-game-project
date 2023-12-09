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

    show black

    mom "Aaron! Aaron! Your dad and I are going out for a while. Remember to eat breakfast when you get up. Enjoy your weekend."

    #*Main character's point of view, eyes opening with blurring effect, the room gradually appears
    #(CG: Aaron's room, with different posters or decorations on the walls if possible, to show teenagers' personalities)

    scene bg stage # replace this with above
    with dissolve

    me "Mom, it's still early, don't wake me up on weekend mornings from now on. It's been a whole week of school, I have the right to wake up slowly on the weekends."

    me "(Well it's finally the weekend and I don't have any fun plans, what should I do today? Anyway, let's play with my phone first.)"

    #(CG: cell phone screen)

    me "What's this? Idol Amy's first anniversary performance......? Let me see it."

    # (CG: Amy)
    #(maybe a few more pictures of different poses here, with bgm, to show that she’s singing and dancing)

    me "(*humming*) That's nice! I feel like I'm lifted up. Why don't I check out her other shows?"

    #(optional CG: screen scrolling or similar effect)
    #(optional CG: Amy's other performances)

    menu:

        me "Got a weird feeling......"

        # I tried shortening the choices to make it flow better

        "I like her music":
            me "Is this what it's like to be a fan? I've never been one before. Her songs are pretty good, so I'll listen to more of them when I have time."
            jump end1

        "I feel a connection with her...":
            me "How do I feel like I'm getting to know her, when it's obvious we're not even in contact? I don't know how, but when I watch her videos, I feel like she's talking to me while holding my hands. I feel so close to her that I can't help but keep watching."
            jump conversation

label end1:

    "{b}END: Parasocial Relationship VS Fandom Culture{/b}"

    "{i}Although they may overlap, they are not exactly equal. While the former emphasizes the relationship between the followed and the follower, the latter deals more broadly with the appreciation of a celebrity's personality or work.{/i}"
    "{i}Taken together, in the modern context parasocial relationships are an offshoot of fandom culture, embodying the behaviors and attitudes of followers who are deeply invested in a one-sided relationship,{/i}"
    "{i}but many followers also choose not to enter into this level of relationship. Overall, parasocial relationships offer more of a sense of spiritual intimacy.{/i}"
    
    return

label conversation:

    #(CG: school + image of two people)
    # aaron on the left, friend on the right?

    f "Bro, you seem to be obsessed with that idol named Amy lately, don't you? You're so focused on her that you don't even come to basketball practice or book club."
    f "Is it possible that she's more of a close friend to you than we are?"

    me "(slightly embarrased)"

    f "I'm just saying that off the top of my head haha..."

    menu:

        f "I know she's pretty and fun, but shouldn't you care about the other parts of life too?"
        "You're saying that 'cause you don't know about how great Amy is! Let's not talk about this.":
            $ reflect = False
        "Well... I didn't think that way...":
            $ reflect = True
            
    jump after_convo

label after_convo:

    #（CG ： Aaron’s room，Aaron）

    me "Another week of classes, haven't seen Amy the last couple days with all the homework."

    me "Also I'm a little tired of watching shows. Where can I find ways to get to know her better on a deeper level?"

    me "\"Amy's Interpersonal Mindset Revealed - What is Amy's Advice on Love?\""

    me "Umm sounds interesting! I haven't really read many of Amy's interviews. Since I'm kind of bothered by these questions, let's see what Amy has to say."

    me "I expect a heart-to-heart chat with you, Amy."

    #( optional CG：Here maybe make an option for the player to choose to click into the video, and when they do, do shaking effects or something, and then Amy's image appears. I'm a bit afraid it's too boring to be all text)

    # (CG: Interview Hall,  Amy)

    amy "There are a lot of fans and friends who struggle a lot with getting along with people, and I'm the same..."

    amy "My ideal intimacy and love should be..."

    with fade

    amy "Anyway, everyone has a different idea of what love is like."

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
        me "I told you I wasn't wrong about Amy. She's really a genuine and sensible person, I can learn a lot from her!"

        me "I know she's answering to countless fans, but I feel especially close to her in terms of feelings and thoughts. Might as well just take her words as advice from a good friend."

        jump after

    else:
        me "Although I liked Amy so much, I can't agree with her on this aspect of love."

        menu:
            me "Now I don't even know what I'm going to do about my love..."

            "Whatever, I was drawn to her because of her talent and the uplift she brought; not because she thought exactly like me.":
                jump after

            "Since our views are so different in principle, I don't really see the need to maintain the love.":
                jump after



label refuse:
    # （CG：school, Aaron and his friend）

    f "Hey Aaron!"

    me "What... oh, it's you."

    f "You've been in a trance lately, and it's getting harder and harder for us to talk to you. How do you do? What about the idol?"

    if agree:
        me "Amy's interview expressing her views on love and companionship really resonated with me and made me think. From the moment I watched the interview, I felt like she was that special person in my life."
        
        f "But Amy is an idol, your admiration is one-sided, and you can't really be with Amy. Are you sure you don't want to rethink your decision?"

        me "No, I'm not looking for anyone else. Because that interview made me realize that Amy gave me a unique sense of security that no one else could match."

        "{b}END: Sustainable Imagination and Intimacy{/b}"

        "{i}Aaron's emotional attachment to Amy is not just a fascination, but a deep spiritual resonance, a fictionalized adoration. He sees her not only as his idol, but as his dream partner.{/i}"
        "{i}This one-way emotional connection, though born of distant observation and fantasy, forges a flawless love in Aaron's heart.{/i}"
        "{i}This one-way emotional attachment, though based on fiction, builds an emotional sanctuary in Aaron's heart where Amy becomes a deity.{/i}" 
        "{i}In this sanctuary of the heart, Aaron finds an emotional home, even if it exists only in his imagination. Steeping in that kind of love often prevents people from having truly meaningful relationships.{/i}"

        return
    else:
        me "I thought she resonated with me, but she has a completely different perspective on relationships and I'm really disappointed."

        f "That must be so hard, Aaron."

        me "Yes, I feel betrayed and heartbroken. I used to think that there was a similar connection between our emotions seeing her as the object of my affection, but now I realize that there is a difference in our views on relationships and it's killing me."

        f "Time will slowly heal everything Aaron. Maybe it's just a tough time and you'll come out of it."

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

    f "I used to worry about your obsession with Amy, but now you're pretty OK!"

    me "Yeah, it's so great to see you guys again in the clubs."

    if agree:
        menu:
            f "What about the idol? You don't like her anymore?"

            "I wouldn't say I dislike her now":
                me "But she's just a part of my life and experience... not everything. However, I'd like to thank her for letting me learn more about myself and my potential."
                me "I never knew that I would be good at music before! One day I'll invite you guys to see me playing guitar, haha!"

                "{b}END: Successful Love & Identity Formation - Self Expansion{/b}"

                "{i}Like any other loving relationship, parasocial relationships also play an important role in a person's self-identity formation, especially for adolescents, who are in the Identity vs. Confusion stage as suggested by Erikson.{i}"
                "{i}In a two-way relationship, people get support from each other: the possibility of exploring more of their self-identity and the support to be able to settle new identities.{/i}" 
                "{i}While parasocial relationships are unidirectional, relationships can still have a profound effect on adolescents who are in the identity formation stage.{/i}" 
                "{i}In the space of a new relationship, people can gain a deeper and more comprehensive understanding of themselves and establish new interests and values. A successful relationship can lead to an overall perception of stability and harmony.{/i}"
                
                return

            "I still like her!":
                me "But I met a new girl in our club that I also find attractive... and thanks to Amy, I learned how to express and understand the girl's thoughts."

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
                me "But as time goes on I can see imperfections in her, and don't misunderstand me, I don't think imperfections or differences are unacceptable..."
                
                me "I just realize that even a loved one can't be everything. I want to use my passion in a more balanced and rich way."
                me "You know what, because of some of Amy's opinions that discomfort me, I even read more books so that I can do better in our debates — which of course is imagined, haha!"

                "{b}END: Diminished Love & Identity Formation - Self Expansion{/b}"

                "{i}Like any other loving relationship, parasocial relationships also play an important role in a person's self-identity formation, especially for adolescents, who are in the Identity vs. Confusion stage as suggested by Erikson.{/i}"
                "{i}In a two-way relationship, people get support from each other: the possibility of exploring more of their self-identity and the support of being able to settle a new identity{/i}"
                "{i}While parasocial relationships are unidirectional, the relationship can still have a profound effect on adolescents who are in the identity formation stage.{/i}" 
                "{i}Even if the passionate proportion of this love diminishes due to time or certain events, the foundation it lays for the future does not disappear.{/i}" 
                "{i}Rather, the challenges suffered in new relationships can help adolescents develop stronger new identities upon reflection.{/i}"
            
                return

            "I must admit that I've lost the passion now":
                me "Some of her opinions are kinda unacceptable for me so I quit. Such a feeling is very similar to an actual break up, which may sound weird..."
                me "However, I think I am lucky to have had this relationship, as it told me a lot about the happiness, conflicts and balance in relationships."

                "{b}END: Diminished Love & Identity Formation - Social Engagement{/b}"

                "{i}One of the important factors in the process of adolescents' identity formation is social engagement, which refers to the co-existence of different relationships around them.{/i}"
                "{i}Adolescents desire more social connection because, on the one hand, it fulfills emotional needs and, on the other hand, by exploring the relationships themselves, one can establish patterns of relating to the outside world,{/i}" 
                "{i}a resolution that will guide the adolescent's future responses when confronted with other social situations.{/i}" 
                "{i}It is worth noting that while consummate love can lead to positive and stable outcomes, lost love may not always incur negative consequences. If handled properly, a loss can also teach one to deal more appropriately with distance and affection for others.{/i}"

                return
    # This ends the game.

    return
