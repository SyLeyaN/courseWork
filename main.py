import GenStats
import Entity

entch = []
entchMod = []
GenStats.genstats(entch, entchMod)
ent = Entity.Entity('Goblin',entch,entchMod)
ent.toString()