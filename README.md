# ipchecker

This is a small script that is meant to be run on a regular basis though something like cron. It checks the public IP address of the local network and compares it to a logged IP. If they differ, it means the ISP has changed your public IP address. The script will then log the new IP address and send you it in an email notification.

There are three files the script looks for, but only one is actually neccassary.

# creds

this is neccassary!

This is simply the credentials for your gmail account

format: just your email address and your password on the next line

Example:

clever.address at dork.com
UNCRACKABLEPASSWARD

# addresses

this is optional.

If you do not make this file you must edit ipChecker.py and add the email addresses manually as arguements in the compose fuction call. The "To" arguement can take a list of addresses nin case you're popular.

format: There must be a "From: " and a "To: " at the beginning of two consecutive lines Ther can be multiple to addresses, just separate them with a comma. make sure there are no spaces between the addresses though

Example:

From: clever.address at dork.com
To: clever.address at dork.com,thedukeking at damoon.uwish

# emailbody

this is optional

Once again if you don't make this file you can edit ipChecker.py and add it to the arguement of the compose function call. It'll be just a really long string.

format: there must be a "subject:" string. Note: theres no space after the colon. Then on a separate line add the body of the email you'll be sending. The new IP address will be app[ended to the end of this. You do not need to leave a space at the end of the message, a space will be added for you.

Example:
Subject:IP Address Change

Yo home-skillet... the NEW IP address of ther server is
