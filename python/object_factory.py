from python.note import Note
from python.chord import Chord
from python.scale import Scale
from python.util import ENotes, EQuality


def calculateScale(root_note, equality):
    scale = Scale(root_note, equality)
    scale.calculateNotes()
    scale.calculateChords()
    return scale


def findContainerScales(chord):
    print("Finding scales that contain the chord ", end='')
    chord.printChord3()

    aM = calculateScale(a_note, EQuality.Mayor)
    bM = calculateScale(b_note, EQuality.Mayor)
    cM = calculateScale(c_note, EQuality.Mayor)
    dM = calculateScale(d_note, EQuality.Mayor)
    eM = calculateScale(e_note, EQuality.Mayor)
    fM = calculateScale(f_note, EQuality.Mayor)
    gM = calculateScale(g_note, EQuality.Mayor)

    am = calculateScale(a_note, EQuality.Minor)
    bm = calculateScale(b_note, EQuality.Minor)
    cm = calculateScale(c_note, EQuality.Minor)
    dm = calculateScale(d_note, EQuality.Minor)
    em = calculateScale(e_note, EQuality.Minor)
    fm = calculateScale(f_note, EQuality.Minor)
    gm = calculateScale(g_note, EQuality.Minor)

    escalas = [aM, bM, cM, dM, eM, fM, gM, am, bm, cm, dm, em, fm, gm]

    escalas_resultado = []
    for s in escalas:
        if s.containsChord(chord):
            escalas_resultado.append(s)
            # print(s.rootNote, " ", s.equality)
    return escalas_resultado


def calculateNotes(self, rootNote, equality):
    ordinal_tonic = rootNote.note.value
    calc_notes = []
    calc_notes[0] = rootNote.note

    if EQuality.Mayor.name == equality.name: #TTSTTTS
        self.supertonic = self.calculateNoteInOctave(2, ordinal_tonic)
        self.notes[1] = self.supertonic.note
        self.mediant = self.calculateNoteInOctave(4, ordinal_tonic)
        self.notes[2] = self.mediant.note
        self.subdominant = self.calculateNoteInOctave(5, ordinal_tonic)
        self.notes[3] = self.subdominant.note
        self.dominant = self.calculateNoteInOctave(7, ordinal_tonic)
        self.notes[4] = self.dominant.note
        self.submediant = self.calculateNoteInOctave(9, ordinal_tonic)
        self.notes[5] = self.submediant.note
        self.leading = self.calculateNoteInOctave(11, ordinal_tonic)
        self.notes[6] = self.leading.note

    elif EQuality.Minor.name == self.equality.name: #TSTTSTT
        self.supertonic = self.calculateNoteInOctave(2, ordinal_tonic)
        self.notes[1] = self.supertonic.note
        self.mediant = self.calculateNoteInOctave(3, ordinal_tonic)
        self.notes[2] = self.mediant.note
        self.subdominant = self.calculateNoteInOctave(5, ordinal_tonic)
        self.notes[3] = self.subdominant.note
        self.dominant = self.calculateNoteInOctave(7, ordinal_tonic)
        self.notes[4] = self.dominant.note
        self.submediant = self.calculateNoteInOctave(8, ordinal_tonic)
        self.notes[5] = self.submediant.note
        self.leading = self.calculateNoteInOctave(10, ordinal_tonic)
        self.notes[6] = self.leading.note


a_note = Note(ENotes.A)
aS_note = Note(ENotes.AS)
b_note = Note(ENotes.B)
c_note = Note(ENotes.C)
cS_note = Note(ENotes.CS)
d_note = Note(ENotes.D)
dS_note = Note(ENotes.DS)
e_note = Note(ENotes.E)
f_note = Note(ENotes.F)
fS_note = Note(ENotes.FS)
g_note = Note(ENotes.G)
gS_note = Note(ENotes.GS)

aM = Chord(EQuality.Mayor, c_note, cS_note, g_note)
bM = Chord(EQuality.Mayor, b_note, dS_note, fS_note)
cM = Chord(EQuality.Mayor, c_note, e_note, g_note)
dM = Chord(EQuality.Mayor, d_note, fS_note, a_note)
eM = Chord(EQuality.Mayor, e_note, gS_note, b_note)
fM = Chord(EQuality.Mayor, fS_note, aS_note, cS_note)
gM = Chord(EQuality.Mayor, g_note, b_note, d_note)

am = Chord(EQuality.Minor, a_note, c_note, e_note)
bm = Chord(EQuality.Minor, b_note, d_note, fS_note)
cm = Chord(EQuality.Minor, cS_note, e_note, gS_note)
dm = Chord(EQuality.Minor, dS_note, fS_note, aS_note)
em = Chord(EQuality.Minor, e_note, g_note, b_note)
fm = Chord(EQuality.Minor, fS_note, a_note, cS_note)
gm = Chord(EQuality.Minor, gS_note, b_note, dS_note)