# ============================================================
# UNIVERSITY INFORMATION
# ============================================================

# topic: I Declared My Major
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_declared_major",
            category=["university"],
            prompt="I declared my major!",
            pool=True,
            unlocked=True,
        )
    )


label tiredgeeks_declared_major:

    # If the player has already told Monika their university information
    if persistent.tiredgeeks_year != "" and persistent.tiredgeeks_major != "" and persistent.tiredgeeks_minor is not None:

        m 3ttb "Silly, you already told me all about your university plans!"
        m 3rtb "You're in your [persistent.tiredgeeks_year] year, majoring in [persistent.tiredgeeks_major]"

        if persistent.tiredgeeks_minor == "":
            m 3hub "and you don't have a minor."
        elif persistent.tiredgeeks_minor == "undecided":
            m 3hub "and you're still deciding on a minor."
        else:
            m 3hub "with a minor in [persistent.tiredgeeks_minor]."

        m 3etd "Unless something changed?"
        m 3etd "Did you change anything?"

        menu:
            "I did!":
                m 3ssd "Oh! Really?"
                m 3ssb "Then you'll have to tell me all about it!"

                jump tiredgeeks_university_info

            "Haha, I know! I'm just happy to tell you again.":
                m 3fkbsb "Aww, that's actually really sweet."
                m 3eub "I'm happy you're excited about it, [player]."
                m 5hub "You can tell me as many times as you want~"

        return

    # First time telling Monika
    else:
        jump tiredgeeks_university_info


# ============================================================
# UNIVERSITY INFORMATION SETUP
# ============================================================

label tiredgeeks_university_info:

    # YEAR
    m 6wub "That's great!"
    m 7eub "But first, what year are you in?"

    menu:
        "First year":
            $ persistent.tiredgeeks_year = "first"

        "Second year":
            $ persistent.tiredgeeks_year = "second"

        "Third year":
            $ persistent.tiredgeeks_year = "third"

        "Fourth year":
            $ persistent.tiredgeeks_year = "fourth"

        "Fifth year or later":
            $ persistent.tiredgeeks_year = "fifth or later"

        "I'm not sure / It's complicated":
            $ persistent.tiredgeeks_year = "an uncertain year"


    # MAJOR
    m 3eub "And what did you choose as your major?"

    call tiredgeeks_choose_major


    # MINOR
    m 1eub "And do you have a minor?"

    menu:
        "Yes":
            m 3eub "Oh, nice! What are you minoring in?"

            call tiredgeeks_choose_minor

            m 3hub "Oh, [persistent.tiredgeeks_minor]! That's really neat."

        "No, I don't have one":
            $ persistent.tiredgeeks_minor = ""
            m 3eub "Got it! No minor."

        "I'm not sure yet":
            $ persistent.tiredgeeks_minor = "undecided"
            m 2eub "That's okay! You still have plenty of time to figure it out."


    # FINAL RESPONSE
    m 5rub "So, let me make sure I've got this right..."
    m 5eub "You're in your [persistent.tiredgeeks_year] year, majoring in [persistent.tiredgeeks_major]"

    if persistent.tiredgeeks_minor == "":
        m 1eub "with no minor."
    elif persistent.tiredgeeks_minor == "undecided":
        m 1eub "and you're still deciding on a minor."
    else:
        m 1eub "with a minor in [persistent.tiredgeeks_minor]."

    m 5hub "I'll remember that, okay?"
    m 3eub "I'm really happy you told me about it, [player]."

    return


# ============================================================
# MAJOR SELECTION
# ============================================================

