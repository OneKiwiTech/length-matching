import pcbnew

class NetData:
    def __init__(self, start_pad, end_pad, board, status):
        self.start_pad = start_pad
        self.end_pad = end_pad
        self.status = status
        self.status.LabelText = 'init'
        net_name = start_pad.GetNetname()
        self.status.LabelText = 'init1'
        net_code = board.GetNetcodeFromNetname(net_name)
        self.status.LabelText = 'ini2'
        self.tracks = board.TracksInNet(net_code)
        self.status.LabelText = 'end init'
        
    def GetLenght(self):
        self.status.LabelText = 'a1'
        current_point = self.start_pad.GetPosition()
        # set default PAD_ATTRIB_PTH
        current_layer = -1
        # if PAD_ATTRIB_SMD
        if self.start_pad.GetAttribute() == PAD_ATTRIB_SMD:
            if self.start_pad.GetParent().IsFlipped():
                # F_Cu = 31
                current_layer = pcbnew.B_Cu
            else:
                # F_Cu = 1
                current_layer = pcbnew.F_Cu

        end_point = self.end_pad.GetPosition()
        end_layer = -1
        if self.end_pad.GetAttribute() == PAD_ATTRIB_SMD:
            if self.end_pad.GetParent().IsFlipped():
                end_layer = pcbnew.B_Cu
            else:
                end_layer = pcbnew.F_Cu
        
        total = []

        isLoop = True
        self.status.LabelText = 'start loop'
        index = 0
        while len(self.tracks) > 0 and isLoop == True:
            self.status.LabelText = str(index)
            index += 1
            for track in self.tracks:
                if track.GetClass() == "VIA":
                    if current_point == track.GetPosition():
                        current_layer = -1
                        total.append(track)
                        self.tracks.remove(track)
                else:
                    if current_point == track.GetStart() and current_point == track.GetLayer():
                        current_point = track.GetEnd()
                        total.append(track)
                        self.tracks.remove(track)
                    if current_point == track.GetStart() and current_layer == -1:
                        current_layer = track.GetLayer()
                        total.append(track)
                        self.tracks.remove(track)
                    if current_point == track.GetEnd() and current_point == track.GetLayer():
                        current_point = track.GetStart()
                        total.append(track)
                        self.tracks.remove(track)
                    if current_point == track.GetEnd() and current_layer == -1:
                        current_layer = track.GetLayer()
                        total.append(track)
                        self.tracks.remove(track)
                if current_point == end_point and current_point == track.GetLayer():
                    isLoop = False
                    self.status.LabelText = 'end'
                if current_point == end_point and current_layer == -1:
                    isLoop = False
                    self.status.LabelText = 'end'

        sum = 0
        self.status.LabelText = 'sum'
        for t in total:
            if track.GetClass() != "VIA":
                sum += track.GetLength()
        return sum