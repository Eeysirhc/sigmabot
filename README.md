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

Valid input: `erg`, `ergopad`, `exle`, `paideia`, `neta`, `sigrsv`, `terahertz`, `egio`, `comet`

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
- [ ] Remove dependency on CSV file for initial tokens list
- [ ] Expand tokens list 
- [ ] Streamline code efficiency (see comments)
- [x] Plot $erg address amount over time 

