from python.util import ENotes, EQuality
from python.chord import Chord
from python.note import Note

class Scale:

    def __init__(self, rootNote, equality, supertonic=None, mediant=None, subdominant=None, dominant=None, submediant=None, leading=None):
        self.rootNote = rootNote
        self.equality = equality
        self.chords = []
        self.notes = dict({})
        # notes = dict({"1": "Sachine Tendulkar", "2": "Dravid"})
        self.supertonic=supertonic
        self.mediant = mediant
        self.subdominant = subdominant
        self.dominant = dominant
        self.submediant = submediant
        self.leading = leading

    def calculateNotes(self):
        ordinal_tonic = self.rootNote.enote.value
        self.notes[0] = self.rootNote

        if EQuality.Mayor.name == self.equality.name: #TTSTTTS
            self.supertonic = self.calculateNoteInOctave(2, ordinal_tonic)
            self.notes[1] = self.supertonic
            self.mediant = self.calculateNoteInOctave(4, ordinal_tonic)
            self.notes[2] = self.mediant
            self.subdominant = self.calculateNoteInOctave(5, ordinal_tonic)
            self.notes[3] = self.subdominant
            self.dominant = self.calculateNoteInOctave(7, ordinal_tonic)
            self.notes[4] = self.dominant
            self.submediant = self.calculateNoteInOctave(9, ordinal_tonic)
            self.notes[5] = self.submediant
            self.leading = self.calculateNoteInOctave(11, ordinal_tonic)
            self.notes[6] = self.leading

        elif EQuality.Minor.name == self.equality.name: #TSTTSTT
            self.supertonic = self.calculateNoteInOctave(2, ordinal_tonic)
            self.notes[1] = self.supertonic
            self.mediant = self.calculateNoteInOctave(3, ordinal_tonic)
            self.notes[2] = self.mediant
            self.subdominant = self.calculateNoteInOctave(5, ordinal_tonic)
            self.notes[3] = self.subdominant
            self.dominant = self.calculateNoteInOctave(7, ordinal_tonic)
            self.notes[4] = self.dominant
            self.submediant = self.calculateNoteInOctave(8, ordinal_tonic)
            self.notes[5] = self.submediant
            self.leading = self.calculateNoteInOctave(10, ordinal_tonic)
            self.notes[6] = self.leading


    def calculateNoteInOctave(self, added, tonic):
        added = tonic + added
        if added >= 12:
            added = added - 12
        return Note(ENotes(added))


    def calculateNoteInScale(self, root_note, added):
        added = root_note + added
        if (added > 6):
            added = added - 7
        return list(self.notes.values())[added]


    def printNotes(self):
        print("Notes: ",  self.rootNote.enote.formatted_note_name(), ", ", self.supertonic.enote.formatted_note_name(), ", ",self.mediant.enote.formatted_note_name(), ", ",self.subdominant.enote.formatted_note_name(), ", ",self.dominant.enote.formatted_note_name(), ", ",self.submediant.enote.formatted_note_name(), ", ",self.leading.enote.formatted_note_name())


    def printChords(self):
        print("Chords: ")
        for c in self.chords:
            c.printChord3()


    def printScaleName(self):
        print("Scale: ", self.rootNote.enote.formatted_note_name(), " ", self.equality.name)
        print()

    def printScaleFull(self):
        print("Scale: ", self.rootNote.enote.formatted_note_name(), " ", self.equality.name)
        self.printNotes()
        self.printChords()
        print()

    def calculateChord(self, root_note, equality):
       # ordinal_tonic = self.notes[root_note].enote.value
        chord_name = self.notes[root_note].enote.name
        if EQuality.Mayor == equality:
            n1 = self.notes.get(root_note)
            n2 = self.calculateNoteInScale(root_note, 2)
            n3 = self.calculateNoteInScale(root_note, 4)
            c = Chord(equality, n1, n2, n3)
            #c.printChord3()
            self.chords.append(c)

        elif EQuality.Minor == equality:
            n1 = self.notes.get(root_note)
            n2 = self.calculateNoteInScale(root_note, 2)
            n3 = self.calculateNoteInScale(root_note, 4)
            c = Chord(equality, n1, n2, n3)
            self.chords.append(c)

        elif EQuality.Diminished == equality:
            n1 = self.notes.get(root_note)
            n2 = self.calculateNoteInScale(root_note, 2)
            n3 = self.calculateNoteInScale(root_note, 4)
            c = Chord(equality, n1, n2, n3)
            self.chords.append(c)


    def calculateChords(self):
        if EQuality.Mayor == self.equality: ##MmmMMmDim
            self.calculateChord(0, EQuality.Mayor)
            self.calculateChord(1, EQuality.Minor)
            self.calculateChord(2, EQuality.Minor)
            self.calculateChord(3, EQuality.Mayor)
            self.calculateChord(4, EQuality.Mayor)
            self.calculateChord(5, EQuality.Minor)
            self.calculateChord(6, EQuality.Diminished)

        elif (EQuality.Minor == self.equality): #mDMmmMM
            self.calculateChord(0, EQuality.Minor)
            self.calculateChord(1, EQuality.Diminished)
            self.calculateChord(2, EQuality.Mayor)
            self.calculateChord(3, EQuality.Minor)
            self.calculateChord(4, EQuality.Minor)
            self.calculateChord(5, EQuality.Mayor)
            self.calculateChord(6, EQuality.Mayor)


    def containsChord(self, chord):
        for c in self.chords:
            # print(chord.root.note)
            # print("croot:" , c.root.name)
            if chord is not None and c is not None and chord.root is not None and c.root is not None\
                    and chord.root.enote == c.root.enote and chord.equality == c.equality:
                return True
        return False
