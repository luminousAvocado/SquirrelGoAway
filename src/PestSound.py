from pygame import *
import glob
import random


class audiofile(object):
    def __init__(self, file, id):
        self.file = file
        self.id = id

    def play_file(self):
        mixer.init()
        mixer.music.load(self.get_file())
        mixer.music.play()

        while mixer.music.get_busy():
            time.Clock().tick(10)

    def get_file(self):
        return self.file

    def get_id(self):
        return self.id


class s_dict(object):

    def __init__(self):
        self.animals = []
        self.frequencies = []
        self.chaos = []
        self.use_animal = True
        self.use_frequencies = True
        self.use_chaos = True

    def set_animals_true(self):
        self.use_animal = True

    def set_animals_false(self):
        self.use_animal = False

    def set_frequencies_true(self):
        self.use_frequencies = True

    def set_frequencies_false(self):
        self.use_frequencies = False

    def set_chaos_true(self):
        self.use_chaos = True

    def set_chaos_false(self):
        self.use_chaos = False

    def get_files(self):
        animal_files = glob.glob("animals/*.wav")
        frequencies_files = glob.glob("frequencies/*.wav")
        chaos_files = glob.glob("chaos/*.wav")

        # id value for files
        n = 0

        # get the files from all folders
        for i in animal_files:
            self.animals.append(audiofile(i, n))
            n += 1
        for i in frequencies_files:
            self.frequencies.append(audiofile(i, n))
            n += 1
        for i in chaos_files:
            self.chaos.append(audiofile(i, n))
            n += 1

    # for testing purposes
    def list_files(self):
        for i in self.animals:
            print(i.get_file())

    def play_rand_file(self):
        sounds = []

        if self.use_animal:
            sounds.extend(self.animals)
        if self.use_frequencies:
            sounds.extend(self.frequencies)
        if self.use_chaos:
            sounds.extend(self.chaos)
        if len(sounds) == 0:
            return

        x = random.randint(0, len(sounds))
        sounds[x].play_file()




