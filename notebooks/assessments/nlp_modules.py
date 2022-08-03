import re
from hazm import *

normalizer = Normalizer()


def clean_tweet(text=None):
    """ get text of tweet and clean it.

        cleaning is done for:
        1- urls
        2- emoticons
        3- mentions from the beginning of text
        4- remove hashtags from the beginning and end of text
        5- punctuations
    :param text: fulltext of tweet
    :return: cleaned text
    """

    full_text = text

    # remove urls
    regex = re.compile('https:\S*')
    it = re.finditer(regex, full_text)
    for match in it:
        full_text = full_text.replace(match.group(0), "")

    # remove emoticons
    emoji_pattern = re.compile(u'['
                               u'\U0001F300-\U0001F64F'
                               u'\U0001F680-\U0001F6FF'
                               u'\u2600-\u26FF\u2700-\u27BF]+',
                               re.UNICODE)
    full_text = emoji_pattern.sub('', full_text)

    # remove mentions
    regex = re.compile('@\w*')
    it = re.finditer(regex, full_text)
    for match in it:
        full_text = full_text.replace(match.group(0), "")

    # remove mention sign from rest of text
    full_text = full_text.replace("@", "")

    # remove hashtags at the end of string
    regex = re.compile('([\n\s]*#\w*)*\Z')
    it = re.finditer(regex, full_text)
    for match in it:
        full_text = full_text.replace(match.group(0), "")

    # remove hashtags in the begining of string
    regex = re.compile('\A([\s\n]*#\w*\s*\n+\s*)*')
    it = re.finditer(regex, full_text)
    for match in it:
        full_text = full_text.replace(match.group(0), "")

    full_text = full_text.replace("#", "")
    full_text = full_text.replace("RT", "")

    # remove punctuations:
    # full_text = re.sub('\S+', lambda m: re.sub('^\W+|\W+$', '', m.group()), full_text)
    full_text = full_text.strip()

    return full_text


def tokenizer_hazm(text):
    tokenized = []
    for sent in sent_tokenize(text):
        tokenized.extend(word_tokenize(sent))
    return tokenized


def process(full_text):
    # clean
    cleaned_text = clean_tweet(text=full_text)
    # normalize
    normalized_text = normalizer.normalize(cleaned_text)
    # tokenize
    tokenized_text = tokenizer_hazm(normalized_text)
    # convert to string
    return " ".join(tokenized_text)
