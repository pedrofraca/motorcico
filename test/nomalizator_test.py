import unittest

from normalizator import normalizator


class nomalizator_testcase(unittest.TestCase):
    string_to_parse = ""

    def test_normalize_string_returns_list(self):
        the_normalizator = normalizator()
        result=[]
        result = the_normalizator.normalize("los planetas")
        self.assertEqual(len(result), 1)
    def test_normalize_string_resturns_correct_array(self):
        the_normalizator = normalizator()
        result=[]
        result = the_normalizator.normalize("los planetas")
        self.assertEqual(result[0], "planetas")
    def test_normalize_string_avoids_articles(self):
        the_normalizator = normalizator()
        result = the_normalizator.normalize("el fary")
        self.assertEqual(result[0], "fary")
    def test_normalize_string_avoids_some_articles(self):
        the_normalizator = normalizator()
        result = the_normalizator.normalize("el fary los planetas")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "fary")
        self.assertEqual(result[1], "planetas")
    def test_normalize_string_avoids_some_articles_and_uppercase(self):
        the_normalizator = normalizator()
        result = the_normalizator.normalize("el Fary LOS PLANETAS")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "fary")
        self.assertEqual(result[1], "planetas")
    def test_normalize_string_avoids_some_articles_languages(self):
        the_normalizator = normalizator()
        result = the_normalizator.normalize("the red hot chili peepers")
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], "red")
        self.assertEqual(result[1], "hot")
        self.assertEqual(result[2], "chili")
        self.assertEqual(result[3], "peepers")


if __name__ == '__main__':
    unittest.main()

