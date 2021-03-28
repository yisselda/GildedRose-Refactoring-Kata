# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_sell_by_date_passed(self):
        items = [Item("foo", 2, 22)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(20, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(16, items[0].quality)

    def test_quality_is_never_negative(self):
        items = [Item("foo", 10, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 10, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_brie_quality_cant_be_more_than_50(self):
        items = [Item("Aged Brie", 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 666, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(666, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(666, items[0].sell_in)

    def test_conjured_quality(self):
        items = [Item("Conjured", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)
        self.assertEqual(8, items[0].sell_in)

        
if __name__ == '__main__':
    unittest.main()
