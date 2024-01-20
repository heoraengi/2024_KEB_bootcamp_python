class Poketmon:
    def __init__(self, name, level, hp, type, sound,skill):
        self.name = name
        self.level = level
        self.hp = hp
        self.type = type
        self.sound = sound
        self.skill = skill

    def show_poketmon(self):
        print(f'이름 : {self.name}, 레벨: {self.level}, HP: {self.hp}, 타입: {self.type}, 울음소리: {self.sound}, 기술: {self.skill.attack_name}')

    def attack(self, target):
        print(f'{self.name}이(가) {target.name}에게 {self.skill.attack_name}을(를) 사용합니다.')

    def defense(self,target):
        print(f'{self.name}이(가) {target.name}의 공격을(를) 피했습니다.')

    def dance(self):
        print(f'{self.name}이(가) 승리의 춤을 춥니다.')

    def level_up(self):
        self.level +=1
        self.hp += 5
        print(f'{self.name}이(가) 레벨업했습니다!')

    def speak(self):
        return self.sound

class Skill:
    def __init__(self, attack_name,attack_power, attack_type):
        self.attack_name = attack_name
        self.attack_power = attack_power
        self.attack_type = attack_type

class Item:
    def __init__(self, item_name, item_type):
        self.itme_name = item_name
        self.item_type = item_type

class Trainer:
    def __init__(self, name, item, poketball):
        self.name = name
        self.item = item
        self.poketball = poketball
    def show_poketmon(self):
        for i,poketmon in enumerate(self.poketball):
            print(f'{i+1}) 이름 : {poketmon.name}, 레벨: {poketmon.level}, HP: {poketmon.hp}, 타입: {poketmon.type}, 울음소리: {poketmon.sound}, 기술: {poketmon.skill.attack_name}')
    def use_item(self,poketmon):
        print(f'{self.item.itme_name}을(를) 사용합니다!')
        if self.item.item_type == poketmon.type :
            print('공격력이 세배로 증가됩니다!')
            poketmon.skill.attack_power *= 3
            self.item = ''
        else:
            print('아이템 효과가 없습니다.')


s1 = Skill('백만볼트', 1, '전기')
s2 = Skill('물대포', 2, '물')
s3 = Skill('잎날가르기',1, '풀')
s4 = Skill('몸통박치기', 1, '노말')
s5 = Skill('전광석화',1, '노말')
s6 = Skill('화염방사',3, '불')

p1 = Poketmon('피카츄', 1, 10, '전기', '삐까삐까츄',s1)
p2 = Poketmon('라프라스', 10, 35, '물', '라프~라스~',s2)
p3 = Poketmon('이상해씨', 1, 10, '풀', '씨~~~',s3)
p4 = Poketmon('메타몽', 5, 20, '노말', '메..타..몽?',s4)
p5 = Poketmon('이브이', 3, 15, '노말', '이쁘잇.',s5)
p6 = Poketmon('어흥염', 15, 50, '불', '어흥!염!',s6)
poketmon_list= [p1,p2,p3,p4,p5,p6]

w1 = Poketmon('파이리',1, 10, '불', '파~~이리!',s6)
w2 = Poketmon('개굴닌자',7, 25, '물', '개굴개굴',s2)
w3 = Poketmon('아르세우스',20, 60, '노말', '아르세우스입니다.',s1)
wild_poketmon_list = [w1,w2,w3]

i1 = Item('불꽃의 돌', '불')
i2 = Item('물의 돌', '물')
i3 = Item('천둥의 돌', '전기')
i4 = Item('리프의 돌', '풀')
i5 = Item('무적의 돌', '노말')
item_list = [i1,i2,i3,i4,i5]

import random
# 포켓몬 게임 입장 확인
while True :
    global game  # game 진행 여부 변수
    game = input('포켓몬스터의 세계에 잘 왔다! 게임을 하겠는가? (y or n): ')
    if game == 'y':
        print('오박사의 연구소로 갑니다...')
        break
    elif game =='n':
        print('당신은 포켓몬을 사랑하지 않는군요... 실망입니다!')
        break
    else :
        print('y 아니면 n 중에서 입력해주세요ㅠㅠ')

