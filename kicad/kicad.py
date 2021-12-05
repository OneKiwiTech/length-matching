import os
import sys
import time
import tempfile
import logging
from datetime import datetime

import pcbnew
from ..core import core
#from ..data.parser_data import ParserData

class SimplePlugin(pcbnew.ActionPlugin, object):

    def __init__(self):
        super(SimplePlugin, self).__init__()

        self.InitLogger()
        self.logger = logging.getLogger(__name__)

        self.name = "Length Matching"
        self.category = "Length Matching"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        icon_dir = os.path.dirname(os.path.dirname(__file__))
        self.icon_file_name = os.path.join(icon_dir, 'icon.png')
        self.description = "Length Matching Plugin"

    def defaults(self):
        pass

    def Run(self):
        board = pcbnew.GetBoard()
        pcb_file_name = board.GetFileName()

        logger = core.Logger()
        if not pcb_file_name:
            logger.error('Please save the board file before generating Simple Plugin.')
            return

        try:
            core.run_with_dialog(logger, board)
        except ParsingException as e:
            logger.error(str(e))

    def InitLogger(self):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)

        # Log to stderr
        handler1 = logging.StreamHandler(sys.stderr)
        handler1.setLevel(logging.DEBUG)

        log_file = os.path.join(os.path.dirname(__file__), "..", "length-matching.log")

        # and to our error file
        handler2 = logging.FileHandler(log_file)
        handler2.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s %(name)s %(lineno)d:%(message)s", datefmt="%m-%d %H:%M:%S"
        )
        handler1.setFormatter(formatter)
        handler2.setFormatter(formatter)
        root.addHandler(handler1)
        root.addHandler(handler2)

