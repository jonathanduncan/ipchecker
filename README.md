# ipchecker

This is a small script that is meant to be run on a regular basis though something like cron. It checks the public IP address of the local network and compares it to a logged IP. If they differ, it means the ISP has changed your public IP address. The script will then log the new IP address and send you it in an email notification.

You need to create a blank text file in the directory of the script, name it 'creds', and put your email and password in it on separate lines.
