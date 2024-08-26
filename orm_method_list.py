def your_method_name(self):
    model.grouped(key) # Grouping
    Model.sorted(key=None, reverse=False) # Sort
    Model.mapped(func) # Maping

    # Filter
    Model.filtered(func)
    Model.filtered_domain(domain)

    # Record(set) information
    Model.ids
    odoo.models.env
    Model.exists()
    Model.ensure_one()
    Model.get_metadata()

    Model.unlink() # Unlink

    # Search / Read
    Model.browse([ids])
    Model.search(domain[, offset=0][, limit=None][, order=None])
    Model.search_count(domain[, limit=None])
    Model.search_fetch(domain, field_names[, offset=0][, limit=None][, order=None])
    Model.name_search(name='', args=None, operator='ilike', limit=100)
    Model.fetch(field_names)
    Model.read([fields])
    Model._read_group(domain, groupby=(), aggregates=(), having=(), offset=0, limit=None, order=None)
    Model.read_group(domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True)