"""
This class uses static methods to operate with the other helper classes to get a corpus or parse / crawl a directory or file.
The filename(s) is sent to the processor class which takes care of parsing the files.
Lastly the similarity class is called, that vectorizes the text and calculates the similarity using numpy

@Author: ovanov
@date: 03.08.21
"""

import os
from typing import List, Dict

from .text_preprocessor import Preprocess
from .similarity import Similarity

class Parser():

    @staticmethod
    def parse_dir(path_to_dir: str, base_file: Dict, lang: str) -> List:
        """
        This function parses the dir and returns a list of similarites. It calls the function "getSimilarity"
        """
        list_of_sims = []
        for file in os.listdir(path_to_dir):
            if file.endswith(".txt"):
                file = os.path.join(path_to_dir, file)
                file_to_compare = Preprocess.preprocess(file, lang)
                cossim = Similarity.get_sim(base_file, file_to_compare) * 100
                list_of_sims.append(round(cossim,6))

        return list_of_sims

    @staticmethod
    def parse_file(path_to_file: str, base_file: Dict, lang:str) -> List:
        """
        This function parses the file and returns a list of similarites. It calls the function "get_sim"
        """

        list_of_sims = []
        file_to_compare = Preprocess.preprocess(path_to_file, lang)
        cossim = Similarity.get_sim(base_file, file_to_compare) * 100
        list_of_sims.append(round(cossim,6))

        return list_of_sims


    def get_corpus(base: str, lang: str) -> Dict:
        """
        This function takes the base value (default == false) as well as the lang (default == 'de)
        and determines by taking both values into account, which corpus should be used.
        If base is 'False' and no language is specified, the standard basefile for german is used.
        If the language is 'en', the standard english corpus is used.
        If a basefile is specified, of course the language flag does not matter and the basefile is
        passed to the "process_base()" function.
        """

        dir = os.path.dirname(__file__) # get relative path to corpora
        standard_german_corpus = os.path.join(dir, 'corpora', 'german.txt')
        standard_english_corpus = os.path.join(dir, 'corpora', 'english.txt')

        if lang == 'de':
            if base == False:
                return Preprocess.preprocess(standard_german_corpus, lang)
            else:
                return Preprocess.preprocess(base, lang)
        elif lang == 'en':
            if base == False:
                return Preprocess.preprocess(standard_english_corpus, lang)
            else:
                return Preprocess.preprocess(base, lang)
