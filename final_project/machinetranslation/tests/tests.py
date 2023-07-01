import unittest
from translator import englishtofrench,frenchtoenglish
class Test(unittest.TestCase):
    def test1(self):
        self.assertEquals(englishtofrench("Hello"),"Pepitoooo")
        self.assertEquals(englishtofrench("How are you"),"Comment allez-vous")
    def test2(self):
        self.assertEquals(frenchtoenglish("Pepitoooo"),"Hello")
        self.assertEquals(frenchtoenglish("Comment allez-vous"),"How are you")

unittest.main()