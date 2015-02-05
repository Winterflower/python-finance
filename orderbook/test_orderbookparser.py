__author__ = 'winterflower'

import unittest
import orderbookparser as obp

class testOrderBookFileParser(unittest.TestCase):
    def setUp(self):
        self.samplefile=open("sample.ob",'r')
    def testReadsDataIntoList(self):
        datalist=obp.parse_file(self.samplefile)
        for key in datalist.get_table().keys():
            self.assertEquals(len(datalist.get_table()[key]),2)
    def testConvertTime(self):
        time=obp.convert_time(3600)
        self.assertEquals("01:00:00")




