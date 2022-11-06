label start:
    "You awaken to the sound of three alarms blaring discordant hard rock from three separate corners of the room, each a failsafe to ensure your body’s need for sleep does not betray you at this critical moment."
    "You rise and silence them one by one. It’s 4am. Motion activated lighting converts your apartment to daytime. A pair of stimulant pills sit on a tiny paper plate on your bedside table, you wash them back with a glass of tainted brown warm water. The aftertaste sucks but your mind clears. Time for the call."
    "You settle into a seat in front of your data terminal. Cold light from the street lamps outside creeps around the cracks in your blinds. A thrumming bassline designed to rock your ribcage thumps from the apartment across the way, the heartbeat of a party that will never end."
    "Out there is Mirage City, your home. Some call it ruthless. Some call it a fantasy. Everyone knows it to be opportunity made manifest."
    "Anyone can make it in Mirage. Mercenaries, corporations, killers, thieves, and anyone else with a dream flocks here to make it big. One way or another the city chews you up and spits you out, it’s up to you whether you come out covered in gold or face down in a gutter."
    "You were born here, left with no choice but to survive. You clawed your way from the street and into this shitty apartment… It’s the best thing that ever happened to you." 
    "Those you grew up with are almost all gone now, most of them were only good at violence, but you have a different talent. You have a head for business, you know people and you know how to get what you want from them. When someone needs something, you want to be the person they contact to make it happen."
    "You want to be a Fixer."
    "Until now you have been handling small-time drug and arms deals for the local gangs, a bunch of unstable psychos who are as liable to blow your brains out as they are to pay you your measly five percent. You need to be a bigger name. You need power, and muscle, and recognition. That’s what today is all about."
    "You are waiting on a call from Mr. Valiant, your first real client. He wants to hire you for a job. If you do it well you’ll see the biggest payday of your life, but more importantly you’ll have proven you can operate in the big leagues. This is your big break."
    "You pull a spool of data cable from the cranial implant behind your ear and plug it into your terminal. Valiant gave instructions on setting up the secure line, you activate the encryption software he recommended and watch as your test communication data packets transform into gibberish. They will be translated using the thousand character cipher key on Valiant’s end."
    "A few agonizing moments pass where your mind tries to convince you that this has all been some sort of prank, that you are not good enough, that Valiant has found somebody else. Then the call comes through, and you’ve answered it before the terminal’s musical jingle can reach the second note."
    "Mr. Valiant’s digital persona forms on your screen. A masculine figure wearing a thin, silken robe accenting a muscular body. A radiant halo revolves lazily around his head, which bears only a mouth where a face should be."
    "Mr. Valiant" "You’re on time, excellent. Punctuality is important in this line of work, it shows respect."
    
menu:
    "Of course, your time is valuable. I wouldn’t waste it.":
        jump respect
        
    "This better be worth it, I had to set so many alarms!":
        jump disrespect

label respect:
    "Mr. Valiant" "And polite, too? More than I expected from a reported gutter rat."
    jump job
    
label disrespect:
    "Mr. Valiant" "…It will be worth your time. Apologies for waking you at this early hour, I was not aware you had such difficulty keeping to a schedule."
    jump job
        
label job:
    "Mr. Valiant" "In any case, I have work for you… I expect it will be a one-person job, but I will leave hiring ‘talent’ to your discretion. I will pay you a flat rate, it is up to you how much of that goes towards mission expenses and how much remains in your pocket."
    "Mr. Valiant" "Here are the details: My business partner has been taking unnecessary and greedy risks behind my back. I discovered this last night when I learned he had been arrested by the MCPD. I was planning to hire you to break him free of his cell, but the situation has… evolved."
    "Mr. Valiant" "Unfortunately, like most everyone in this city, I have enemies. The police transport carrying my partner was hit just a few hours ago, dead cops everywhere, and now my partner is missing. I believe this was orchestrated by The Fringe, an organized crime outfit that love nothing more than punching above their weight class."
    "Mr. Valiant" "The Fringe failed to disable my partner’s tracking beacon in time, so I have the location of their hideout. I just need someone to gather intel, hire an appropriate heavy hitter, and retrieve my partner… Or, failing that, bring me the data chip stored in his head. I expect that is what The Fringe are looking for. It cannot fall into their hands."
label questions:
    "Mr. Valiant" "Questions? Yes, ask away."
   
menu:
    "Tell me about The Fringe.":
        jump fringe
        
    "Tell me about this data chip.":
        jump chip
        
    "How much money are we talking?":
        jump money
        
    "Who should I hire?":
        jump hire
        
    "Okay, I’m ready to go to work!":
        jump end
        
label fringe:
    "Mr. Valiant" "They are small fish in a vast ocean, but they behave as though nobody can touch them. I expect you to prove them wrong. Dumb muscle and limited tech capabilities, they largely deal in protection rackets, some legitimate bodyguard work, and the occasional smuggling job."
    "Mr. Valiant" "Anything else?"
    
label chip:

label money:

label hire:

label end: