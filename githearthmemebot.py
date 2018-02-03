#!/usr/bin/python
# coding=UTF8
import praw
import re
from collections import deque
from time import sleep
from datetime import datetime
import sys
import time

username = "CasualHearthMemeBot"

reddit = praw.Reddit('bot2')

# /r/hearthstone refugee
subreddit = reddit.subreddit("hearthstonecirclejerk")

kappa = [("(^|[^A-Za-z0-9\'\"])[Gg][Ii][Tt] [Gg][Uu][Dd]([^A-Za-z0-9\'\"]|$)", "    git: 'gud' is not a git command. See 'git --help'."),
         ("^[Gg]it \-?\-?[Hh]elp$", "See [here](https://education.github.com/git-cheat-sheet-education.pdf) for more information."),
         ("^[^A-Za-z0-9]*[Aa][Ll][Ll] *[Mm][Ii][Nn][Ii][Oo][Nn][Ss][^A-Za-z0-9]*$", "**Taunt. Taunt. Taunt. Taunt. Taunt.**"),
         ("([^A-Za-z0-9]*[Tt][Aa][Uu][Nn][Tt][^A-Za-z0-9]*){3,}", "She friendly minion."),
         ("[Ss]he *[Ff]riendly *[Mm]inion[^A-Za-z0-9]*$", "Destroy your hero and replace it with Purlot."),
         ("(^|[^A-Za-z0-9])[Pp][Uu][Rr][Ll][Oo][Tt]([^A-Za-z0-9]|$)", "Deal 1 damage to a minion and Peter it."),
         ("(^|[^A-Za-z0-9])[Pp][Rr][Ii][Ee][Ss][Tt][Ss]?([^A-Za-z0-9]|$)", "Until Blizzard decides to nerf Priest don't bother playing PvP. The frustration is unbearable and unavoidable as he is everywhere and nearly impossible to beat. I say nearly because there is luck and player error on their part but that's the only way you'll win. He's just too OP, his spell's low mana costs compared to the power they have combined with the minions he has just makes a guy who can use only 5 mana to make a 20/20 minion. No other class compares without having extremely well developed deck that takes time and/or money to make; EVEN THEN it is no guarantee because even his basic deck can go head to head with that. Please nerf him Blizzard he's cancer and is ruining the game."),
         ("[Vv][Oo][Ll][Cc][Aa][Nn][Oo][Ss][Aa][Uu][Rr]", "That Volcanosaur is pretty good with cannot be targeted adapt"),
         ("([Tt][Aa][Ll][Dd][Aa][Rr][Aa][Mm]|[Qq]uest[^A-Za-z0-9]*[Pp][Aa][Ll][Aa][Dd][Ii][Nn])","I get that everyone is looking at the 99% scenario where Prince Taldaram is a vanilla 3 mana 3/3; however, only true card game wizards like me can see the brilliance and overpoweredness in the design of this card.\n\nImagine this scenario - t1 your hand is pyroblast, pyroblast, fireball, frost nova\n\nYour opponent is druid and innervates out a millhouse manastorm. You topdeck shatter, and you play out your entire hand, leaving the druid at 4 health and killing his millhouse. Now, at this point, you're screwed, since you included only zero attack minions for the entire rest of your deck. The druid can simply hero power out of lethal range every time you ping.\n\nHowever!!! You have Prince Taldaram in your deck, which is not a zero attack minion. You coin it out to copy the opponent's vicious fledgling. A 3 mana 3/3 that adapts every time it attacks a hero? broken!\n\nYour opponent misplays by hitting face with his vicious fledgling, and you take the win.\n\nI realize that some bad players may object to my example, and I do agree there a few flaws. For example, the example that I just gave is a fairly unlikely scenario; it would only happen in 50% of all games. Furthermore, people might say why use Prince Taldaram when you could use vicious fledgling. Well, the answer is simple: if you included vicious fledgling in your deck, then Prince Taldaram's effect wouldn't activate. Obviously you can't include vicious fledglings in your deck.\n\nThis card is insanely good and is being underrated just like paladin quest was. In fact, I am so confident this card will be in all competitive decks after KFT release that I will even downvote my own post if I am wrong."),
         ("(^|[^A-Za-z0-9])([Hh][Uu][Nn][Tt][Ee][Rr][Ss]?|[Cc][Aa][Tt][Ss]?)([^A-Za-z0-9]|$)", "I was playing a ton of Hunter today on ladder and I noticed something pretty fucked up. Why is it that almost every time I play Alleycat, the Alleycat gets killed first? When I played another hunter, why did they always trade in their Alleycat before Tabbycat? Or let Tabbycat be the only one to feel the glorious power of Crackling Razormaw?It seemed really strange to me that everyone would be so negligent of Alleycat, so I started digging for answers. I went on the subreddit, I watched streamers, I even started adding people I played, and everyone told me the same thing: Tabbycat is Cute Cat, and Alleycat is Ugly Cat.\n\n\"Cute Cat.\" What. The. Fuck.\n\nSeriously, what the fuck? First, that name doesn't even make sense. I'm more of a snek guy than a cat guy, but I still know a cute cat when I see one, and they're both cute. Seriously, I can acknowledge that Tabbycat is cute. Those beautiful green eyes say, \"hey, wanna hang out?\" He has an adorable stance too, very triumphant. He looks a little too big for his britches, and it is cute! I get that!\n\nBut Alleycat is JUST AS CUTE, PEOPLE. His eyes betray a little timidness. Maybe he's nervous because he likes you so much, but is he not still walking towards you? Coming to play, even though there's some sewer gunk in front of him? He's looking right up at you and he looks more humble, more appreciative. Also, his tooth jewelry is a little more tasteful IMO. The only problem I see is a little underbite, but maybe he's just chewing something! A cat has to eat!\n\nI honestly hate to bring this up, but look at the background of Alleycat's art, too. Tabbycat is there, and he looks like a total asshole! Look, he's probably just waking up from a nap or something so I don't want to make any huge assumptions, but come on. Are you really going to tell me with that face that Tabbycat has a \"cute cat\" personality?\n\nI know this seems dumb, but as someone who suffers from acne, who is a little overweight, and who doesn't have the most symmetrical face, I feel the sting of \"Ugly Cat.\" Yeah, I'm Ugly Cat, and it feels like I get killed first too, even though I have the exact same value as the Cute Cat. And everytime Ugly Cat gets shafted in the game, I have to just take it like its my fault. Well, it's not my fault.\n\nIT'S NOT MY FUCKING FAULT I'M AN UGLY PIECE OF SHIT. IF A GIRL WOULD GIVE ME A FUCKING CHANCE I THINK PEOPLE WOULD UNDERSTAND THAT BUT THEY DON'T BECAUSE THEY'RE TOO BUSY WITH CUTE CAT CHADS.\n\nFuck you for printing this card Blizzard, it makes your playerbase feel specifically targeted. After I go buy 10 packs I'm totally never giving you money again except for preorders or if I'm missing a legendary."),
         ("[Rr][Ii][Gg][Gg][Ee][Dd]","Played the game since beta, about four years now, every..single..day. Here's some observations. If you have ever got the feeling the matches and matchmaking was rigged, you are correct. Although nothing can be 100% proven without viewing the actual programmed code for the game, the fact remains that collectively many humans experience, intuition, and millions of play time hours is just as powerful as seeing code. And where there is smoke, there is fire. It's been a rigorous issue for many years, and staunchly defended by Blizzard and concealed in their forums. A genuine third party confirmation has never even been offered to put the question to bed. The game is free to play..But it is rigged, preprogrammed probably to force a 50/50 win rate.. so, you can only really gain up ladder on player misplays, which can be hard to setup. The card drawing is rigged in favor of the hero that directly counters the others deck. When you win a match, the next match your more likely to lose. The heroes all each have at least three counter heroes. 9 total heros, each has three. When you are matched with your heroes counter, your card draw is negatively affected, and the opponents is positively affected. Play a few hundred games and it becomes clear as day. The more games you attempt in a short period of time, it will increase your chances of matching your deck to a counter deck and likely cause you to lose more often. When you make a deck card change, your first match you will likely lose, being outmatched. Also the more games in a row you win, your chances of seeing a counter to your deck increase as you gain on ladder. Your cards are often exacting matched with opponents in the matchmaking. Also counters to your cards. Which often will be top-carded if your hero has to play its counter hero. Even seemingly random cards ..are not at all, the game will create the corresponding outcome for the board state., For example the mech shredder with deathrattle will put out the perfect counter minion often if your hero is the favoured over the opponents. How man times does mech shredder have to put out a doomsayer to destroy your board. The less value cards in your deck, the faster your game plays. Higher values such as 4+ mana cost, will match you to players with higher cards and healing etc. lengthening the match.. One card over 4 mana in your deck could cause you to be matched to a priest that comes back at turn 5 and beats you with heals. Legendaries don't help. They just don't. They offer a chance at winning, but if you fail to use it at the right time, you lose. You will just be overmatched for whichever or how many ever legendaries you stack in your deck with a counter opponent found in matchmaking. Stack 6+ legendaries in your deck and watch as you get matched to a deck that counters every one of your legendaries perfectly.. The matches are predecided to favor one player over the other. This may even include how often you have purchased. You may be the best player, but stuck at rank 20-15 for a purchase-to-time ratio algorithm. There may even exist a seperate matchmaking pool for this purpose. Blizzard employees search out forums and posts that discuss how rigged the game is. Then blast many many \"anti-rigged\" posts from various user IDs. Note all the comments will say confirmation bias, tinfoil hat, and cast insults mainly. You can see the shotgun blast of posts on THE same day just below. Its pretty wild that companies do this to stay afloat. Blizzard eSport tournaments \"cherry pick\" the players that are selected to play ..based on their \"work\" they contribute to Hearthstone. This means you will be vetted for your postings on forums, YouTube streams, etc. Any potentially percieved negative opinions of the game such as my post here, will prevent you from admission to their rigged tournaments. Obviously, they dont want the secret out, and dont want popular tournament winning players catching on and publicizing it later either. The message is this.. \"Either act right..or you lose and wont be invited to tournaments no matter what you achieve on ladder.\""),
         ("([Mm][Uu][Rr][Ll][Oo][Cc])|([Hh][Yy][Dd][Rr][Oo][Ll])","As one of the only two murlocs who have learned to speak the human language, along with Sir Finley, Hydrologist cements her rank and prestige amongst murlocs, and amongst ALL creatures in her world, in or out of Un'goro. She is a smart, independent hydrologist who don’t need no murloc warleader. According to the Bureau of Labor Statistics, our lovely Hydrologist makes about $38 per hour and $80,000 per year. If you see her on Tinder make sure you have a solid life foundation, because you probably won’t be able to keep up with her. Obviously having gone to one of the most prestigious universities in her world, Hydrologist is used to class and civility. As you can hear in her death quote 'Excuse me..', she expresses that she is only fighting to protect her discoveries! She does not want to fight, but sometimes these things must be done. As one of her best friends always says, 'Justice demands retribution!' Hydrologist is no stranger to success, as she has discovered some of the world's best kept secrets. She has found the ability to make even the most menacing of foes kneel in repentance and forfeit of their evil ways. She has found a way to make her friends in battle rise from the dead, to swing the sword one more time in their shining moment of redemption. She has the charisma to rally even the least of her friends to lay down their life in the most noble sacrifice, to die for one’s friends. She is truly a saint amongst all creatures and, oh by the way, a very good hydrologist to boot! She is really passionate about researching ways to minimize the negative impacts of erosion, sedimentation, or pollution on the environment in Un’goro, and it shows. She knows no equal in her field. Too be so accomplished is truly amazing, but to be a total babe at the same time? Some creatures really do have everything, don't they? Our Hydrologist is a lovey murloc with long locks of red hair, and luscious lips. She is cute and she knows it, that is why she wears a flower on her hat. And you know what they say about females with red hair don't you? She definitely lets loose during the night time, but stays civil and classy during the day. As you can hear in her fight quote 'Mrrgglll mrgglll mrrgll.. heh heh', she sometimes loses herself in a moment of passion, but quickly realizes she what she is doing and decides to pull back. She is passionate in so many ways, but knows when and where to let totally lose. With so many suitors have failed in their attempts to woo her (most notably Sir Finley, Finja, and Uther) it is clear that Hydrologist just doesn’t have time for love. She is married to her work. So the next time you play Hydrologist onto your board, or put her in your deck, or discover her with your broken Dragonid OPerative, respect the grace you have the honor to behold. And thank the gods that you are allowed to put two copies of her in your deck, for she is truly legendary. In fact she was slated as a legendary minion that could only be summoned if you played 3 Tirions, but she asked to be made a common. Why you ask? She said it's because she loves the kids. What a lady!"),
         ("[Pp][Ii][Rr][Aa][Tt][Ee][Ss]?.*[Ww][Aa][Rr][Rr]?[Ii][Oo][Rr]","I'm currently rank 24 in Wild, and this place is completely infested by Pirate Warrior bots. Out of 10 Pirate Warrior bots, 6 of them were against Pirate Warrior bots. I try to report them to piratewarriorbots.com, but it's rediculous to sit and write Pirate Warrior bot scripts all night when you want to enjoy Pirate Warrior bots This is a Pirate Warrior bot. One can argue about how fun and interactive Pirate Warrior bots is to begin with, but having to play against a Pirate Warrior bots that has a 7 second interval Pirate Warrior bots every single action is so boring and Pirate Warrior bots make you want to quit the game.Blizzard, Pirate Warrior bots is ruining your Pirate Warrior bots, and you need ot stay on top of Pirate Warrior bots. In it's current Pirate Warrior bots Wild is close to Pirate Warrior bots, and I fear Pirate Warrior bots is the next target if we don't see Pirate Warrior bots soon. (For what it's worth, it seems like Pirate Warrior bots share a names with reddit spam Pirate Warrior bots) EDIT: Since many Pirate Warrior bots are asking in the comments, these are signs that you might be facing Pirate Warrior bots: *Most obvious clue is how long time Pirate Warrior bots spend between each action. f2p player don't think it's always the same interval between each action, but the bots \"think\" way too long between each action. Like if Pirate Warrior bots have 5 dudes on the board and mine is empty, Pirate Warrior bots spend 30-40 seconds wacking em in the face because Pirate Warrior bots \"think\" between each minion going face. *Pirate Warrior bots also randomly look at cards in their hand, even if Pirate Warrior bots have only 1 card in hand in it's been there for ages. *Incredibly dumb plays like playing Heroic Strike when hero is frozen (this could happen depending on rank of course) *Also, Pirate Warrior bots never concede even though Pirate Warrior bots're out of cards and f2p player just played Reno/Amara. *My personal emote-trigger test (don't do this at home): BM as much as humanly possible, try to rope a few turns. f2p player try to trigger at least an emote from your opponent, it's strengthens your assuption about your opponent being a bot. Note: of course worthless test without any others signs of Pirate Warrior bots. f2p btw"),
         ("([Ww][Aa][Rr][Ll][Oo][Cc][Kk]|[Ll][Aa][Kk][Kk][Aa][Rr][Ii]|[[Dd][Ii][Ss][Cc][Aa][Rr][Dd][Ll])","Like many others, I believed the reviews on the new Warlock quest and happily sacrificed two useless legendaries and a lot of dust to Lakkari. And I thought it was worth it - for the last few months, I've played hundreds of Discolock games in Wild and reached the heady heights of Rank 15 last week. Imagine my excitement today when, for the first time, my Turn 2 Soulfire to Face didn't discard Doomguard, and I got to play it three turns later! But then I heard its Attack cry. WTF? A poultry tax? What does it mean? Is it going to nerf my Angry Chicken? Steal a whelp from Leeroy? I conceded, spent the next 10 minutes googling, but still couldn't find ANY explanation for this cry. What type of poultry tax? Is it some kind of subtle political message? Why does he say this? I can't continue playing Discolock without knowing. It's absolutely ridiculous that Blizzard should have a card say something totally weird without any explanation. I've been playing for five years now, and I'm still too nervous to continue with the deck. It must be incredibly scary for a new player to get such incomprehensible messages. If I dust all my warlock cards, I may have enough to get The Marsh Queen."),
         ("(^|[^A-Za-z0-9])[Aa][Yy][Aa]([^A-Za-z0-9]|$)|(^|[^A-Za-z0-9])[Jj][Aa][Dd][Ee]([^A-Za-z0-9]|$)","Aya Blackpaw is the reason I work out. I have this fantasy where we start talking at Talan's Bar with her approaching me saying 'Golems are a girl's best friend.' We exchange a few pleasantries. She asks what I do. I say i'm a main Aggro Shaman. She laughs. I get my drink.\n\n'Greetings, friend.' I say and walk away. I've got her attention now. How many guys voluntarily leave a conversation with Aya Blackpaw? She touches her neck as she watches me leave. Later, as the night's dragged on and the coterie of gorgeous narcissists grows increasingly loose, she finds me on the balcony, my bowtie undone, summoning a jade golem. 'Got a spare?' she asks.\n\n'What's in it for me?' I say as I hand her one of my big green boys. She smiles.\n\n'Conversation with me, duh.'\n\nI laugh.\n\n'What's so funny?' she protests.\n\n'Nothing, nothing... It's just... don't you grow tired of taunt minions?'\n\n'You get used to it,' she says, placing her 7/7 and handing me back the 8/8.\n\n'What would you do if you weren't a playable card?' I ask.\n\n'Jade druid, I think.'\n\n'And if I was your student, what would I be learning?'\n\n'Infinite value,' she says quickly, looking up into my eyes, before changing the subject. 'Where are you from?'\n\n'Gadgetzan,' I say.\n\n'Oh wow. That's lovely.'\n\n'It's ok,' I admit. 'Not everything is to my liking.'\n\n'What could possibly be not to your liking in Gadgetzan?' she inquires.\n\n'I don't like Kazakus,' I tell her. 'It's coarse and rough and irritating and it gets everywhere.'"),
         ("(^|[^A-Za-z0-9])[Gg][Ww][Ee][Nn][Tt]","Gwent is gwent, but it could be a longterm gwent. The gwent in Gwent is really gwent, but Gwent on the other hand only has less gwent. I gwent that Gwent might become the next Gwent, actually it could even gwent the gwent Gwent.\n\nA gwenty Gwent you Gwent"),
         ("[Dd][Ii][Ss][Cc][Oo][Vv][Ee][Rr]","As much as most of us seem to hate the pirate meta. Something I want to get off of my chest is how unfair I think Drakonid Operative is, and how it compares to another, better designed Discover card. Let's compare Drakonid Operative to Jeweled Scarab, which in my opinion is still the best designed discover card to date. When you play Scarab, not only is it a 2 mana 1/1, which in this meta is awful. But on the rare occasion you may discover great like Brann which can swing the game, or Mind Control Tech which is only good in certain situations. But other options include: Silverback Patriarch, Magma Rager, Dalaran Mage etc. So while on rare occasions you may get something good, there are a lot of terrible 3 cost cards that Scarab can discover. Now, Drakonid Operative. Operative unlike Scarab has great stats for its cost. You get intel on your opponents deck. 'Oh, he's running Mind Control Tech? Good to know, now I can play around that'. And you will always discover a good/great card. Because obviously your opponent is going to have a deck full of cards they deem solid enough to win them matches. Unless you're a brand new player or you're playing some gimmick deck, all your cards are going to be high tier cards. The other glaring issue is that you can use multiple Operatives in a single match to gain even more knowledge on what you're up against. And what your opponent doesn't have in their hand yet. If discovered with Historian and multiple Operatives are used with Brann, Priest could easily see 1/3rd of your entire deck. Now I know come the first 2017 expansion Dragon Priest is going to take a massive hit anyway. Losing Technician, Guardian, Corrupter etc. So unless Blizzard introduces card good enough to replace them, Dragon Priest will see far less play. But at the moment, unlike Patches or Buccaneer, the card I hate playing against the most is Drakonid Operative. tl;dr. Jeweled Scarab is a really well designed discover card and in my opinion the best designed in the game. Drakonid Operative is not."),
         ("(^|[^A-Za-z0-9])[Bb][Ll][Aa][Dd][Ee]?([^A-Za-z0-9]|$)","The problem was the interaction with blade flurry. Now, as it is, even the old blade flurry would be a balanced blade flurry.\n\nWithout blade flurry giving us extra blade flurry we're completely defenseless as soon as the opponent's blade flurry is getting a blade flurry. Almost every blade flurry can deal with a spell like blade flurry, but for Rogue a card like blade flurry almost wins the blade flurry on its own.\n\nI'm OK with Rogue having no blade flurry, but ffs, blade flurry is NEEDED in this card game.\n\nNot having blade flurry makes Rogue almost unable to develop blade flurry other than blade flurry; which is a sad thing because blade flurry, blade flurry or “blade flurry” Rogue for instance are super cool decks to blade flurry."),
         ("(^|[^A-Za-z0-9])[Rr][Oo][Gg][Uu][Ee][Ss]?([^A-Za-z0-9]|$)", "> RO**UG**E\n\nFTFY^Kappa"),
         ("^<[\-~]{2,}", "f2p btw"),
         ("(^|[^A-Za-z0-9])[Rr][Oo][Aa][Cc][Hh] *[Bb][Oo][Yy]([^A-Za-z0-9]|$)", "Support the pyramid roach boy =)")]
