# Tutorial: How to start

* If you have never seen a Python code, this it the time to look at the basics. Python is a very powerful language and within Blender, it gives you infinite possibilities. Basicaly, as a programming language, you will do some calculation, comparaison, import and export data, and so on... 

* In Blender, you will be able to "call" any existing features, create some interface design, add some extra features or arrange features that produce a specific result, and this is what we got to do.

* To start, here is the basic implementation of a script or add-on, ready to be loaded in Blender 2.8x:

```python

bl_info = {
	"name": "YourSnippetName",
	"description": "YourDescription",
	"author": "yourName",
	"version": (0, 1, 0),
	"blender": (2, 80, 0),
	"location": "PathToView if exist",
	"category": "Development Snippets"
}

# ########################################
# IMPORTS SECTION
# ########################################

import bpy

# ########################################
# YOUR CODE HERE !
# ########################################



# ########################################
# REGISTER SECTION
# ########################################

classes = (
	#yourclass_1, yourclass_2,...
)

def register():
	# Register the classes
	from bpy.utils import register_class
	for cls in classes:
		register_class(cls)


def unregister():
	# Unregister the classes
	from bpy.utils import unregister_class
	for cls in reversed(classes):
		unregister_class(cls)


if __name__ == "__main__":
	register()
```

> This page is in progress, please, come back soon !

Documentation and tutorials

- properties and operator null
- header comments
- scripts comments
- import and registering
- license
