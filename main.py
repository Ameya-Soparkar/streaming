from stream_service import Stream
import random
import logging

stream_user = Stream(name = 'test')


names = ['java', 'python', 'c', 'golang', 'c++', 'rust']
version = [1,2,3,4,5,6,7]



# producer
for i in range(0,5000):
    r = random.randint(0,3)
    d = {'name': names[r], 'version':version[r]}
    stream_user.stream_logic(d)
    




"""
data --
    stream name

        -- Topic name
            -- file

"""