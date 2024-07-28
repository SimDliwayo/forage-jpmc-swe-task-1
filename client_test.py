import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(price, (bid_price + ask_price) / 2)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(price, (bid_price + ask_price) / 2)


  """ ------------ Add more unit tests ------------ """

  def test_getDataPoint_correctValues(self):
        quote = {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(stock, 'ABC')
        self.assertEqual(bid_price, 120.48)
        self.assertEqual(ask_price, 121.2)
        self.assertEqual(price, 120.84)


  def test_getDataPoint_floatPrices(self):
        quote = {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertIsInstance(bid_price, float)
        self.assertIsInstance(ask_price, float)
        self.assertIsInstance(price, float)

  def test_getDataPoint_missingData(self):
        quote = {'top_ask': None, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': None, 'id': '0.109974697771', 'stock': 'ABC'}
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(stock, 'ABC')
        self.assertIsNone(bid_price)
        self.assertIsNone(ask_price)
        self.assertIsNone(price)


if __name__ == '__main__':
    unittest.main()
