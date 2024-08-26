from odoo import api

@api.autovacuum
# Start with _gc
def _gc_your_method_name(self):
    pass
"""
@api.autovacuum:
- Purpose: Used for system maintenance and cleanup tasks during the autovacuum process.
- Example: Used in methods starting with `_gc_`, like `_gc_clean_old_records`.
"""

@api.constrains('field_nm_1', 'field_nm_2')
# Start with _check
def _check_your_method_name(self):
    pass
"""
@api.constrains:
- Purpose: Ensures data validation and field integrity by defining constraints on specified fields.
- Example: Used for methods starting with `_check_`, like `_check_valid_dates`.
"""

@api.depends('field_nm_1', 'field_nm_2')
# Start with _compute
def _compute_your_method_name(self):
    pass
"""
@api.depends:
- Purpose: Automatically computes field values based on the specified dependent fields.
- Example: Used for methods starting with `_compute_`, like `_compute_total_amount`.
"""

@api.depends_context('field_nm')
# Start with _compute
def _compute_your_method_name(self):
    pass
"""
@api.depends_context:
- Purpose: Automatically computes field values based on context variables.
- Example: Used for methods starting with `_compute_`, like `_compute_based_on_context`.
"""

@api.model
# Start with _get
def _get_your_method_name(self):
    pass
"""
@api.model:
- Purpose: Declares a method that operates at the model level, not tied to specific records.
- Example: Used for methods starting with `_get_`, like `_get_default_values`.
"""

@api.model_create_multi
# Always method name of create()
def create(self, vals_list):
    pass
"""
@api.model_create_multi:
- Purpose: Optimizes the creation of multiple records at once.
- Example: Used for the `create()` method.
"""

@api.ondelete(at_uninstall=False)
# Start with _unlink_except
def _unlink_except_your_method_name(self):
    pass
"""
@api.ondelete:
- Purpose: Controls behavior when records are deleted, especially during module uninstallation.
- Example: Used for methods starting with `_unlink_except_`, like `_unlink_except_for_conditions`.
"""

@api.onchange('field_nm_1', 'field_nm_2')
# Start with _onchange
def _onchange_your_method_name(self):
    pass
"""
@api.onchange:
- Purpose: Dynamically updates fields in the user interface when the specified fields change.
- Example: Used for methods starting with `_onchange_`, like `_onchange_product_id`.
"""

@api.onchange('field_nm_1', 'field_nm_2')
# Start with _onchange
def onchange_your_method_name(self):
    pass
"""
@api.onchange (Non-prefixed method):
- Purpose: Similar to the previous `@api.onchange`, but without the `_onchange_` naming convention.
- Example: Used for non-prefixed methods to handle UI field changes.
"""

@api.returns('self', lambda value: value.id)
# Always method name of copy()
def copy(self, default=None):
    pass
"""
@api.returns:
- Purpose: Specifies the return type of the method, typically used for methods like `copy()`.
- Example: Used for methods like `copy()` to ensure correct return types.
"""
