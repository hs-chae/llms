import json
import random

skills = ["parallel", "length"]
count = [10000, 10000]
new_data = []
name = ""

for i, skill in enumerate(skills):
    # Read data from JSON file
    with open(f"data/{skill}.json", 'r') as f:
        tmp_data = json.load(f)

    # Take random count[i] amount from tmp_data
    sampled_data = random.sample(tmp_data, count[i])

    # Extend them to new_data
    new_data.extend(sampled_data)

    # Update name
    name += skill[:2] + "-"

# Add the total count to the name
name += f"{sum(count) // 1000}k"
random.shuffle(new_data)
# Save new_data as JSON
with open(f"data/mixed_{name}.json", 'w') as f:
    json.dump(new_data, f)

print(f"Generated mixed_{name}.json")
