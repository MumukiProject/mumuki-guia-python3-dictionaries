Remember we learned that a list can be composed of other lists? The same is true with dictionaries! :hushed: If we have a complex data structure, it may not be enough to represent it only by strings, numbers, booleans and lists, but we need _another_ dictionary in it.

You can't live on desserts! Well, maybe yes, but let's stick to a healthy diet :stuck_out_tongue_winking_eye:. Using a dictionary, we want to model a complete menu: it consists of a main course :curry:, the vegetables from the salad that accompanies it :tomato:, and a dessert :custard: as we have been working on, that is, it is still a dictionary.

For example, below you'll find a menu with aubergine parmigiana :eggplant: as the main course, a potato salad :potato:, and a cheesecake for dessert. Since the dictionary is a bit long, and to make it more readable, we'll format it as follows:

```python
daily_menu = {
  "main_dish": "aubergine parmigiana",
  "salad": ["potato", "carrot", "peas"],
  "dessert": { "ingredients": ["cream cheese", "raspberries"], "cook_time": 80 }
}
```

> Find out the `ingredients` of the `dessert` of the `kids_menu`. Since it is a dictionary within a dictionary, we need to access the `dessert` field first and then its `ingredients` field. If you can't think of how, you can look at the hint. :mag:
