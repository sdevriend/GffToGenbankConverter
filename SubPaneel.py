"""

Een standaard subpaneel.
"""

import wx

class SubPaneel(wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize,
                 style=wx.BORDER_DEFAULT):
        super(SubPaneel, self).__init__(parent, id, size=size, style=style)
