a = [3, 5, 7, 2, 8, -1]
b = [4, 9, 1, 6, 0, -2.3]

combined_list = a + b
print("Combined List:", combined_list)
sorted_list = sorted(combined_list)
print("Sorted List:", sorted_list)
count_items = len(sorted_list)
print("Number of Items in Sorted List:", count_items)

max_value = max(sorted_list)
min_value = min(sorted_list)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)