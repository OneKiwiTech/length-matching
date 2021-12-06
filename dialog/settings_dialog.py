"""Subclass of settings_dialog, which is generated by wxFormBuilder."""
import os
import re

import wx

from . import dialog_base


def pop_error(msg):
    wx.MessageBox(msg, 'Error', wx.OK | wx.ICON_ERROR)


class SettingsDialog(dialog_base.SettingsDialogBase):
    def __init__(self, board):
        dialog_base.SettingsDialogBase.__init__(self, None)
        self.panel = SettingsDialogPanel(self, board)
        best_size = self.panel.BestSize
        # hack for some gtk themes that incorrectly calculate best size
        best_size.IncBy(dx=0, dy=30)
        self.SetClientSize(best_size)
        self.SetTitle('Simple Plugin v1.0')

    # hack for new wxFormBuilder generating code incompatible with old wxPython
    # noinspection PyMethodOverriding
    def SetSizeHints(self, sz1, sz2):
        try:
            # wxPython 3
            self.SetSizeHintsSz(sz1, sz2)
        except TypeError:
            # wxPython 4
            super(SettingsDialog, self).SetSizeHints(sz1, sz2)

    # def set_extra_data_path(self, extra_data_file):
    #     self.panel.extra.netlistFilePicker.Path = extra_data_file
    #     self.panel.extra.OnNetlistFileChanged(None)


# Implementing settings_dialog
class SettingsDialogPanel(dialog_base.SettingsDialogPanel):
    def __init__(self, parent, board):
        #self.config_save_func = config_save_func
        dialog_base.SettingsDialogPanel.__init__(self, parent)
        self.general = GeneralSettingsPanel(self.notebook, board)
        self.notebook.AddPage(self.general, "General")

    def OnExit(self, event):
        self.GetParent().EndModal(wx.ID_CANCEL)

    def OnSaveSettings(self, event):
        self.GetParent().EndModal(wx.ID_OK)


# Implementing GeneralSettingsPanelBase
class GeneralSettingsPanel(dialog_base.GeneralSettingsPanelBase):

    def __init__(self, parent, board):
        dialog_base.GeneralSettingsPanelBase.__init__(self, parent)
        #self.file_name_format_hint = file_name_format_hint
        bds = board.GetDesignSettings()
        # type wxString
        netclasses = [str(k) for k, v in bds.GetNetClasses().NetClasses().items()]

        for s in netclasses:
            self.choiceClass.Append(s)

        for net in bds.GetNetClasses().Find(netclasses[0]).NetNames():
            self.listboxNet.Append(str(net))
        

        #txt = str(bds.GetNetClasses().GetCount())
        #self.labelStatus.LabelText = keys[0]
    def OnClassNetSelected(self, event):
        #self.comboClass.GetString(event.GetSelection())
        #bds = self.board.GetDesignSettings()
        # type wxString
        #netclasses = [str(k) for k, v in bds.GetNetClasses().NetClasses().items()]
        index = event.GetSelection()
        self.listboxNet.Clear()
        #for net in bds.GetNetClasses().Find(netclasses[index]).NetNames():
            #self.listboxNet.Append(str(net))
        self.labelStatus.LabelText = str(event.GetSelection())

