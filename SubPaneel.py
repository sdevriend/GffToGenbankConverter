"""

Een standaard subpaneel.
"""

import wx

class SubPaneel(wx.Panel):
    """
    De class maakt een subpaneeltje aan die vanuit andere classes
    gebruikt kan worden.
    """
    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize,
                 style=wx.BORDER_DEFAULT):
        super(SubPaneel, self).__init__(parent, id, size=size, style=style)
