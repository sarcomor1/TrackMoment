python3 -m venv .venv
source .venv/bin/activate
pip install --no-index --find-links=wheelhouse -r requirements.txt
echo "good!   installed requirements "
