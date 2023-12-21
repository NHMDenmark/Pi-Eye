#!/bin/bash

output=~/network.log
max_lines=15

# Function to add a timestamp
add_timestamp() {
    date +"%Y-%m-%d %T"
}

# Ping a reliable host (e.g., Google DNS) to check for internet connectivity
if ping -c 3 google.com; then
    echo "Internet is up $(add_timestamp)" >> "$output"
else
    echo "Internet is down - rebooting... $(add_timestamp)" >> "$output"
    sudo reboot
fi

# Limit the log file to the last 10 entries
if [ "$(wc -l < "$output")" -gt "$max_lines" ]; then
    tail -n "$max_lines" "$output" > "$output.tmp"
    mv "$output.tmp" "$output"
fi
