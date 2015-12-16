#will be audio
label school_option1:
    
    play voice "2a.ogg"
    l "嗨，王朋，最近怎么样啊？"
    show li at left with moveinleft
    $ renpy.pause(1.5)
    
    show wp at right with moveinleft
    play voice "3a.ogg"
    
    w "还不错啊，你怎么样？"
    $ renpy.pause(1.5)
    
    play voice "4a.ogg"
    l "也挺好"
    
    play voice "5a.ogg"
    w "这周末你忙不忙？"
    
    play voice "6a.ogg"
    l "不怎么忙，怎么了？"
    
    play voice "7a.ogg"
    w "我想请你看电影，James Cameron 的《泰坦尼克号》，3D版你看过吗？"
    jump accept_scene
    return
    
    
label school_option2:
    play voice "2b.ogg"
    l "吃了，您呢"
    show li at left with moveinleft
    show wp at right with moveinleft
    
    $ renpy.pause(1.5)
    play voice "3b.ogg"
    w "刚吃完"
    $ renpy.pause(1.5)
    play voice "4b.ogg"
    l "嗯..."
    $ renpy.pause(2.5)
    play voice "7a.ogg"
    w "我想请你看电影好吗？James Cameron 的《泰坦尼克号》，3D版你看过吗？"
    jump accept_scene
    return
label school_option3:
    play voice "2c.ogg"
    l "我去上学啊"
    show li at left with moveinleft
    show wp at right with moveinleft
    $ renpy.pause(2.0)
    play voice "3c.ogg"
    w "哦 我也是..."
    $ renpy.pause(2.0)
    ###face change to rush
    play voice "4c.ogg"
    l "我最近可事不少?"
    $ renpy.pause(2.0)
    play voice "7a.ogg"
    w "我想请你看电影好吗？James Cameron 的《泰坦尼克号》，3D版你看过吗"
    ###Face changes to surprise
    ### face change to happy
    jump accept_scene
    return
label accept_scene:
    play voice "8a.ogg"
    l "没有呢，我很喜欢那个电影，还有谁一起去吗？"
    menu: 
        "只有我们俩":
            play voice "9a.ogg"
            $ renpy.pause(1.5)
            play voice "10a.ogg"
            l "好啊好啊"
            $ renpy.pause(2.0)
            $ happiness += 1
            play voice "11a.ogg"
            w "太棒了，那我可以几点去开车接你？"
            $ renpy.pause(2.0)
            play voice "12a.ogg"
            l "六点吧，看完正好能一起吃晚饭"
            $ renpy.pause(2.0)
            play voice "13a.ogg"
            w "没问题"
            jump map_scene
            
        "还有我的前女友":
            play voice "9b.ogg"
            ### face change to disappointed
            $ renpy.pause(2.0)
            play voice "10b.ogg"
            l "那我看情况"
            $ happiness -= 1
            $ renpy.pause(2.0)
            play voice "11b.ogg"
            w "我还没有女朋友，就咱们俩好吗。"
            $renpy.pause(2.0)
            play voice "12b.ogg"
            l "好啊"
            $ renpy.pause(1.5)
            ### face change to blush
            play voice "13b.ogg"
            w "行行行"
            jump map_scene

        "几个哥们(buddies)一起":
            play voice "9c.ogg"
            $ renpy.pause(2.0)
            play voice "10c.ogg"
            l "哦，也行吧"
            $ happiness -= 1
            ### face changed to disappointed
            $ renpy.pause(2.0)
            play voice "11c.ogg"
            w "你要是想，我可以去接你"
            $ happiness += 1
            $ renpy.pause(2.0)
            play voice "12c.ogg"
            l "好啊"
            ### face change to blush
            $ renpy.pause(2.0)
            play voice "13c.ogg"
            w "那行，咱们六点见"
            jump map_scene
        

        
    
label ontime_option1:
    ###face change to smile
    play voice "16a.ogg"
    l "嗯！"
    ###Show back of car
    return
label ontime_option2:
    play voice "16b.ogg"
    l "来啦"
    
    return
label ontime_option3:
    play voice "16c.ogg"
    l "行行行，催什么催"
    
    return
label late_option1:
    1 "下次迷路就给我打电话啊"
    w "真对不起，不过快一点能赶上电影"
    ###face change to happier
    l "好吧"

    return

label late_option2:
    l "....."
    play voice "20a.ogg"
    w "真对不起，不过快一点能赶上电影"
    $ renpy.pause(3.0)
    ###face change to happier
    play voice "20b.ogg"
    l "好吧"
    return
    
label late_option3:
    l "....."
    play voice "20a.ogg"
    w "真对不起，不过快一点能赶上电影"
    $ renpy.pause(3.0)
    ###face change to happier
    play voice "20b.ogg"
    l "好吧"
    return
    


