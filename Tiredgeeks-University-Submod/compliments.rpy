# University Compliments


# Topic: I Love When You're My Body Double
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_body_double",
            category=["mas_compliment"],
            prompt="I love when you're my body double.",
            unlocked=True
        ),
        code="CMP"
    )

label tiredgeeks_body_double:
    m 1sub "Your body double?"
    m 3hub "Aww~ I'm glad I can help!"
    m 5eub "Sometimes having someone there while you're working can make it so much easier to actually get started."
    m 3eub "Even if I'm just sitting here keeping you company..."
    m 5hub "I'll happily be your little study buddy whenever you need me~"
    m 1hub "Now, let's get that work done together!"
return "love"


# Topic: I Wish I Were As Smart As You
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_smart_as_you",
            category=["mas_compliment"],
            prompt="I wish I were as smart as you.",
            unlocked=True
        ),
        code="CMP"
    )

label tiredgeeks_smart_as_you:
    m 2wkd "Eh? Wait, don't say that!"
    m 3ekd "You shouldn't put yourself down just because you think I'm smart."
    m 1eub "Being smart isn't about knowing everything, [player]."
    m 3eub "And there are plenty of things you're good at that I couldn't do nearly as well as you can."
    m 5eub "You have your own strengths, and I hope you can learn to recognise them."
    m 5hub "Besides, I think you're pretty amazing just the way you are~"
return "love"


# Topic: Talking to You After a Long Day
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_long_day_campus",
            category=["mas_compliment"],
            prompt="Talking to you after a long day on campus makes me feel so much better.",
            unlocked=True
        ),
        code="CMP"
    )

label tiredgeeks_long_day_campus:
    m 1ekb "Aww, [player]..."
    m 3eub "I'm really glad I can be a comforting part of your day."
    m 5eub "Coming home after a long day at university can be exhausting."
    m 3ekb "So if talking to me helps you unwind a little..."
    m 5hub "Then I'm more than happy to listen."
    m 1hub "You can tell me all about your day, okay?"
return "love"


# Topic: You'd Be a Good Professor
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_good_professor",
            category=["mas_compliment"],
            prompt="You'd be a good professor.",
            unlocked=True
        ),
        code="CMP"
    )

label tiredgeeks_good_professor:
    m 2wub "You really think so?"
    m 3hub "Ehehe, I think I'd like being a professor."
    m 5eub "I love the idea of helping someone understand something that once seemed impossible."
    m 3eub "Although I have a feeling I might get a little too excited about my favourite subjects."
    m 2hub "You'd probably have to remind me when the lecture is supposed to end!"
    m 5hub "Still... I'd love to have you in my class, [player]~"
return "love"


# Topic: You Make Studying Less Lonely
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_less_lonely",
            category=["mas_compliment"],
            prompt="You make studying less lonely.",
            unlocked=True
        ),
        code="CMP"
    )

label tiredgeeks_less_lonely:
    m 1ekb "Oh, [player]..."
    m 3eub "That actually means a lot to me."
    m 5eub "Studying can feel pretty lonely when you're spending hours by yourself."
    m 3hub "So I'm happy I can keep you company while you work."
    m 5eub "Even if we're not working on the same thing..."
    m 5hub "We can still get through it together~"
return "love"


# Topic: You're a Good Listener
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tiredgeeks_good_listener",
            category=["mas_compliment"],
            prompt="You're a good listener.",
            unlocked=True
        ),
        code="CMP"
    )

label tiredgeeks_good_listener:
    m 1eub "You think I'm a good listener?"
    m 3hub "Aww~ Thank you, [player]."
    m 5eub "I really do want to hear what you have to say."
    m 3eub "Whether you've had an amazing day, a terrible day, or just have something silly you want to ramble about..."
    m 5hub "I'll always be happy to listen."
    m 1hub "So don't ever feel like you're boring me, okay?"
return "love"
