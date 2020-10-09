# Doudizhu
# 345678910JQKA2 Joker JOKER
# Solo 3 4 5 6 7 8 9 10 J Q K A 2 Joker JOKER
# Pair 33 44 55 66 77 88 99 1010 JJ QQ KK AA 22 Joker&JOKER

print(""" 
             _   _                 
 _ __  _   _| |_| |__   ___  _ __  
| '_ \| | | | __| '_ \ / _ \| '_ \ 
| |_) | |_| | |_| | | | (_) | | | |
| .__/ \__, |\__|_| |_|\___/|_| |_|
|_|    |___/                       
     _                 _ _     _           
  __| | ___  _   _  __| (_)___| |__  _   _ 
 / _` |/ _ \| | | |/ _` | |_  / '_ \| | | |
| (_| | (_) | |_| | (_| | |/ /| | | | |_| |
 \__,_|\___/ \__,_|\__,_|_/___|_| |_|\__,_|
""")

# Card_Check
import random


def mode(num):
    list1 = list(str(num))
    dict1 = {}
    for i in list1:
        skey = dict1.get(i)
        if skey == None:
            dict1[i] = 1
        else:
            dict1[i] += 1
    sk = dict1.keys()
    sv = dict1.values()
    for i in sk:
        if dict1[i] == (max(sv)):
            mode = i
    return mode

#三带一
def isTrio_1(Cards):
    List1 = list(Cards)
    vaild = True
    if len(List1) == 4:
        for i in range(0, 2):
            if List1[0] != List1[i + 1]:
                vaild = False
                break
    else:
        vaild = False
    return vaild

#三带二
def isTrio_2(Cards):
    List1 = list(Cards)
    vaild = True
    if len(List1) == 5:
        for i in range(0, 2):
            if List1[0] != List1[i + 1]:
                vaild = False
                break
            for i in range(0, 2):
                if List1[3] != List1[4]:
                    vaild = False
                    break
    else:
        vaild = False
    return vaild

#四带二
def isBomb_2(Cards):
    List1 = list(Cards)
    vaild = True
    if len(List1) == 6:
        for i in range(0, 3):
            if List1[0] != List1[i + 1]:
                vaild = False
                break
    else:
        vaild = False
    return vaild

#四带两对
def isBomb_2x2(Cards):
    List1 = list(Cards)
    vaild = True
    if len(List1) == 8:
        for i in range(0, 3):
            if List1[0] != List1[i + 1]:
                vaild = False
                break
        for i in range(0, 2):
            if List1[4] != List1[5]:
                vaild = False
                break
        for i in range(0, 2):
            if List1[6] != List1[7]:
                vaild = False
                break
    else:
        vaild = False
    return vaild

#顺子
def isShunZi(nums):
    vaild = True
    List1 = list(nums)

    if len(nums) >= 5:
        for i in range(0, len(List1) - 1):
            if List1[i] + 1 != List1[i + 1]:
                vaild = False
                break
    else:
        vaild = False
    return vaild


def isDualShunZi(nums):
    vaild = True
    List1 = list(nums)
    if int(len(List1)) >= 6 and int(len(List1)) % 2 == 0:
        for i in range(0, len(List1) - 1, 2):
            if List1[i] != List1[i + 1]:
                vaild = False
                break
    else:
        vaild = False
    return vaild


def isTriShunZi(nums):
    vaild = True
    List1 = list(nums)
    if int(len(List1)) >= 6 and int(len(List1)) % 3 == 0:
        for i in range(0, len(List1), 4):
            if List1[i] != List1[i + 1]:
                vaild = False
                break
    else:
        vaild = False
    return vaild


def isTriShunZi_1(nums):
    vaild = True
    List1 = list(nums)
    if int(len(List1)) >= 8 and int(len(List1)) % 4 == 0:
        for i in range(0, len(List1), 4):
            if List1[i] != List1[i + 1]:
                vaild = False
                break
    else:
        vaild = False
    return vaild


def isTriShunZi_2(nums):
    vaild = True
    List1 = list(nums)
    if int(len(List1)) >= 10 and int(len(List1)) % 5 == 0:
        for i in range(0, len(List1), 4):
            if List1[i] != List1[i + 1]:
                vaild = False
                break
        for i in range(0, 2):
            if List1[6] != List1[7]:
                vaild = False
                break
        for i in range(0, 2):
            if List1[8] != List1[9]:
                vaild = False
                break
    else:
        vaild = False
    return vaild


def isEXBomb(nums):
    vaild = False
    List1 = list(nums)
    V = 0
    if len(List1) == 2:
        for i in range(0, 2):
            V = V + value_change(List1[i])
        if V == 33:
            vaild = True
    else:
        vaild = False
    return vaild


