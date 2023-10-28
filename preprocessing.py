__author__ = "Younes Karimi"
__email__ = "younes@psu.edu"
__description__ = "This file contains functions for preprocessing text files"

import re

def remove_urls(text):
  # urls.extend(re.findall('http[s]?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text))
  # urls.extend(re.findall('www.(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text))
  return re.sub(r'(www.[^\s]+)', ' ', re.sub(r'(https?://[^\s]+)', ' ', text))

def remove_handles(text):
  return re.sub(r'@([^\s:]+)', ' ', text)

def replace_hashtags(text):
  return text.replace('#', ' ').replace('_', ' ')

def remove_punctuations(text):
  punctuations = ['،', '؛', '«', '»', ':', '؟', '>', '<', '{', '}', '!', '٫', '٪', '*', '(', ')', '/', '\\', '|']
  return ''.join([word for word in text if word not in punctuations])

# ToDo if tokenized analysis is needed
def remove_stopwords(tokens):
  stopwords = []
  # remove stopwords
  return [token for token in tokens if token not in stopwords]

def preprocess(text, token_analysis=False):
  if token_analysis: # use this for analyzing individual tokens, rather than sentences
    return remove_stopwords(remove_punctuations(replace_hashtags(remove_handles(remove_urls(text)))))
  return replace_hashtags(remove_handles(remove_urls(text)))