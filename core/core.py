from __future__ import absolute_import

import logging
import os
import sys
from datetime import datetime

import wx

from ..dialog import SettingsDialog


class Logger(object):

    def __init__(self, cli=False):
        self.cli = cli
        self.logger = logging.getLogger('LaserStencil')
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter(
                "%(asctime)-15s %(levelname)s %(message)s")
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def info(self, *args):
        if self.cli:
            self.logger.info(*args)

    def error(self, msg):
        if self.cli:
            self.logger.error(msg)
        else:
            wx.MessageBox(msg)

    def warn(self, msg):
        if self.cli:
            self.logger.warn(msg)
        else:
            wx.LogWarning(msg)


log = None  # type: Logger or None

# -----------------------------------------------------------------------------

def main(logger):
    # type: (EcadParser, Config, Logger) -> None
    global log
    log = logger
    


# -----------------------------------------------------------------------------

def run_with_dialog(logger):

    #config.load_from_ini()
    dlg = SettingsDialog()
    try:
        #config.netlist_initial_directory = os.path.dirname(parser.file_name)
       
        #config.transfer_to_dialog(dlg.panel)
        if dlg.ShowModal() == wx.ID_OK:
            #config.set_from_dialog(dlg.panel)
            main(logger)
    finally:
        dlg.Destroy()
