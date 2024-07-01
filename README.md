mkdir projectA
cd projectA
python3.12 -m venv bot_env

source bot_env/bin/activate
~ deactivate

pip install -r requirements.txt

virtualenv venv --distribute