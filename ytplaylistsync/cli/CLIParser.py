import argparse
import string

class CLIParser:

    def __init__(self):
        self.__description = "Youtube to GDrive playlist syncronizer"
        self.__parser = argparse.ArgumentParser(description=self.__description)

        self.__parser.add_argument('-p', '--playlist-url', type=string, required=True)
        
    def parse(self) -> argparse.Namespace:
        return self.__parser.parse_args()