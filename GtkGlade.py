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
# the builder got our gui describe in our file
abuilder.connect_signals(aClassThatHandleGtkSignals)
ourForm1 = abuilder.get_object("form1")
ourForm1.show_all()
Gtk.main()