def isBomb(nums):
    if len(nums) == 4 and min(nums) == max(nums):
        return True


class PlayCards():
    def __init__(self, Ctype='None', value='0'):
        self.Ctype = type_check()
        self.value = value_exchange


def type_check(Ctype):
    if len(Ctype) == 1:
        Ctype = 'Solo'
    elif len(Ctype) == 2 and min(Ctype) == max(Ctype):
        Ctype = 'Pair'
    elif isEXBomb(Ctype) == True:
        Ctype = 'EXBomb'
    elif len(Ctype) == 3 and min(Ctype) == max(Ctype):
        Ctype = 'Trio'
    elif isBomb(Ctype) == True:
        Ctype = 'Bomb'
    elif isTrio_1(Ctype) == True:
        Ctype = 'Trio_1'
    elif isTrio_2(Ctype) == True:
        Ctype = 'Trio_2'
    elif isDualShunZi(Ctype) == True:
        Ctype = 'DualShunZi'  # 必须 3 对或 3 对以上连续的对牌
    elif isTriShunZi_2(Ctype) == True:
        Ctype = 'TriShunZi_2'
    elif isTriShunZi_1(Ctype) == True:
        Ctype = 'TriShunZi_1'
    elif isTriShunZi(Ctype) == True:
        Ctype = 'TriShunZi'  # 必须 2 个或 2 个以上连续的三张牌
    elif isShunZi(Ctype) == True:
        Ctype = 'ShunZi'
    elif isBomb_2x2(Ctype) == True:
        Ctype = 'Bomb_2x2'
    elif isBomb_2(Ctype) == True:
        Ctype = 'Bomb_2'
    else:
        Ctype = False
    return Ctype


EXBomb_value = 100


def value_change(value):
    if value == 'X':
        return 10
    elif value == 'J':
        return 11
    elif value == 'Q':
        return 12
    elif value == 'K':
        return 13
    elif value == 'A':
        return 14
    elif value == '2':
        return 15
    elif value == '-':
        return 16
    elif value == '+':
        return 17
    else:
        return int(value)


def value_change_Str(value):
    if value == 'X':
        return '10'
    elif value == 'J':
        return '11'
    elif value == 'Q':
        return '12'
    elif value == 'K':
        return '13'
    elif value == 'A':
        return '14'
    elif value == '2':
        return '15'
    elif value == '-':
        return '16'
    elif value == '+':
        return '17'
    else:
        return str(value)


def value_change_back(value):
    if value == 10:
        return 'X'
    elif value == 11:
        return 'J'
    elif value == 12:
        return 'Q'
    elif value == 13:
        return 'K'
    elif value == 14:
        return 'A'
    elif value == 15:
        return '2'
    elif value == 16:
        return '-'
    elif value == 17:
        return '+'
    else:
        return str(value)


def change(num):
    List1 = []
    for i in range(0, len(num)):
        List1.append(value_change(num[i]))
    return List1


def changeStr(num):
    List1 = []
    for i in range(0, len(num)):
        List1.append(value_change_Str(num[i]))
    return List1


def change_back(num):
    List1 = []
    for i in range(0, len(num)):
        List1.append(value_change_back(num[i]))
    return List1


'''
print('出牌检测')
print('单张：可以是手中的任意一张牌如8 ')
print('一对：两张牌点相同的牌，两张牌的花色可以不同（如 88 ）')
print('三同张：三张牌点相同的牌，三张牌的花色可以不同（如 888 ')
print('三带一：三张牌点相同的牌和另外一张牌一起出。 ( 如 888+9')
print('三带二：三张牌点相同的牌和另外两张牌点相同的牌一起出。 ( 如 888+99')
print('四带二单：必须带两张单牌，不能带大王，小王 ( 如 8888+79')
print('四带二对：必须带两个对牌，对子可以不用相连。如 8888+7799')
print('单顺：必须 5 张或 5 张以上连续的单牌，且其中不能有 2 或大小王 ( 如 45678 或 10JQKA')
print('对顺 ( 连对 ) ：必须 3 对或 3 对以上连续的对牌，且其中不能有 2 或大小王 ( 如 667788 或 3344556677')
print('三顺带一：必须 2 个或 2 个以上连续的三张牌，加上相同牌数的任意单牌，且任意单牌中不能含有大小王（如： 444555+79 ')
print('三顺带对：类似三顺带一，区别是带牌必须为对牌 （如： 444555+77 或 333444555+7799JJ ')
print('炸弹：四张一样牌点的牌（如 8888 ')
print('火箭：大王跟小王一起为火箭')
print('如果是10请用X代替')
TC = input("输入你要打得牌(三带一一类的牌请遵循上面的格式):")
TC1 = list(TC)
TC2 = change(TC1)
print(type_check(TC2))
input("输入任何退出")
'''


