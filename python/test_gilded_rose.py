# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # This test should fail. The names do not match.
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)
    
    # This test should fail. An item's quality value cannot be over 50. 
    def test_max_quality(self):
        items = [Item("Aged Brie", 53, 55)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

        # This test should fail. An item's quality cannot go below 0. 
    def negative_quality(self):
        items = [Item("Elixir of the Mongoose", 2, -3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    # Checks if conjured items degrade in value correctly. 
    def test_conjured_items(self):
        items = [Item("Conjured Mana Cake", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        
if __name__ == '__main__':
    unittest.main()
