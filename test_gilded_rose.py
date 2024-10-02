# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
    
    def test_aged_brie_quality(self):
        brie = "Aged Brie"
        items = [Item(brie, 2, 0), Item(brie, 1, 1)]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.items[0].quality == 2
        assert gr.items[1].quality == 0
    
    def test_sulfuras_quality_and_sell_in(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 0, 80), Item(sulfuras, -1, 80)]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.items[0].quality == 81
        assert gr.items[0].sell_in == 1
        assert gr.items[1].quality == 81
        assert gr.items[1].sell_in == 0
    
    def test_backstage_passes_quality(self):
        backstage_pass = "Backstage passes to a TAFKAL80ETC concert"
        items = [
            Item(backstage_pass, 10, 20),
            Item(backstage_pass, 5, 20),
            Item(backstage_pass, 0, 20),
        ]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.items[0].quality == 23
        assert gr.items[1].quality == 24
        assert gr.items[2].quality == 1




if __name__ == '__main__':
    unittest.main()
