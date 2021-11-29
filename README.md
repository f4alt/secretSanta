# secretSant
Python based secret Santa generator which randomizes players and notifies via an email to remain anonymous.

# Usage
The main sending email is specified in _config.py_.
- Requires the full email and password for a gmail account within the ```gmail_user``` and ```gmail_password``` fields
- Sending account must have 'less secure apps' enabled within gmail
- Other mail servers and username / passwords can be used here if you know what you're doing

Players are specified in the _config.py_
- Players should be added to the ```player_info``` array in the form of key value pairs player_name:player_email.
- The player_name is used to identify the recipient. So use last names if needed

Changes to the sent email can be done in _main.py_. Feel free to update the message ```body``` and ```subject``` fields to suit your needs.

On error, the email in question will be printed to the console.
<br>**NOTE:** if it errors on all emails, you probably have not enabled 'less secure apps' for the sending gmail.

All connections are written to _log.txt_.
