from ._anvil_designer import Form1Template
from anvil import *
from datetime import date

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def date_picker_2_change(self, **event_args):
    if self.date_picker_1.date is not None and self.date_picker_2.date is not None:
      self.label_1.text = self.date_picker_2.date - self.date_picker_1.date

  def date_picker_1_change(self, **event_args):
    if self.date_picker_1.date is not None and self.date_picker_2.date is not None:
      self.label_1.text = self.date_picker_2.date - self.date_picker_1.date

  def button_1_click(self, **event_args):
    Notification("A menu item").show()

