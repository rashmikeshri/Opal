'''
Created on 14-Nov-2015

@author: vijay
'''

'''
Created on 14-Nov-2015
@author: vijay
'''

import wx


from src.ui.view.opalview.win import MainFrame
# 
global appPath 

class Main():
    
    def __init__(self):
        pass
    def myMain(self):

        app = wx.App()
        frame = MainFrame(None )
        frame.Show()
        app.MainLoop()
if __name__ == '__main__':
    Main().myMain()
pass