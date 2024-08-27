mkdir projectA
cd projectA
python3.12 -m venv bot_env

source bot_env/bin/activate
~ deactivate

pip install -r requirements.txt

virtualenv venv --distribute

cmd = "ssh -i ec2_key ubuntu@i-0801d56b767444e6e -o ProxyCommand='aws ec2-instance-connect open-tunnel --instance-id i-0801d56b767444e6e'"