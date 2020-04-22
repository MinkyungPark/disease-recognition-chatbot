# %%
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

import keras.backend.tensorflow_backend as tb
tb._SYMBOLIC_SCOPE.value = True

import numpy as np
import pandas as pd
import sys

seed = 0
np.random.seed(seed)


import pickle

# Dictionary LOAD
with open('data/word_index_v3.pickle', 'rb') as fr:
    word_index = pickle.load(fr)

with open('data/index_word_v3.pickle', 'rb') as fr:
    index_word = pickle.load(fr)

with open('data/category_to_idx_v3.pickle', 'rb') as fr:
    category_to_idx = pickle.load(fr)

with open('data/idx_to_category_v3.pickle', 'rb') as fr:
    idx_to_category = pickle.load(fr)

# {0: '가래', 1: '가슴통증', 2: '고열', 3: '관절통', 4: '구취', 5: '구토', 6: '기침', 7: '다뇨', 8: '다식', 9: '다음', 10: '두통', 11: '반신마비', 12: '방사통', 13: '복부팽만', 14: '복시', 15: '복통', 16: '설사', 17: '소양감', 18: '소화불량', 19: '손발저림', 20: '시력감소', 21: '시야장애', 22: '식욕부진', 23: '심계항진', 24: '어지럼증', 25: '언어장애', 26: '연하곤란', 27: '오심', 28: '요통', 29: '운
# 동장애', 30: '잇몸염증', 31: '천명', 32: '체중감소', 33: '피로감', 34: '하지마비', 35: '호흡곤란'}




#####
from keras.models import load_model
model = load_model('data/bilstm_model64_total_true_0.h5')
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])


from konlpy.tag import Kkma
from keras.preprocessing.sequence import pad_sequences

# 들어온 데이터 전처리

def preprocess(sents):
    kkma = Kkma()
    tagged = kkma.pos(sents)

    result = []
    for word, tag in tagged:        
        if tag in ['NNG']: #and len(word) > 1:
            result.append(word)
        if tag in ['VV', 'VA']:
            result.append(word + "다")

    result = ' '.join(result)

    return result

sents_len = 512

# 전처리된 데이터 sequences로 만들기
def txt_to_seq(sentence):
    encoded=[]
    tmp = []

    for w in sentence.split():
        try:
            tmp.append(word_index[w])
        except KeyError:
            tmp.append(word_index['OOV'])
    
    encoded.append(tmp)
    seq = pad_sequences(encoded, maxlen=sents_len)

    return seq[0]


def idx_to_txt(indexs, vocadic):
    indexs = np.argmax(indexs, axis=-1)
    sentence = ''

    for idx in indexs:
        if vocadic.get(idx) is not None:
            sentence += vocadic[idx]

    return indexs, sentence



def get_category(speech):
    pre_speech = preprocess(speech)
    input_seq = txt_to_seq(pre_speech)
    input_seq = input_seq.reshape(1,512)
    result_idx = model.predict(input_seq)
    proba = model.predict_proba(input_seq)
    result_category = idx_to_txt(result_idx, idx_to_category)

    # return proba, pre_speech, result_category
    return str(result_category[1])


