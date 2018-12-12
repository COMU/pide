import xml.etree.ElementTree as ET
import gi, sys
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

def glade_create_files(project_name): #glade format requires code
	interface= ET.Element('interface')
	requires=ET.SubElement(interface,'requires')
	requires.set('lib', 'gtk+')
	requires.set('version', '3.20')
	obj= ET.SubElement(interface,'object')
	obj.set('class','GtkWindow')
	obj.set('id',project_name)
	prop= ET.SubElement(obj,'property')
	prop.set('name', 'can_focus')
	prop.text="False"
	child= ET.SubElement(obj,'child')
	ET.SubElement(child,'placeholder')
	ET.dump(interface)
	
	return interface
