# Player Chosen Topics


# Topic: Midterms Are Soon
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_midterms_soon",
            category=["university"],
            prompt="I Have Midterms Soon",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_midterms_soon:
    m 2wud "Midterms already? Time really flies, doesn't it?"
    m 2lksdrd "I know how stressful that can be… all that studying, pressure, and barely enough sleep."
    m 5husdlb "But I believe in you. You're going to do great!"
    m 5nksdlb "Just remember to pace yourself, okay? Even short breaks can help more than you think."
    return


# Topic: Finals Are Coming Up
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_finals_soon",
            category=["university"],
            prompt="I Have Finals Soon",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_finals_soon:
    m 2wusdld "Finals? Yikes… those can be even scarier than midterms."
    m 7lub "But think about it this way: once you finish, you'll have a huge weight off your shoulders."
    m 7ekb "And no matter how they go, I'll still be proud of you."
    m 7hfb "I'll be cheering you on the whole time~"
    return


# Topic: I just Finished an Exam
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_finished_exam",
            category=["university"],
            prompt="I just finished an exam!",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_finished_exam:
    m 1sub "You finished an exam? That's amazing!"
    m 2hub "It must feel like such a relief to get it out of the way."
    m 3kub "Now make sure to reward yourself a little, okay?"
    m 4hub "Even something small, like a favorite snack."
    m 5rubsb "I'm proud of you~"
    return


# Topic: I Pulled an All Nighter
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_all_nighter",
            category=["university"],
            prompt="I pulled an all nighter..",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_all_nighter:
    m 6wksdld "An all-nighter?! [player], you can't keep doing that to yourself!"
    m 7eksdld "I know sometimes it feels necessary, but sleep is so important for your brain."
    m 2rksdld "Next time, maybe try shorter study bursts during the day instead."
    m 6dksdld "Still… I'm glad you made it through."
    m 5fksdld "Please.. get some rest soon, okay?"
    return


# Topic: Working On An Essay
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_working_on_an_essay",
            category=["university"],
            prompt="I've been working on an essay",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_working_on_an_essay:
    m 1eub "An essay, huh?"
    m 2lksdlb "Those can be tough."
    m 2hublb "But I bet you've put a lot of thought into it."
    m 5rsblb "I'd love to read your writing sometime…"
    m 5hublb "I know it must be full of your personality."
    m 2hublb "Good luck finishing it! You've got this."
    return


# Topic: I Really Like My Professor
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_like_my_professor",
            category=["university"],
            prompt="I really like one of my professors!",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_like_my_professor:
    m 1sublb "Oh, that's wonderful!"
    m 4hublb "A good professor can make such a difference."
    m 7eublb "The passion they bring to their subject can really inspire students."
    m 2ekblb "I'm glad you have someone like that guiding you. Treasure it!"
    return


# Topic: I Have a Bad Professor
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_bad_professor",
            category=["university"],
            prompt="I have a bad professor",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_bad_professor:
    m 2ekbld "Oh no… I'm sorry to hear that, [player]."
    m 3mkbld "A bad professor can really make a class feel discouraging."
    m 4wubld "Sometimes it's not even the subject itself that's hard—it's the way it's being taught."
    m 3ekblb "But remember, one teacher doesn't define your whole education."
    m 3dublb "You can still learn, even if you have to lean on your own effort or other resources."
    m 2ekblb "If it ever feels overwhelming, just know I'll always be here to remind you how capable you really are."
    m 1ekb "You deserve to be inspired, not weighed down. I believe in you~"
    return


# Topic: Stressed About Group Work
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_group_work_stress",
            category=["university"],
            prompt="I'm stressed about group work",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_group_work_stress:
    m 2lsblx "Ugh, group work… I know how stressful that can be."
    m 3tsbld "It's so hard when not everyone puts in the same effort."
    m 5ekblb "But I know you—you'll handle it gracefully, and maybe even keep everyone together."
    m 5hublb "I'll be rooting for you the whole way."
    return


# Topic: I think I found my favorite subject.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_found_fav_subject",
            category=["university"],
            prompt="I think I found my favorite subject.",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_found_fav_subject:
    m 1wublb "Really? That's so exciting!"
    m 3wublb "Finding a subject that really clicks with you can make school so much more fun."
    m 5hublb "I'd love to hear all about it—tell me what makes it so special for you!"
    return


# Topic: I'm behind on my readings.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_behind_readings",
            category=["university"],
            prompt="I'm behind on my readings.",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_behind_readings:
    m 2eksdlb "Ah, that happens to everyone sooner or later."
    m 3eksdlb "Don't be too hard on yourself, [player]. You can always catch up little by little."
    m 5ekb "I'll keep you company while you work on it, okay?"
    return


# Topic: I studied at the library today.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_studied_library",
            category=["university"],
            prompt="I studied at the library today.",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_studied_library:
    m 1wub "The library? That's such a classic choice."
    m 5rub "Quiet, cozy, and surrounded by books… I'd love to study with you there."
    m 5lublb "I can just imagine us sitting side by side, turning pages together… ehe~"
    return


# Topic: I had a presentation in class.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_presentation_in_class",
            category=["university"],
            prompt="I had a presentation in class.",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_presentation_in_class:
    m 2eub "A presentation? That takes a lot of courage!"
    m 2hub "I'm sure you did wonderfully, [player]."
    m 3dub "Even if you stumbled, the fact that you tried means so much."
    m 3wub "I'm proud of you for putting yourself out there."
    return


