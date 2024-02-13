
# 42_py_logtime

Small script for Ecole 42 students to get the total intranet log time of the current month.

## Installation
1) **(Linux / MacOS)** Run `./install.sh`.

2) Get your API credentials from the intranet.

	a) Go to intranet profile.

	b) Click your name on top right.

	c) Go to "Settings".

	d) Go to "API".

	e) Click on "Register New API". Now you should be at the URL `https://profile.intra.42.fr/oauth/applications/new`.
	
	f) Fill out the name field with a name of your choice.
	
	g) Fill out the "Redirect URI" field with a valid URI like `https://www.google.com/`.
	
	h) Click "Submit".
	
	i) You should be seeing your credentials now, proceed to the next step.

3) Go to `credentials.py` and fill it with the template below where `UID` and `SECRET` are your 42 API credentials and save it.
	```
	UID = "your 42 API UID from intranet API page"
	SECRET = "your 42 API SECRET from intranet API page"
	USERNAME = "your intra nickname"
	```
	**WARNING**: Don't share these credentials!

## Usage

**(Linux / MacOS)** Run `./logtime.sh`.