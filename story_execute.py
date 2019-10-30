import mysql.connector
import sys
import game_data

class Execute:
    def __init__(self):
        data = game_data.Data()
        self.person_list = data.person_list
        self.thing_list = data.thing_list
        self.room_list = data.room_list
        self.bag = []
        self.current=1
        help = """
        in this game, you are playing as a detective. solve the case :)
        there is what you cna do
        move : to move to different rooms
        look : to look at the room and see what is there and how does it looks like
        lookAt : to look at a special thing and see if there is any finger print
        pick : to pick some thing and add it to your bag
        help : you can ask from some special character to do some thing for you like-->
                interrogator : person with this ability can tell you what is someones idea about somebody else
                fire : person with this ability can kill anyone you want
        CHOOSE : you can say who is the bad gay and the game will finished if you are right gg end if not, 
                            such an unworthy detective
                            
        Story of Death:
        a professional programmer Max is founded dead on his houses yard whit a garden knife in his head
        people works in his house are a gardener and a chef and a house keeper 
        he also has a Neighbor 
        who killed him?
        """
        print(help)

    def run(self):
        while True:
            do=input('what do you want to do?').lower()
            if do == 'move':
                where = input('where do you want to go?').lower()
                for i in self.room_list:
                    if where == i.name:
                        self.current = i.id
            elif do == 'look' :
                for i in self.room_list:
                    if self.current == i.id:
                        i.room_look()
            elif do == 'lookAt':
                where=input('what do you want to look at?')
                for i in self.room_list:
                    if self.current == i.id:
                        for j in self.thing_list:
                            if where == j.name:
                                i.lookAt(j, self.person_list)
            elif do == 'pick':
                what=input('what do you want to pick')
                for i in self.room_list:
                    if self.current == i.id:
                        for j in self.thing_list:
                            if what == j.name:
                                i.pick(j, self.bag)
            elif do == 'help':
                who = input('whose help you need ')
                for i in self.person_list:
                    if who == i.name:
                        what=input('what do you want from this person?\n1-kill\n2-interrogate')
                        if what == '1':
                            who2 = input('who do you want to kill?')
                            for j in self.person_list:
                                if j.name == who2:
                                    i.kill(j, self.person_list)
                        if what == '2':
                            who2 = input('who do you want to ask from?')
                            about=input('you want to ask about whom?')
                            for j in self.person_list:
                                if who2 == j.name:
                                    for h in self.person_list:
                                        if about == h.name:
                                            i.interrogation(j, h)
            elif do == 'choose':
                who = input('who is the criminal ?')
                for i in self.person_list:
                    if who == i.name:
                        try:
                            if i.criminal: raise
                            sys.exit("you loose the game criminal was {}".format(i.name))

                        except:
                            print('you choose right\nyou win the game\nWP')