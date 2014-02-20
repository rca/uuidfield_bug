Django 1.7 migrations issue with custom field
---------------------------------------------

This project uses UUIDField from the
[django-uuidfield](https://github.com/dcramer/django-uuidfield) app.  When
running `manage.py makemigrations` the migration includes a UUIDField:

```
('uuid', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, blank=True)),
```

But running `manage.py migrate` does not produce the `uuid` field in the database.

The problem appears to be around
[schema.py:193](https://github.com/django/django/blob/master/django/db/backends/schema.py#L193),
where an empty definition will skip the field:

```
definition, extra_params = self.column_sql(model, field)
if definition is None:
    continue
```
