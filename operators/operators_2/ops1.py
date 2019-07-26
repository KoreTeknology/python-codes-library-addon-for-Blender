import bpy
from bpy.types import Panel


# ------------------------------------------------------
# Defines UI panel
# ------------------------------------------------------
class TEXTEDITOR_PT_panel(bpy.types.Panel):
    bl_idname = "TEXTEDITOR_PT_panel"
    bl_space_type = "TEXT_EDITOR"
    bl_region_type = "UI"
    bl_label = "Template"
    bl_category = "Template"
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Hola")

        
classes = (
    TEXTEDITOR_PT_panel,
)

# -----------------------------------------------------
# Registration
# ------------------------------------------------------
def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()