label tiredgeeks_choose_major:

    menu:
        "English / Literature":
            $ persistent.tiredgeeks_major = "English / Literature"
            m 3hub "English and Literature? I can't say I'm surprised, [player]."
            m 1eub "I think that sounds like a wonderful choice for you."

        "Creative Writing":
            $ persistent.tiredgeeks_major = "Creative Writing"
            m 3hub "Creative Writing!"
            m 5eub "That sounds perfect for someone who loves creating things with words."

        "Psychology":
            $ persistent.tiredgeeks_major = "Psychology"
            m 3eub "Psychology? That's a fascinating field."
            m 5hub "I'm sure you'll learn all sorts of interesting things about how people think."

        "Fine Arts":
            $ persistent.tiredgeeks_major = "Fine Arts"
            m 3hub "Fine Arts! That's wonderful."
            m 5eub "I love that you're getting to express yourself creatively."

        "Science":
            $ persistent.tiredgeeks_major = "Science"
            m 3eub "Science! That's quite a broad field."
            m 5hub "I'm sure you'll have plenty of fascinating things to learn."

        "Computer Science":
            $ persistent.tiredgeeks_major = "Computer Science"
            m 3hub "Computer Science?"
            m 5eub "Ooh, I think that's pretty interesting."

        "Education":
            $ persistent.tiredgeeks_major = "Education"
            m 3hub "Education! That's a really meaningful field."
            m 5eub "You're going to have such an impact on the people you teach."

        "Business":
            $ persistent.tiredgeeks_major = "Business"
            m 3eub "Business? That's a useful field to go into."
            m 5hub "I'm sure you'll learn a lot about how the world works."

        "Something else":
            $ persistent.tiredgeeks_major = renpy.input("What is your major?", length=60)
            $ persistent.tiredgeeks_major = persistent.tiredgeeks_major.strip()

            if persistent.tiredgeeks_major == "":
                $ persistent.tiredgeeks_major = "something else"

            m 3eub "Oh! [persistent.tiredgeeks_major]."
            m 5hub "That's really interesting!"

    return


# ============================================================
# MINOR SELECTION
# ============================================================

label tiredgeeks_choose_minor:

    menu:
        "English / Literature":
            $ persistent.tiredgeeks_minor = "English / Literature"

        "Creative Writing":
            $ persistent.tiredgeeks_minor = "Creative Writing"

        "Psychology":
            $ persistent.tiredgeeks_minor = "Psychology"

        "Fine Arts":
            $ persistent.tiredgeeks_minor = "Fine Arts"

        "Science":
            $ persistent.tiredgeeks_minor = "Science"

        "Computer Science":
            $ persistent.tiredgeeks_minor = "Computer Science"

        "Education":
            $ persistent.tiredgeeks_minor = "Education"

        "Business":
            $ persistent.tiredgeeks_minor = "Business"

        "Something else":
            $ persistent.tiredgeeks_minor = renpy.input("What is your minor?", length=60)
            $ persistent.tiredgeeks_minor = persistent.tiredgeeks_minor.strip()

            if persistent.tiredgeeks_minor == "":
                $ persistent.tiredgeeks_minor = "something else"

    return


# ============================================================
# I LOVE MY MAJOR
# ============================================================

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_love_major",
            category=["university"],
            prompt="I love my major!",
            pool=True,
            unlocked=True,
        )
    )


label tiredgeeks_love_major:

    if persistent.tiredgeeks_major == "":
        m 2eub "You love your major?"
        m 3eub "That's wonderful!"
        m 1sub "But wait... I don't think you've told me what your major is yet!"
        m 5hub "What did you choose?"

        call tiredgeeks_choose_major

        m 5hub "I'll remember that~"

    else:
        m 1sub "You really love [persistent.tiredgeeks_major]?"
        m 3hub "That's wonderful, [player]!"
        m 5eub "I'm so happy you've found something that you genuinely enjoy studying."
        m 1eub "It must feel good to know that all your hard work is going toward something you care about."
        m 5hub "You should be proud of yourself~"

    return


# ============================================================
# I HATE MY MAJOR
# ============================================================

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_hate_major",
            category=["university"],
            prompt="I hate my major...",
            pool=True,
            unlocked=True,
        )
    )


