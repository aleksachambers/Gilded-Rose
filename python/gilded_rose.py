# -*- coding: utf-8 -*-

class GildedRose(object):

    """This code has been updated with the 'raise_quality' and 'lower_quality' methods, 
    to simplify the process of adding new items to the 'update_quality' method."""

    def __init__(self, items):
        self.items = items

    # Raises the quality value of the item.
    def raise_quality(self, item):
        if item.quality <= 50:
            item.quality += 1


    # Lowers the quality value of the item. The 'loss_of_value' parameter allows items to degrade at different rates.
    def lower_quality(self, item, loss_of_value=1):
        if item.sell_in >= 0:
            item.quality -= loss_of_value
        else:
            item.quality -= 2 * loss_of_value
            
        if item.quality < 0:
                item.quality = 0


    def update_quality(self):
        for item in self.items:

            # Meet conditions for Aged Brie.
            if item.name == "Aged Brie":
                item.sell_in -= 1
                self.raise_quality(item)     


            # Meet conditions for Sulfuras, Hand of Ragnaros.
            elif item.name == "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in
                item.quality = 80


            # Meet conditions for Backstage Pass. 
            elif item.name == "Backstage passes to a TAFKAL80ETC concert": 
                item.sell_in -= 1
                
                if item.sell_in < 0:
                    item.quality = 0

                elif item.sell_in < 6:
                    self.raise_quality(item)
                    self.raise_quality(item)
                    self.raise_quality(item)

                elif item.sell_in < 11:
                    self.raise_quality(item)
                    self.raise_quality(item)

                else:
                    self.raise_quality(item)


            # Condition for Conjured items. 
            elif "Conjured" in item.name:
                item.sell_in -= 1
                self.lower_quality(item, loss_of_value=2)


            # Condition for normal items. 
            else:
                item.sell_in -= 1
                self.lower_quality(item, loss_of_value=1)


# DON'T TOUCH THIS!!
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)