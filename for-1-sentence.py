import random

print('무작위 배열할 문장을 "한 문장씩" 입력해주세요!!')
while True:
    sentence = input().split()
    random.shuffle(sentence)
    question = '('
    for sentence_tmp in sentence:
        question = question + sentence_tmp + '/'
    print('단어 무작위 배열 결과: ' + question[:-1] + ')')
