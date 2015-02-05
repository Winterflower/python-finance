__author__ = 'winterflower'

import orderbook as ob

def parse_file(fileobject):
    """
    Parses a file object and returns an OrderBookTable corresponding to the fileobject
    :param fileobject:
    :return orderbooktable:
    """
    orderbook=ob.OrderBookTable()
    for line in fileobject:
        if line[0]!='#':
            #this style of coding is very bad and contains a lot of duplication
            #TODO: figure out a way more elegant way of doing this
            line_elements=line.split(',')
            orderbook.type.append(line_elements[0])
            orderbook.time.append(line_elements[1])
            orderbook.ID.append(line_elements[2])
            orderbook.price.append(line_elements[3])
            orderbook.size.append(line_elements[4])
            orderbook.bidask.append(line_elements[5])
            orderbook.status.append(line_elements[6])
    return orderbook


def convert_time(seconds):
    """
    :param seconds:
    :return time after midnight:
    """
    minutes=seconds//60
    seconds_remainder=seconds%60

    hours=minutes//60
    minutes_remainder=minutes%60


    time_after_midnight=''
    if hours<10:
        time_after_midnight=time_after_midnight+'0'+str(hours)+':'
    if minutes_remainder<10:
        time_after_midnight=time_after_midnight+'0'+str(minutes_remainder)+':'
    if seconds_remainder<10:
        time_after_midnight=time_after_midnight+'0'+str(seconds_remainder)
    return time_after_midnight
