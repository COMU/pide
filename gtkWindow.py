import xml.etree.ElementTree as ET
import gi, sys
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
def glade_create_files(save_name,project_name):
	a= ET.Element('interface')
	b=ET.SubElement(a,'requires')
	b.set('lib', 'gtk+')
	b.set('version', '3.20')
	c= ET.SubElement(a,'object')
	c.set('class','GtkWindow')
	c.set('id',project_name)
	d= ET.SubElement(c,'property')
	d.set('name', 'can_focus')
	d.text="False"
	e= ET.SubElement(c,'child')
	ET.SubElement(e,'placeholder')
	send = ET.tostring(a,encoding='utf8',method='xml').decode()
	ET.dump(a)
	yn = open(save_name+".glade", "w")
	yn.write(send)