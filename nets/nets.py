import pcbnew

class NetData:
    def __init__(self, start_ref, start_pin, end_ref, end_pin, board, status):
        self.start_pad = board.FindFootprintByReference(start_ref).FindPadByNumber(start_pin)
        self.end_pad = board.FindFootprintByReference(end_ref).FindPadByNumber(end_pin)
        self.status = status
        self.status.LabelText = 'init'
        net_name = self.start_pad.GetNetname()
        self.status.LabelText = 'init1'
        net_code = board.GetNetcodeFromNetname(net_name)
        self.status.LabelText = 'ini2'
        self.tracks = board.TracksInNet(net_code)
        self.status.LabelText = 'end init'
        self.pad_start_layer = board.FindFootprintByReference(start_ref).IsFlipped()
        self.pad_end_layer = board.FindFootprintByReference(end_ref).IsFlipped()
        
    def GetLenght(self):
        self.status.LabelText = 'a1'
        current_point = self.start_pad.GetPosition()
        # set default PAD_ATTRIB_PTH
        current_layer = -1
        # if PAD_ATTRIB_SMD
        #self.status.LabelText = str(self.start_pad.GetAttribute())
        if self.start_pad.GetAttribute() == pcbnew.PAD_ATTRIB_SMD:
            self.status.LabelText = 'a11'
            if self.pad_start_layer == True:
                # F_Cu = 31
                self.status.LabelText = 'a12'
                current_layer = pcbnew.B_Cu
            else:
                # F_Cu = 1
                self.status.LabelText = 'a13'
                current_layer = pcbnew.F_Cu
        else:
            self.status.LabelText = 'hole start'

        end_point = self.end_pad.GetPosition()
        end_layer = -1
        self.status.LabelText = 'a2'
        if self.end_pad.GetAttribute() == pcbnew.PAD_ATTRIB_SMD:
            if self.pad_end_layer == True:
                end_layer = pcbnew.B_Cu
            else:
                end_layer = pcbnew.F_Cu
        else:
            self.status.LabelText = 'hole end'
        
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