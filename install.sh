echo "Installing 42_py_logtime..."
echo "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Giving execution permission to logtime.sh..."
chmod +x logtime.sh
echo "UID = \"your 42 API UID from intranet API page\"\nSECRET = \"your 42 API SECRET from intranet API page\"\nUSERNAME = \"your intra nickname\"" > credentials.py
echo "credentials.py file created, please fill it with your 42 API credentials as explained in the README."
echo "42_py_logtime installation complete!"
