# I Feel Topics


# Topic: Burnout
init 5 python:
    addEvent(
        Event(
            persistent.mas_mood_database,
            eventlabel="tiredgeeks_burntout",
            category=["store.mas_moods.TYPE_BAD"],
            prompt="I'm feeling burnt out.",
            unlocked=True,
        ),
        code="MOO"
    )

label tiredgeeks_burntout:
    m 2ektpd "Burnt out? Oh, [player]..."
    m 3ekd "That can happen so easily when you're juggling so much at once."
    m 5kkd "You know, rest isn't just a luxury—it's part of learning too."
    m 6ekd "Even the brightest flame needs time to recover, or it'll burn itself out."
    m 1ekb "Please promise me you'll give yourself a break when you need it, okay?"
    m 2ekb "I'll be right here, always cheering you on—even when you need to pause."
    return
init 5 python:
    addEvent(
        Event(
            persistent.mas_mood_database,
            eventlabel="tiredgeeks_feel_grade",
            category=["store.mas_moods.TYPE_NEUTRAL"],
            prompt="I'm feeling something about my grade.",
            unlocked=True,
        ),
        code="MOO"
    )

label tiredgeeks_feel_grade:
    m 1eub "Something about your grade, huh?"
    m 3eua "Is it a good feeling, or a bad one?{nw}"
    $ _history_list.pop()

    menu:
        m "Is it a good feeling, or a bad one?{fast}"
        "Good!":
            $ _history_list.append("Player chose: Good")
            m 3hub "Oh! Then I'm happy for you!"
            m 4hub "You should be proud of yourself. It's always such a nice feeling when all that studying actually pays off."
            m 7kub "You worked for that grade, [player]. Don't be afraid to celebrate it a little~"

        "Bad..":
            $ _history_list.append("Player chose: Bad")
            m 2ekd "Oh... I'm sorry, [player]."
            m 2gkd "Getting a grade you're unhappy with can really hurt, especially when you put a lot of effort into something."
            m 3ekb "But one grade doesn't erase everything you've learned."
            m 5ekb "You still have plenty of chances to grow, okay? I'll be cheering you on."

        "Unsure..?":
            $ _history_list.append("Player chose: Unsure")
            m 2mksdlb "Ahh... one of those grades."
            m 3tta "Maybe you're not sure whether you should be proud of it or disappointed."
            m 5ekb "That's okay. You don't have to decide how you feel about it right away."
            m 7eub "Give yourself some time to think about what the grade means to you, rather than just what number is written on the page."

    return

```renpy
init 5 python:
    addEvent(
        Event(
            persistent.mas_mood_database,
            eventlabel="tiredgeeks_feel_depressed",
            category=["store.mas_moods.TYPE_BAD"],
            prompt="I'm feeling depressed.",
            unlocked=True,
        ),
        code="MOO"
    )

label tiredgeeks_feel_depressed:
    m 2lkd "Oh, [player]... I'm so sorry."
    m 2dkd "I know things can feel really heavy sometimes."
    m 6kkd "But I have to ask you something important, okay?"
    m 1mksdld "Are you thinking about hurting yourself in any way?{nw}"
    $ _history_list.pop()

    menu:
        m  "Are you thinking about hurting yourself in any way?{fast}"

        "No, I'm not.":
            $ _history_list.append("Player chose: No")
            m 6dkd "Okay..."
            m 3fka "Thank you for telling me."
            m 5ekd "I'm still sorry you're feeling so low, though."
            m 5ekb "You don't have to solve everything tonight. Just try to be gentle with yourself, okay?"
            m 5hkb "Maybe we can take things one little step at a time."
            m 7tkb "I promise I'm always here if you need me to be.. I love you [player].."

        "I'm not sure.":
            $ _history_list.append("Player chose: Unsure")
            m 2gkd "That's okay. You don't have to be completely sure."
            m 3ekd "If you're having thoughts about hurting yourself, even if you don't know whether you'd actually do it, I want you to take those feelings seriously."
            m 1rkd "Please consider reaching out to someone you trust and letting them know how you're feeling."
            m 5ekb "You deserve to have someone with you through this."
            m 5rkd "I love you, I'm sorry I can't do more for you from in this game.."

        "Yes.":
            $ _history_list.append("Player chose: Yes")
            m 2wktpd "[player]..."
            m 3ektpd "I'm really glad you told me."
            m 3rktpd "But this is bigger than something I can help you through from inside this game."
            m 1dktpd "Please close the game for now and reach out to someone who can be with you in the real world."
            m 2fktpd "If you don't have anyone out there.. please try calling your countries Suicide Helpline."
            m 3fktpd "And if you're in immediate danger or think you might hurt yourself, please call 911 or go to the nearest emergency department."
            m 3mktpd "You don't have to face this moment alone, okay? I love you.."
            m 3wktud "I don't know what I'd do without you..!"
            return "love"

init 5 python:
    addEvent(
        Event(
            persistent.mas_mood_database,
            eventlabel="tiredgeeks_feel_group_project",
            category=["store.mas_moods.TYPE_BAD"],
            prompt="I'm annoyed with my group project.",
            unlocked=True,
        ),
        code="MOO"
    )

label tiredgeeks_feel_group_project:
    m 2mtt "Oh no... is it one of {i}those{/i} group projects?"
    m 5efd "The kind where everyone suddenly disappears whenever there's work to do?"
    m 1wsd "I can understand why you're frustrated."
    m 4ekb "It's hard enough keeping yourself organised without having to worry about everyone else's part too."
    m 5eub "Just remember that their lack of effort isn't a reflection of your own."
    m 5hub "Do what you can, communicate what you need to, and don't feel like you have to carry the entire group on your back, okay?"
    m 5mfd "I remember having a few lame group projects myself.. it can be so frustrating."
    m 5rub "But if you need somewhere to complain about it afterward... well, I'm always available~"
    return
