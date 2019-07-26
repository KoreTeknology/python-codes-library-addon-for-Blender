bl_info = {
	"name": "Code Snippets Library",
	"author": "Uriel Deveaud",
	"version": (0, 1, 0),
	"blender": (2, 80, 0),
	"location": "Text Editor > Header, ... > Sidebar",
	"description": "Add Code Snippets Library to Developper's tools",
	"warning": "",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Development"
}


import os
import bpy

from bpy.types import (Panel, Operator, Menu, UIList, AddonPreferences)

from . import addon_updater_ops

# ##########################################################
# PATH
# ##########################################################



class DemoPreferences(bpy.types.AddonPreferences):
	bl_idname = __package__

	# addon updater preferences

	auto_check_update = bpy.props.BoolProperty(
		name="Auto-check for Update",
		description="If enabled, auto-check for updates using an interval",
		default=False,
		)
	updater_intrval_months = bpy.props.IntProperty(
		name='Months',
		description="Number of months between checking for updates",
		default=0,
		min=0
		)
	updater_intrval_days = bpy.props.IntProperty(
		name='Days',
		description="Number of days between checking for updates",
		default=7,
		min=0,
		max=31
		)
	updater_intrval_hours = bpy.props.IntProperty(
		name='Hours',
		description="Number of hours between checking for updates",
		default=0,
		min=0,
		max=23
		)
	updater_intrval_minutes = bpy.props.IntProperty(
		name='Minutes',
		description="Number of minutes between checking for updates",
		default=0,
		min=0,
		max=59
		)

	def draw(self, context):
		layout = self.layout
		# col = layout.column() # works best if a column, or even just self.layout
		mainrow = layout.row()
		col = mainrow.column()

		# updater draw function
		# could also pass in col as third arg
		addon_updater_ops.update_settings_ui(self, context)

		# Alternate draw function, which is more condensed and can be
		# placed within an existing draw function. Only contains:
		#   1) check for update/update now buttons
		#   2) toggle for auto-check (interval will be equal to what is set above)
		# addon_updater_ops.update_settings_ui_condensed(self, context, col)

		# Adding another column to help show the above condensed ui as one column
		# col = mainrow.column()
		# col.scale_y = 2
		# col.operator("wm.url_open","Open webpage ").url=addon_updater_ops.updater.website








# Manage path to snippets folders
current_dir = os.path.dirname(__file__)

basics_folder = "basics"
basics_dir = os.path.join(current_dir, basics_folder)

uidesign_folder = "uidesign"
uidesign_dir = os.path.join(current_dir, uidesign_folder)

operators_folder = "operators"
operators_dir = os.path.join(current_dir, operators_folder)

helper_folder = "helpers"
helpers_dir = os.path.join(current_dir, helper_folder)

custom_folder = "custom"
custom_dir = os.path.join(current_dir, custom_folder)


# ##########################################################
# Sub Menus
# ##########################################################

# ######################################################################################
# BASICS FOLDER

def get_subdir_basics(basics_dir):
	for f in os.listdir(basics_dir):
		if f in {'__pycache__', '.git'}:
			continue
			
		joined_basics = os.path.join(basics_dir, f)
		if os.path.isdir(joined_basics) and os.listdir(joined_basics):
			yield joined_basics


def make_menu_basics(name, path):

	def draw(self, context):
		layout = self.layout
		# print([path])
		self.path_menu(searchpaths=[path], operator="text.open", props_default={"internal": True})

	folder_name_basics = 'TEXT_MT_basics_' + name
	attributes_basics = dict(bl_idname=folder_name_basics, bl_label=name, draw=draw)
	
	return type(name, (bpy.types.Menu,), attributes_basics)

submenus_basics = []
menu_names_basics = []

for subdir_basics in get_subdir_basics(basics_dir):
	submenu_name_basics = os.path.basename(subdir_basics)
	menu_names_basics.append(submenu_name_basics)
	dynamic_class_basics = make_menu_basics(submenu_name_basics, subdir_basics)
	submenus_basics.append(dynamic_class_basics)

	
def get_submenu_name_basics():
	for k in sorted(menu_names_basics):
		yield k, 'TEXT_MT_basics_' + k



class TEXT_MT_snippets_menu_basics(bpy.types.Menu):
	bl_idname = "TEXT_MT_snippets_menu_basics"
	bl_label = "Basics"
    
	def draw(self, context):
		layout = self.layout
		layout.operator("template.donothing", text="Do Nothing", icon='PREFERENCES')
		
		layout.separator()
		# for eachh submenus_helpers
		for name, long_name in get_submenu_name_basics():
			# draw menu and replace _ and space
			self.layout.menu(long_name, text=name.replace('_', ' '), icon="FILEBROWSER")


 
 # ######################################################################################
# UIDESIGN FOLDER

def get_subdir_uidesign(uidesign_dir):
	for f in os.listdir(uidesign_dir):
		if f in {'__pycache__', '.git'}:
			continue
			
		joined_uidesign = os.path.join(uidesign_dir, f)
		if os.path.isdir(joined_uidesign) and os.listdir(joined_uidesign):
			yield joined_uidesign


