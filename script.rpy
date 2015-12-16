

# You can place the script of your game in this file.
# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image hallway = "hallway.jpg"
image li = "goodLiYou.png"
image wp = "wangpeng.png"
image din = "liyou_behind_table2.png"
image door = "front_door.jpg"
image restaurant = "Restaurant.png"
image waiter = "Waiter.png"
image map = "map.jpg"
image map1 = "Map1.png"
image map2 = "Map2.png"
image map3 = "Map3.png"
image theatre = "cinema.jpg"
image theatre_hallway = "Movie_hallway.jpg"
image blush_closed = "li you blush closed.png"
image blush_open = "li you blush open.png"
image concerned = "li you concerned.png"
image discontent = "li you discontent.png"
image mad = "li you mad.png"
image rage = "li you rage.png"
image sad = "li you sad.png"

# Declare characters used by this game.
define w = Character('Wang Peng',color="#0000CC")
define l = Character('Li You', color="#FF66CC")
define n = Character('Narrator', color = "#FFFFFF")
define g = Character('Waiter', color = "#CFCFCF")

#Universal Variables?
# The game starts here.
label start:
    $ happiness = 0;
    $ early = True;

    scene hallway
    n "王朋在上学的路上和李友巧遇，他准备前去搭讪"
    show li at center with moveinright
    n "How will you approach her?"
    menu:
        "嗨，你好!":
            play voice "1a.ogg"
            $ renpy.pause(2.5)
            call school_option1
        "哎，吃了吗?":
            play voice "1b.ogg"
            $renpy.pause(1.5)
            call school_option2
        "前面的，你干啥去啊?":
            play voice "1c.ogg"
            $renpy.pause(1.5)
            call school_option3
label map_scene:
    scene map1
    play voice "n1.ogg"
    play voice "n2.ogg"
    menu:
        "先向北，再向西":
            jump arrival
        "先向北，再向东":
            $ early = False
            jump arrival
    
label arrival:
    play voice "n3.ogg"
    n "这里就是李友的家了"

    if early == True:
        scene door with dissolve
        show blush_closed at center with dissolve
        ###happy face
        
        play voice "14a.ogg"
        l "这么准时啊！"
        $ happiness +=1
        show wp at right with moveinright
        menu:
            "应该的，怎么样，准备好出发啦？":
                play voice "15a.ogg"
                $ renpy.pause(3.0)
                call ontime_option1
            "电影都开始了，别磨蹭，上车":
                play voice "15c.ogg"
                $ renpy.pause(3.0)
                call ontime_option2
            "快点着，赶紧上车":
                play voice "15b.ogg"
                $ renpy.pause(3.0)
                call ontime_option3
    if early == False:
        scene door with dissolve
        show mad at left with dissolve
        show wp at right with dissolve 
        ###disappointed/angry face
        play voice "17a.ogg"
        l "你看看都几点了！"
        $ happiness -= 1
        menu:
            "我...忘了怎么走了":
                play voice "18b.ogg"
                $ renpy.pause(3.0)
                call late_option1
            "八点整，咋啦？":
                play voice "18a.ogg"
                $ renpy.pause(3.0)
                $ happiness -= 1
                call late_option2
            "我睡午觉来着":
                play voice "18c.ogg"
                $ renpy.pause(3.0)
                $ happiness -= 1
                call late_option3
    scene theatre_hallway with dissolve
    show li at center with dissolve
    play voice "21a.ogg"
    l "I’ve been wanting to see this movie for a long time."
    scene theatre_hallway with dissolve
    show blush_closed at center with dissolve
    ###change face to excited
    l "I'm so happy you got tickets for this."
    l "What theatre is our movie in?"
    jump movie_choice
label movie_choice:
    ###scene chart with movie names
    menu:
        "Movie 1 - Room 1 一号厅":
            play voice "22a.ogg"
            $ renpy.pause(2.0)
            scene theatre
            show sad at center with dissolve
            ###change expression to sad
            play voice "23a.ogg"
            l "不对吧，不是这间"
            $ happiness -= 1
            jump movie_choice
            
        "Movie 2 - Room 2 二号厅":
            play voice "22b.ogg"
            $ renpy.pause(2.0)
            scene theatre
            show sad at center with dissolve
            play voice "23a.ogg"
            l "不对吧，不是这间"
            $ happiness -= 1
            jump movie_choice
            
        "Our Movie - Room 3 三号厅":
            play voice "22c.ogg"
            $ renpy.pause(2.0)
            scene theatre
            show li at left with dissolve
            ### change expression to happy
            play voice "23c.ogg"
            l "对，没错"
            $ happiness += 1
            $ renpy.movie_cutscene("Titanic.mpg")
            stop movie
            hide movie
            ###scene: theatre hallway
            scene theatre_hallway
            show li at center with dissolve
            play voice "24a.ogg"
            l "嗯，电影真好看啊"
            menu: 
                "可不是么，看得我垂涎三尺":
                    play voice "25a.ogg"
                    $ renpy.pause(3.0)
                    play voice "26a.ogg"
                    l "你有病啊！"
                    scene theatre_hallway
                    show discontent at center with dissolve
                    ### face change to sad
                    $ happiness -=1
                "可不是么， 看得我蠢蠢欲动":
                    play voice "25b.ogg"
                    $ renpy.pause(3.0)
                    play voice "26b.ogg"
                    l "你有病啊！"
                    scene theatre_hallway
                    show discontent at center with dissolve
                    ### face change to sad
                    $ happiness -=1
                "可不是么，看得我心潮澎湃":
                    play voice "25c.ogg"
                    $ renpy.pause(3.0)
                    play voice "26c.ogg"
                    l "我也是"
                    $ happiness +=1 
                    show blush_closed at center with dissolve
                    scene theatre_hallway
                    ###face change to happy
            $ renpy.pause()
            play voice "27a.ogg"
            l "你饿不饿？去吃晚饭吧"
            jump restaurant
