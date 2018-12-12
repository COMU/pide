import gi, sys
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk
import gtkWindow as gw
import tempXml as txml


whatis = lambda obj: (type(obj), "\n\t"+"\n\t".join(dir(obj))) # for obj attributes



class ListBoxRowWithData(Gtk.ListBoxRow):
	def __init__(self, data):
		super(Gtk.ListBoxRow, self).__init__()
		self.data = data
		self.add(Gtk.Label(data))


class aClassThatHandleGtkSignals:
    tempTree = ""
    lastClicked = ""
    fileAddress = ""
    window = Gtk.Window() # application window
    window.set_default_size(587,540)
    window.set_position(Gtk.WindowPosition.CENTER)
    window.set_name("newProject")
    
    def onQuit(self, *a, **kv):
        print("exit")
        sys.exit(0)
    def newProject(self, *a, **kv): # newProject button on clicked
        aClassThatHandleGtkSignals.window.show_all()
        aClassThatHandleGtkSignals.tempTree = txml.glade_create_files("newProject")
        aClassThatHandleGtkSignals.window.connect("button-press-event", aClassThatHandleGtkSignals.windowClicked)
        Gtk.main()

    def saveProject(self, *a, **kv):
    	if(aClassThatHandleGtkSignals.window.get_name()=="newProject"): #this means if the projectName is not saved
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
    		gw.save_temp_file(self.dialog.get_filename(), save_name, aClassThatHandleGtkSignals.tempTree) #glade_create_files function on gtkWindow.py
    		aClassThatHandleGtkSignals.window.set_name(save_name) # application window name
    		aClassThatHandleGtkSignals.window.set_title(save_name) # application window title name
    		aClassThatHandleGtkSignals.fileAddress = self.dialog.get_filename()
    		self.dialog.destroy()
    	else:
    		if(aClassThatHandleGtkSignals.fileAddress != ""):
    			gw.update_file(aClassThatHandleGtkSignals.fileAddress, aClassThatHandleGtkSignals.tempTree)

    	#gw.ET.dump(aClassThatHandleGtkSignals.tempTree)
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

    def windowClicked(self, *a, **kv):
        aClassThatHandleGtkSignals.lastClicked = self.get_name()
        print(aClassThatHandleGtkSignals.lastClicked)

    def labelEkle(self, *a, **kv): # labelEkle button is clicked
        print("Label Adding Start ! ")
        self.label = Gtk.Label()
        self.label.set_label("label")
        #6aralikstart
        self.label.set_has_window(True)
        self.label.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self.label.connect("button-press-event", aClassThatHandleGtkSignals.labelPropShow)
        #6aralikend
        aClassThatHandleGtkSignals.window.add(self.label) # add label to application window
        aClassThatHandleGtkSignals.window.show_all()
        gw.addLabel(aClassThatHandleGtkSignals.lastClicked,aClassThatHandleGtkSignals.tempTree) # addLabel function on gtkWindow.py ,this function saves in xml format,
    def labelPropShow(self, *a, **kv):
    	print(aClassThatHandleGtkSignals.tempTree)

    def butonEkle(self, *a, **kv): # butonEkle button is clicked #NOT COMPLETED YET
        print("Buton Adding Start ! ")
        self.buton = Gtk.Button(label = "Click Me !")
        self.buton.connect("clicked",MainWindow.button_clicked)
        aClassThatHandleGtkSignals.window.add(self.buton)
        aClassThatHandleGtkSignals.window.show_all()
    def gridEkle(self, *a, **kv): #NOT COMPLETED YET
    	self.grid = Gtk.Grid()
    	gw.addGrid(aClassThatHandleGtkSignals.lastClicked, aClassThatHandleGtkSignals.tempTree)
        
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
#ourListBox = abuilder.get_object("listBox")
ourForm1.show_all()
Gtk.main()
