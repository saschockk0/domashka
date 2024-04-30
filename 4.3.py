import random

print('Сейчас вы увидите случайную анаграмму, вам нужно угадать слово.\n')
input('Нажмите Entr, чтобы начать')
words = ('медведь',
         'канистра',
         'грильяж',
         'табуретка',
         'программист')

word = random.choice(words)
anagramm = ''
word2 = word
while word2:
    length = len(word2)
    symb_index = random.randint(0, (length-1))
    symb = word2[symb_index]
    anagramm += symb
    if symb_index != 0:
        word_start = word2[:symb_index]
    else:
        word_start = ''
    word_end = word2[(symb_index+1):]
    word2 = word_start+word_end
print(anagramm)
print('Можно сразу попробовать угадать слово или попросить подсказку\n')
version = input('Нужна подсказка? y/n\n')
points = 100
if version == 'y':
    print('Слово начинается так:', word[:2], '...?')
    points -= 5
answer = input('Напишите слово и нажмите Entr, чтобы проверить вашу версию\n')
while answer != word:
    answer = input('Напишите слово и нажмите Entr, чтобы проверить вашу версию\n')
    points -= 1
print('Поздравляю, вы угадали!')
print('Вы набрали', points, 'из 100')
input('Нажмите Entr, чтобы выйти')
