# KK 2nd, List Types // Notes

# lists
siblings = ["Alex","Katie","Andrew","Tia","Treyson","Xavier","Jake"]
siblings[-1] = "DOW"
siblings.append("Alex")
print(siblings)
# used for; categories, data storage, control randomization
# methods; .append .pop .remove .sort len() .clear .index .extend .reverse

# tuples; ordered, unchangeable
white = (255, 255, 255)
# white[1] = 0
print(white[0])
# unpacking tuples
r, g ,b = white
print(r)
# can be used for; level info, starting point, preset data, & anything you don't want changed !
# methods; .count .index

# sets; unordered, mutable/changeable
fruits = {"apple", "orange", "kiwi","pineapple","pear","pomegranate","orange"}
fruits.remove("pineapple")
fruits.add("watermelon")
print(fruits)

# used for; character lists, loot, passwords, randomization
# methods; .clear .difference .copy .pop
