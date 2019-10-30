import mysql.connector



class Person:
    def __init__(self):
        connector = mysql.connector.connect(user='root', database='DeadStory', password='3Amypc3A')
        self.cur = connector.cursor()
        sql="""
        
        """
        self.name = self.cur.execute(sql)
        sql = """

                """
        self.id = self.cur.execute(sql)
        sql = """

                """
        ################################################333returns bool??
        self.fire = self.cur.execute(sql)
        sql = """

                """
        ################################################333returns bool??
        self.interrogator = self.cur.execute(sql)
        sql = """

                """
        sql = """

                """
        self.criminal = self.cur.execute(sql)
        self.idea_list=self.cur.execute(sql).split('***')
        self.alive=True

    def kill(self, person, person_list):
        flag = True
        if self.fire:
            for i in person_list:
                if i.id == person.id:
                    if person.alive:
                        person.alive = False
                        flag = False
            if flag:
                print('you cant kill {}'.format(person.name))
            else: print('{} is dead now'.format(person.name))
        else:print('this character cant kill anyone')

    def interrogation(self, person, about_person):
        if self.interrogator:
            if person.alive:
                for i in range(len(person.idea_list)):
                    ##########################################################################equals?
                    if person.idea_list[i].__eq__(about_person.id):
                        print(person.idea_list[i+1])
            else:print(' this person is dead')
        else:print('{} is not interrogator and cant interrogate'.format(self.name))

class Things:
    def __init__(self):
        connector = mysql.connector.connect(user='root', database='DeadStory', password='3Amypc3A')
        self.cur = connector.cursor()
        sql = """

                """
        self.id = self.cur.execute(sql)
        sql = """

                """
        self.name = self.cur.execute(sql)
        sql = """

                """
        ################################################333returns bool??
        self.pickable = self.cur.execute(sql)
        sql = """

                """
        x = self.cur.execute(sql)
        self.finger_prints = x.split()
        self.isPicked = False

    def print_finger(self, person_list):
        print('there is fingerprint of')
        ########################################################what is type of  i  ?  ?
        for i in (self.finger_prints):
           for j in person_list:
               if i.__eq__(j.id):
                   print(j.name+'and')

    def pick(self, bag):
        if self.pickable:
            if not self.isPicked:
                self.isPicked = True
                bag.append(self)
            else:print('this thing is picked before')
        else:print('this is not pickable')


class Room:
    def __init__(self, things_list):
        connector = mysql.connector.connect(user='root', database='DeadStory', password='3Amypc3A')
        self.cur = connector.cursor()
        sql = """

                        """
        self.id = self.cur.execute(sql)
        sql = """

                        """
        self.name = self.cur.execute(sql)
        sql = """

                        """
        if self.cur.execute(sql) != None:
            self.sound = self.cur
        else: self.sound = None
        sql = """

                        """
        if self.cur.execute(sql) != None:
            self.look = self.cur
        else: self.look = None
        self.things=things_list

    def room_look(self):
        if self.look != None:
            print(self.look)
        if self.look != None:
            print(self.sound)
        print('in this rom U see')
        for i in self.things:
            print(i.name)

    def lookAt(self, thing, person_list):
        found = False
        for i in range(len(self.things)):
            if thing.id == self.things[i].id:
                thing.print_finger(person_list)
                found = True
        if not found:
            print('this thing is not in this room')

    def pick(self, thing, bag):
        found = False
        for i in range(len(self.things)):
            if thing.id == self.things[i].id:
                thing.pic(bag)
                found = True
        if not found:
            print('this thing is not in this room')