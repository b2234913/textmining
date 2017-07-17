# -*- coding=utf-8 -*-
import json
import collections
from collections import OrderedDict
from counter import Counter
import numpy as np
import random
import math
def LearnVocabFromTrainFile():
        
    # 開啟唐詩語料庫

    f = open("poem.txt")
 
    # 統計唐詩語料庫中每個字出現的頻率

    vcount = Counter()
    for line in f.readlines():
        for w in line.decode("utf-8").strip().split():
            vcount.update(w)
            
    # 僅保留出現次數大於五的字，並按照出現次數排序

    vcount_list = sorted(filter(lambda x: x[1] >= 5, vcount.items())
                         , reverse=True, key=lambda x: x[1])
                         
    # 建立字典，將每個字給一個id ，字為 key, id 為 value

    vocab_dict = OrderedDict(map(lambda x: (x[1][0], x[0]), enumerate(vcount_list)))
    
    # 建立詞頻統計用的字典，給定某字，可查到其出現頻率

    vocab_freq_dict = OrderedDict(map(lambda x: (x[0], x[1]), vcount_list))
    return vocab_dict, vocab_freq_dict
    
vocab_dict, vocab_freq_dict =  LearnVocabFromTrainFile()
for w,wid in vocab_dict.items():
	print("%s : %s"%(w,wid))
