When you queried the existing dictionaries, it looked something like the following:

```python
ムthat_mahal
{ "name": "Taj Mahal", "location": "Agra, India", "year_of_construction": 1653 }
```

That query was useful because we were inspecting the entire `taj_mahal` dictionary, including all its fields. But `dict`s may also be queried by a particular field! Look :eyes::

```python
ムtaj_mahal["location"]
"Agra, India"
ムtaj_mahal["year_of_construction"]
1653
```

> We initialized the planets `mercury`, `mars` and `saturn` as dictionaries with the fields `name`, `average_temperature` and if `has_rings`.
> Check their individual fields in the console and when you're done type `done()`.
