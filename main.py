
#Lists
print("-===Lists===-")

Friends = ["Dan", "David", "Anne"]
Friend_and_ages = [
    ["Dan", 34],
    ["Bob", 35],
    ["Dana", 38]
]

#filtering list
Dana = Friend_and_ages[2][0]
Dana_Age = Friend_and_ages[2][1]
print(Friend_and_ages)
print("Filters Dana's name from the list:", Dana)
print("Filters Dana's age from the list:", Dana_Age)
#remove from list
Friend_and_ages.remove(["Dana", 38])
print(Friend_and_ages)
# Append value to a list
Friends.append("Keren")
print(Friends)
# Remove from a list
Friends.remove("Keren")
print(Friends)

#tuple
print("-===Tuple===-")
short_tuple = "Ben", "Dani"
print("Short way of tuple", short_tuple)
a_bit_clearer = ("Ben", "Dani")
not_a_tuple = "Ben",
Friends_tuple = ("Dan", "David", "Anne")
print(Friends_tuple)
# you cannot added tp a tuple
# This will create a new tuple
Friends_tuple = Friends_tuple + ("Dana",)
print(Friends_tuple)

#Sets
print("-===SETS===-")
print("Arts Friends:")
art_friends = {"Bob", "Anne", "Jen"}
print(art_friends)
print("Science Friends:")
science_friends = {"Jen", "Charlie"}
arts_but_not_science = art_friends.difference(science_friends)
print("Arts but not science:\n", arts_but_not_science)
science_but_not_art = science_friends.difference(art_friends)
print("Science but not science:\n", science_but_not_art)

not_in_both = art_friends.symmetric_difference(science_friends)
print("friends that are not in both groups:\n",  not_in_both)
art_and_science = art_friends.intersection(science_friends)
print("Friends that are in both arts and science groups:\n", art_and_science)
all_friends = art_friends.union(science_friends)
print("All friends:\n", all_friends)


nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
friend_name = input("Add a friend name")
# Add the name to the empty set
user_friends.add(friend_name)
# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
print(nearby_people.intersection(user_friends))
