import unicodedata
import re
import json
import spacy
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import pandas as pd
import acquire
from typing import List, Dict

def basic_clean(text):
    text = unicodedata.normalize('NFKD', text.lower())\
        .encode('ascii', 'ignore')\
        .decode('utf-8', 'ignore')
    return re.sub(r"[^a-z0-9'\s]", '', text)

def stem(text):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in text.split()]
    return ' '.join(stems)

def lemmatize(text):
    nlp = spacy.load('en', parse=True, tag=True, entity=True)
    doc = nlp(text) # process the text with spacy
    lemmas = [word.lemma_ for word in doc]
    text_lemmatized = ' '.join(lemmas)
    return re.sub(r"\s*(-PRON-|\'s|\')", '', text_lemmatized)

def remove_stopwords(text):
    tokenizer = ToktokTokenizer()
    stopword_list = stopwords.words('english')
    stopword_list.remove('no')
    stopword_list.remove('not')
    tokens = tokenizer.tokenize(text)
    filtered_tokens = [t for t in tokens if t not in stopword_list]
    return ' '.join(filtered_tokens)

def prep_text(text):
    return {
        'original': text,
        'stemmed': stem(basic_clean(text)),
        'lemmatized': lemmatize(basic_clean(text)),
        'clean': remove_stopwords(basic_clean(text))
    }

def prepare_article_data(articles: List[Dict[str, str]]):
    return [{**article, **prep_text(article['content'])} for article in articles]
