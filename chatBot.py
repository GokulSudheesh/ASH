from fun import funsies
from tensorflow.keras.models import load_model
import numpy as np
import nltk
import json
from random import choice

words = np.load("words.npy")
words_len = len(words)
classes = np.load("classes.npy")
ignore = [".", "?","!",","]

lemma = nltk.wordnet.WordNetLemmatizer()
with open("intents.json") as json_data:
    intents = json.load(json_data)

def encode_sentence(sentence):
    bag = []
    # Tokenize and lemmatize (I'm lemmatizing)
    tokens = nltk.word_tokenize(sentence)
    token_words = [lemma.lemmatize(w.lower(), pos="v") for w in tokens if w not in ignore]
    for w in words:
        if w in token_words:
            bag.append(1)
        else:
            bag.append(0)
    return np.array(bag)

def get_response(sentence):
    sentence = encode_sentence(sentence)
    comparison = sentence == np.array([0]*words_len)
    if (comparison.all()):
        for intent in intents["intents"]:
            if intent["tag"] == "noanswer":
                return choice(intent["responses"])
    result = model.predict(sentence.reshape(-1, words_len))
    tag = classes[np.argmax(result, axis=1)[0]]
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            response = choice(intent["responses"])
            if (response in list(funsies.keys())):
                return funsies[response](response)
            return response

model = load_model("models/model-191.model")

def main():
    while (True):
        user_message = input(">")
        print(get_response(user_message))

if __name__ == '__main__':
    main()
