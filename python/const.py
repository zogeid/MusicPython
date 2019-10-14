from python.object_factory import *
from python.util import *


a_note = ObjectFactory.createNote(ENotes.A)
aS_note = ObjectFactory.createNote(ENotes.AS)
b_note = ObjectFactory.createNote(ENotes.B)
c_note = ObjectFactory.createNote(ENotes.C)
cS_note = ObjectFactory.createNote(ENotes.CS)
d_note = ObjectFactory.createNote(ENotes.D)
dS_note = ObjectFactory.createNote(ENotes.DS)
e_note = ObjectFactory.createNote(ENotes.E)
f_note = ObjectFactory.createNote(ENotes.F)
fS_note = ObjectFactory.createNote(ENotes.FS)
g_note = ObjectFactory.createNote(ENotes.G)
gS_note = ObjectFactory.createNote(ENotes.GS)

aM = ObjectFactory.createChord(EQuality.MAYOR, c_note, cS_note, g_note);