from enum import Enum, unique
import winsound


class EQuality(Enum):
    Mayor = 0
    Minor = 1
    Perfect = 2
    Diminished = 3
    Augmented = 4


class EModifier(Enum):
    MAYOR = 0
    MINOR = 1
    DIMINISHED = 2
    AUGMENTED = 3


class ENotes(Enum):
    A = 0
    AS = 1
    B = 2
    C = 3
    CS = 4
    D = 5
    DS = 6
    E = 7
    F = 8
    FS = 9
    G = 10
    GS = 11

    def describe(self):
        # self is the member here
        return self.name, self.value

    def __str__(self):
        return 'my custom str! {0}'.format(self.value)

    def formatted_note_name(self):
        # self is the member here
        if self.name == self.AS.name:
            return 'A#'
        elif self.name == self.CS.name:
            return 'C#'
        elif self.name == self.DS.name:
            return 'D#'
        elif self.name == self.FS.name:
            return 'F#'
        elif self.name == self.GS.name:
            return 'G#'
        else:
            return self.name


class ENotesSP(Enum):
    La = 0
    LaS = 1
    Si = 2
    Do = 3
    DoS = 4
    Re = 5
    ReS = 6
    Mi = 7
    Fa = 8
    FaS = 9
    Sol = 10
    SolS = 11


def beep(self, frequency, duration):
    # frequency = 2500  # Set Frequency To 2500 Hertz
    # duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
