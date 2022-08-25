# sigmabot

Discord bot for frequently asked questions about Ergo.

## Quick Start

### Create `.env` file

```bash
DISCORD_TOKEN="<SECRET-BOT-TOKEN>"
```

### Launch bot

```python
python3 sigmabot.py
```

## Commands

### Ergo block height

![](https://preview.redd.it/hmpx5ejxpih91.png?width=1706&format=png&auto=webp&s=53394032970c0e9b37c39bffc8506595781dde8e)

### Coming Soon

* `.help`
* `.wallets`
* `.mining`
* `.dex`
* `.ergomixer`
* `.sigmaverse`
* `.geterg`
* `.cex`

## Customization

Developers can change config settings in the `sigmabot.py` file.

### Prefix

`command_prefix`: instead of the default `.` can modify to `$`, `#`, `!` or whatever you prefer.

### Status

`discord.Game()`: default is `in Sigmaverse`.

## Contributing

The spaghetti code for this bot is held together by hope and a lot of bubble gum. It would be ideal for someone with actual software development skills can improve upon this and make it better. Thus, any improvements to this package is highly appreciated.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-stuff`)
3. Commit your changes (`git commit -am "Add new stuff improvements"`)
4. Push to branch (`git push origin feature/new-stuff`)
5. Open a pull request



