# Every code related to Location page goes here
import os

class Location():
    def ShowLocation():
        Location_Files = []
        for i in os.listdir("Database"):
            if i.endswith('.xlsx'):
                Location_Files.append(i)
                
        return Location_Files