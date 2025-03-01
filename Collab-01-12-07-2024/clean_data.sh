#!/bin/bash

# Define the input and output files
input_file="simple_stream_subscribers.csv"
cleaned_file="cleaned_data.csv"

echo "Cleaning data..."

# Remove rows with invalid emails and missing names or countries
awk -F, 'NR==1 {print $0} NR>1 {if ($3 != "invalid_email" && $2 != "" && $6 != "") print $0}' "$input_file" > "$cleaned_file"

echo "Data cleaned and written to $cleaned_file"