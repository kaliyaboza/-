# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 19:36:13 2023

@author: 想不到你真的打开了源代码，你将会发现一些彩蛋
"""
import sys
#x:san y:hp
san=['疯狂','极差','较差','良好','优秀']
def check(word='',cyc=True):        
    if cyc:
        print('精神状态：'+san[x])
        print('剩余血量：'+str(y))
    else:
        print('精神状态：？')
        print('剩余血量：？')
    print(word)
def goal(nn):
    print('获得成就'+'【'+nn+'】')
def update():
    if x<0:
        print('角色理智值过低')
    if y<=0:
        print('角色生命值过低')
    if x<0 or y<=0:
        print('角色死亡，游戏结束，print anything to end the game')
        print('YOU LOSE，望周知')
        input()
        sys.exit()
    return
ct=0
x=4
y=100
bag=set()
print('欢迎来到陈亚偲的游戏')#笨蛋
print('输入“check”可以查看角色血量等状态')
if input()=='check':
    print('现在角色还没有构建，但很高兴你输入了正确的东西')
else:
    for i in range(10):
        print('系统异常，游戏结束')#救赎之道，就在其中
    k=set()
    for i in range(5):
        #boza=True
        a=input('请输入8位密码：')
        if a in k:
            print('我建议你试试新的')
            #boza=False
        if a=='13810253910':
            print('密码不是你的手机号')
            #boza=False
        if a.lower() in {'mikemike','mikelose','losemike'}:
            print('不错的尝试，Mike，可惜不对')
        if a=='20050509':#正确密码
            print('这是gwk的生日，恭喜你通过了游戏，新年快乐！')
            print('获得成就：【时空之歌】')
            print('YOU WIN，望周知')
            while True:
                lqy=input()
                if lqy=='check':
                    check('恭喜通关')
                else:
                    print('这是一个彩蛋，但你肯定发现不了')#除非你打开了源代码
                    break
            sys.exit()
        if a=='20041006':
            print('恭喜你触发了彩蛋，希望你能在朦胧的黑夜中，找到光明')
            sys.exit()#一闪而过的文字，游戏就闪退了，嘿嘿
        if a=='sillyegg':
            print('笨蛋')
        if i!=4:
            print('密码错误，你还有'+str(4-i)+'次机会')
        else:
            print('密码错误，你没有机会了，YOU LOSE，望周知')
            input()
            sys.exit()
        k.add(a)
print()
print('你将扮演一名叫做“Mike”的旅行者')
print('在一片大漠中航行')
print('--------------------------')
print('万千世界，孰真孰幻')
print('星光璀璨，我却已忘记来时的路')
print('--------------------------')
print("游戏已经开始，祝你好运，Mike")
if input('print anything to continue: ')=='check':
    check('第一章：沉默')
print()
print('你来到了一栋黑暗的房子前')
print('房门半敞，里面没有灯，传来飘渺的低语')
a=input('print 1 to get in: ')
while True:
    if a=='1':
        ct+=1
        print('进入房子，房中有一个老人，坐在椅子上，看着窗外')
        print('老人没有转头看你，而是自言自语地说：“自由是时间的自由，生命又是什么？”')
        b=input('旅行者说，生命是【请输入】')
        if b=='自由的生命':
            print('老人叹了口气，不再说话，你走出门外')
            print()
            goal('古老的疑问')
        else:
            print('老人摇了摇头，你走出了屋子')
            x-=2
        break
    elif a=='check':
        check('第一关开始就check，令人钦佩的冷静')
        a=input('print 1 to get in: ')
    else:
        print('这漆黑的房子令旅行者恐惧')
        break
print()
print('旅行者在荒漠中走着')
print('他感到口渴')
x-=1
update()
print('沙子中半埋着一瓶水')
drink=False
a=input('print 1 to pick it up: ')
while True:
    if a=='1':
        print('你把水瓶捡了起来，抖掉了一些沙土')
        bag.add('water')
        break
    elif a=='check':
        check('你最好捡起来')
        a=input('print 1 to pick it up: ')
    else:
        goal('拾金不昧')
        break
if 'water' in bag:
    a=input('print 1 to use it, you can use it in anytime: ')
    while True:
        if a=='1':
            print('你拿起水，一饮而尽')
            x=4
            drink=True
            break
        elif a=='check':
            check('水没毒，真的')
            a=input('print 1 to drink: ')
        else:
            print('你看了看水杯，相信它一定会有更大的用处')
            break
print()
print('旅行者继续向前走着，他也不知道他要去何方')
a=input('print anything to continue: ')
while True:
    if a=='check':
        check('第二章：谷底')
        a=input('print anything to continue: ')
    elif a=='1':
        if 'water' in bag:
            if not drink:
                drink=True
                x=4
                print('你将水一饮而尽，感觉好多了')
            else:
                print('你拿出了水瓶，可惜已经空了')
        else:
            print('你在背包中摸索，没有找到水瓶')
        a=input('print anything to continue: ')
    else:
        break
print()
print('相传绝望之谷中有一块哭泣石')
print('摸到它的人会不可避免地陷入失落')
print()
print('旅行者在荒漠中永无止境地前行着，没有终点')
print('太阳从未升起，旅行者在黑夜中沉没')
print()
x-=2
update()
if x==0:
    y-=10
    print('理智的丧失令旅行者身心俱疲')
print('脚下的沙地早已不复存在，取而代之的是一片漆黑，或是一片虚无')
print('旅行者注意到了一块石头，毫不起眼，但在单调的大地上分外突兀')
a=input('print 2 to pick it up: ')
while True:
    if a=='1':
        if 'water' in bag:
            if not drink:
                drink=True
                x=4
                print('你将水一饮而尽')
            else:
                print('你拿出了水瓶，可惜已经空了')
        else:
            print('你在背包中摸索，没有找到水瓶')
        a=input('print 2 to pick it up: ')
    elif a=='2':
        print('你拿起了石头')
        x-=1
        update()
        bag.add('stone')
        break
    elif a=='check':
        check('也许真理和虚无之间，只差一点点疯狂')
        a=input('print 2 to pick it up: ')
    else:
        print('在生存和毁灭间，你选择了无休止的前进')
        break
if 'stone' in bag:
    a=input('print 2 to touch the stone: ')
    while True:
        if a=='1':
            if 'water' in bag:
                if not drink:
                    drink=True
                    x=4
                    print('你将水一饮而尽，感觉好多了')
                else:
                    print('你拿出了水瓶，可惜已经空了')
            else:
                print('你在背包中摸索，没有找到水瓶')
            a=input('print 2 to touch the stone: ')
        elif a=='2':
            print('你摸了摸石头，悲伤决堤般倾泻而下')
            x-=1
            update()
            a=input('print 2 to touch the stone: ')
        elif a=='check':
            check('适可而止吧！')
            a=input('print 2 to touch the stone: ')
        else:
            print('你把石头放进了背包(print 2 to use it in anytime)')
            break
if x==0:
    y-=20
    print('理智的丧失令旅行者感到乏力')
print()
print('不知何时下起了雪')
if 'stone' in bag:
    ct+=1
    print('旅行者见到了死亡')
    print('黑色的镰刀劈将过来，避无可避')
    if x!=0:
        y-=100
        update()
    print('镰刀停住了')
    a=input('print anything to continue: ')
    while True:
        if a=='1':
            if 'water' in bag:
                if not drink:
                    drink=True
                    x=4
                    print('你将水一饮而尽，准备迎接自己的谢幕')
                else:
                    print('你拿出了水瓶，可惜已经空了')
            else:
                print('你在背包中摸索，没有找到水瓶')
            a=input('print anything to continue: ')
        elif a=='2':
            print('你摸了摸石头，悲伤决堤般倾泻而下')
            x-=1
            update()
            a=input('print anything to continue: ')
        elif a=='check':
            check('也许登场即为谢幕，那又何妨？',False)
            a=input('print anything to continue:  ')
        else:
            print('旅行者静静地等待着')
            break
    print('崖壁上传来呼喊声')
    print('那是一个疯子，有着和旅行者类似的装束')
    print('--------------------------')
    print('我将化作尘埃，我将凝于烈火')
    print('但在此之前')
    print('我就是太阳！')
    print('--------------------------')
    print('那团黑云转身向崖壁飞去')
    print('最终和崖壁上的人一同闪灭')
    print('像流星一样')
    x=min(x+1,4)
    goal('雪夜流星')
print()
print('旅行者仍向前行进着，一刻不停，他爬上一座高山，可四周只有白色的雪和幽暗的混沌')

x-=1
update()
if x==0:
    y-=30
    print('理智的丧失令旅行者疲惫不堪')
print('也许，是时候回去了')
a=input('print 3 to stay and print 4 to come back: ')
while True:
    if a=='1':
        if 'water' in bag:
            if not drink:
                drink=True
                x=4
                print('旅行者将水一饮而尽，看向无尽的远方')
            else:
                print('旅行者拿出了水瓶，可惜已经空了')
        else:
            print('旅行者在背包中摸索，没有找到水瓶')
        a=input('print 3 to stay and print 4 to come back: ')
    elif a=='2':
        if 'stone' in bag:
            print('旅行者摸了摸石头，悲伤决堤般倾泻而下')
            x-=1
            update()
        else:
            print('旅行者在背包中摸索，没有找到石头')
        a=input('print 3 to stay and print 4 to come back: ')
    elif a=='check':
        check('做出选择吧')
        a=input('print 3 to stay and print 4 to come back: ')
    elif a=='3':
        if 'stone' in bag:
            print('旅行者留在了崖壁上，于兹，他将迎接自己和自己的落幕')
            goal('旅行者的谢幕')
            input('print anything to end the game: ')
            sys.exit()
        else:
            print('旅行者留在了崖壁上，在这里，循环和寒冷同样致命')
            x-=5
            y-=100
            update()
            sys.exit()
    elif a=='4':
        break
    else:
        print('这一刻，旅行者必须做出选择')
        a=input('print 3 to stay and print 4 to come back: ')
print()
print('归途并不漫长，好像旅行者从未离开')
print('旅行者又见到了他来时曾见的房子，房门半开，一片寂静')
a=input('print 5 to get in: ')
while True:
    if a=='5':
        print('进入房子，房中空无一人')
        print('窗外,繁星闪烁')
        if 'water' in bag and not drink and 'stone' in bag:
            print('旅行者打开了他留存一路的水，泼在了地上')
            print('我想，他已经知道了答案')
            print('20050509')
            print('拿去吧，Mike，游戏还未结束')
            input('print anything to quit the game: ')
            sys.exit()
        else:
            print('旅行者留在了房中，他可能永远都解不开心中的疑虑，但至少他将记得来时的路')
            input('print anything to end the game: ')
            sys.exit()
    elif a=='check':
        check('终章：轮回')
        a=input('print 5 to get in: ')
    else:
        print('旅行者没有进入房子，他知道，这已经没有意义了')
        break
print()
print('旅行者向前走着，直到他分不清现实与幻觉，直到他忘记了来时的路')
if 'water' in bag and not drink and ct==2:
    goal('一步之遥')
if ct==0:
    goal('百代过客')
input('print anything to end the game: ')
sys.exit()
#获得成就:【岁月之外】    
    
    