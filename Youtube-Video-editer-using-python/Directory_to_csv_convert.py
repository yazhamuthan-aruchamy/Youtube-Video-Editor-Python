import os
import csv

directory_path = r'D:\Output files\Reels output\100+ HQ Motivational Reels Hindi'
empty_path = []
for dirpath, dirname, filenames in os.walk(directory_path):
    for filename in filenames:
        file_add = os.path.join(directory_path, filename)
        empty_path.append((filename, file_add))

csv_file = r'D:\Output files\Reels output\video_List.csv'
with open(csv_file, "w", newline='') as updated_csv_file:
    csv_added = csv.writer(updated_csv_file) # Updated variable name
    csv_added.writerow(["File name", "File path"])
    csv_added.writerows(empty_path) # Use writerows() to write multiple rows
print("Successfully completed")