label restaurant:
    scene restaurant with dissolve
    show waiter at center with dissolve
    play voice "28a.ogg"
    g "里面请，请问一共几位？"
    show waiter at left with moveinright
    show li at right with moveinright
    play voice "29a.ogg"
    l "两位"
    $ renpy.pause(1.5)
    play voice "30a.ogg"
    g "二位这边请"
    scene restaurant with dissolve
    show din at center with dissolve
    
    play voice "31a.ogg"
    g "请问您要些什么"
    $ renpy.pause(2.0)
    
    play voice "32a.ogg"
    n "请问有什么好吃的？（对了，李友吃素）"
    menu:
        "红烧牛肉":
            $ happiness += 1
            play voice "33a.ogg"
            $ renpy.pause(2.0)
            play voice "34a.ogg"
            l "对了，我吃素，不吃肉？"
            $ renpy.pause(2.0)
            play voice "35a.ogg"
            w "哦，对不起，我忘了，那我们要凉拌黄瓜。"
        "饺子":
            play voice "33b.ogg"
            $ renpy.pause(3.0)
            
            play voice "34b.ogg"
            l "饺子要素的，不要肉的"
            $renpy.pause(1.5)
            play voice "35b.ogg"
            w "我可不是吃素的！"
            
        "凉拌黄瓜":
            play voice "33c.ogg"
            $ renpy.pause(2.0)
            $ happiness += 1
            play voice "34c.ogg"
            l "Oh. You remembered that I don’t eat meat! 你知道我吃素！"
            $ renpy.pause(2.0)
            play voice "35c.ogg"
            w "他们的素菜做得可好啦！"
            
            
    n "你和李友聊得很高兴"
    n "菜上齐了"
    
    $renpy.pause()
    play voice "36a.ogg"
    l "哇，看着不错，那咱们吃吧"
    menu: 
        "嗯！真好吃":
            play voice "37a.ogg"
             ###face change to happy
            $ renpy.pause(2.0)
            $ happiness += 1 
            l "你多吃点!"
            play voice "38a.ogg"
            $ renpy.pause(2.0)
            
        "是啊, 真好喝!":
            play voice "37b.ogg"
             ### face change to sad
            $ renpy.pause(2.0)
            $ happiness -= 1
            
            l "你在说什么？"
            play voice "38b.ogg"
            $ renpy.pause(2.0)
        "是啊，真好玩!":
            play voice "37c.ogg"
             ### face change to sad
            $ renpy.pause(2.0)
            $ happiness -= 1
            
            l "你在说什么？"
            play voice "38c.ogg"
            $ renpy.pause(2.0)
            
    play voice "39a.ogg"
    $ renpy.pause(2.0)
    l "哎呀，这么晚了，要不咱们回去吧？"
    
    jump final_scene
    ### scene town map, car transition
label final_scene:
    if happiness < 0:
        scene black with dissolve
        n "The End: Bad Ending. Try Again"
        return
    else:
        scene door with dissolve
        show li at center with dissolve
        
        if happiness == 0:
            play voice "40c.ogg"
            l "再见"
            
        elif happiness == 1 :
            scene door with dissolve
            show blush_closed at center with dissolve
            play voice "40b.ogg"
            l "谢谢你今天约我出来"
            
        else:
            scene door with dissolve
            show blush_open at center with dissolve
            play voice "40a.ogg"
            l "王朋，你愿意当我男朋友吗？"
        return
        
        
        
        
        
        
        
        
        
        
#        l "Thanks for taking me out tonight. 谢谢你约我出来！"
#        menu:
#            "No problem. Good night 哪里哪里，晚安":
#                l "Good night?...... 那晚安喽～"
#                w "Bye. 再见"
#                scene black with dissolve
#                n "The End"
#            "I could do this most nights if you want. 大宝(a famous lotion brand)天天见！":
#                l "Oh really? I think I’d be interested in that. 是你的益达(a famous gum brand)！"
#                w "So then, would you go out with me? 哈哈，你是我的优乐美(a famous milktea brand)？"
#                l "I will. =) 是的"
#                scene black with dissolve
#                n "The End"
#            "So, the total comes down to about 1000 kuai for the whole night. 呵呵，我可是破费了！":
#                l "Ha. That’s menu really funny. 呵呵"
#                w "So then, would you go out with me? 哈哈，你是我的优乐美(a famous milktea brand)？"
#                ###face change to angry
#                l "Throws money at you and slams door in frustration and anger and emotions and …. 咱见"
#                scene black with dissolve
#                n "The End"


                

    


        



                    


    

                




