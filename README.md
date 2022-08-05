# Simple Spam Scripts

These are a set of scripts written in Python, with assumed compatibility for Python 3.x and above. The intention behind them is to generate spammy text messages, that you can then copy and paste from the text files to your choice of messenger, whether that be WhatsApp, Discord or Telegram. Some of the scripts may have emojis written using the format supported by Discord and WhatsApp Web; use the correct option while running the script. Note that, while the options are designed to be case-insensitive, there is no error handling. I am not responsible for any strong language, mature themes, or otherwise problematic stuff in the scripts/options. Currently, there are only two scripts, but I shall work on more when I'm bored enough.

# spamresponsibly.py

This is a simple script that repeats a string n number times, depending on user input. User first enters a number, then selects a string using a single letter code. For reasons pertaining to GitHub ToS, I cannot mention the options the script gives you for the single letter codes here.

Run it in your folder of choice by using
```bash
$ python3 spamresponsibly.py
```

Output spam is generated in a file called `outputtings.txt` in the working directory; user cannot specify custom filenames or other directories.

# retarded.py

This script chooses from various different copypastas, depending on user input, and outputs the chosen copypasta to a text file named `retarded.txt` in the working directory. User input is a single alphabet, case-insensitive, with no error handling. Proper attribution has been given to the authors of the copypastas.
The options given to the user are

```bash
[V]elo
[C]at
[D]utch
[O]nestone
```

Run the script in your working directory by using
```bash
$ python3 retarded.py
```
User may not specify a custom output directory or different filename for output.
