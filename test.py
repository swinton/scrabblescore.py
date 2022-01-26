"""
Run the tests with: python -m unittest
"""
import unittest

import scrabblescore

class Tests(unittest.TestCase):
  def test_blankword(self):
    self.assertEqual(scrabblescore.scrabblescore(''), 0)

  def test_scrabblescore(self):
    self.assertEqual(scrabblescore.scrabblescore('oxyphenbutazone'), 41)
