from odoo import api

# Methods starting with "action"
def action_your_method_name(self):
    pass
"""
Purpose: Handles various actions triggered in the UI, often related to button clicks or business logic.
Example: Used for methods such as action_confirm, action_cancel.
"""

# Methods starting with "button"
def button_your_button_name(self):
    pass
"""
Purpose: Typically used for button actions in form views, like executing operations directly tied to user interaction.
Example: button_confirm, button_cancel.
"""

@api.returns('self', lambda value: value.id)
# Methods starting with "copy"
def copy(self, default=None):
    pass
"""
Purpose: Duplicates a record and returns the copy. Commonly used for the copy method in Odoo models.
Example: copy.
"""

@api.depends('field_nm_1', 'field_nm_2')
# Methods starting with _compute
def _compute_your_method_name(self):
    pass
"""
Purpose: Computes a field's value based on other fields. Automatically triggered when dependent fields are modified.
Example: _compute_total, _compute_name.
"""

@api.model # [optional]
@api.depends('field_nm') # [optional]
# Methods starting with "format"
def format_your_method_name(self):
    pass
"""
Purpose: Formats data, often used to convert or structure data before it is displayed or saved.
Example: format_address, format_price.
"""

# Methods starting with "convert"
def convert_your_method_name(self):
    pass
"""
Purpose: Converts data from one format to another, such as converting between units or transforming inputs.
Example: convert_amount, convert_to_local_currency.
"""

# Methods starting with "check"
def check_your_method_name(self):
    pass
"""
Purpose: Checks or validates conditions. Can be used for custom checks that ensure data integrity or correctness.
Example: check_availability, check_validity.
"""

# Methods starting with "change"
def change_your_method_name(self):
    pass
"""
Purpose: Often used to indicate changes in states, status, or other operational transitions in business logic.
Example: change_state, change_order_status.
"""

@api.model
# Always named "default_get"
def default_get(self, fields):
    pass
"""
Purpose: Provides default values for fields when creating a new record. 
Example: default_get.
"""

# Methods starting with "format"
def format_your_method_name(self):
    pass
"""
Purpose: Similar to the previous "format" methods, often used for converting or organizing data.
Example: format_display_name, format_account_number.
"""

@api.model
# Methods starting with "fields"
def fields_get(self, allfields=None, attributes=None):
    val_nm = super().fields_get(allfields, attributes)
"""
Purpose: Provides metadata for fields in the model, such as labels, types, and relations.
Example: fields_get.
"""

# Methods starting with "get"
def get_your_method_name(self):
    pass
"""
Purpose: Retrieves or fetches specific data. Used to implement custom getters.
Example: get_name, get_records.
"""

# Always named "init"
def init(self):
    pass
"""
Purpose: Initializes data or sets up certain configurations. Typically used during the module initialization.
Example: init.
"""

# Methods starting with "is"
def is_your_method_name(self):
    pass
"""
Purpose: Checks a specific condition or state and returns a boolean value.
Example: is_done, is_valid.
"""

# Always named "migrate"
def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})
"""
Purpose: Handles data migration during module updates or version upgrades.
Example: migrate.
"""

# Always named "setUp"
def setUp(self):
    pass
"""
Purpose: Prepares the environment before tests are executed. Common in unit tests.
Example: setUp.
"""

@classmethod
# Always named "setUpClass"
def setUpClass(cls):
    super().setUpClass()
"""
Purpose: Sets up the class-level environment for testing. This method runs once for the entire test class.
Example: setUpClass.
"""

@classmethod
# Always named "setUpClass" with custom parameters
def setUpClass(cls, chart_template_ref=None):
    super().setUpClass(chart_template_ref=chart_template_ref)
"""
Purpose: Another variant of setUpClass but allows for additional parameters, typically used in custom modules.
Example: setUpClass with chart_template_ref.
"""

# Methods starting with "test"
def test_your_method_name(self):
    pass
"""
Purpose: Defines a unit test case. These methods test specific functionality in the module.
Example: test_create_record, test_validation.
"""