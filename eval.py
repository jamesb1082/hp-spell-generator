import sys
sys.path.insert(0, "/hp_spells")
from hp_spells import hp_spells

model = hp_spells.load("../vectors/GoogleNews-vectors-negative300.bin")  

print hp_spells.generateSpell("open the door quietly")
