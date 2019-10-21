from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Bird:
    def _base_speed(self):
        return 12.0


class EuropeanParrot(Bird):
    def speed(self):
        return self._base_speed()


class AfricanParrot(Bird):
    def __init__(self, number_of_coconuts):
        self._number_of_coconuts = number_of_coconuts

    def _load_factor(self):
        return 9.0

    def speed(self):
        return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)

class NorwegianBlue(Bird):
    def __init__(self, voltage, nailed):
        self._voltage = voltage
        self._nailed = nailed

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    def speed(self):
        if self._nailed:
            return 0
        else:
            return self._compute_base_speed_for_voltage(self._voltage)


class Parrot:

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
        if self._type == ParrotType.EUROPEAN:
            self._parrot = EuropeanParrot()
        elif self._type == ParrotType.NORWEGIAN_BLUE:
            self._parrot = NorwegianBlue(voltage, nailed)
        else:
            self._parrot = AfricanParrot(number_of_coconuts)

    def speed(self):
        return self._parrot.speed()
