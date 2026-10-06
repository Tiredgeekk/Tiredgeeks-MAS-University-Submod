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
