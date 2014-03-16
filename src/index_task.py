from google.appengine.ext import webapp
from google.appengine.api import memcache
from Index import index_item_and_store_item
from google.appengine.ext.webapp.util import run_wsgi_app

class IndexTaskHandler(webapp.RequestHandler):
    def post(self):
        all_items = memcache.get("items")
        if all_items:
            for item in all_items:
                index_item_and_store_item(item)

application = webapp.WSGIApplication(
                                     [('/index/index', IndexTaskHandler)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
