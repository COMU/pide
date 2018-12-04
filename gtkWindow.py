import xml.etree.ElementTree as ET
import gi, sys
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
def glade_create_files(save_name,project_name): #glade format requires code
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
	send = ET.tostring(a,encoding='utf8',method='xml').decode() #send variable for saveFile
	ET.dump(a)
	yn = open(save_name+".glade", "w") # new file create
	yn.write(send) #xml format file writing
	yn.close()
def addLabel(project_name): #addLabel buton is clicked ,this function add xml file,
	yn = open(project_name+".glade")
	ynoku = yn.read()
	root = ET.fromstring(ynoku)
	print(root.tag)
	temp=0
	for child in root.findall('object'):
		for i in child.attrib.keys():
			if i=="id":
				if child.attrib["id"]==project_name:
					new_child = ET.Element("child")
					new_label = ET.SubElement(new_child,"object")
					new_label.set("class","GtkLabel")
					property_1=ET.SubElement(new_label,"property")
					property_1.set("name","visible")
					property_1.text="True"
					property_2=ET.SubElement(new_label,"property")
					property_2.set("name","can_focus")
					property_2.text="False"
					property_3=ET.SubElement(new_label,"property")
					property_3.set("name","label")
					property_3.set("translatable","yes")
					property_3.text="label"
					child.append(new_child)
	yn1= open(project_name+".glade","w")	
	yn1.write(ET.tostring(root,encoding='utf8',method='xml').decode())