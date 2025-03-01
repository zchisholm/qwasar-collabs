#!/bin/bash

# Define the input and output files
cleaned_file="cleaned_data.csv"
sorted_file="sorted_data.csv"

echo "Sorting data by Subscription Start Date..."

# Sort data by Subscription Start Date
sort -t, -k4,4 "$cleaned_file" > "$sorted_file"

echo "Data sorted and written to $sorted_file"