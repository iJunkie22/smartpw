import random
__author__ = 'ethan'


vowels1 = "AEIOUY"
vowels2 = (65, 69, 73, 79, 85, 89)
vowels3 = (97, 101, 105, 111, 117, 121)

rand = random.Random()
rand.seed(5)


class LetterFactory:
    ascii_special = range(33, 48) + range(58, 65) + range(91, 97) + range(123, 127)
    ascii_numbers = range(48, 58)
    ascii_uppercase = range(ord("A"), ord("Z") + 1)
    ascii_lowercase = range(ord("a"), ord("z") + 1)
    ascii_letters = ascii_uppercase + ascii_lowercase
    vowels_upper = [ord(u_v) for u_v in "AEIOUY"]
    vowels_lower = [ord(l_v) for l_v in "aeiouy"]
    consos_upper = sorted(list(set(ascii_uppercase) - set(vowels_upper)))
    consos_lower = sorted(list(set(ascii_lowercase) - set(vowels_lower)))
    ascii_vowels = vowels_upper + vowels_lower
    ascii_consos = consos_upper + consos_lower

    def __init__(self, seed=None):
        self.rand = random.Random()
        self.rand.seed(seed)
        self.last_used = None
        self.last_was_conso = False
        self.last_was_vowel = False

    @staticmethod
    def coerce_to_ascii_int(c1):
        test_char_int = None
        try:
            test_char_int = int(c1)
        except ValueError as _ve:
            test_char_int = ord(c1)
        finally:
            assert isinstance(test_char_int, int)
        return test_char_int

    def make(self, kind=2, vowel=2):
        """


        :type vowel: int
        :param kind: 0=spec, 1=int, 2=letter, 3=non-special, 4=random
        :type kind: int
        :param vowel: 0=vowel, 1=consonants, 2=random
        :return:
        """
        if kind == 3:
            kind = self.rand.randint(1, 2)
        elif kind == 4:
            kind = self.rand.randint(0, 2)

        if kind == 0:
            c_set = self.ascii_special
            self.last_was_vowel = False
            self.last_was_conso = False

        elif kind == 1:
            c_set = self.ascii_numbers
            self.last_was_vowel = False
            self.last_was_conso = False

        elif kind == 2:
            if self.last_was_conso:
                vowel = 0
            if self.last_was_vowel:
                vowel = 1

            if vowel == 2:
                vowel = self.rand.randint(0, 1)
            if vowel == 0:
                c_set = self.vowels_lower
                self.last_was_vowel = True
                self.last_was_conso = False
            elif vowel == 1:
                c_set = self.consos_lower
                self.last_was_vowel = False
                self.last_was_conso = True
            else:
                raise Exception(vowel)
        else:
            raise Exception(kind)

        return chr(self.rand.choice(c_set))

    ###########################################
    #
    #   Letter Classifications
    #
    ###########################################

    ###########################################
    #   Vowels
    ###########################################

    @classmethod
    def is_vowel_upper(cls, c2):
        return cls.coerce_to_ascii_int(c2) in cls.vowels_upper

    @classmethod
    def is_vowel_lower(cls, c3):
        return cls.coerce_to_ascii_int(c3) in cls.vowels_lower

    @classmethod
    def is_vowel_any(cls, c4):
        return cls.is_vowel_upper(c4) or cls.is_vowel_lower(c4)

    ###########################################
    #   Consonants
    ###########################################

    @classmethod
    def is_conso_upper(cls, c5):
        return cls.coerce_to_ascii_int(c5) in cls.consos_upper

    @classmethod
    def is_conso_lower(cls, c6):
        return cls.coerce_to_ascii_int(c6) in cls.consos_lower

    @classmethod
    def is_conso_any(cls, c7):
        return cls.is_conso_upper(c7) or cls.is_conso_lower(c7)


def run_factory(factory, s_length):
    assert isinstance(factory, LetterFactory)
    assert isinstance(s_length, int)
    return ''.join([factory.make() for i in range(0, s_length)])

