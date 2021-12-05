import wx
import wx.xrc

###########################################################################
## Class SettingsDialogBase
###########################################################################

class SettingsDialogBase(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__ (self, parent, id = wx.ID_ANY, 
          title = u"Simple Plugin", pos = wx.DefaultPosition, 
          size = wx.Size(463, 497), 
          style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP|wx.BORDER_DEFAULT)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)


        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
## Class SettingsDialogPanel
###########################################################################

class SettingsDialogPanel (wx.Panel):

    def __init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(400,300), style = wx.TAB_TRAVERSAL, name = wx.EmptyString):
        wx.Panel.__init__ (self, parent, id = id, pos = pos, size = size, style = style, name = name)

        bSizer20 = wx.BoxSizer(wx.VERTICAL)

        self.notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_TOP|wx.BORDER_DEFAULT)

        bSizer20.Add(self.notebook, 1, wx.EXPAND |wx.ALL, 5)

        bSizer39 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button41 = wx.Button(self, wx.ID_ANY, u"Save Settings", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_DEFAULT)
        bSizer39.Add(self.m_button41, 0, wx.ALL, 5 )

        self.m_button43 = wx.Button(self, wx.ID_CANCEL, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_DEFAULT)
        bSizer39.Add(self.m_button43, 0, wx.ALL, 5)


        bSizer20.Add(bSizer39, 0, wx.ALIGN_CENTER, 5)


        self.SetSizer(bSizer20)
        self.Layout()

        # Connect Events
        self.m_button41.Bind(wx.EVT_BUTTON, self.OnSaveSettings)
        self.m_button43.Bind(wx.EVT_BUTTON, self.OnExit)

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnSaveSettings(self, event):
        event.Skip()

    def OnExit(self, event):
        event.Skip()


###########################################################################
## Class GeneralSettingsPanelBase
###########################################################################

class GeneralSettingsPanelBase ( wx.Panel ):

    def __init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString):
        wx.Panel.__init__ (self, parent, id = id, pos = pos, size = size, style = style, name = name)

        sizerMain = wx.BoxSizer(wx.VERTICAL)
        sizerGroup = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"label"), wx.VERTICAL)
        sizerBox = wx.BoxSizer(wx.VERTICAL)
        sizerClass = wx.BoxSizer(wx.HORIZONTAL)
        self.labelClass = wx.StaticText(sizerGroup.GetStaticBox(), wx.ID_ANY, u"Net Class", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelClass.Wrap(-1)

        sizerClass.Add(self.labelClass, 0, wx.ALL, 5)

        comboClassChoices = []
        self.comboClass = wx.ComboBox(sizerGroup.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, comboClassChoices, 0)
        sizerClass.Add(self.comboClass, 0, wx.ALL, 5)


        sizerBox.Add(sizerClass, 0, wx.EXPAND, 5)

        sizerNet = wx.BoxSizer(wx.HORIZONTAL)

        self.labelNet = wx.StaticText(sizerGroup.GetStaticBox(), wx.ID_ANY, u"Net Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelNet.Wrap(-1)

        sizerNet.Add(self.labelNet, 0, wx.ALL, 5)

        listboxNetChoices = []
        self.listboxNet = wx.ListBox(sizerGroup.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listboxNetChoices, 0)
        sizerNet.Add(self.listboxNet, 0, wx.ALL, 5)


        sizerBox.Add(sizerNet, 0, wx.EXPAND, 5)

        sizerPad = wx.BoxSizer(wx.HORIZONTAL)

        self.labelFromPad = wx.StaticText(sizerGroup.GetStaticBox(), wx.ID_ANY, u"From Pad", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelFromPad.Wrap(-1)

        sizerPad.Add(self.labelFromPad, 0, wx.ALL, 5)

        comboFromPadChoices = []
        self.comboFromPad = wx.ComboBox(sizerGroup.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, comboFromPadChoices, 0)
        sizerPad.Add(self.comboFromPad, 0, wx.ALL, 5)

        self.labelToPad = wx.StaticText(sizerGroup.GetStaticBox(), wx.ID_ANY, u"To Pad", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelToPad.Wrap(-1)

        sizerPad.Add(self.labelToPad, 0, wx.ALL, 5)

        comboToPadChoices = []
        self.comboToPad = wx.ComboBox(sizerGroup.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, comboToPadChoices, 0)
        sizerPad.Add(self.comboToPad, 0, wx.ALL, 5)


        sizerBox.Add(sizerPad, 0, wx.EXPAND, 5)

        self.labelStatus = wx.StaticText(sizerGroup.GetStaticBox(), wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelStatus.Wrap(-1)

        sizerBox.Add(self.labelStatus, 0, wx.ALL, 5)


        sizerGroup.Add(sizerBox, 1, wx.EXPAND, 5)


        sizerMain.Add(sizerGroup, 1, wx.EXPAND, 5)
# -------------------------------------------------------------

        self.SetSizer(sizerMain)
        self.Layout()
        sizerMain.Fit(self)

        # Connect Events
        #self.buttonShow.Bind(wx.EVT_BUTTON, self.OnShowClick)
        

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    #def OnSize( self, event ):
        #event.Skip()

    def OnShowClick(self, event):
        event.Skip()
