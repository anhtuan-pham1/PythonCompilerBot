# Discord Bot
A  bot that allows users to compile Python script on Discord


#Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install requirements.txt
```

# Usage

Navigate to discordbot/App folder, open app.py. Change "TOKEN", "CLIENT_URL", "WELCOME_CHANNEL_ID", and "LEAVE_CHANNEL_ID" to your discord server.
You can find all the information how to generate a user Token for your discord channel [here](https://discord.com/developers/)

```python
# initialize toke and client url
TOKEN = os.getenv("TOKEN")
CLIENT_URL = os.getenv("CLIENT_URL")
# initialize channel ID
WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID"))
LEAVE_CHANNEL_ID = int(os.getenv("LEAVE_CHANNEL_ID"))
```
Then open compile.py. Change "CLIENTID" and "CLIENTSECRET" to your own. Information how to generate Token for a discord compiler API can be find [here](https://www.jdoodle.com/).

```python
CLIENTID = os.getenv("ClientID")
CLIENTSECRET = os.getenv("ClientSecret")
```

Note: In my code, I used a .env file to store all of my Token. That is why I have the path to the file in order to get the token. If you don't use .env, you can simply change the code as follow:

```python
# initialize toke and client url
TOKEN = ("TOKEN")
CLIENT_URL = ("CLIENT_URL")
# initialize channel ID
WELCOME_CHANNEL_ID = int("WELCOME_CHANNEL_ID")
LEAVE_CHANNEL_ID = int("LEAVE_CHANNEL_ID")
```

```python
CLIENTID = ("ClientID")
CLIENTSECRET = ("ClientSecret")
```

After changing to all the necessary tokens, you can run ```python app.py``` to start the bot.
