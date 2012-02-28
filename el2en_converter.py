# coding: utf-8
from gettext import gettext as _
from gi.repository import GObject, Gtk, Gedit
from converter import Converter

# Menu item example, insert a new item in the Tools menu
ui_str = """<ui>
  <menubar name="MenuBar">
    <menu name="ToolsMenu" action="Tools">
      <placeholder name="ToolsOps_2">
        <menuitem name="Invert keyboard" action="el2en"/>
      </placeholder>
    </menu>
  </menubar>
</ui>
"""

class El2enWindowActivatable(GObject.Object, Gedit.WindowActivatable):
  __gtype_name__ = "El2enWindowActivatable"

  window = GObject.property(type=Gedit.Window)

  def __init__(self):
    GObject.Object.__init__(self)
    self.converter = Converter()

  def do_activate(self):
    # Insert menu items
    self._insert_menu()

  def do_deactivate(self):
    # Remove any installed menu items
    self._remove_menu()

    self._action_group = None

  def _insert_menu(self):
    # Get the Gtk.UIManager
    manager = self.window.get_ui_manager()

    # Create a new action group
    self._action_group = Gtk.ActionGroup("El2enPluginActions")
    self._action_group.add_actions([("el2en", None, _("Toggle layout (El/En)"),
                                     None, _("Toggle layout (El/En)"),
                                     self.on_clear_document_activate)])

    # Insert the action group
    manager.insert_action_group(self._action_group, -1)

    # Merge the UI
    self._ui_id = manager.add_ui_from_string(ui_str)

  def _remove_menu(self):
    # Get the Gtk.UIManager
    manager = self.window.get_ui_manager()

    # Remove the ui
    manager.remove_ui(self._ui_id)

    # Remove the action group
    manager.remove_action_group(self._action_group)

    # Make sure the manager updates
    manager.ensure_update()

  def do_update_state(self):
    self._action_group.set_sensitive(self.window.get_active_document() != None)

  # Menu activate handlers
  def on_clear_document_activate(self, action):
    doc = self.window.get_active_document()
    if not doc:
        return
    
    if not doc.get_has_selection():
        return

    (start, end) = doc.get_selection_bounds()
    selection = doc.get_text(start, end, True) #True: get non-printable characters too
    new_text = self.converter.toggle_layout(selection)
    for ch in selection:
        new_text += '*'
    doc.delete(start, end)
    doc.insert(start, new_text)
        
