# sudo apt install wxglade for gui builder
# https://wiki.wxpython.org/AnotherTutorial
import wx
import os
import pcbnew

class PanelDisplay(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        
        groupClass = wx.StaticBoxSizer(wx.StaticBox( self, wx.ID_ANY, "Net Classes"), wx.VERTICAL)
        groupNet = wx.StaticBoxSizer(wx.StaticBox( self, wx.ID_ANY, "Nets"), wx.VERTICAL)

        comboClassChoices = []
        comboClass = wx.ComboBox(self, choices=comboClassChoices, value="")
        groupClass.Add(comboClass, 0, wx.ALL|wx.EXPAND, 4)

        buttonUpdate = wx.Button(self, label="Update")
        groupNet.Add(buttonUpdate, 0, wx.ALL|wx.EXPAND, 4)

        labelDimensions = wx.StaticText(self, label = "All dimensions are in millimeters (mm). L = L0 + L1 + L2")
        groupNet.Add(labelDimensions, 0, wx.ALL|wx.EXPAND, 8)

        tableNet = wx.grid.Grid(self)
        tableNet.CreateGrid(1, 8)
        tableNet.EnableEditing(False)
        #tableNet.EnableGridLines( True )
        #tableNet.EnableDragGridSize( False )
        #tableNet.SetMargins( 0, 0 )

        # Columns
        #tableNet.AutoSizeColumns()
        tableNet.EnableDragColMove( False )
        tableNet.EnableDragColSize( True )
        tableNet.SetColLabelValue(0, u"Name")
        tableNet.SetColLabelValue(1, u"Total Length (L)")
        tableNet.SetColLabelValue(2, u"Track Length (L2)")
        tableNet.SetColLabelValue(3, u"Via Length (L1)")
        tableNet.SetColLabelValue(4, u"Length Inside (L0)")
        tableNet.SetColLabelValue(5, u"Via Count")
        tableNet.SetColLabelValue(6, u"From Pad")
        tableNet.SetColLabelValue(7, u"To Pad")
        tableNet.SetColSize(0, 160)
        tableNet.SetColSize(1, 160)
        tableNet.SetColSize(2, 160)
        tableNet.SetColSize(3, 160)
        tableNet.SetColSize(4, 160)
        tableNet.SetColSize(5, 160)
        tableNet.SetColSize(6, 160)
        tableNet.SetColSize(7, 160)
        tableNet.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
        groupNet.Add(tableNet, 0, wx.ALL|wx.EXPAND, 4)

        boxDisplay = wx.BoxSizer(wx.VERTICAL)
        boxDisplay.Add(groupClass, 0, wx.ALL|wx.EXPAND, 4)
        boxDisplay.Add(groupNet, 0, wx.ALL|wx.EXPAND, 4)
		
        self.SetSizer(boxDisplay)

class PanelSettings(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        
        groupAddClass = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Add Net Class"), wx.VERTICAL)
        groupNetClass = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Net Classes"), wx.VERTICAL)
        groupNets = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Nets"), wx.VERTICAL)
        
        # 1 Add Net Class
        labelClassName = wx.StaticText(self, label = "Class Name")
        textClassName = wx.TextCtrl(self, value="")
        buttonAddClass = wx.Button(self, label="Add Class Name")
        
        boxAddClass = wx.BoxSizer(wx.HORIZONTAL)
        boxAddClass.Add(labelClassName, 1, wx.ALL, 4)
        boxAddClass.Add(textClassName, 1, wx.EXPAND |wx.ALL, 4)
        boxAddClass.Add(buttonAddClass, 1, wx.ALL, 4)
        groupAddClass.Add(boxAddClass, 1, wx.EXPAND, 4)

        # 2 Net Classes
        # 2.1
        boxClassA1 = wx.BoxSizer(wx.VERTICAL)
        boxClassA1.Add(wx.StaticText(self, label = "Add net to Class"), 0, wx.EXPAND |wx.ALL, 4)
        boxClassA1.Add(wx.StaticText(self, label = "from net class (Kicad)"), 0, wx.EXPAND |wx.ALL, 4)
        boxClassA1.Add(wx.StaticText(self, label = "Filter Net"), 0, wx.EXPAND |wx.ALL, 4)

        # 2.2
        comboToClass = wx.ComboBox(self, choices=[], value="")
        comboFromClass = wx.ComboBox(self, choices=[], value="")
        textFilter = wx.TextCtrl(self, value="")
        boxClassA2 = wx.BoxSizer(wx.VERTICAL)
        boxClassA2.Add(comboToClass, 1, wx.EXPAND |wx.ALL, 4)
        boxClassA2.Add(comboFromClass, 1, wx.EXPAND |wx.ALL, 4)
        boxClassA2.Add(textFilter, 1, wx.EXPAND |wx.ALL, 4)

        # 2.3
        buttonFilter = wx.Button(self, label="Filter")
        boxClassA3 = wx.BoxSizer(wx.VERTICAL)
        boxClassA3.Add( ( 0, 0), 1, wx.EXPAND, 4)
        boxClassA3.Add( ( 0, 0), 1, wx.EXPAND, 4)
        boxClassA3.Add( buttonFilter, 0, wx.EXPAND, 4)
        
        # 2.4
        buttonUpdate = wx.Button(self, label="Update")
        boxClassA4 = wx.BoxSizer(wx.VERTICAL)
        boxClassA4.Add( buttonUpdate, 0, wx.EXPAND, 4)
        

        boxClassA = wx.BoxSizer(wx.HORIZONTAL)
        boxClassA.Add(boxClassA1, 1, wx.EXPAND |wx.ALL, 4)
        boxClassA.Add(boxClassA2, 1, wx.EXPAND |wx.ALL, 4)
        boxClassA.Add(boxClassA3, 1, wx.EXPAND |wx.ALL, 4)
        boxClassA.Add(boxClassA4, 1, wx.EXPAND |wx.ALL, 4)
        
        # 2.3
        listFrom = wx.ListBox(self, choices=[], style = wx.LB_SINGLE)
        boxClassB1 = wx.BoxSizer(wx.VERTICAL)
        boxClassB1.Add(listFrom, 1, wx.EXPAND |wx.ALL, 4)

        #listFrom = wx.ListBox(self, choices=[], style = wx.LB_SINGLE)
        bitmaps = os.path.join(os.path.dirname(__file__), "image")
        buttonAdd = wx.BitmapButton(self)
        buttonAddAll = wx.BitmapButton(self)
        buttonRemove = wx.BitmapButton(self)
        buttonRemoveAll = wx.BitmapButton(self)
        buttonAdd.SetBitmap(wx.Bitmap(os.path.join(bitmaps, "forward.png"), wx.BITMAP_TYPE_PNG))
        buttonAddAll.SetBitmap(wx.Bitmap(os.path.join(bitmaps, "double_right.png"), wx.BITMAP_TYPE_PNG))
        buttonRemove.SetBitmap(wx.Bitmap(os.path.join(bitmaps, "back.png"), wx.BITMAP_TYPE_PNG))
        buttonRemoveAll.SetBitmap(wx.Bitmap(os.path.join(bitmaps, "double_left.png"), wx.BITMAP_TYPE_PNG))
        boxClassB2 = wx.BoxSizer(wx.VERTICAL)
        boxClassB2.Add(buttonAdd, 1, wx.EXPAND |wx.ALL, 4)
        boxClassB2.Add(buttonAddAll, 1, wx.EXPAND |wx.ALL, 4)
        boxClassB2.Add(buttonRemove, 1, wx.EXPAND |wx.ALL, 4)
        boxClassB2.Add(buttonRemoveAll, 1, wx.EXPAND |wx.ALL, 4)

        listTo = wx.ListBox(self, choices=[], style = wx.LB_SINGLE)
        boxClassB3 = wx.BoxSizer(wx.VERTICAL)
        boxClassB3.Add(listTo, 1, wx.EXPAND |wx.ALL, 4)

        boxClassB = wx.BoxSizer(wx.HORIZONTAL)
        boxClassB.Add(boxClassB1, 1, wx.EXPAND |wx.ALL, 4)
        boxClassB.Add(boxClassB2, 0, wx.EXPAND |wx.ALL, 4)
        boxClassB.Add(boxClassB3, 1, wx.EXPAND |wx.ALL, 4)

        boxClass = wx.BoxSizer(wx.VERTICAL)
        boxClass.Add(boxClassA, 1, wx.EXPAND |wx.ALL, 4)
        boxClass.Add(boxClassB, 0, wx.EXPAND |wx.ALL, 4)
        groupNetClass.Add(boxClass, 1, wx.EXPAND, 4)

        # 3 Nets
        comboNetClass = wx.ComboBox(self, choices=[], value="")
        buttonUpdateNet = wx.Button(self, label="Update")
        boxNetA = wx.BoxSizer(wx.HORIZONTAL)
        boxNetA.Add(wx.StaticText(self, label = "Net Class"), 0, wx.EXPAND |wx.ALL, 4)
        boxNetA.Add(comboNetClass, 1, wx.EXPAND |wx.ALL, 4)
        boxNetA.Add(buttonUpdateNet, 1, wx.EXPAND |wx.ALL, 4)

        boxNetB = wx.BoxSizer(wx.HORIZONTAL)
        textTarget = wx.TextCtrl(self, value="")
        textLowTolerance = wx.TextCtrl(self, value="")
        textHighTolerance = wx.TextCtrl(self, value="")
        boxNetB.Add(wx.StaticText(self, label = "Target Length"), 0, wx.EXPAND |wx.ALL, 4)
        boxNetB.Add(textTarget, 1, wx.EXPAND |wx.ALL, 4)
        boxNetB.Add(wx.StaticText(self, label = "Low Tolerance"), 0, wx.EXPAND |wx.ALL, 4)
        boxNetB.Add(textLowTolerance, 1, wx.EXPAND |wx.ALL, 4)
        boxNetB.Add(wx.StaticText(self, label = "High Tolerance"), 0, wx.EXPAND |wx.ALL, 4)
        boxNetB.Add(textHighTolerance, 1, wx.EXPAND |wx.ALL, 4)

        tableNet = wx.grid.Grid(self)
        tableNet.CreateGrid(1, 4)
        tableNet.EnableEditing(False)
        tableNet.EnableDragColMove( False )
        tableNet.EnableDragColSize( True )
        tableNet.SetColLabelValue(0, u"Name")
        tableNet.SetColLabelValue(1, u"Length Inside")
        tableNet.SetColLabelValue(2, u"From Pad")
        tableNet.SetColLabelValue(3, u"To Pad")
        tableNet.SetColSize(0, 160)
        tableNet.SetColSize(1, 160)
        tableNet.SetColSize(2, 160)
        tableNet.SetColSize(3, 160)
        tableNet.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        boxNets = wx.BoxSizer(wx.VERTICAL)
        labelDimensions = wx.StaticText(self, label = "All dimensions are in millimeters (mm)")
        boxNets.Add(boxNetA, 0, wx.ALL|wx.EXPAND, 4)
        boxNets.Add(boxNetB, 0, wx.ALL|wx.EXPAND, 4)
        boxNets.Add(labelDimensions, 0, wx.ALL|wx.EXPAND, 4)
        boxNets.Add(tableNet, 0, wx.EXPAND|wx.ALL, 4)
        groupNets.Add(boxNets, 1, wx.EXPAND, 4)

        boxSettings = wx.BoxSizer(wx.VERTICAL)
        boxSettings.Add(groupAddClass, 0, wx.EXPAND|wx.ALL, 4)
        boxSettings.Add(groupNetClass, 0, wx.EXPAND|wx.ALL, 4)
        boxSettings.Add(groupNets, 0, wx.EXPAND|wx.ALL, 4)

        self.SetSizer(boxSettings)

class LengthMatchingGui(wx.Frame):
    def __init__(self, parent, board):
        wx.Frame.__init__(self, parent, title="Length Matching", size=(1600,700))
        self.panel = wx.Panel(self)
        notebook = wx.Notebook(self.panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        labelStatus = wx.StaticText(self.panel, label = "Status")
        labelStatus.Wrap(-1)

        tabOne = PanelSettings(notebook)
        notebook.AddPage(tabOne, "Settings")

        tabTwo = PanelDisplay(notebook)
        notebook.AddPage(tabTwo, "Display")

        
        #notebook.AddPage(PanelDisplay(notebook),"Editor") 

        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(notebook, 1, wx.EXPAND|wx.ALL, 5)
        box.Add(labelStatus, 0, wx.ALL, 5 )
        self.panel.SetSizer(box)


    
def InitGUI(board):
        sg = LengthMatchingGui(None, board)
        sg.Show(True)
        return sg
