import json


def fix_id_order(data):
    challenges = data.get("CHALLENGES", [])
    for i, challenge in enumerate(challenges):
        challenge["id"] = i
    return data


# Read the JSON data from a file
with open('database_filled.json', 'r') as file:
    json_data = json.load(file)

# Fix the ID order
fixed_data = fix_id_order(json_data)

# Write the fixed data back to a file
with open('database_final.json', 'w') as file:
    json.dump(fixed_data, file, indent=4)
