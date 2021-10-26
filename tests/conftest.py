import unittest

from src.mwparallelparser import Parser


class ParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def assertParsed(self, wikitext, lines, tags=None):
        result = self.parser.parse(wikitext)
        self.assertEqual(lines, result['lines'])
        if tags is not None:
            self.assertEqual(tags, result['tags'])