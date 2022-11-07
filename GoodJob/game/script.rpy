define v=Character('Mr. Valiant',color="c8c8ff")

$ positiverelationshipvaliant=0
$ negativerelationshipvaliant=0

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
    v "You’re on time, excellent. Punctuality is important in this line of work, it shows respect."
    
menu:
    "Of course, your time is valuable. I wouldn’t waste it.":
        jump respect
        
    "This better be worth it, I had to set so many alarms!":
        jump disrespect

label respect:
    $ positiverelationshipvaliant=1
    v "And polite, too? More than I expected from a reported gutter rat."
    jump job
    
label disrespect:
    $ negativerelationshipvaliant=1
    v "…It will be worth your time. Apologies for waking you at this early hour, I was not aware you had such difficulty keeping to a schedule."
    jump job
        
label job:
    v "In any case, I have work for you… I expect it will be a one-person job, but I will leave hiring ‘talent’ to your discretion. I will pay you a flat rate, it is up to you how much of that goes towards mission expenses and how much remains in your pocket."
    v "Here are the details: My business partner has been taking unnecessary and greedy risks behind my back. I discovered this last night when I learned he had been arrested by the MCPD. I was planning to hire you to break him free of his cell, but the situation has… evolved."
    v "Unfortunately, like most everyone in this city, I have enemies. The police transport carrying my partner was hit just a few hours ago, dead cops everywhere, and now my partner is missing. I believe this was orchestrated by The Fringe, an organized crime outfit that love nothing more than punching above their weight class."
    v "The Fringe failed to disable my partner’s tracking beacon in time, so I have the location of their hideout. I just need someone to gather intel, hire an appropriate heavy hitter, and retrieve my partner… Or, failing that, bring me the data chip stored in his head. I expect that is what The Fringe are looking for. It cannot fall into their hands."
label questions:
    v "Questions? Yes, ask away."
   
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
    v "They are small fish in a vast ocean, but they behave as though nobody can touch them. I expect you to prove them wrong. Dumb muscle and limited tech capabilities, they largely deal in protection rackets, some legitimate bodyguard work, and the occasional smuggling job."
label fringequery:
    v "Anything else?"
    
menu:
    "What sort of firepower should we be expecting?":
        jump firepower
        
    "How do you know The Fringe?":
        jump valiantfringe
        
    "There are some other details I'd like to discuss.":
        jump questions
        
label firepower:
    v "The Fringe is a glorified street gang. They don’t have much to speak of in terms of numbers, but if they hit a police transport they must have upgraded their hardware recently. Perhaps you can take a look at the crime scene, or get your hands on the police report somehow. Then you’ll have the info you need."
    jump fringequery
        
label valiantfringe:
    v "I have had some minor business dealings with them in the past. There’s not much to say, and I’d rather not discuss it."

menu:
    "Listen, I can’t do my job if I’m in the dark. I need to know what your connection is with them.":
        jump valiantfringeunhappy
        
    "Got it, I don’t need to know any more than that.":
        jump valiantfringehappy
        
label valiantfringeunhappy:
    $ negativerelationshipvaliant+=1
    v "…Mr partner and I work for a group that sometimes has access to armaments and cyber augmentations. We were selling surplus goods to The Fringe until they started making unreasonable demands." 
    v "I cut off contact, but my partner must have continued to deal with them against my better judgment. Obviously it didn’t go well for him."
    v "I believe they want to use the information on his data chip to go straight to the source, cut out the middlemen and take the goods directly from my employers. This would be disastrous. The Fringe wouldn’t stand a chance, and it’s likely my connection to them would be revealed in the process. That cannot happen, understand?"
    jump fringequery
    
label valiantfringehappy:
    $ positiverelationshipvaliant+=1
    v "I appreciate that. Privacy is important in this line of work, it doesn’t pay to go prying into your employers’ business. The less we all know about each other, the better. Everyone stays isolated, everyone stays safe."
    jump fringequery
    
label chip:
    v "It is a standard encrypted ZeroPoint Technologies data chip designed to be slotted into any universal data port, in this case it is concealed within my partner’s brain port."
label chipquery:
    v "Do you need more information?"
    
