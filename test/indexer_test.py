import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir+"/src") 

from normalizator import expand_items
class ItemMock:
    links_list = ['a','b','c']

class nomalizator_testcase(unittest.TestCase):
    string_to_parse = ""

    def test_expand_all(self):
        items_list = []
        for i in range(10):
            items_list.append(ItemMock())
        self.assertEqual(10,len(items_list))
        final_list = expand_items(items_list)
        self.assertEqual(30,len(final_list))


if __name__ == '__main__':
    unittest.main()

