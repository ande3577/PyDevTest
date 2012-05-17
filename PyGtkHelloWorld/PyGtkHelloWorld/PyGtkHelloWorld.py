'''
Created on May 16, 2012

@author: dsanderson
'''

import pygtk
pygtk.require('2.0')
import gtk

class PyGtkHelloWorld:
    
    def hello(self, widget, data=None):
        print "Hello World"
    
    def delete_event(self, widget, event, data=None):
        print "Delete event occurred"
        return False
    
    def destroy(self, widget, data=None):
        gtk.main_quit()
    
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.show()
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)
        self.button = gtk.Button("Hello World")
        self.button.connect("clicked", self.hello, None)
        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
        self.window.add(self.button)
        self.button.show()
        self.window.show()
        
   
    def main(self):
        gtk.main()
   
print __name__
if __name__ == "__main__":
    pygtkHelloWorld = PyGtkHelloWorld()
    pygtkHelloWorld.main()
