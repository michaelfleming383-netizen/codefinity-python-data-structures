# Initial travel wishlist with nested lists
travel_wishlist = [
    ["Paris", "France", 2000],
    ["Tokyo", "Japan", 3000],
    ["New York", "USA", 2500]
]

# Applying a 20% discount to the estimated cost
travel_wishlist[0][-1] = travel_wishlist[0][-1] * 0.8
travel_wishlist[1][-1] = travel_wishlist[1][-1] * 0.8
travel_wishlist[2][-1] = travel_wishlist[2][-1] * 0.8

# Printing the updated travel_wishlist to verify the change
print('Updated list:', travel_wishlist)