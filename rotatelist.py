collection_of_strings = [word for word in input().split(' ')]
new_collection = collection_of_strings[-1:] + collection_of_strings[:-1]

print(' '.join(new_collection))