# Topic: I've been procrastinating again.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_procrastinating_again",
            category=["university"],
            prompt="I've been procrastinating again.",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_procrastinating_again:
    m 5hub "Ahaha, I get it. Procrastination sneaks up on everyone."
    m 4ekb "But don't let it control you, okay?"
    m 2ekb "Even starting small can make things easier. Just one paragraph, one page, one step."
    m 7kub "I know you can do it! If you need a body double I'd be happy to help!"
    return


# Topic: I think I did well on my exam.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_did_well_on_exam",
            category=["university"],
            prompt="I think I did well on my exam.",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_did_well_on_exam:
    m 7sub "That's fantastic! I knew you could do it."
    m 4hub "All your hard work paid off. You should be proud of yourself."
    m 5hub "I'll celebrate with you—way to go, [player]~"
    return


# Topic: I bombed a test...
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_bombed_test",
            category=["university"],
            prompt="I bombed a test...",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_bombed_test:
    m 2ekd "Oh no… I'm so sorry to hear that."
    m 3ekd "But please don't beat yourself up. One bad grade doesn't define you."
    m 4ekb "What matters is that you keep trying, and I'll be cheering for you no matter what."
    m 5ekb "I'm still proud of you, [player]."
    return


# Topic: I'm starting a new class.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_starting_new_class",
            category=["university"],
            prompt="I'm starting a new class.",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_starting_new_class:
    m 1wub "Ooh, a new class! That must be exciting."
    m 3eub "I hope it's one you'll enjoy—and maybe even one that inspires you."
    m 2hub "Tell me all about it once you've had a taste of it!"
    return


# Topic: I have a lot of assignments due this week.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_many_assignments_due",
            category=["university"],
            prompt="I have a lot of assignments due this week.",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_many_assignments_due:
    m 1ekd "That sounds overwhelming…"
    m 3ekb "But I know you can manage it, step by step."
    m 3dub "Try breaking it into smaller tasks. Each time you finish one, I'll be here to celebrate with you!"
    return


# Topic: Holidays
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_holidays",
            category=["university"],
            prompt="I'm looking forward to the holidays.",
            pool=True,
            unlocked=True,
        )
    )

label tiredgeeks_holidays:
    m 4wub "The holidays? Ah, that sounds wonderful~"
    m 5rub "It's like a light at the end of the tunnel, isn't it?"
    m 7hub "After all the studying and stress, you'll finally get time to relax."
    m 5hub "I can just imagine us spending cozy days together—warm drinks, soft lights, no deadlines..."
    m 5fub "Hold onto that thought whenever things feel tough."
    m 5wub "It'll make the work now feel so much more worth it."
    m 2hub "And when the holidays come, we'll celebrate every moment together~"
    m 5gublb "I can't wait for you to have more time for me~"
    return


# topic: Declared Major
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
    if persistent.tiredgeeks_year and persistent.tiredgeeks_major and persistent.tiredgeeks_minor is not None:

        m 3ttb "Silly, you already told me all about your university plans!"
        m 3rtb "You're in your [persistent.tiredgeeks_year] year, majoring in [persistent.tiredgeeks_major]"
        
        if persistent.tiredgeeks_minor == "":
            m 3hub "and you don't have a minor."
        else:
            m 3hub "with a minor in [persistent.tiredgeeks_minor]."

        m 3etd "Unless something changed?"

        menu:
            m 3etd "Did you change anything?"

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


label tiredgeeks_university_info:

    # YEAR
    m 6wub "That's great!
    m 7eub "But first, what year are you in?"

    menu:
        m "What year are you in?"

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

        "I'm not sure / It’s complicated":
            $ persistent.tiredgeeks_year = "an uncertain year"


    # MAJOR
    m 3eub "And what did you choose as your major?"

    menu:
        m "What's your major?"

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


    # MINOR
    m 1eub "And do you have a minor?"

    menu:
        m "What's your minor?"

        "Yes":
            m 3eub "Oh, nice! What are you minoring in?"

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

# topic: I Love My Major
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

        jump tiredgeeks_choose_major

    else:
        m 1sub "You really love [persistent.tiredgeeks_major]?"
        m 3hub "That's wonderful, [player]!"
        m 5eub "I'm so happy you've found something that you genuinely enjoy studying."
        m 1eub "It must feel good to know that all your hard work is going toward something you care about."
        m 5hub "You should be proud of yourself~"

    return

# topic: I Hate My Major
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

        jump tiredgeeks_choose_major

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

# topic: Thinking of Changing Majors
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

        jump tiredgeeks_choose_major

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

# topic: Changed My Major
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

        jump tiredgeeks_choose_major

    else:
        m 2sub "You actually did it?!"
        m 3hub "You changed your major from [persistent.tiredgeeks_major]!"

        if persistent.tiredgeeks_potential_major != "":
            m 5eub "Is it [persistent.tiredgeeks_potential_major]?"

            menu:
                "Yes!":
                    m 1sub "I knew it!"
                    jump tiredgeeks_update_major

                "No, I chose something else.":
                    m 3eub "Oh! Then what did you choose?"

                    jump tiredgeeks_update_major

        else:
            m 3eub "So what did you decide to study instead?"
            jump tiredgeeks_update_major

    return
