'''
Created on May 16, 2012

@author: dsanderson
'''

import pygtk
pygtk.require('2.0')
import gtk

class PyGladeTest:
    '''
    classdocs
    '''

    def delete_event(self, widget, event, Data=None):
        print "Delete occurred"
        gtk.main_quit()
        
    def okClicked(self, widget, Data=None):
        print "Ok pressed"
        return False
    
    def cancelClicked(self, widget, Data=None):
        print "Cancel pressed"
        return False
    
    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        '''
        Constructor
        '''
        builder = gtk.Builder()
        builder.add_from_file("PyGlade.glade")
        self.window = builder.get_object("window")
        self.okButton = builder.get_object("okButton")
        self.cancelButton = builder.get_object("cancelButton")
        
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        
        self.okButton.connect("clicked", self.okClicked)
        self.okButton.connect_object("clicked", gtk.Widget.destroy, self.window)
        
        self.cancelButton.connect("clicked", self.cancelClicked)
        self.cancelButton.connect_object("clicked", gtk.Widget.destroy, self.window)
        
        self.window.show()
        
    def main(self):
        gtk.main();
        
        
print __name__
if __name__ == "__main__":
    pyGladeTest = PyGladeTest()
    pyGladeTest.main()
