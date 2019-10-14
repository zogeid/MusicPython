class Chord:

    def __init__(self, equality, root, second, third=None, fourth=None, fifth=None, sixth=None, seventh=None):
        self.equality = equality
        self.root = root
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth
        self.sixth = sixth
        self.seventh = seventh

    def printChord3(self):
        print(self.root.enote.formatted_note_name(), "", self.equality.name, ": ", end='')
        s = [self.root.enote.formatted_note_name(), self.second.enote.formatted_note_name()]

        if self.third is not None:
            s.append(self.third.enote.formatted_note_name())
        if self.fourth is not None:
            s.append(self.fourth.enote.formatted_note_name())
        if self.fifth is not None:
            s.append(self.fifth.enote.formatted_note_name())
        if self.sixth is not None:
            s.append(self.sixth.enote.formatted_note_name())
        if self.seventh is not None:
            s.append(self.seventh.enote.formatted_note_name())

        print(' '.join(filter(None, s)))
