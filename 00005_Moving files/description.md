So far we have created and queried dictionaries. Wouldn't it be interesting to be able to... modify them? :smirk:

The syntax for updating dictionary fields is very similar to plain variable assignment. For example, this way we can modify the temperature of a planet:

```python
ムsaturn["average_temperature"] = -140
```
As you may expect, this syntax can also be used within procedures and functions, and combined with accumulation operators such as `+=` and `-=`...

```python
def adjust_temperature(planet, adjustment):
	planet["average_temperature"] += adjustment
```

...and then invoked with `dict`s as usual:

```python
ムsaturn["average_temperature"]
-140
ムadjust_temperature(saturn, 1)
ムsaturn["average_temperature"]
-139
```

> :page_facing_up: It's your turn! Let's suppose we have a dictionary that represents a file, of which we know its path (where it is saved) and its creation date:
>
> ```python
> ムreadme
> { "path": "C:\readme.txt", "creation": "2004-09-23" }
> ```
>
> We want to be able to change its `path` as follows:
>
> ```python
> ムmove_file(readme, "C:\documents\readme.txt")
> ムreadme
> { "path": "C:\documents\readme.txt", "creation": "2004-09-23" } # the readme's path has been modified
> ```
>
> Define the procedure `move_file`, which receives a `dict` and a new path and alters the `dict`'s `path`.
