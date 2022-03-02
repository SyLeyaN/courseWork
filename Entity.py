import GenStats
class Entity:
    name = ""
    healthPoints = 0
    armorClass = 10
    speed = 30
    characteristics = {'str':0, 'dex':0,'con':0,'int':0,'wis':0,'cha':0}
    characteristicsMod = {'strMod':0, 'dexMod':0,'conMod':0,'intMod':0,'wisMod':0,'chaMod':0}

    def __init__(self,name,ch,chM):
        self.name=name
        self.characteristics=ch
        self.characteristicsMod=chM

    def toString(self):
        print('Name',self.name)
        print('Characteristics',self.characteristics)
        print('Mode',self.characteristicsMod)

