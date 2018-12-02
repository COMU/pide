import gi, sys
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

#def whatis(obj):
#    props = dir(obj)
#    print(type(obj))
#    print("\t"+"\t\n\t".join(props))

whatis = lambda obj: print(type(obj), "\n\t"+"\n\t".join(dir(obj)))

class aClassThatHandleGtkSignals:

    window = Gtk.Window()
    def onQuit(self, *a, **kv):
        print("exit")
        sys.exit(0)
    def newProject(self, *a, **kv):
        print("CLICKED")
        
        aClassThatHandleGtkSignals.window.show_all()
        Gtk.main()
    def saveProject(self, *a, **kv):
    	print("metoda girdim")
    	if(aClassThatHandleGtkSignals.window!=0):
    		print("ife girdin")
    		import gtkWindow as gw
    		self.dialog = Gtk.FileChooserDialog("please", None, Gtk.FileChooserAction.SAVE,(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.ACCEPT))
    		aClassThatHandleGtkSignals.add_filters(None,self.dialog)
    		response = self.dialog.run()
    		Gtk.FileChooser.set_do_overwrite_confirmation(self.dialog, True)
    		if response == Gtk.ResponseType.ACCEPT:
    			print("Open clicked")
    			print("File selected: " + self.dialog.get_filename())
    		elif response == Gtk.ResponseType.CANCEL:
    			print("Cancel clicked")
    		gw.glade_create_files(self.dialog.get_filename(),self.dialog.get_filename().split('/')[-1])
    		self.dialog.destroy()
    def add_filters(self, dialog):
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

    def labelEkle(self, *a, **kv):
        print("Label Adding Start ! ")
        self.label = Gtk.Label()
        self.label.set_label("Label Eklendi !")
        aClassThatHandleGtkSignals.window.add(self.label)
        aClassThatHandleGtkSignals.window.show_all()
    def butonEkle(self, *a, **kv):
        print("Buton Adding Start ! ")
        self.buton = Gtk.Button(label = "Click Me !")
        self.buton.connect("clicked",MainWindow.button_clicked)
        aClassThatHandleGtkSignals.window.add(self.buton)
        aClassThatHandleGtkSignals.window.show_all()
    def gridEkle(self, *a, **kv):
    	print("Grid ekleniyor")
    	self.grid = Gtk.Grid()
    	aClassThatHandleGtkSignals.window.add(self.grid)
    	aClassThatHandleGtkSignals.window.show_all()
        
class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title = "Button Clicker")

        self.button = Gtk.Button(label = "click here")
        self.button.connect("clicked",self.button_clicked)
        self.add(self.button)

    def button_clicked(self, widget):
        print("GameTime")

abuilder = Gtk.Builder()
abuilder.add_from_file("forms1.glade")
abuilder.connect_signals(aClassThatHandleGtkSignals)
ourForm1 = abuilder.get_object("form1")
ourForm1.show_all()
Gtk.main()