def make_menu_uidesign(name, path):

	def draw(self, context):
		layout = self.layout
		# print([path])
		self.path_menu(searchpaths=[path], operator="text.open", props_default={"internal": True})

	folder_name_uidesign = 'TEXT_MT_uidesign_' + name
	attributes_uidesign = dict(bl_idname=folder_name_uidesign, bl_label=name, draw=draw)
	
	return type(name, (bpy.types.Menu,), attributes_uidesign)

submenus_uidesign = []
menu_names_uidesign = []

for subdir_uidesign in get_subdir_uidesign(uidesign_dir):
	submenu_name_uidesign = os.path.basename(subdir_uidesign)
	menu_names_uidesign.append(submenu_name_uidesign)
	dynamic_class_uidesign = make_menu_uidesign(submenu_name_uidesign, subdir_uidesign)
	submenus_uidesign.append(dynamic_class_uidesign)

	
def get_submenu_name_uidesign():
	for k in sorted(menu_names_uidesign):
		yield k, 'TEXT_MT_uidesign_' + k


 
 
class TEXT_MT_snippets_menu_uidesign(bpy.types.Menu):
	bl_idname = "TEXT_MT_snippets_menu_uidesign"
	bl_label = "UI Design"
    
	def draw(self, context):
		layout = self.layout
		layout.operator("template.donothing", text="Do Nothing", icon='PREFERENCES')
		layout.separator()
		# for eachh submenus_helpers
		for name, long_name in get_submenu_name_uidesign():
			# draw menu and replace _ and space
			self.layout.menu(long_name, text=name.replace('_', ' '), icon="FILEBROWSER")


# ######################################################################################
# OPERATORS FOLDER

def get_subdir_operators(operators_dir):
	for f in os.listdir(operators_dir):
		if f in {'__pycache__', '.git'}:
			continue
			
		joined_operators = os.path.join(operators_dir, f)
		if os.path.isdir(joined_operators) and os.listdir(joined_operators):
			yield joined_operators


def make_menu_operators(name, path):

	def draw(self, context):
		layout = self.layout
		# print([path])
		self.path_menu(searchpaths=[path], operator="text.open", props_default={"internal": True})

	folder_name_operators = 'TEXT_MT_operators_' + name
	attributes_operators = dict(bl_idname=folder_name_operators, bl_label=name, draw=draw)
	
	return type(name, (bpy.types.Menu,), attributes_operators)

submenus_operators = []
menu_names_operators = []

for subdir_operators in get_subdir_operators(operators_dir):
	submenu_name_operators = os.path.basename(subdir_operators)
	menu_names_operators.append(submenu_name_operators)
	dynamic_class_operators = make_menu_operators(submenu_name_operators, subdir_operators)
	submenus_operators.append(dynamic_class_operators)

	
def get_submenu_name_operators():
	for k in sorted(menu_names_operators):
		yield k, 'TEXT_MT_operators_' + k


class TEXT_MT_snippets_menu_operators(bpy.types.Menu):
	bl_idname = "TEXT_MT_snippets_menu_operators"
	bl_label = "Operators"
    
	def draw(self, context):
		layout = self.layout
		layout.operator("template.donothing", text="Do Nothing", icon='PREFERENCES')
		layout.separator()
		# for eachh submenus_helpers
		for name, long_name in get_submenu_name_operators():
			# draw menu and replace _ and space
			self.layout.menu(long_name, text=name.replace('_', ' '), icon="FILEBROWSER")

		
# ######################################################################################
# HELPER FOLDER

def get_subdir_helpers(helpers_dir):
	for f in os.listdir(helpers_dir):
		if f in {'__pycache__', '.git'}:
			continue
			
		joined_helpers = os.path.join(helpers_dir, f)
		if os.path.isdir(joined_helpers) and os.listdir(joined_helpers):
			yield joined_helpers


def make_menu_helpers(name, path):

	def draw(self, context):
		layout = self.layout
		# print([path])
		self.path_menu(searchpaths=[path], operator="text.open", props_default={"internal": True})

	folder_name_helpers = 'TEXT_MT_helpers_' + name
	attributes_helpers = dict(bl_idname=folder_name_helpers, bl_label=name, draw=draw)
	
	return type(name, (bpy.types.Menu,), attributes_helpers)

submenus_helpers = []
menu_names_helpers = []

for subdir_helpers in get_subdir_helpers(helpers_dir):
	submenu_name_helpers = os.path.basename(subdir_helpers)
	menu_names_helpers.append(submenu_name_helpers)
	dynamic_class_helpers = make_menu_helpers(submenu_name_helpers, subdir_helpers)
	submenus_helpers.append(dynamic_class_helpers)

	
def get_submenu_name_helpers():
	for k in sorted(menu_names_helpers):
		yield k, 'TEXT_MT_helpers_' + k


