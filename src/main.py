import time
import datetime
from Search import create_search_term, get_five_most_search_terms
import webapp2
from item import Item
from Index import index_item_and_store_item
from itemsearcher import itemsearcher
from google.appengine.ext.webapp import template
from counters import get_item_counter

import os
#import PyRSS2Gen

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {'items':get_item_counter(),'most_searched':get_five_most_search_terms()}
        path = os.path.join(os.path.dirname(__file__),'templates/main.html')
        self.response.out.write(template.render(path,template_values))

class IndexItem(webapp2.RequestHandler):
    def get(self):
        term_to_index=self.request.get('t')
        link_to_index=self.request.get('l')
        item=Item()
        item.title=term_to_index
        item.link=link_to_index
        index_item_and_store_item(item)
        template_values = {}
        path = os.path.join(os.path.dirname(__file__),'templates/main.html')
        self.response.out.write(template.render(path,template_values))

class Searcher(webapp2.RequestHandler):
    def get(self):
        term_to_search=self.request.get('c')
        page=self.request.get('p')
        format_=self.request.get('f')
        if self.verify(term_to_search):
            create_search_term(term_to_search)
            t0 =time.time()
            total,pages=itemsearcher().get_number_of_pages(term_to_search)
            items = itemsearcher().search_items_by_string(term_to_search,page)
            if format_:
                if format_=='rss':
                    self.print_results_as_rss(items, term_to_search,time.time() - t0,pages,total)
                else:
                    self.print_results(items, term_to_search,time.time() - t0,pages,total)
            else:
                self.print_results(items, term_to_search,time.time() - t0,pages,total)
        else:
            self.redirect('/')
    
    def print_results(self,items,searchTerm,seconds = 1,pages=1,total=1):
        template_values = {
        'items_found':total,
        'seconds':seconds,
        'pages':range(1,pages+1),
        'search_term':searchTerm,
        'items':items}
        path = os.path.join(os.path.dirname(__file__),'templates/results.html')
        self.response.out.write(template.render(path,template_values))
    

    def print_results_as_rss(self,items,searchTerm,seconds=1,pages=1):
        rss_items = []
        for item in items:
            rss_items.append(PyRSS2Gen.RSSItem(title=item.title,
                                               link=item.link,
                                               description=item.as_html(),
                                               guid = PyRSS2Gen.Guid(item.image),
                                               pubDate = datetime.datetime.now()))
        
        rss = PyRSS2Gen.RSS2(title=searchTerm,link="http://sviniyls.com",description="returned in seconds",items=rss_items)

        self.response.out.write(rss.to_xml())
        
    def verify(self,searchTerm):
        if searchTerm.strip()=='':
            return False
        return True

app = webapp2.WSGIApplication(        [('/', MainPage),
                                       ('/index',IndexItem),
                                       ('/result',Searcher)],
                                     debug=True)

