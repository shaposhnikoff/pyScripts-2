#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.5 on Sun Jun 16 19:34:29 2013

import wx

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("simple-glade")
        self.SetSize((631, 386))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class MyFrame
class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        DerekFirstTitle = MyFrame(None, -1, "")
        self.SetTopWindow(DerekFirstTitle)
        DerekFirstTitle.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
