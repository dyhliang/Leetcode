​Done without if statements:
-Map the amount of big (1), med (2), small (3) spaces available in a tracking hashmap as the keys
-The value for each key is: [spaces available, spaces parked], spaces available uses the 3 values passed into the constructor, spaces parked is 0 by default.
-addCar() always increments tracking[carType][1] (spaces parked) by 1
-return a boolean statement checking if tracking[carType][1] is less than or equal to tracking[carType][0] (spaces available)
