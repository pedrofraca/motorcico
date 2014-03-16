import string
import base64
import copy
import logging
from item import Item
class normalizator():
    def remove_words_in_list(self,words_to_remove,list):
        for word in list:
            for remove_word in words_to_remove:
                if word == remove_word:
                    list.remove(word)
        return list

    def normalize(self,string_to_normalize):
        articles = ['el','la','los','las','un','una','unos','unas','lo','al','del','the']
        string_to_normalize = string.lower(string_to_normalize)
        return self.remove_words_in_list(articles,string_to_normalize.split(' '))

    def as_base_64(self,words_list):
        phrase=""
        for word in words_list:
            phrase += word
            phrase_encoded = base64.b64encode(phrase.encode('utf-8'))
        return phrase_encoded
def expand_items(list_to_expand):
    list_to_return = []
    logging.info(list_to_expand)
    for item in list_to_expand:
        if item.links_list:
            if len(item.links_list)>0:
                for link in item.links_list:
                    new_item = copy.deepcopy(item)
                    new_item.link = link
                    new_item.price = item.price_list[item.links_list.index(link)]
                    list_to_return.append(new_item)
    return list_to_return
