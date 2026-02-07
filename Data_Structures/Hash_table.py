# Hashing
dictionary = {}

# Insertion
dictionary ["a"] = "apple"
dictionary ["b"] = "ball"
dictionary ["c"] = "cat"
dictionary ["d"] = "dog"

print(dictionary)

# Search
print(f"value is: {dictionary ["a"]}")
print(f"value is: {dictionary ["b"]}")
print(f"value is: {dictionary ["c"]}")
print(f"value is: {dictionary ["d"]}")

# Deletion
del dictionary ["a"]

print(dictionary)

# insert (key, val)

# 1- Find the hash code, hash(key) = hash code
# 2- Calculate index
# 3- Check slot is empty (bucket in the index is empty)
# if bucket is empty insert the key, val pair
# if there is collision
#     use chaining
#     use open addressing