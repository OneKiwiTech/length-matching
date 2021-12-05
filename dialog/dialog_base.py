import wx
import wx.xrc

###########################################################################
## Class SettingsDialogBase
###########################################################################

class SettingsDialogBase (wx.Dialog):

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

        box1 = wx.BoxSizer(wx.VERTICAL)

        group1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Group Name" ), wx.VERTICAL)

        self.textInput = wx.TextCtrl(group1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonShow = wx.Button(group1.GetStaticBox(), wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0)
		

        self.labelStatus = wx.StaticText(group1.GetStaticBox(), wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelStatus.Wrap(-1)
        
        group1.Add(self.textInput, 1, wx.EXPAND, 5)
        group1.Add(self.buttonShow, 0, wx.ALL, 5)
        group1.Add(self.labelStatus, 0, wx.ALL, 5)

        box1.Add(group1, 0, wx.ALL|wx.EXPAND, 5)

# -------------------------------------------------------------

        self.SetSizer(box1)
        self.Layout()
        box1.Fit(self)

        # Connect Events
        self.buttonShow.Bind(wx.EVT_BUTTON, self.OnShowClick)
        

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    #def OnSize( self, event ):
        #event.Skip()

    def OnShowClick(self, event):
        event.Skip()
