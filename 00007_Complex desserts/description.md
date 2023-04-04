A few exercises earlier, we learned about the difference between lists and dictionaries.  But that doesn't mean we can't use both data structures at the same time! :wink:

For example, a list can be a field of a dictionary. 🍮 Take a look at these dessert dictionaries! We know how many minutes of cooking time they take and what ingredients they contain:


```python
flan = { "ingredients": ["eggs", "milk", "sugar", "vanilla"], "cook_time": 50 }
cheesecake = { "ingredients": ["cream cheese", "raspberries"], "cook_time": 80 }
lemon_pie = { "ingredients": ["lemon juice", "cornstarch", "milk", "eggs"], "cook_time": 65 }
```

> Define the function `most_difficult_to_cook`, which receives two dessert dictionaries as argument and returns the one with more ingredients of the two:

> ```python
ムmost_difficult_to_cook(flan, cheesecake)
{ "ingredients": ["eggs", "milk", "sugar", "vanilla"], "cook_time": 50 }
```
