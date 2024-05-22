import csv
import random

# Define column names
columns = [
    "Floor",
    "Parking Number",
    "Parking Status",
    "Parking Type",
    "Metadata"
]

# Define possible values for some columns
statuses = ["Empty", "Filled"]
types = ["Special Need", "VIP", "Normal"]
yes_no = ["Yes", "No"]
metadata1 = ["Near to Door", "Left Corner", "Right Corner", "Near to Lift", "Near to Stairs"]

# Generate data
data = []
for i in range(1000):
    floor = random.randint(1, 5)  # Assuming 5 floors
    parking_number = i + 1
    status = random.choice(statuses)
    p_type = random.choice(types)
    metadata = random.choice(metadata1)
    
    data.append([
        floor,
        parking_number,
        status,
        p_type,
        metadata
    ])

# Write to CSV
file_path = "apps/find_parking/parking_spots.csv"
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)  # Write header
    writer.writerows(data)    # Write data

file_path
