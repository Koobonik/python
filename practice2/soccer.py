class Person(object):
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


    def __str__(self):
        '''초기화 함수'''
        return "이름은 {} 이며 키 {}cm 몸무게 {}kg 입니다.".format(self.name, self.height, self.weight)


class SoccerPlayer(Person):
    def __init__(self, position, backNumber, Person):
        self.position = position
        self.backNumber = backNumber
        self.height = Person.height
        self.weight = Person.weight
        self.name = Person.name


    def __str__(self):
        return "이 선수의 이름은는 {}이며".format(self.name)



person = Person("구본익", 175, 60)
print(person)

player = SoccerPlayer('forward', 50, person)
print(player)