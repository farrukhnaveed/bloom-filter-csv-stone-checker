import csv
import os
import glob
import math
import time
from pybloom_live import BloomFilter

# Function to count the total number of rows in all CSV files
def count_total_rows(folder_path):
    total_rows = 0
    for csv_filename in glob.glob(os.path.join(folder_path, '*.csv')):
        with open(csv_filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            row_count = sum(1 for row in reader) - 1  # Subtract 1 for header row
            total_rows += row_count
    return total_rows

# Function to read stones from a CSV file and add to Bloom Filter
def add_stones_to_bloom_filter(csv_filename, stone_column_index, bloom_filter):
    with open(csv_filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) > stone_column_index:  # Check if row has enough columns
                stone = row[stone_column_index]
                bloom_filter.add(stone)

# Function to create a Bloom Filter from multiple CSV files in a folder
def create_bloom_filter_from_folder(folder_path, stone_column_index, error_rate):
    total_rows = count_total_rows(folder_path)
    
    # Calculate optimal Bloom Filter size and number of hash functions
    m = - (total_rows * math.log(error_rate)) / (math.log(2) ** 2)
    k = (m / total_rows) * math.log(2)
    bloom = BloomFilter(capacity=total_rows, error_rate=error_rate)
    
    # Iterate over all CSV files in the folder
    for csv_filename in glob.glob(os.path.join(folder_path, '*.csv')):
        add_stones_to_bloom_filter(csv_filename, stone_column_index, bloom)

    return bloom

# Function to check if a stone exists in the Bloom Filter
def stone_exists(bloom_filter, stone):
    return stone in bloom_filter

# Main function to demonstrate the usage
def main():
    folder_path = os.getenv('CSV_FOLDER_PATH', 'path/to/csv/folder')  # Get folder path from environment variable
    stone_column_index = 1  # 2nd column in the CSV (0-based index)
    error_rate = 0.001  # Desired false positive rate
    
    # Create Bloom Filter from all CSV files in the folder
    bloom_filter = create_bloom_filter_from_folder(folder_path, stone_column_index, error_rate)
    
    # Get the test stone from an environment variable
    test_stone = os.getenv('TEST_STONE', 'abcd1234')

    # Measure the time taken to check if the stone exists
    start_time = time.time()
    exists = stone_exists(bloom_filter, test_stone)
    end_time = time.time()

    # Print the result and time taken
    if exists:
        print(f'{test_stone} might exist in the CSV files.')
    else:
        print(f'{test_stone} definitely does not exist in the CSV files.')

    print(f"Time taken to complete the search: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()
