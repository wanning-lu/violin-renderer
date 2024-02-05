import random

# List of Paths W/ index Referring to Different Dataset
file_paths = [f"violin-renderer/bach-violin-dataset/dataset_{idx}" for idx in range(1,21)] # Note : Modify Range Accordingly

# Map Index
dict_mapping = {}
for idx, path in enumerate(file_paths, start = 1):
    dict_mapping[idx] = path

# Size = 90% * length of dictionary
size = (int) (0.9 * len(dict_mapping))

random_listing = random.sample(list(dict_mapping.keys()), size)
print(random_listing)
print("\nEntire Random Listing:")

gather_paths = []
for idx in random_listing:
    gather_paths.append(dict_mapping[idx])
for file in gather_paths:
    print(file)

distribution = (int) (0.5 * len(gather_paths)) # Note : 50% | 50%
training_set = gather_paths[:distribution]
validate_set = gather_paths[distribution:]

print("\nTraining Set:")
for path in training_set:
    print(path)
print("\nValidate Set:")
for path in validate_set:
    print(path)
