
class ParserData(board):
    def __init__(self, board):
        bds = board.GetDesignSettings()
        self.count = bds.GetNetClasses().GetCount()
        
class NetClass():
    def __init__(self):
        self.name = ''
        self.nets = []