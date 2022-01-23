import unittest

from tests.conftest import ParserTestCase


class TableTestCase(ParserTestCase):
    def test_basic(self):
        wikitext = "{|\n|-\n| Example\n|}"
        tags = [{'type': 'table_cell',
                 'spans': [{'line': 0, 'start': 0, 'length': 7}],
                 'attributes': {'destination': 'Example', 'row': 0, 'column': 0}}]
        self.assertParsed(wikitext, ['Example'], tags)

    def test_columns(self):
        wikitext = "{|\n|-\n| Example || Example2\n|}"
        tags = [{'type': 'table_cell',
                 'spans': [{'line': 0, 'start': 0, 'length': 7}],
                 'attributes': {'destination': 'Example', 'row': 0, 'column': 0}},
                {'type': 'table_cell',
                 'spans': [{'line': 0, 'start': 8, 'length': 8}],
                 'attributes': {'destination': 'Example2', 'row': 0, 'column': 1}}]
        self.assertParsed(wikitext, ['Example Example2'], tags)

    def test_rows(self):
        wikitext = "{|\n|-\n| Example\n|-\n| Example2\n|}"
        tags = [{'type': 'table_cell',
                 'spans': [{'line': 0, 'start': 0, 'length': 7}],
                 'attributes': {'destination': 'Example', 'row': 0, 'column': 0}},
                {'type': 'table_cell',
                 'spans': [{'line': 0, 'start': 8, 'length': 8}],
                 'attributes': {'destination': 'Example2', 'row': 1, 'column': 0}}]
        self.assertParsed(wikitext, ['Example Example2'], tags)

    def test_caption(self):
        wikitext = "{|\n|+ Caption text\n|-\n| Example || Example || Example\n|}"
        self.assertParsed(wikitext, ['Example Example Example'])

    def test_class(self):
        wikitext = '{| class="wikitable"\n|-\n| Example || Example || Example\n|}'
        self.assertParsed(wikitext, ['Example Example Example'])

    def test_header(self):
        wikitext = "{|\n|-\n! Header !! Header\n|-\n| Example || Example\n|}"
        tags = [{'type': 'table_cell',
                 'spans': [{'line': 0, 'start': 0, 'length': 6}],
                 'attributes': {'destination': 'Header', 'row': 0, 'column': 0}},
                {'type': 'table_cell',
                 'spans': [{'line': 0, 'start': 7, 'length': 6}],
                 'attributes': {'destination': 'Header', 'row': 0, 'column': 1}},
                {'type': 'table_cell',
                 'spans': [{'line': 0, 'start': 14, 'length': 7}],
                 'attributes': {'destination': 'Example', 'row': 1, 'column': 0}},
                {'type': 'table_cell',
                 'spans': [{'line': 0, 'start': 22, 'length': 7}],
                 'attributes': {'destination': 'Example', 'row': 1, 'column': 1}}]
        self.assertParsed(wikitext, ['Header Header Example Example'], tags)

    def test_link(self):
        wikitext = "{|\n|-\n! [[Header]]\n|-\n| [[Example]]\n|}"
        tags = [{'type': 'table_cell',
                 'spans': [{'line': 0, 'start': 0, 'length': 6}],
                 'attributes': {'destination': 'Header', 'row': 0, 'column': 0}},
                {'type': 'table_cell',
                 'spans': [{'line': 0, 'start': 7, 'length': 7}],
                 'attributes': {'destination': 'Example', 'row': 1, 'column': 0}}]
        self.assertParsed(wikitext, ['Header Example'], tags)
