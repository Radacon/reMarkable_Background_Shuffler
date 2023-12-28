#!/bin/bash

# All backgrounds should be stored in ~/backgrounds/ as
# "suspended_optxx.png" xx being a number from 00 to 99
# I haven't tested over 30 files. 

# Defines the destination directory where services are stored and ran
# Chatgpt says it can live in the Users directory but I've found it only
# runs in the system directory. 
destination_dir="/lib/systemd/system/"

# Copy .Timer and and .Service to systemctl default directory
# Edit .Timer to change how often backgrounds get changed!
cp "changebg.service" "$destination_dir/"
cp "changebg.timer" "$destination_dir/"

# Reload systemd daemon to pick up new unit files
systemctl daemon-reload

# Enable and start the systemd services
systemctl enable changebg.timer

# Start Background Shuffler Service
systemctl start changebg.timer

# Reload again
systemctl daemon-reload

# Optionally, you can check the status of the services
systemctl list-timers --all

# Optionally, perform additional tasks as needed

echo "Installation complete!"
