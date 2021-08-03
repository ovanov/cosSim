"""
This class calculates the similarity using cosine similarity. The bag of words list is transformed to a vector, that
is used to calculate the cosine similarity

@Author: ovanov
@date: 03.08.21
"""
import numpy as np
from typing import List, Dict

class Similarity():

    @staticmethod
    def cos_sim(a: List[int], b: List[int]) -> int:
        """
        The calculation uses the standard formula for cosine similarities.
        """
        dot_product = np.dot(a, b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        return dot_product / (norm_a * norm_b)


    @staticmethod
    def get_sim(dict1: Dict, dict2: Dict) -> int:
        """
        This function uses numpy to create empty arrays, that fill in the occurance of specific words.
        Every word has a position and has a counter so to say. The arrays reseble 'vectors' that, that are compared in cos_sim.
        """
        all_words_list = []
        for key in dict1:
            all_words_list.append(key)
        for key in dict2:
            all_words_list.append(key)
        all_words_list_size = len(all_words_list)

        v1 = np.zeros(all_words_list_size, dtype=np.float64)
        v2 = np.zeros(all_words_list_size, dtype=np.float64)
        i = 0
        for (key) in all_words_list:
            v1[i] = dict1.get(key,0)
            v2[i] = dict2.get(key,0)
            i = i + 1
        return Similarity.cos_sim(v1,v2)