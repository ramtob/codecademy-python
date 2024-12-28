#
#  What happens when you apply str.join() to a dictionary?
#

my_dict = {"name": "Ankit", "country": "India"}
my_delim = ":::"
x = my_delim.join(my_dict)

print(x)