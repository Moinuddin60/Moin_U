#  sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Result union
union_set = A.union(B)
union_set_Join = A|B
# Result intersection
intersection_set = A.intersection(B)
intersection_set_new = A & B
# Result difference (A - B)

difference_set = A.difference(B)
difference_set_new = A - B

# Display results
print("Set A:", A)
print("Set B:", B)
print("Union:", union_set)
print("Union_Join:", union_set_Join)
print("Intersection:", intersection_set)
print("Intersection_New:", intersection_set_new)
print("Difference (A - B):", difference_set)
print("Difference_New (A - B):", difference_set_new)
