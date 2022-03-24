from ytplaylistsync.cli.CLIParser import CLIParser


class YTPlaylistSync:

    def __init__(self):
        print("Init")

    def main():
        #parse args
        self.__args = CLIParser.parse()
        
        #do the thing

        #auth to drive
        token = Authentication.authenticate()
        
        #sync
