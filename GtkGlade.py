import gi, sys
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import gtkWindow as gw

whatis = lambda obj: print(type(obj), "\n\t"+"\n\t".join(dir(obj))) # for obj attributes


class aClassThatHandleGtkSignals:

    window = Gtk.Window() # application window
    def onQuit(self, *a, **kv):
        print("exit")
        sys.exit(0)
    def newProject(self, *a, **kv): # newProject button on clicked
        aClassThatHandleGtkSignals.window.show_all()
        Gtk.main()
    def saveProject(self, *a, **kv): #saveProject button on clicked
    	if(aClassThatHandleGtkSignals.window.get_name()=="GtkWindow"): #this means if the projectName is not saved
    		# FileChooserDialog settings for SAVE
    		self.dialog = Gtk.FileChooserDialog("please", None, Gtk.FileChooserAction.SAVE,(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.ACCEPT))
    		aClassThatHandleGtkSignals.add_filters(None,self.dialog)
    		response = self.dialog.run() # Show FileChooserDialog
    		Gtk.FileChooser.set_do_overwrite_confirmation(self.dialog, True)
    		if response == Gtk.ResponseType.ACCEPT:
    			print("Open clicked")
    			print("File selected: " + self.dialog.get_filename())
    		elif response == Gtk.ResponseType.CANCEL:
    			print("Cancel clicked")
    		save_name=self.dialog.get_filename().split('/')[-1] # save_name is the name of the saved project
    		gw.glade_create_files(self.dialog.get_filename(),save_name) #glade_create_files function on gtkWindow.py
    		aClassThatHandleGtkSignals.window.set_name(save_name) # application window name
    		aClassThatHandleGtkSignals.window.set_title(save_name) # application window title name
    		self.dialog.destroy() # FileChooserDialog closing
    def add_filters(self, dialog): # FileChooserDialogs adding filter function
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def labelEkle(self, *a, **kv): # labelEkle button is clicked
        print("Label Adding Start ! ")
        self.label = Gtk.Label()
        self.label.set_label("label")
        aClassThatHandleGtkSignals.window.add(self.label) # add label to application window
        aClassThatHandleGtkSignals.window.show_all()
        if aClassThatHandleGtkSignals.window.get_name()!="GtkWindow": # if Project was saved
        	gw.addLabel(aClassThatHandleGtkSignals.window.get_name()) # addLabel function on gtkWindow.py ,this function saves in xml format,
        

    def butonEkle(self, *a, **kv): # butonEkle button is clicked #NOT COMPLETED YET
        print("Buton Adding Start ! ")
        self.buton = Gtk.Button(label = "Click Me !")
        self.buton.connect("clicked",MainWindow.button_clicked)
        aClassThatHandleGtkSignals.window.add(self.buton)
        aClassThatHandleGtkSignals.window.show_all()
    def gridEkle(self, *a, **kv): #NOT COMPLETED YET
    	print("Grid ekleniyor")
    	self.grid = Gtk.Grid()
    	aClassThatHandleGtkSignals.window.add(self.grid)
    	aClassThatHandleGtkSignals.window.show_all()
        
class MainWindow(Gtk.Window): #TEST

    def __init__(self):
        Gtk.Window.__init__(self, title = "Button Clicker")

        self.button = Gtk.Button(label = "click here")
        self.button.connect("clicked",self.button_clicked)
        self.add(self.button)

    def button_clicked(self, widget):
        print("GameTime")

#Builder for Gtk and Glade relationship
abuilder = Gtk.Builder()
abuilder.add_from_file("forms1.glade")
abuilder.connect_signals(aClassThatHandleGtkSignals) #Formda gerceklesen olaylar
ourForm1 = abuilder.get_object("form1")
ourForm1.show_all()
Gtk.main()
