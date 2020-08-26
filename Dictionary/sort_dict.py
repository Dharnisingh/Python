# Perform sort operation on dictionary

d = {'key1': 1, 'key2': 3, 'key3': 2, 'key1': 1, 'key2': 2, 'kye5': 5}

# Sort dictionary by keys
srt_by_key = dict(sorted(d.items()))
print(srt_by_key)

#sort dictionary by values
srt_by_val = dict(sorted(d.items(), key = lambda x: x[1], reverse= True))
print(srt_by_val)
