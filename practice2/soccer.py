import random



class Person(object):
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


    def __str__(self):
        '''초기화 함수'''
        return "이름은 {} 이며 키 {}cm 몸무게 {}kg 입니다.".format(self.name, self.height, self.weight)


class SoccerPlayer(Person):
    player_count = 0
    player_bacnNumber = []
    def __init__(self, position, backNumber, Person):
        super().__init__(Person.name, Person.height, Person.weight)
        self.position = position
        self.backNumber = backNumber
        SoccerPlayer.player_count += 1


    def __del__(self):
        print("삭제")
        SoccerPlayer.player_count -= 1


    def __str__(self):
        return "이 선수의 이름은는 {}이며 키 {}cm 몸무게 {}kg 포지션 {} 등번호 {}번 입니다.".format(self.name, self.height, self.weight, self.position, self.backNumber)



person = Person("구본익", 175, 60)
print("사람 객체 " + person.__str__())

player = SoccerPlayer("공격수", 50, person)
print(player)

print(player)
del player

print(SoccerPlayer.player_count)

j = 0
for i in range(1, 27):
    j += 5000 * i
    print(i , j)


print(26 * 5000)