
import json

# Explore the structure of the data.
filename = 'Chapter16/recent_seven_days_quakes.json'
with open(filename, encoding="utf8") as f:
   all_eq_data = json.load(f)

readable_file = 'Chapter16/earthquakes_readable.json'
with open(readable_file, 'w') as f:
   json.dump(all_eq_data, f, indent=4)
