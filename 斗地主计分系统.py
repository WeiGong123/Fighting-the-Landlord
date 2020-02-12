print("斗地主积分系统")

# 安琪=A 妈妈=B 龚伟=C
players = ["A", "B", "C"]
dict = {players[0]:'安琪', players[1]:'妈妈', players[2]:'龚伟'}
role = ["地主", "农民"]

# 玩家初始分数
print("玩家初始分数均为100")
score_A = score_B = score_C = 100

# 单局分数
p = 1

# 局数
N = 1
while True:
    print("第{}局开始".format(N))
    landlord = input("地主是谁? 安琪=A 妈妈=B 龚伟=C: ").upper()
    print("好的，本局地主是{}".format(dict[landlord]))
    p = int(input("本局抢地主次数是： "))
    p = 2**p
    print("本局分数目前为：{}".format(p))
    is_show = 2 if input("是否有人明牌？(Y/N): ").upper()=="Y" else 1
    p *= is_show
    print("本局分数目前为：{}".format(p))
    is_spring = 2 if input("是否春天？(Y/N): ").upper()=="Y" else 1
    p *= is_spring
    if p > 16:
        p = 16
    print("本局分数目前为：{}".format(p))
    bomb = 2**int(input("本局共多少枚炸弹？: "))
    p *= bomb
    if p > 16:
        p = 16
    print("本局分数目前为：{}".format(p))
    iswin_landlord = 1 if input("地主是否赢得本局斗争？(Y/N): ").upper()=="Y" else 0
    print("本局结束，{}胜利，玩家分数情况如下:".format(role[iswin_landlord-1]))
    if iswin_landlord:
        if landlord == "A":
            score_A += p*2
            score_B -= p
            score_C -= p
        elif landlord == "B":
            score_B += p*2
            score_A -= p
            score_C -= p
        else:
            score_C += p*2
            score_B -= p
            score_A -= p
    else:
        if landlord == "A":
            score_A -= p*2
            score_B += p
            score_C += p
        elif landlord == "B":
            score_B -= p*2
            score_A += p
            score_C += p
        else:
            score_C -= p*2
            score_B += p
            score_A += p
            
    # 安琪分数不能低于60
    if score_A < 60:
        score_B -= (60 - score_A)/2
        score_C -= (60 - score_A)/2
        score_A = 60
        
    
    print("{}：{}".format(dict["A"], score_A))
    print("{}：{}".format(dict["B"], score_B))
    print("{}：{}".format(dict["C"], score_C))
    
    if input("以上分数是否有误？(Y/N): ").upper()=="Y":
        score_A = int(input("请输入{}的正确分数： ".format(dict["A"])))
        score_B = int(input("请输入{}的正确分数： ".format(dict["B"])))
        score_C = int(input("请输入{}的正确分数： ".format(dict["C"])))
    
    is_play = 1 if input("是否继续下一局？(Y/N): ").upper()=="Y" else 0
    if not is_play:
        print("谢谢，期待与您下次见面！")
        break
        
    N += 1