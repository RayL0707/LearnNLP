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
        print(self.nlp.sentiment(self.text))
    def __getAPI(self):
        with open(API_PATH, "r") as api:
            return api.read().split('\n')[0]

    def __getTXT(self):
        with open(INPUT_PATH, "r") as data:
            text = "".join(data.read().split())
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
            print(' '.join(['%s/%s' % it for it in zip(d['word'], d['tag'])]))

    def getEntity(self):
        result = self.nlp.ner(self.text)[0]
        words = result['word']
        entities = result['entity']
        dicts = {}
        for entity in entities:
            word, cluster = ''.join(words[entity[0]:entity[1]]), entity[2]
            if cluster in dicts:
                dicts[cluster].append(word)
            else:
                dicts[cluster] = [word]

        for key, value in dicts.items():
            print("%s: %s" %(key, ", ".join(value)))
        return dicts



if __name__ == "__main__":
    NLPanalyzer = NLPanalyzer()
    # print("#####################\n")
    # print("original text:\n")
    # print("#####################\n")
    # print(NLPanalyzer.text)
    #
    # print("#####################\n")
    # print("Summary:\n")
    # print("#####################\n")
    # NLPanalyzer.getSummary()
    #
    # print("#####################\n")
    # print("top %d key words:\n" % KEYS)
    # print("#####################\n")
    # NLPanalyzer.getTopKeyWords(KEYS)
    #
    # print("#####################\n")
    # print("Tokens: \n")
    # print("#####################\n")
    # NLPanalyzer.getTokens()

    print("#####################\n")
    print("Entities: \n")
    print("#####################\n")
    NLPanalyzer.getEntity()

