Hints:

cd bot_env && python3.12 -m venv bot_env

cd tg_bot

screen -S bot_session

source bot_env/bin/activate
OR
source bot_env/bin/deactivate

pip install -r requirements.txt

virtualenv venv --distribute

sudo timedatectl set-timezone Europe/Kyiv

  152  cd tgbot/
  153  screen -ls
  154  screen -r 31627.bot
  155  ll
  156  source bot_env/bin/activate

Screen:
screen -S session_name - Create session
Ctrl+a и d - detache
screen -r - attach




