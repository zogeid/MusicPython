class Note:

    def __init__(self, enotes=None):
        print("Creating note: ", enotes)
        self.enote = enotes  # util.ENotes

    def __init__(self, enotes=None, emodifier=None, octave=None):
        self.enote = enotes  # util.ENotes
        self.modifier = emodifier
        self.octave = octave

    def print(self):
        string_print = []

        print(self.enote.formatted_note_name, " ", self.modifier, " ", self.octave)