menu:
    "Is there a risk of it being damaged?":
        jump chipdamage
        
    "What's on the chip?":
        jump chipdetails
        
    "It sounds like you care more about the chip than your partner.":
        jump chippartner
        
    "That's all I need about the chip.":
        jump questions
        
label chipdamage:
    v "I expect The Fringe will be trying to decrypt the information on the chip. They might have damaged it already, or there may be a risk of damage when you retrieve it from wherever they are keeping it."
    v "I admit I am not a tech expert, you may want to ask someone with more knowledge on the subject so your chosen ‘talent’ can be informed of proper handling procedure."
    jump chipquery
        
label chipdetails:
    v "…Information that is vital to my continued survival, and therefore vital to you and I having an ongoing beneficial relationship. I’d really rather not go into more detail than that."
    
menu:
    "If I’m going to retrieve this chip for you, I need to know what’s on it. Those are my terms.":
        jump valiantchipunhappy
        
    "Understood, discretion is the name of the game.":
        jump valiantchiphappy
        
label valiantchipunhappy:
    $ negativerelationshipvaliant+=1
    v "…It is a detailed list of every weak point, blind spot, and back door that can be used to take advantage of my employers for profit. My partner and I use this data to run our business, to calculate methods of producing maximum profit with minimum risk."
    v "The Fringe will use it as a battering ram to achieve short term gains. This will expose every weakness to my employers and those targets will quickly be hardened."
    v "I have worked tirelessly to erect my business, my work cannot be undone by a group of clowns with machine guns."
    jump chipquery
        
label valiantchiphappy:
    $ positiverelationshipvaliant+=1
    v "Thank you. I promise there is nothing on the chip that you need to be concerned about, the information it contains is uniquely valuable to me."
    jump chipquery
        
label chippartner:
    v "And my partner appears to care more about money than he does my safety. This situation calls for pragmatism, not sentimentality. Our business arrangement is certainly terminated."
    v "Given his behavior I have no obligation to save him. If you can rescue him, we’ll consider it a lucky bonus for him, but the data chip is all I need. I hope you don’t have a problem with that."
    jump chipquery
    
label money:
    v "Thirty thousand dollars for retrieval of the data chip and delivery into my hands. As speed is of the essence, I will pay you the full amount up front to facilitate hiring of talent and any other preparations you deem necessary. I cannot go any higher for this operation."
label moneyquery:
    v "What else do you need to know?"
    
menu:
    "That’s a lot of money. Is that a typical price for this kind of job?":
        jump moneyprice
        
    "How are you going to pay me?":
        jump moneyhow
        
    "You said I can keep what I don’t spend?":
        jump moneykeep
        
    "I’ll make good use of the money, but I have other questions.":
        jump questions
        
label moneyprice:
    v "It’s considerably more than someone would usually pay for this sort of job. I need the job done fast and you will need money to make connections and get the job done, both factors have been accounted for and your pay has been increased accordingly."
    v "The price is more than fair, remember I am doing you a significant favor here, this will help you break into the industry."
        
menu:
    "It sounds like you’re desperate and time is running out. The price needs to come up.":
        jump valiantmoneyunhappy
        
    "It’s more money than I’ve seen in my life. Definitely seems fair.":
        jump valiantmoneyhappy
        
label valiantmoneyunhappy:
    $ negativerelationshipvaliant+=1
    v "Not desperate enough to be strong-armed by a no-name fixer on their first job. You can negotiate payments when you have more of a reputation."
    v "For now, I am already giving you the best deal I can. Given that issues such as rent and food are likely still a problem for you, I suggest you take it."
    jump moneyquery
        
label valiantmoneyhappy:
    $ positiverelationshipvaliant+=1
    v "Of course, neither of us should be greedy. That kind of thinking is what landed my partner in all this trouble in the first place."
    jump moneyquery
        
label moneyhow:
    v "I have taken the liberty of setting up an off-shore bank for you. It cannot be traced back to you, and you won’t have to worry about taxes."
    v "I will be transferring the full amount there once our meeting is concluded. Feel free to consult with a financial expert to ensure the account is up to your standards."
    jump moneyquery
        
