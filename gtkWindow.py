import xml.etree.ElementTree as ET
import gi, sys
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import os
def save_temp_file(save_name, project_name, tempTree): #new project save
	for child in tempTree.findall('object'):
		for i in child.attrib.keys():
			if i =="id":
				if child.attrib["id"] == "newProject":
					child.attrib["id"] = project_name

	send = ET.tostring(tempTree, encoding='utf8', method='xml').decode() #send variable for saveFile
	yn = open(save_name+".glade", "w") # new file create
	yn.write(send) #xml format file writing
	yn.close()
def update_file(project_name, tempTree): # update project
	os.system('cp '+project_name+ ".glade "+project_name+".glade.temp")
	try:
		send = ET.tostring(tempTree, encoding='utf8', method='xml').decode()
		updatefile = open(project_name+".glade","w")
		updatefile.write(send)
		updatefile.close()
		os.system('rm '+project_name+".glade.temp")
	except Exception as e:
		os.rename(project_name+".temp",project_name+".glade")
	else:
		pass
	finally:
		pass
def addLabel(lastClicked,tempTree): #addLabel buton is clicked ,this function add xml file
	for child in tempTree.findall('object'):
		for i in child.attrib.keys():
			if i=="id":
				if child.attrib["id"]==lastClicked:
					new_child = ET.SubElement(child,"child")
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

def addGrid(lastClicked, tempTree):  # add grid to temp tree file 
	for child in tempTree.findall('object'):
		for element in child.attrib.keys():
			if element == "id":
				if child.attrib["id"] == lastClicked:
					lastClickedChild = ET.SubElement(child,"child")
					new_grid = ET.SubElement(lastClickedChild, "object")
					new_grid.set("class","GtkGrid")
					new_grid.set("id","grid1")
					property_1 = ET.SubElement(new_grid, "property")
					property_1.set("name","visible")
					property_1.text = "True"
					property_2 = ET.SubElement(new_grid, "property")
					property_2.set("name","can_focus")
					property_2.text = "False"
					property_3 = ET.SubElement(new_grid, "property")
					property_3.set("name","row-_spacing")
					property_3.text = "1"
					property_4 = ET.SubElement(new_grid, "property")
					property_4.set("name","column_spacing")
					property_4.text = "1"
					property_5 = ET.SubElement(new_grid, "property")
					property_5.set("name","row_homogeneous")
					property_5.text = "True"
					property_6 = ET.SubElement(new_grid, "property")
					property_6.set("name","column_homogeneous")
					property_6.text = "True"
					

					for i in range(3):
						for j in range(3):
							gridChild = ET.SubElement(new_grid,"child")
							new_img = ET.SubElement(gridChild, "object")
							new_img.set("class","GtkImage")
							new_img.set("id","im"+str(i)+str(j))
							prop1 = ET.SubElement(new_img, "property")
							prop1.set("name","visible")
							prop1.text = "True"
							prop2 = ET.SubElement(new_img, "property")
							prop2.set("name","can_focus")
							prop2.text = "False"
							prop3 = ET.SubElement(new_img, "property")
							prop3.set("name","hexpand")
							prop3.text = "True"
							prop4 = ET.SubElement(new_img, "property")
							prop4.set("name","vexpand")
							prop4.text = "True"
							prop5 = ET.SubElement(new_img, "property")
							prop5.set("name","pixbuf")
							prop5.text = "emptygrid.png"
							pack_img = ET.SubElement(gridChild, "packing")
							packprop1 = ET.SubElement(pack_img, "property")
							packprop1.set("name","left_attach")
							packprop1.text = str(j)
							packprop2 = ET.SubElement(pack_img, "property")
							packprop2.set("name", "top_attach")
							packprop2.text = str(i)


