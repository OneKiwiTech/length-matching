import pcbnew
import os

from .lengthmatching_gui import InitGUI

class LengthMatching(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Length Matching"
        self.category = "A descriptive category name"
        self.description = "A description of the plugin and what it does"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'lengthmatching.png')
        self.show_toolbar_button = True

    def Run(self):
        InitGUI(pcbnew.GetBoard())