# Bloom Filter CSV Stone Checker

This project implements a Bloom filter to efficiently check if a stone exists in multiple CSV files. The Bloom filter is built using Python and Docker, and can handle large datasets with low false positive rates.

## Prerequisites

- Docker
- Docker Compose

### A typical top-level directory layout

    .
    ├── Dockerfile
    ├── docker-compose.yml
    ├── main.py
    ├── requirements.txt    
    ├── csv_folder
       ├── feedfiles1.csv
       ├── feedfiles2.csv


## Setting Up the Project

1. **Clone the Repository**

   ```sh
   git clone https://github.com/farrukhnaveed/bloom-filter-csv-stone-checker.git
   cd bloom-filter-csv-stone-checker

2. **Copy CSV Files**
  Create a directory named csv_folder and add your CSV files there.

  For example, `feedfiles1.csv` and `feedfiles2.csv` with 2nd column as the stone identity.
  
  Example:
  
  `feedfiles1.csv`:
  
    id,stock_id
    1,IM-300-012-00,ROUND,1234.56
    2,ABC22/44,ROUND,123.00
    3,XYZ123/3-22,ROUND,5678.00

## Building and Running the Project
1. **Build the Docker Image**
   ```sh
   docker-compose build
2. **Run the Docker Container**
   ```sh
   docker-compose up

  By default, this will run the script and check if Stock ID: abcd1234 exists in the CSV files.
  
The output will indicate if the stone might exist or definitely does not exist, along with the time taken for the search.


3. **Run the Docker Container with a Custom Test Stock ID**
   ```sh
   docker-compose run -e TEST_STONE=abcd1234 bloom_filter

  Replace `abcd1234` with the stone you want to check.

## Explanation
  Dockerfile: Defines the Docker image, setting up a Python environment and copying the project files into the container.

  docker-compose.yml: Defines the Docker Compose configuration, specifying the service, volumes, and environment variables.
  
  main.py: The main Python script that creates the Bloom filter from the CSV files and checks for the existence of a specified Stock ID.
  
  requirements.txt: Lists the Python dependencies (pybloom-live).

## Customization
  CSV_FOLDER_PATH: The path to the folder containing the CSV files. By default, it is set to ./csv_folder but can be modified in the docker-compose.yml file or overridden at runtime.
  
  TEST_STONE: The Stock ID to check. Set this environment variable to specify a different Stock ID without rebuilding the Docker image.

1. **Example Output**
   ```sh
   abcd1234 definitely does not exist in the CSV files.
   Time taken to complete the search: 0.000123 seconds
