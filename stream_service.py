from datetime import datetime
import logging

# slave for all streams
class Stream:
    def __init__(self, name):
        self.name = name + '.log'
        logging.basicConfig(filename = self.name, filemode = 'a', level=logging.INFO, format='%(acetime)s - %(message)s')

    def assign_topic(self, topic_name):
        pass

    def assign_producer(self, producer):
        pass

    def stream_logic(self , payload):
        with open(self.name , 'a') as log_file:
            log_file.write(f"{datetime.now()} - {payload}\n")
        


# master for all streams

"""
Stream service will be 
 - used to create stream using create_stream
 - keep info of all streams using stream_list
 - 
 
 Function
 will create a new fodler. 
 each stream will have a new folder
 it will have topics and then the logs will be save in it

 the metadata of streams will be stroed in a separate json 
 stream service will uyse this json
"""

class StreamService:
    def __init__(self, service_service_name):
        self.service_service_name = service_service_name
        self.stream_list = []


    def create_stream(self, name, topic):
        self.stream = Stream(name)
        self.stream_list.append(self.stream)

    def assign_to_topic(self):
        pass

    def insert_data(self):
        pass

    def stream_storage(self):
        pass





