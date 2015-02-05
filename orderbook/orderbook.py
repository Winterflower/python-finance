__author__ = 'winterflower'

"""
Main class for the orderbook project
"""

class OrderBookTable:
    """
    Data structure for holding orderbook data
    """
    def __init__(self):
        self.ID=[]
        self.type=[]
        self.bidask=[]
        self.time=[]
        self.size=[]
        self.status=[]
        self.price=[]
    def get_table(self):
        """
        :return:dict representation of the orderbook data
        """
        orderbook_table={'type':self.type,
                         'ID': self.ID,
                         'bidask':self.bidask,
                         'time':self.time,
                          'size':self.size,
                         'status':self.status,
                         'price':self.price}
        return orderbook_table