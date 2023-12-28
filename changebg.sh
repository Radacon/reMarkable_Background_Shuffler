#!/bin/bash

# Source directory (B)
src_dir="/home/root/backgrounds/"

# Destination directory (A)
dest_dir="/usr/share/remarkable/"

# Check if the source directory exists
if [ ! -d "$src_dir" ]; then
  echo "Source directory does not exist: $src_dir"
  exit 1
fi

# Check if the destination directory exists
if [ ! -d "$dest_dir" ]; then
  echo "Destination directory does not exist: $dest_dir"
  exit 1
fi

# Use find to list all matching files in the source directory
files=($(find "$src_dir" -type f -name "suspended_opt*.png"))

# Check if there are any matching files
if [ ${#files[@]} -eq 0 ]; then
  echo "No matching files found in $src_dir"
  exit 1
fi

# Generate a random index to select a file
random_index=$((RANDOM % ${#files[@]}))

# Get the random file from the array
random_file="${files[$random_index]}"

# Copy the random file to the destination directory with the name "suspended.png"
cp "$random_file" "$dest_dir/suspended.png"

echo "Random file '$random_file' copied and renamed to '$dest_dir/suspended.png'"

