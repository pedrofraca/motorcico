from google.appengine.ext import db

class Counters(db.Model):
    items_count = db.IntegerProperty(default=0)
    created = db.DateTimeProperty(auto_now_add=True)

def increase_item_counter():
    counters_db_key = db.Key.from_path("Counters", "1")
    counters_object = db.get(counters_db_key)
    if counters_object:
        counters_object.items_count+=1;
    else :
        counters_object = Counters(key_name="1",items_count=1)
    counters_object.put()

def get_item_counter():
    counters_db_key = db.Key.from_path("Counters", "1")
    counters_object = db.get(counters_db_key)
    if counters_object:
        return counters_object.items_count
    else:
        return 0
