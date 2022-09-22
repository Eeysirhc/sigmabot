# sigmabot

## Quick Start

### Linux/Ubuntu

```bash
sudo apt install python3 python3-pip -y
pip install discord python-dotenv
```

### Discord

Follow the instructions for creating a bot: https://discordpy.readthedocs.io/en/stable/discord.html

When in the Bots tab of Applications, make sure to turn on the slider for all privileged Gateway Intents to test the bot.

### bash

#### add to `$HOME/.profile`:

```bash
# set PATH so it includes user's local bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```

#### create `$HOME/bin/sigmabot/main/.env` and add line:

```bash
DISCORD_TOKEN="<SECRET-BOT-TOKEN>"
```

### Launch

```python
python3 sigmabot.py
```

### Help

For a list of available commands send `.help` as a message in Discord or Telegram.

## Customization

Developers can change config settings in the `sigmabot.py` file.

### Prefix

`command_prefix`: instead of the default `.` can modify to `/`, `$`, `#`, `!` or whatever you prefer.

### Status

`discord.Game()`: default is `on the Rosen Bridge`.

## Contributing

The spaghetti code for this bot is held together by hope and a lot of bubble gum. It would be ideal for someone with actual software development skills can improve upon this and make it better. Thus, any improvements to this package is highly appreciated.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-stuff`)
3. Commit your changes (`git commit -am "Add new stuff improvements"`)
4. Push to branch (`git push origin feature/new-stuff`)
5. Open a pull request




