#!/usr/bin/env python3

from pydub import AudioSegment
import csv
import os

os.mkdir('results')

t1 = 3000  # Works in milliseconds
wordList = [line.rstrip('\n') for line in open('words.txt')]


with open('results/audio_words.csv', mode='w') as audio_words:
    words_writer = csv.writer(audio_words, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    words = AudioSegment.from_file("words.wav", format="wav")

    count = len(wordList)

    for i in range(0, count):
        name = 'results/' + "audio000" + str(i) + ".wav"
        new = words[i*t1:i*t1+t1]
        new.export(name, format="wav")
        words_writer.writerow([name, wordList[i]])

