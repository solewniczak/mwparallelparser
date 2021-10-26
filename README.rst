mwparallelparser
================

**mwparallelparser** (the *MediaWiki Parallel Parser*) is a Python package
that provides parallel parser for MediaWiki_ wikicode

The name parallel parser refers to idea of `parallel markup`_ proposed
by Ted Nelson. In the parallel markup approach the raw text data and the
formatting information are kept separately. Each formatting tag contains
information about its position in the document. This format has many
advantages over traditional embedded markup.  Among others, it is much more
nautral for many machine learning related topics.

There several key assumptions for the parser, that should be kept in mind:
* The raw text data should be as clean as possible. Parser should remove
any formatting syntax, even when corresponding parallel markup isn't produced.
* The white spaces should be removed if they don't provide any
additional information. That means that several following spaces in the wikicode
should be rendered as one space character if it is a part of a normal paragraph.

Usage
-----
Normal usage is rather straightforward (where ``parallel_wikicode`` is the wikicode):

>>> from mwparallelparser import Parser
>>> parser = Parser()
>>> parallel_wikicode = parser.parse(parallel_wikicode)
>>> print(wikicode['lines'])
>>> print(wikicode['tags'])

The ``wikicode['lines']`` contains the raw text lines, generated from the given wikicode.
The lines are kept in Python list and doesn't contain ending new line character.

Tags supported
---------------
wiki link


.. _MediaWiki:        https://www.mediawiki.org
.. _parallel markup:  https://www.xml.com/pub/a/w3j/s3.nelson.html