label moneykeep:
    v "Yes, that’s how most fixers make their money. A client such as myself will pay you a lump sum for you to spend on talent and information gathering. Whatever you don’t spend is your paycheck for the job."
    v "The more money you spend on a job, the more likely it is to succeed. That will give you a good reputation, but you won’t get very far in this city without cash. It’s up to you to balance resources for the job and your own income."
    jump moneyquery
    
label hire:
    v "…I would hope that you have some names in mind already, given the business you are in. Managing mercenary talent and fitting them to each job is one of your primary responsibilities as a fixer."
    v "I am afraid I cannot offer much guidance, you will need to gather information and make an informed decision as to who is the best choice."
    
label hirequery:
    v "…I’ll see if I can answer your questions."
    
menu:
    "Do you have a preference for how the job is handled?":
        jump hirepreference
        
    "Wait, you’ve gotta know I’m less connected than other fixers. Why not go to them?":
        jump hiresuspicious
        
    "Right, that’s all I need to know.":
        jump questions
        
label hirepreference:
    v "So long as the data chip is recovered and delivered to me safely and intact, I’m not overly concerned with the details."
    v "I certainly won’t shed any tears if The Fringe don’t live to see the sunrise, but if you’d rather handle it quietly that’s fine by me. Just don’t fail, that’s all that matters."
    jump hirequery
        
label hiresuspicious:
    v "The more reputable fixers in the city have a lot on their plate. I was not able to contract them on such short notice, and I was confident you would be willing to move fast for the promise of money."
    v "This is not a complicated job, so that’s all I need from a fixer right now. I also thought you would be grateful for the significant opportunity."
    
menu:
    "That doesn’t make sense. No way the bigger fixers can’t move fast enough to deal with this job. Why me?":
        jump valianthireunhappy
        
    "I guess I’m lucky they’re all so busy, I’ll happily fill the niche.":
        jump valianthirehappy
        
label valianthireunhappy:
    $ negativerelationshipvaliant+=1
    v "…Fine. I was concerned that a fixer with better connections would see more profit in taking advantage of my situation rather than helping me."
    v "They might try to take the data chip for themselves and use what’s on it for their own purposes. "
    v "In your case, I do not believe you have the connections to try that, and I am confident I could eliminate you and take the chip back if you did."
    v "You have far more to gain by working with me, and far more to lose by working against me. That’s how it is."
    
menu:
    "You’re working with me because you think you can kill me if I betray you!?":
        jump outrage
        
    "That’s cold, but I suppose I’d better get used to that kind of thinking.":
        jump acceptance
        
label outrage:
    v "It’s one of the factors in play, I have no intention of harming you otherwise."
    v "Think of it this way: I would be foolish not to consider the possibility of betrayal, wouldn’t you agree? And you would not want to work with a fool, would you? Now, let’s talk no more of this unpleasantness."
    jump hirequery
        
label acceptance:
    v "I agree, and I would encourage you to start thinking along those lines yourself. My level of caution is common in this business, but there may be others out there who would rather turn on you than pay you."
    v "Best be cautious yourself in that case, don’t you think? Now…"
    jump hirequery
        
label valianthirehappy:
    $ positiverelationshipvaliant+=1
    v "Luck is simply opportunity plus preparedness. When an opportunity came your way, you were ready to seize it. That is the pathway to success, remember that. "
    jump hirequery

label end:
    if positiverelationshipvaliant>negativerelationshipvaliant:
        v "Excellent! You have been very thorough, I am impressed. I must admit a certain degree of trepidation in hiring such a green fixer, but you have assuaged my worries."
        v "I wish you the best of luck, I hope you will have good news when next we speak."
        jump conclusion
            
    else:
        v "…Yes. Please remember, I am placing a great deal of trust in you. I could have easily contacted a more reputable fixer."
        v "I am doing you a significant favor here, do not disappoint me. I hope you will have good news when next we speak."
        jump conclusion
            
label conclusion:
    "And with that, Mr. Valiant’s digital form phases out of your vision with a curt nod. The call disconnects a moment later, leaving you alone once more in your cramped apartment." 
    "A notification on your terminal draws your attention, it tells you that thirty thousand dollars have been transferred to your account. Suddenly, the apartment seems just a little bigger." 
    "All you have to do now… Is earn it."