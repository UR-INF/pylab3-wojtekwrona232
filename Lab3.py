# fragmenty dotyczące rozwiązania poszczególnych zadań proszę oddzielić odpowiednimi komentarzami
from array import *
import random
import numpy as np


# zad 2
def zad2():
    m_array = array('u', [])

    number = int(input('Podaj ilość znaków wproadzanych'))
    ii = 0
    while ii < number:
        m_array.append(input('Podaj jakikolwiek znak'))
        ii += 1

    for i in reversed(m_array):
        print(i)


# zad 3
def zad3():
    m_array = []
    number = int(input('Podaj ilość znaków wproadzanych'))
    ii = 0
    while ii < number:
        m_array.append(random.randrange(-5, 5))
        ii += 1
    file = open('results.txt', 'w')
    file.write(m_array.__str__())


# zad 4
def zad4():
    array = np.array([[2, 3, 4, 5, 6],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0]
                      ], dtype=np.float)
    for i in range(1, 5):
        for j in range(5):
            array[i][j] = array[i - 1][j] * array[i - 1][j]

    print(array)


# zad 5
def zad5():
    file_name = input("Podaj nazwę pliku")
    file = open(file_name+'.txt')
    histogram = {}
    while True:
        character = file.read(1)
        if not character:
            break
        if character in histogram:
            il = histogram.get(character)
            histogram[character] = il + 1
        else:
            histogram[character] = 1
    file.close()
    print(histogram)


# zad 6
def zad6():
    def deck():
        deck = [('2', 'c'), ('2', 'd'), ('2', 'h'), ('2', 's'), ('3', 'c'), ('3', 'd'), ('3', 'h'), ('3', 's'),
                ('4', 'c'), ('4', 'd'), ('4', 'h'), ('4', 's'), ('5', 'c'), ('5', 'd'), ('5', 'h'), ('5', 's'),
                ('6', 'c'), ('6', 'd'), ('6', 'h'), ('6', 's'), ('7', 'c'), ('7', 'd'), ('7', 'h'), ('7', 's'),
                ('8', 'c'), ('8', 'd'), ('8', 'h'), ('8', 's'), ('9', 'c'), ('9', 'd'), ('9', 'h'), ('9', 's'),
                ('10', 'c'), ('10', 'd'), ('10', 'h'), ('10', 's'), ('J', 'c'), ('J', 'd'), ('J', 'h'), ('J', 's'),
                ('D', 'c'), ('D', 'd'), ('D', 'h'), ('D', 's'), ('K', 'c'), ('K', 'd'), ('K', 'h'), ('K', 's'),
                ('A', 'c'), ('A', 'd'), ('A', 'h'), ('A', 's')]
        return deck

    def shuffle_deck(deck_):
        random.shuffle(deck_)
        return tuple(deck_)

    def deal(deck_, n):
        card_list = []
        shuffled_deck = shuffle_deck(deck_)
        x = 0
        for i in range(n):
            for j in range(5):
                card_list.append(shuffled_deck[x])
                x = x + 1

        print(card_list)

    deal(deck(), 5)


# Wywołanie zadania
zad6()