# Cards_arrangement: 整理手牌
def Cards_arrangement(Cards):
    Cards = [x.strip() for x in Cards if x.strip() != '']
    Cards = change(Cards)
    Cards.sort()
    Cards = change_back(Cards)
    return Cards


# compare value: C1为先手 C2为后手

def Compare_value(Cards1, Cards2):
    Cards1 = change(Cards1)
    Cards2 = change(Cards2)
    List1 = list(Cards1)
    value1 = int(List1[0])
    List2 = list(Cards2)
    value2 = int(List2[0])
    if isEXBomb(Cards1):
        return False
    elif isEXBomb(Cards2):
        return True
    elif isBomb(Cards1) == True:
        if isBomb(Cards2) != True:
            return False
        elif isBomb(Cards2) == True:
            if len(List1) == len(List2):
                if value1 >= value2:
                    return False
                else:
                    return True
            else:
                return False
    elif isBomb(Cards1) != True:
        if isBomb(Cards2) == True:
            return True
        
    if len(List1) == len(List2):
        if value1 >= value2:
            return False
        if value1 < value2:
            return True
    else:
        return False


def vaild_out(C1, C2):
    if Compare_value(C1, C2) == True:
        return True
    elif Compare_value(C1, C2) == False:
        print("你的出手不合理")
        return False  # 你的出手不合理
    else:
        return False


'''
print("卡牌对比器")
A = input("先手")
B = input('后手')
A1 = list(A)
A2 = change(A1)
B1 = list(B)
B2 = change(B1)
print(vaild_out(A2,B2))
input("输入任何退出")
'''


# 发牌♠♥♣♦-+

