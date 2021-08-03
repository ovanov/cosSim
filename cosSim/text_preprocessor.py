"""
This Preprocess class parses each file and counts each occurance of each word

@Author: ovanov
@Date: 03.08.21
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from typing import Dict
import nltk


class Preprocess():

    @staticmethod
    def preprocess(file: str, *args) -> Dict:
        """
        process, when called, crawls through the directory or file and opens it. The text is tokenized, stemmed and listed.
        """
        with open (file, 'r', encoding='utf-8', errors='ignore') as f:
            readfile = f.read()
            tokens = word_tokenize(readfile)
            words = [w.lower() for w in tokens]

            porter = nltk.PorterStemmer()
            stemmed_tokens = [porter.stem(t) for t in words]

            #Remove stopwords
            if args[0] == 'de':
                stop_words = set(stopwords.words('german'))
            elif args[0] == 'en':
                stop_words = set(stopwords.words('english'))
            else:
                stop_words = set(stopwords.words('german'))

            filtered_tokens = [w for w in stemmed_tokens if not w in stop_words]

            # count words
            count = nltk.defaultdict(int)
            for word in filtered_tokens:
                count[word] += 1
            return count
