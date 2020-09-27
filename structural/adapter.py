from abc import ABC, abstractmethod


class Sentence(ABC):
    def __init__(self):
        self.words = ''

    def add_word(self, word):
        self.words += ' ' + word

class BigSentence(Sentence):
    @abstractmethod
    def print_big_words(self):
        raise NotImplementedError


class SmallSentence(Sentence):
    @abstractmethod
    def print_small_words(self):
        raise NotImplementedError


class BigWords(BigSentence):
    def __init__(self):
        self.words = "i have the biggest words:".upper()

    def print_big_words(self):
        if not self.words.isupper():
            raise ValueError('i only print big words'.upper())
        print(self.words)


class SmallWords(SmallSentence):
    def __init__(self):
        self.words = "my words are small but they are mine:"

    def print_small_words(self):
        if not self.words.islower():
            raise ValueError('i only print small words')
        print(self.words)


class SmallWordsAdapter(BigSentence):
    def __init__(self, small_words):
        self.words = small_words.words

    def print_big_words(self):
        print(self.words.upper())


if __name__ == '__main__':
    # create small words
    small_words = SmallWords()
    small_words.add_word('inertia')
    small_words.print_small_words()
    # create big words
    big_words = BigWords()
    big_words.add_word('CAT')
    big_words.print_big_words()
    # create big words from small words adapter
    small_words.add_word('fireball')
    adapter = SmallWordsAdapter(small_words)
    adapter.print_big_words()
