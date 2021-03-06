from collections import namedtuple
from Fetchers.DataModel import *

Price = namedtuple("Price", ["open","close","high","low","volume"])

class IFetcher():
    def __init__(self,configPath):
        self.configPath = configPath

    def processConfig():
        # TODO - Possibly move all the initialization into some
        # factory-lile class
         raise NotImplementedError("Base data fetcher class\
                                    cannot process config file")
