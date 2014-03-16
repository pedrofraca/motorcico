
from Index import get_items_by_search_term,get_number_of_pages , index_item_and_store_item
from normalizator import normalizator
from google.appengine.api import memcache
from google.appengine.api import taskqueue
class itemsearcher:
    def search_items_by_string(self,text,page=0):
        if page=='' or page ==None or page=='0':
            page=0
        else:
            page=int(page)-1
            
        text_normalized = normalizator().normalize(text)
        all_items = get_items_by_search_term(text_normalized,page)
        if all_items==None:
            self.get_data_from_server_and_store_it(text)
            all_items = get_items_by_search_term(text_normalized)
        if len(all_items)<5 and page==0:
            self.get_data_from_server_and_store_it(text)
            all_items = get_items_by_search_term(text_normalized)
        return all_items
    
    def get_number_of_pages(self,text):
        text_normalized = normalizator().normalize(text)
        return get_number_of_pages(text_normalized)
    
    def get_data_from_server_and_store_it(self,text):
        #call to servers
        pass