kappa = map(lambda x: (re.compile(x[0]), x[1]), kappa)

def check_condition(c, regex):
    if username == c.author.name:
        return False
    matches1 = set(re.findall(regex, c.title))
    matches2 = set(re.findall(regex, c.selftext))
    return True if matches1 or matches2 else False

def bot_action(c, r):
    print(c.selftext.encode('utf-8'))
    c.reply(r)

start_time = time.time()
ref_time = start_time - 90
print "bot is running..."
running = True
i = 0
backoff = 8
while running:
    try:
        if time.time() - start_time > 42000:
            print("I'm gonna rest for a bit...")
            sys.exit(0)
        commentz = subreddit.new(limit=1)
        i = (i + 1) % 65536
        if i % 256 == 0:
            print i
        for comment in commentz:
            if comment.created_utc <= ref_time:
                break
            ref_time = comment.created_utc + 1
            for x in kappa:
                bot_condition_met = check_condition(comment, x[0])
                if bot_condition_met:
                    bot_action(comment, x[1])
                    break
                backoff = 8
        time.sleep(30)
    except KeyboardInterrupt:
        running = False
    except Exception as e:
        print("[ERROR]:{}".format(e))
        print("sleeping in {} sec".format(backoff))
        sleep(backoff)
        if backoff < 1024:
            backoff = backoff * 2
