# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
API_PATH = "api.txt"
INPUT_PATH = "input.txt"
KEYS = 10

class NLPanalyzer(object):
    def __init__(self):
        self.nlp = BosonNLP(self.__getAPI())
        self.text = self.__getTXT()
    def __getAPI(self):
        with open(API_PATH, "r") as api:
            return api.read().split('\n')[0]

    def __getTXT(self):
        with open(INPUT_PATH, "r") as data:
            text = data.read()
            return text

    def getTopKeyWords(self, k):
        result = self.nlp.extract_keywords(self.text, top_k = k)
        for weight, word in result:
            print(weight, word)

    def getSummary(self):
        smry = self.nlp.summary('', self.text)
        print(smry)

    def getTokens(self):
        result = self.nlp.tag(self.text)
        for d in result:
            print(' '.join(['%s/%s\n' % it for it in zip(d['word'], d['tag'])]))

if __name__ == "__main__":
    NLPanalyzer = NLPanalyzer()
    print("original text:\n")
    print(NLPanalyzer.text)

    print("top key words: %d\n", (KEYS))
    NLPanalyzer.getTopKeyWords(KEYS)

    print("Summary: %d\n")
    NLPanalyzer.getSummary()

    print("Tokens: \n")
    NLPanalyzer.getTokens()