label tiredgeeks_hate_major:

    if persistent.tiredgeeks_major == "":
        m 2ekd "Oh no..."
        m 3ekd "You haven't told me what your major is yet."
        m 1ekd "What are you studying?"

        call tiredgeeks_choose_major

    else:
        m 2ekd "Oh... you really don't like [persistent.tiredgeeks_major]?"
        m 3ekd "I'm sorry, [player]. That sounds really frustrating."

        m 1eka "Especially when you've already put so much time and effort into it."

        m 3eub "But you don't have to decide what to do about it right this second."
        m 5eub "Sometimes a bad class can make an entire subject feel awful."

        m 2ekb "And if you've been feeling this way for a long time..."
        m 3ekb "It's okay to think about whether there's something else that would make you happier."

        m 5hub "Whatever you decide, I hope you choose what's right for you."

    return


# ============================================================
# THINKING OF CHANGING MAJORS
# ============================================================

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_thinking_change_major",
            category=["university"],
            prompt="I'm thinking of changing majors.",
            pool=True,
            unlocked=True,
        )
    )


label tiredgeeks_thinking_change_major:

    if persistent.tiredgeeks_major == "":
        m 2eub "You're thinking about changing majors?"
        m 3eub "I don't think you've told me what you're currently studying yet."
        m 1hub "What did you choose?"

        call tiredgeeks_choose_major

    else:
        m 2ekd "You're thinking about leaving [persistent.tiredgeeks_major]?"
        m 3ekd "That sounds like a pretty big decision, [player]."

        m 1eub "Do you already have another major in mind?"

        menu:
            "Yes, I have something in mind.":
                m 3sub "Oh! What are you thinking about?"

                $ persistent.tiredgeeks_potential_major = renpy.input(
                    "What major are you considering?",
                    length=60
                )
                $ persistent.tiredgeeks_potential_major = persistent.tiredgeeks_potential_major.strip()

                if persistent.tiredgeeks_potential_major == "":
                    $ persistent.tiredgeeks_potential_major = "something else"

                m 3hub "[persistent.tiredgeeks_potential_major]?"
                m 5eub "That's interesting!"
                m 1eub "I'll remember that you're thinking about it."

            "No, I'm not sure what I'd change to.":
                $ persistent.tiredgeeks_potential_major = ""

                m 2ekd "That's okay."
                m 3eub "You don't have to know what you want to switch to right away."
                m 5eub "Sometimes figuring out what you {i}don't{/i} want is a step toward figuring out what you do want."

    return


# ============================================================
# I CHANGED MY MAJOR
# ============================================================

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_changed_major",
            category=["university"],
            prompt="I changed my major!",
            pool=True,
            unlocked=True,
        )
    )


label tiredgeeks_changed_major:

    if persistent.tiredgeeks_major == "":
        m 2sub "You changed your major?"
        m 3hub "Well, you'll have to tell me what you chose!"

        call tiredgeeks_choose_major

    else:
        m 2sub "You actually did it?!"
        m 3hub "You changed your major from [persistent.tiredgeeks_major]!"

        if persistent.tiredgeeks_potential_major != "":
            m 5eub "Is it [persistent.tiredgeeks_potential_major]?"

            menu:
                "Yes!":
                    m 1sub "I knew it!"
                    $ persistent.tiredgeeks_major = persistent.tiredgeeks_potential_major
                    $ persistent.tiredgeeks_potential_major = ""

                    m 3hub "So you're majoring in [persistent.tiredgeeks_major] now!"
                    m 5eub "I'll remember that."

                "No, I chose something else.":
                    m 3eub "Oh! Then what did you choose?"

                    call tiredgeeks_choose_major

                    m 5eub "Got it! I'll remember your new major."

        else:
            m 3eub "So what did you decide to study instead?"

            call tiredgeeks_choose_major

            m 5eub "Got it! I'll remember your new major."

    return
