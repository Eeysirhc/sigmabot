# sigmabot

Discord bot for all things Ergo with the following available services:

* SpectrumDEX (formerly ErgoDEX) price charts
* Ergo block height
* Address balance history charts

## Prerequisites

* Create a Discord bot account ([instructions](https://discordpy.readthedocs.io/en/stable/discord.html))
* Python dependencies

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

### Token price charts

Valid input: `sigusd`, `ergopad`, `exle`, `paideia`, `neta`, `sigrsv`, `terahertz`, `egio`, `comet`, `ergold`, `migoreng`, `erdoge`

```python
.spf <token>
```

### Ergo block height

```python
.blox 
```

### Address balance history 

```python
.addy <ergo-address>
```

## Customization

Developers can change config settings in the `sigmabot.py` file.

### Prefix

Line #20: instead of the default `.` can modify to `$`, `#`, `!` or whatever you want.

### Status

Line #28: default is `on the Rosen Bridge`.

## Backlog

- [ ] Add requirements.txt installation step
- [ ] Functionality to intake multiple tokens and plot all on the same graph
- [ ] Remove dependency on CSV file for initial tokens and expand list
- [ ] Streamline code efficiency (see inline comments)
- [x] Plot $ERG address amount over time 
- [ ] Plot token address balance over time 
- [x] Replace USD with $ERG values only
- [ ] Address balance ranking (whale, shark, shrimp, etc.)
- [ ] Token information such as market cap, circulating supply, etc.


## Contributing

The spaghetti code for this bot is held together by hope and a lot of bubble gum. It would be ideal for someone with actual software development skills can improve upon this and make it better. Thus, any improvements to this package is highly appreciated.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-stuff`)
3. Commit your changes (`git commit -am "Add new stuff improvements"`)
4. Push to branch (`git push origin feature/new-stuff`)
5. Open a pull request