## 포켓몬 게임 입장
while game == 'y' :
    trainer_name = input('당신의 이름은 무엇인가요 ? : ')
    trainer = Trainer(trainer_name,'', [])
    print(f'{"="*24}오박사의 포켓몬 연구실{"="*24}')
    for num, p in enumerate (poketmon_list):
        # name, level, hp, type, sound
        print(f'{num+1}) ',end='')
        p.show_poketmon()
    print("="*67)

    # 포켓몬 선택 확인 및 poketball에 넣는다.
    while True :
        select_poketmon = list(map(int,input(f'{trainer.name}님 원하는 포켓몬 3마리를 고르세요 (1~6) :  ').split()))
        if all( s in list(range(1,len(poketmon_list)+1)) for s in select_poketmon ) and len(set(select_poketmon))==3:
            for s in select_poketmon :
                trainer.poketball.append(poketmon_list[s-1])
            break
        else :
            print('선택 범위를 넘어갔거나 선택한 포켓몬이 3마리가 아닙니다!')

    print('아래와 같이 포켓몬이 선택됐습니다!')
    trainer.show_poketmon()

    print('그럼 이제 모험을 떠나렴!')
    while True :
        select = input(f'1)숲으로 간다\t2)게임종료 : ')
        if select== '1' :
            print('숲을 돌아다닌다...')
            random_num = random.randint(1,3)
            if random_num < 3 :
                random_poketmon = random.randint(0, (len(wild_poketmon_list)-1))
                wild_poketmon = wild_poketmon_list[random_poketmon]
                print(f'앗! 야생의 {wild_poketmon.name}이(가) 나타났다!!')
                wild_poketmon.show_poketmon()
                wild_poketmon.speak()
                battle = None
                while True :
                    battle_or_escape = input(f'1)싸운다 2)도망친다. : ')
                    if battle_or_escape == '1':
                        battle = True
                        break
                    elif battle_or_escape == '2':
                        battle = False
                        break
                    else :
                        print('1과 2 중에서 선택하세요!')

                while wild_poketmon.hp > 0 :
                    if battle :
                        trainer.show_poketmon()
                        select_poketmon = int(input(f'싸울 포켓몬을 선택하세요 (1~{len(trainer.poketball)}) : '))
                        my_poketmon = trainer.poketball[select_poketmon-1]
                        while True :
                            select = input('1) 공격 2) 방어 3) 아이템 사용 : ')
                            if select == '1':
                                my_poketmon.attack(wild_poketmon)
                                wild_poketmon.hp -= (my_poketmon.level * my_poketmon.skill.attack_power)
                                if wild_poketmon.hp <= 0 :
                                    wild_poketmon.hp = 0
                                print(f'야생 포켓몬 hp : {wild_poketmon.hp}')
                                if wild_poketmon.hp <= 0 :
                                    print(f'{wild_poketmon.name}을 쓰러트렸습니다.')
                                    my_poketmon.dance()
                                    my_poketmon.level_up()
                                    wild_poketmon_list.remove(wild_poketmon)
                                    break
                            elif select == '2':
                                my_poketmon.defense(wild_poketmon)
                            elif select =='3' :
                                if trainer.item :
                                    trainer.use_item(my_poketmon)
                                else :
                                    print('아이템이 없습니다.')
                            else :
                                print('1~3 중에서 선택하세요!')

                    else :
                        escape = random.randint(0,1)
                        if escape == 0:
                            print('도망에 성공했습니다.')
                            break
                        else :
                            print('도망에 실패했습니다.')
                            battle = True

            else :
                random_item = random.randint(0,len(item_list)-1)
                print(f'{item_list[random_item].itme_name} 아이템을 발견했습니다!')
                print(f'아이템을 주머니에 넣겠습니까? 단,주머니에는 한개의 아이템만 들어갑니다.')
                if trainer.item :
                    print(f'주머니 상태 : {trainer.item.itme_name}')
                else :
                    print(f'주머니 상태 : 없음' )
                while True :
                    get_item = input(f'1) 넣는다. 2) 안 넣는다. : ')
                    if get_item == '1' :
                        if trainer.item :
                            print(f'원래 가지고 있던 {trainer.item.itme_name}을(를) 버립니다.')
                        trainer.item = item_list[random_item]
                        print(f'변경된 주머니 상태 : {trainer.item.itme_name}')
                        break
                    elif get_item == '2':
                        break
                    else :
                        print('1과 2 중에서 선택하세요!')

        elif select == '2':
            print("여행을 마치겠습니다. 안녕히가십쇼")
            game = 'n'
            break
        else :
            print('1과 2 중에서 선택하세요!')

        if not wild_poketmon_list :
            print(f'모든 야생 포켓몬을 쓰러트렸습니다!')
            print(f'포켓몬 마스터가 되신 걸 축하드립니다!')
            game = 'n'
            break


    break


