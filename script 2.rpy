# You can place the script of your game in this file.
# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image car = "chart.png"
image hallway = "Screen Shot 2015-04-19 at 11.40.01 PM.png"
image bike = "1111.jpg"
image motor = "_MG_7338.jpg"
image hangzhou = "IMG_2069.jpg"
image mayun = "Bloomberg1.png"
image mayun2 = "Screen Shot 2015-04-19 at 9.19.49 PM.png"
image ma = "ma.png"
image pi = "IMG_3483.png"
image p2 = "Screen Shot 2015-04-19 at 6.24.55 PM.png"
image p3 = "Screen Shot 2015-04-19 at 6.25.11 PM.png"
image p4 = "Screen Shot 2015-04-19 at 6.26.03 PM.png"
image a1 = "IMG_4198 2.JPG"
image a2 = "IMG_4188.JPG"
image a3 = "1426252829413588.jpg"
image a4 = "Screen Shot 2015-04-19 at 8.53.03 PM.png"
image a5 = "Screen Shot 2015-04-19 at 9.00.06 PM.png"
image a6 = "_MG_7613.JPG"
image a7 = "Screen Shot 2015-04-19 at 9.45.44 PM.png"
image a8 = "Screen Shot 2015-04-19 at 9.52.54 PM.png"
image a9 = "Screen Shot 2015-04-19 at 9.58.54 PM.png"
image a10 = "_MG_7616.JPG"
image a11 = "Screen Shot 2015-04-19 at 10.11.35 PM.png"
image a12 = "Screen Shot 2015-04-19 at 10.17.11 PM.png"
image a13 = "Screen Shot 2015-04-19 at 10.22.03 PM.png"
image a14 = "Screen Shot 2015-04-19 at 10.24.33 PM.png"
image life = "life-of-pi1.png"
image blush_open = "li you blush open.png"
image concerned = "li you concerned.png"
image discontent = "li you discontent.png"
image mad = "li you mad.png"
image easy = "easy.png"
image chart = "chart.png"
image p1 = "Screen Shot 2015-04-19 at 6.24.45 PM.png"
image end = "Screen Shot 2015-04-19 at 11.35.14 PM.png"

# Declare characters used by this game.
define m = Character('Jack Ma',color="#CFCFCF")
define l = Character('Pi', color="#FF66CC")
define n = Character('Narrator', color = "#FFFFFF")
define g = Character('Analysis', color = "#CFCFCF")
define s = Character('Statistics', color = "#CFCFCF")
define q = Character('Tom Goforth',color="#CFCFCF")
define con = Character('To Conclude', color = "#CFCFCF")
define su = Character('Suggestions', color = "#CFCFCF")



#Universal Variables?
# The game starts here.
label start:


    scene hallway
    $renpy.pause(2.2)
    
    n"With the prevalence of internet, a new way of consuming comes to our daily life."
    n"Online shopping"
   
    n "Question: Where did you buy your clothes last time?"
    menu:
        "Taobao!":
   
            call school_option1
        "Other websites":

            call school_option2
        "Exclusive shop or shopping mall":

            call school_option3
         
label online:          
    
    scene bike with dissolve 
    m "Online shopping is now in its golden era! "
    
    scene car with dissolve
    m" Unprecedented growth!"
    
    scene hangzhou with dissolve
    n" We no longer have to get out to purchase stuff."
    n" Everything can be done with an easy click on your mouse."
    
label pi1:
    scene easy with dissolve
    n "Convenient, addictive"
    n " 'Consumer addiction, a new hallmark of our era' --Richard Eckersley"


    scene life with dissolve
    n "Story time...Life of Pi " 
    
    show pi at center with moveinright
    l "Hi, my name is Pi, I am a student in Shanghai. "
    l "Consumers love my name."
    l "Because it sounds like Pay or Buy..."
    
    scene p1 with dissolve
    n "One day, Pi's friends said he will be more attractive if he change a shirt."
    n "and Pi decided to buy it on taobao."
    n" Should Pi buy it? What do you think?"
    menu:
        "Buy!":
         l "Yeah, I need it!"   
        "Of course":
         l "Yeah, I need it!"
        "Maybe not":
         l "Well, I still think I need it..."
        
        
    
    scene p2 with dissolve
    l" While searching for shirts, Pi also saw a really cool hat by chance..."
    l" It's so charming, should Pi buy it?!"
    menu:
        "Buy!":
   
         l "Yeah, I think I need it!"
        "Of course":
         l "Yeah, I think I need it!"
        "Maybe not":
         l " Anyway, I still think I need it, so..."
    
    scene p3 with dissolve
    n" After Pi got his hat, He can't help buying more and more stuff"
    n "Would Pi continue doing this?"
    menu:
        "Your heart will go on!":
   
         l "You jump, I jump, into the trap!"   
         l "But I promise it's the last time..."
        
        "No, you should stop":
         l "Sorry, I can't; my heart will go on..."
         l "But I promise it's the last time..."
         
    scene p4 with dissolve
    g "Reflection time"
    
    scene a6 with dissolve
    s "Approximately, 35.9percent of the online shopping consumers are college students just like us"
    s "About 59.3percent will shopping online regularly."
    
    g "What are some traits of addicts?"
    scene a1 with dissolve
    g "They often knowingly overspend and buy useless items."

    scene a2 with dissolve
    g "They tend to neglect their jobs and families."
    scene a3 with dissolve
    g "They lie about their purchases and what they spent."
    scene a4 with dissolve
    g "They accumulate massive amounts of debt."

    scene a5 with dissolve
    g " So how can we avoid getting addicted?"
    g " First, consider causes and triggers."
    g " Second, rational consumption"
    g " Last but not least, a good deal=/=self-actualisation."
    
    scene a7 with dissolve
    q "'In fact, addiction is not innate to human species.'"
    q "'It is something we developed to cope with our emptiness, fear, and predicament'"
    
    scene a8 with dissolve
    g "How can we find our true self?"
    scene a10 with dissolve
    su "Nature."
    scene a11 with dissolve
    su "Emptiness=>Knowledge."
    scene a12 with dissolve
    su "Find your love..."
    scene a13 with dissolve
    su "Friendship..."
    scene a14 with dissolve
    su "Aspiration and interests..."

    
    scene a9 with dissolve
    con " Remember, ¥=/=Happiness, there is more happiness that you can get without money."

    
    scene end
    $ renpy.pause(3.0)

    
    


