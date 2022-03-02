class Race:
    name = ''
    speed = 0
    maxAge = 0
    description = ''

    def create(self,file):
        f = open(file,"r")
        self.name = f.readline()
        self.speed = f.readline()
        self.maxAge = f.readline()
        self.description = f.readline()


    def toString(self):
        print('Name',self.name)
        print('Speed',self.speed)
        print('Max age',self.maxAge)
        print('Description',self.description)

file = "elf.txt"
race = Race()
race.create(file)
race.toString()