def fapai():
    global Landlord
    global card_output
    global Current_Player
    order = 1  # 牌排列顺序 默认为1 即从小到大顺序排列  0：从大到小排列
    Player_Num = 3  # 三名玩家
    N = 54  # 一副牌有54张（包含大小王）
    times = 1  # 一副牌
    leftover = 3  # 3张底牌

    card0 = list(range(0, N))
    card0 = card0 * times
    # ♠♥♣♦
    schar = '    -+'
    card1 = []
    left = N * times
    for i in range(N * times):
        rdi = random.randint(0, left - 1)
        card1.append(card0[rdi])
        card0.pop(rdi)
        left -= 1
        if left == 0:
            break

    Player = []
    for i in range(Player_Num):
        Player.append([])
    for i in range(N * times - leftover):
        Player[i % Player_Num].append(card1[i])
    Player.append([])
    for i in range(N * times - leftover, N * times):
        Player[Player_Num].append(card1[i])
    for i in range(Player_Num + 1):

        Player[i].sort()
        if order == 0:
            Player[i].reverse()

    card_output = []
    for i in range(Player_Num + 1):
        card_output.append([])
    for i in range(Player_Num + 1):
        for j in range(len(Player[i])):
            if Player[i][j] == 53 or Player[i][j] == 52:
                card_output[i].append(str(schar[Player[i][j] % 2 + 4]).rjust(3))
            else:
                cardnumber = (Player[i][j] // 4 + 2) % 13 + 1
                cardflower = 3 - Player[i][j] % 4
                if cardnumber == 1:
                    card_output[i].append('A'.rjust(2) + str(schar[cardflower]))
                elif cardnumber == 11:
                    card_output[i].append('J'.rjust(2) + str(schar[cardflower]))
                elif cardnumber == 12:
                    card_output[i].append('Q'.rjust(2) + str(schar[cardflower]))
                elif cardnumber == 13:
                    card_output[i].append('K'.rjust(2) + str(schar[cardflower]))
                else:
                    card_output[i].append(str(cardnumber).rjust(2) + str(schar[cardflower]))

    for x in range(0, 4):
        # print(card_output[x])
        List1 = []
        List2 = []
        for i in range(0, len(card_output[x])):
            c = card_output[x][i]
            b = c.split()
            List1.append(b)

        for i in range(0, len(card_output[x])):
            List2.append(List1[i][0])
        card_output[x] = List2

        '''
        print(List1)
        print(List2)
        '''


'''             
for i in range (Player_Num):
    print('玩家{:>2}的手牌为:'.format(i+1),' '.join(card_output[i]))

print('剩余的{}张底牌为:'.format(leftover),' '.join(card_output[Player_Num]))
'''


# card_output[0] Player 1
# card_output[1] Player 2
# card_output[2] Player 3
# card_output[3] 地主的牌


# 抢地主
def QiangDiZhu():
    global Landlord
    global card_output
    global Current_Player
    global Current_Player_0
    Landlord = 0
    Current_Player = 0
    Current_Player_0 = int(random.randint(1, 3))
    Times = 0
    NTime = 0
    Current_choice = str('A')
    while Times < 3 and Current_choice != 'Y':
        while (Current_choice != 'Y') or (Current_choice != 'N'):
            print("Player", Current_Player_0 % 3 + 1)
            Current_Player = Current_Player_0 % 3 + 1
            print("This is your cards", card_output[Current_Player - 1])
            Current_choice = input('Do you want to be landlord?(Y/N)')
            if Current_choice == 'Y' or Current_choice == 'N':
                if Current_choice == 'N':
                    NTime = NTime + 1
                break
            break
        Times = Times + 1
        Current_Player_0 = Current_Player_0 + 1
    if NTime < 3:
        Landlord = Current_Player
        print("Landlord is player", Landlord)
        print("展示地主牌", Cards_arrangement(card_output[3]))
    else:
        print("重新发牌")
        return False

    for i in range(0, 3):
        if i == Landlord - 1:
            card_output[i] = card_output[i] + card_output[3]


# Cards_Check:检查玩家出牌是否合理

def inter(a, b):
    return list(set(a) & set(b))


def Cards_Check():
    global Landlord
    global card_output
    global Current_Player
    global Cards_out
    global Last_Cards
    Cards_on_hand = card_output[Current_Player - 1]
    Cards_on_hand = list(Cards_on_hand)
    # Cards_on_hand = changeStr(Cards_on_hand)

    '''
    print(card_output[0])
    print(card_output[1])
    print(card_output[2])
    print(card_output[Current_Player-1])
    print(Current_Player-1)
    '''

    Count = 0
    Cards_on_hand_C = Cards_on_hand

    for x in range(0, len(Cards_out)):
        for i in range(0, len(Cards_on_hand_C) - 2):
            if Cards_out[x] == Cards_on_hand_C[i]:
                Cards_on_hand_C.remove(Cards_out[x])
                Count = Count + 1

    Temp = int(Count) == int(len(Cards_out))

    if type_check(Cards_out) == False:
        print('你的出牌不符合游戏规则')
        return False

    elif vaild_out(Last_Cards,Cards_out) == False:
        print('你的出牌小于上家的牌')
        return False

    elif Temp == False:
        print('你的手里没有这些牌')
        return False

    else:
        return True
    '''
    elif list(set(Cards_on_hand)&set(Cards_out)) != Cards_out:
        print(list(set(Cards_on_hand)&set(Cards_out)))
        print('你的手里没有这些牌')
        return False
    '''


def ChuPai():
    global Landlord
    global card_output
    global Current_Player
    global Cards_out
    global Last_Cards
    Cards_out_vaild = False
    tempC = []
    tempA = []
    print("Player", Current_Player)
    card_output[Current_Player - 1] = Cards_arrangement(card_output[Current_Player - 1])
    print("This is your cards", card_output[Current_Player - 1])
    Cards_on_hand = card_output[Current_Player - 1]

    while Cards_out_vaild == False:
        Cards_out = input("选择你要打出的打牌(不需要包含花色,place replace 10 with X):")
        Cards_out = list(Cards_out)
        # Cards_out = changeStr(Cards_out)
        Cards_out_vaild = Cards_Check()

    if Cards_out_vaild == True:
        for i in range(0, len(Cards_out)):
            for x in range(0, len(Cards_on_hand) - 2):
                if Cards_on_hand[x] == Cards_out[i]:
                    Cards_on_hand.remove(Cards_out[i])
        print("你现在的手牌", Cards_arrangement(Cards_on_hand))
        Last_Cards = Cards_out
    if Cards_out_vaild == False:
        print("请打出合理的出牌")


def GameEnd():
    for i in range(0, 3):
        if len(Cards_on_hand[i]) == 0:
            print("Winner is:", Player, "i")
            return True


# main function:
Test_out = '34'
Last_Cards = '0'
GameEnd = False


fapai()
while QiangDiZhu() == False:
    fapai()
    QiangDiZhu()

while GameEnd == False:
    ChuPai()
    Current_Player_0 = Current_Player_0 + 1
    Current_Player = Current_Player % 3 + 1


'''
Cards_on_hand =[3,4,5,6,7,8,9]
Cards_out = [3,4,5,6,7]
Cards_Check
Cards_on_hand =[3,4,5,6,7,8,9]
Cards_out = [3,4,5,6,7]
print(type_check(Cards_out))
print(vaild_out(Last_Cards,Cards_out))
if list(set(Cards_on_hand)&set(Cards_out)) != Cards_out:
    print('1')
'''





















