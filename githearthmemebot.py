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

comment_cache = deque(maxlen=200)

kappa = [("(^|[^A-Za-z0-9\'\"])[Gg][Ii][Tt] [Gg][Uu][Dd]([^A-Za-z0-9\'\"]|$)", "    git: 'gud' is not a git command. See 'git --help'."),
         ("^[Gg]it \-?\-?[Hh]elp$", "See [here](https://education.github.com/git-cheat-sheet-education.pdf) for more information."),
         ("^[^A-Za-z0-9]*[Aa][Ll][Ll] *[Mm][Ii][Nn][Ii][Oo][Nn][Ss][^A-Za-z0-9]*$", "**Taunt. Taunt. Taunt. Taunt. Taunt.**"),
         ("([^A-Za-z0-9]*[Tt][Aa][Uu][Nn][Tt][^A-Za-z0-9]*){3,}", "She friendly minion."),
         ("[Ss]he *[Ff]riendly *[Mm]inion[^A-Za-z0-9]*$", "Destroy your hero and replace it with Purlot."),
         ("(^|[^A-Za-z0-9])[Pp][Uu][Rr][Ll][Oo][Tt]([^A-Za-z0-9]|$)", "Deal 1 damage to a minion and Peter it."),
         ("(^|[^A-Za-z0-9])[Pp][Rr][Ii][Ee][Ss][Tt][Ss]?([^A-Za-z0-9]|$)", "Until Blizzard decides to nerf Priest don't bother playing PvP. The frustration is unbearable and unavoidable as he is everywhere and nearly impossible to beat. I say nearly because there is luck and player error on their part but that's the only way you'll win. He's just too OP, his spell's low mana costs compared to the power they have combined with the minions he has just makes a guy who can use only 5 mana to make a 20/20 minion. No other class compares without having extremely well developed deck that takes time and/or money to make; EVEN THEN it is no guarantee because even his basic deck can go head to head with that. Please nerf him Blizzard he's cancer and is ruining the game."),
         ("[Vv][Oo][Ll][Cc][Aa][Nn][Oo][Ss][Aa][Uu][Rr]", "That volcanosaur is pretty good with cannot be targeted adapt"),
         ("(^|[^A-Za-z0-9])[Hh][Uu][Nn][Tt][Ee][Rr][Ss]?([^A-Za-z0-9]|$)", "I was playing a ton of Hunter today on ladder and I noticed something pretty fucked up. Why is it that almost every time I play Alleycat, the Alleycat gets killed first? When I played another hunter, why did they always trade in their Alleycat before Tabbycat? Or let Tabbycat be the only one to feel the glorious power of Crackling Razormaw?It seemed really strange to me that everyone would be so negligent of Alleycat, so I started digging for answers. I went on the subreddit, I watched streamers, I even started adding people I played, and everyone told me the same thing: Tabbycat is Cute Cat, and Alleycat is Ugly Cat.\n\n\"Cute Cat.\" What. The. Fuck.\n\nSeriously, what the fuck? First, that name doesn't even make sense. I'm more of a snek guy than a cat guy, but I still know a cute cat when I see one, and they're both cute. Seriously, I can acknowledge that Tabbycat is cute. Those beautiful green eyes say, \"hey, wanna hang out?\" He has an adorable stance too, very triumphant. He looks a little too big for his britches, and it is cute! I get that!\n\nBut Alleycat is JUST AS CUTE, PEOPLE. His eyes betray a little timidness. Maybe he's nervous because he likes you so much, but is he not still walking towards you? Coming to play, even though there's some sewer gunk in front of him? He's looking right up at you and he looks more humble, more appreciative. Also, his tooth jewelry is a little more tasteful IMO. The only problem I see is a little underbite, but maybe he's just chewing something! A cat has to eat!\n\nI honestly hate to bring this up, but look at the background of Alleycat's art, too. Tabbycat is there, and he looks like a total asshole! Look, he's probably just waking up from a nap or something so I don't want to make any huge assumptions, but come on. Are you really going to tell me with that face that Tabbycat has a \"cute cat\" personality?\n\nI know this seems dumb, but as someone who suffers from acne, who is a little overweight, and who doesn't have the most symmetrical face, I feel the sting of \"Ugly Cat.\" Yeah, I'm Ugly Cat, and it feels like I get killed first too, even though I have the exact same value as the Cute Cat. And everytime Ugly Cat gets shafted in the game, I have to just take it like its my fault. Well, it's not my fault.\n\nIT'S NOT MY FUCKING FAULT I'M AN UGLY PIECE OF SHIT. IF A GIRL WOULD GIVE ME A FUCKING CHANCE I THINK PEOPLE WOULD UNDERSTAND THAT BUT THEY DON'T BECAUSE THEY'RE TOO BUSY WITH CUTE CAT CHADS.\n\nFuck you for printing this card Blizzard, it makes your playerbase feel specifically targeted. After I go buy 10 packs I'm totally never giving you money again except for preorders or if I'm missing a legendary."),
         ("(^|[^A-Za-z0-9])[Bb][Ll][Ii][Zz][Zz]", "I've been a hearthstone player for 5 years, and I've been the most unlucky person that has ever existed. I have opened 41 packs from every single expansion, including the unannounced upcoming expansion, and I have yet to get a single legendary, let alone an epic. Every single one of my packs has been a 40 dust pack, and I've never gotten a golden card in my lifetime. Blizzard's been telling me that the pity timer is 40 packs and that I'll definitely get one every 40 packs, but I'm living proof that this isn't true. I've never even gotten a single legendary. My collection is full of basic, common and rare cards. I didn't manage to get C'Thun because when I opened my WOTOG pack, it told me that I was the 666th person to collect the free C'Thun, so I was denied the reward. I could never buy adventures because whenever I hit the 'Confirm Purchase' button, the game would take my gold and crash, causing my gold to be lost forever. I've spent over US$10,000 on this game, and I've nothing to show for it, other than my 100 Alarm-O-Bots. The one glorious time I saw an orange glow in my packs, it turned out to be a visual glitch that the game client had just for me. When I had finally been able to buy an adventure, I could not exit the game because it displayed the 'Hearthstone is not responding' error, prompting me to delete my account. But today, when I opened a pack, I managed, at last, to get TWO rares in my pack. Not one, but two. The old gods have shined upon me today and have bestowed me with the first non-40 dust pack that I have ever opened. I have never felt more joy in my life than when I saw that I packed not one, but two alarm-o-bots from the same pack. I could not be happier. I just want to thank Blizzard. For the few pixels that have completely changed my life. I'm off to buy 1,000 more Un'Goro packs. Maybe I'll get my first epic."),
         ("[Pp][Ii][Rr][Aa][Tt][Ee][Ss]?.*[Ww][Aa][Rr][Rr]?[Ii][Oo][Rr]","I'm currently rank 24 in Wild, and this place is completely infested by Pirate Warrior bots. Out of 10 Pirate Warrior bots, 6 of them were against Pirate Warrior bots. I try to report them to piratewarriorbots.com, but it's rediculous to sit and write Pirate Warrior bot scripts all night when you want to enjoy Pirate Warrior bots This is a Pirate Warrior bot. One can argue about how fun and interactive Pirate Warrior bots is to begin with, but having to play against a Pirate Warrior bots that has a 7 second interval Pirate Warrior bots every single action is so boring and Pirate Warrior bots make you want to quit the game.Blizzard, Pirate Warrior bots is ruining your Pirate Warrior bots, and you need ot stay on top of Pirate Warrior bots. In it's current Pirate Warrior bots Wild is close to Pirate Warrior bots, and I fear Pirate Warrior bots is the next target if we don't see Pirate Warrior bots soon. (For what it's worth, it seems like Pirate Warrior bots share a names with reddit spam Pirate Warrior bots) EDIT: Since many Pirate Warrior bots are asking in the comments, these are signs that you might be facing Pirate Warrior bots: *Most obvious clue is how long time Pirate Warrior bots spend between each action. f2p player don't think it's always the same interval between each action, but the bots \"think\" way too long between each action. Like if Pirate Warrior bots have 5 dudes on the board and mine is empty, Pirate Warrior bots spend 30-40 seconds wacking em in the face because Pirate Warrior bots \"think\" between each minion going face. *Pirate Warrior bots also randomly look at cards in their hand, even if Pirate Warrior bots have only 1 card in hand in it's been there for ages. *Incredibly dumb plays like playing Heroic Strike when hero is frozen (this could happen depending on rank of course) *Also, Pirate Warrior bots never concede even though Pirate Warrior bots're out of cards and f2p player just played Reno/Amara. *My personal emote-trigger test (don't do this at home): BM as much as humanly possible, try to rope a few turns. f2p player try to trigger at least an emote from your opponent, it's strengthens your assuption about your opponent being a bot. Note: of course worthless test without any others signs of Pirate Warrior bots. f2p btw"),
         ("[Dd][Ii][Ss][Cc][Oo][Vv][Ee][Rr]","As much as most of us seem to hate the pirate meta. Something I want to get off of my chest is how unfair I think Drakonid Operative is, and how it compares to another, better designed Discover card. Let's compare Drakonid Operative to Jeweled Scarab, which in my opinion is still the best designed discover card to date. When you play Scarab, not only is it a 2 mana 1/1, which in this meta is awful. But on the rare occasion you may discover great like Brann which can swing the game, or Mind Control Tech which is only good in certain situations. But other options include: Silverback Patriarch, Magma Rager, Dalaran Mage etc. So while on rare occasions you may get something good, there are a lot of terrible 3 cost cards that Scarab can discover. Now, Drakonid Operative. Operative unlike Scarab has great stats for its cost. You get intel on your opponents deck. 'Oh, he's running Mind Control Tech? Good to know, now I can play around that'. And you will always discover a good/great card. Because obviously your opponent is going to have a deck full of cards they deem solid enough to win them matches. Unless you're a brand new player or you're playing some gimmick deck, all your cards are going to be high tier cards. The other glaring issue is that you can use multiple Operatives in a single match to gain even more knowledge on what you're up against. And what your opponent doesn't have in their hand yet. If discovered with Historian and multiple Operatives are used with Brann, Priest could easily see 1/3rd of your entire deck. Now I know come the first 2017 expansion Dragon Priest is going to take a massive hit anyway. Losing Technician, Guardian, Corrupter etc. So unless Blizzard introduces card good enough to replace them, Dragon Priest will see far less play. But at the moment, unlike Patches or Buccaneer, the card I hate playing against the most is Drakonid Operative. tl;dr. Jeweled Scarab is a really well designed discover card and in my opinion the best designed in the game. Drakonid Operative is not."),
         ("(^|[^A-Za-z0-9])[Bb][Ll][Aa][Dd][Ee]?([^A-Za-z0-9]|$)","The problem was the interaction with blade flurry. Now, as it is, even the old blade flurry would be a balanced blade flurry.\n\nWithout blade flurry giving us extra blade flurry we're completely defenseless as soon as the opponent's blade flurry is getting a blade flurry. Almost every blade flurry can deal with a spell like blade flurry, but for Rogue a card like blade flurry almost wins the blade flurry on its own.\n\nI'm OK with Rogue having no blade flurry, but ffs, blade flurry is NEEDED in this card game.\n\nNot having blade flurry makes Rogue almost unable to develop blade flurry other than blade flurry; which is a sad thing because blade flurry, blade flurry or “blade flurry” Rogue for instance are super cool decks to blade flurry."),
         ("(^|[^A-Za-z0-9])[Gg][Ww][Ee][Nn][Tt]","Gwent is gwent, but it could be a longterm gwent. The gwent in Gwent is really gwent, but Gwent on the other hand only has less gwent. I gwent that Gwent might become the next Gwent, actually it could even gwent the gwent Gwent.\n\nA gwenty Gwent you Gwent"),
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
    print(c.selftext)
    c.reply(r)

start_time = time.time()
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
            if comment.id in comment_cache:
                break
            comment_cache.append(comment.id)
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