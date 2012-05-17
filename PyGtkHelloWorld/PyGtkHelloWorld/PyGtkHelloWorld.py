'''
Created on May 16, 2012

@author: dsanderson
'''

import pygtk
pygtk.require('2.0')
import gtk

class PyGtkHelloWorld:
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.show()
   
    def main(self):
        gtk.main()
   
print __name__
if __name__ == "__main__":
    pygtkHelloWorld = PyGtkHelloWorld()
    pygtkHelloWorld.main()