class TEXT_MT_snippets_menu_helpers(bpy.types.Menu):
	bl_idname = "TEXT_MT_snippets_menu_helpers"
	bl_label = "Helpers"
    
	def draw(self, context):
		layout = self.layout
		layout.operator("template.donothing", text="Do Nothing", icon='PREFERENCES')
		layout.separator()
		# for eachh submenus_helpers
		for name, long_name in get_submenu_name_helpers():
			# draw menu and replace _ and space
			self.layout.menu(long_name, text=name.replace('_', ' '), icon="FILEBROWSER")
			

# ######################################################################################
# CUSTOM FOLDER

def get_subdir_custom(custom_dir):
	for f in os.listdir(custom_dir):
		if f in {'__pycache__', '.git'}:
			continue
			
		joined_custom = os.path.join(custom_dir, f)
		if os.path.isdir(joined_custom) and os.listdir(joined_custom):
			yield joined_custom


def make_menu_custom(name, path):

	def draw(self, context):
		layout = self.layout
		# print([path])
		self.path_menu(searchpaths=[path], operator="text.open", props_default={"internal": True})

	folder_name_custom = 'TEXT_MT_custom_' + name
	attributes_custom = dict(bl_idname=folder_name_custom, bl_label=name, draw=draw)
	
	return type(name, (bpy.types.Menu,), attributes_custom)

submenus_custom = []
menu_names_custom = []

for subdir_custom in get_subdir_custom(custom_dir):
	submenu_name_custom = os.path.basename(subdir_custom)
	menu_names_custom.append(submenu_name_custom)
	dynamic_class_custom = make_menu_custom(submenu_name_custom, subdir_custom)
	submenus_custom.append(dynamic_class_custom)

	
def get_submenu_name_custom():
	for k in sorted(menu_names_custom):
		yield k, 'TEXT_MT_custom_' + k


class TEXT_MT_snippets_menu_custom(bpy.types.Menu):
	bl_idname = "TEXT_MT_snippets_menu_custom"
	bl_label = "Custom Snippets"
    
	def draw(self, context):
		layout = self.layout
		layout.operator("template.donothing", text="Do Nothing", icon='PREFERENCES')
		layout.separator()
		# for eachh submenus_helpers
		for name, long_name in get_submenu_name_custom():
			# draw menu and replace _ and space
			self.layout.menu(long_name, text=name.replace('_', ' '), icon="FILEBROWSER")


# ##########################################################
# MAIN MENU
# ##########################################################

# CREATE menu and ADD items
class TEXT_MT_snippets_menu(bpy.types.Menu):
	bl_idname = "TEXT_MT_snippets_menu"
	bl_label = "Code Snippets"

	def draw(self, context):
		layout = self.layout
		layout.operator("template.donothing", text="Do Nothing", icon='PREFERENCES')
		layout.separator()
		layout.menu('TEXT_MT_snippets_menu_basics', icon="PACKAGE")
		layout.menu('TEXT_MT_snippets_menu_uidesign', icon="PACKAGE")
		layout.menu('TEXT_MT_snippets_menu_operators', icon='PACKAGE')
		layout.menu('TEXT_MT_snippets_menu_helpers', icon='PACKAGE')
		layout.menu('TEXT_MT_snippets_menu_custom', icon='PACKAGE')


def draw_snippets_menu(self, context):
	self.layout.menu('TEXT_MT_snippets_menu')


# ##########################################################
# REGISTER
# ##########################################################
		
classes = (
	DemoPreferences,
	TEXT_MT_snippets_menu_basics,
	TEXT_MT_snippets_menu_uidesign,
	TEXT_MT_snippets_menu_operators,
	TEXT_MT_snippets_menu_helpers,
	TEXT_MT_snippets_menu_custom,
	TEXT_MT_snippets_menu,
)

        
def register():

	addon_updater_ops.register(bl_info)

	for menu in submenus_basics:
		bpy.utils.register_class(menu)
	
	for menu in submenus_uidesign:
		bpy.utils.register_class(menu)
		
	for menu in submenus_helpers:
		bpy.utils.register_class(menu)
		
	for menu in submenus_operators:
		bpy.utils.register_class(menu)
	
	for menu in submenus_custom:
		bpy.utils.register_class(menu)


	from bpy.utils import register_class
	for cls in classes:
		register_class(cls)

	bpy.types.TEXT_MT_editor_menus.append(draw_snippets_menu)
    
	print ("the Addon was activated")

    
def unregister():
    
	bpy.types.TEXT_MT_editor_menus.remove(draw_snippets_menu)
    
	from bpy.utils import unregister_class
	for cls in reversed(classes):
		unregister_class(cls)

	for menu in reversed(submenus_basics):
		bpy.utils.unregister_class(menu)

	for menu in reversed(submenus_uidesign):
		bpy.utils.unregister_class(menu)
		
	for menu in reversed(submenus_helpers):
		bpy.utils.unregister_class(menu)
	
	for menu in reversed(submenus_operators):
		bpy.utils.unregister_class(menu)
		
	for menu in reversed(submenus_custom):
		bpy.utils.unregister_class(menu)

	print ("the Addon was desactivated")


if __name__ == "__main__":
    register()