# Simple Spam Scripts

These are a set of scripts written in Python, with assumed compatibility for Python 3.x and above. The intention behind them is to generate spammy text messages, that you can then copy and paste from the text files to your choice of messenger, whether that be WhatsApp, Discord or Telegram. Some of the scripts may have emojis written using the format supported by Discord and WhatsApp Web; use the correct option while running the script. Note that, while the options are designed to be case-insensitive, ~~there is no error handling~~ I am not responsible if you bork shizz up. I am not responsible for any strong language, mature themes, or otherwise problematic stuff in the scripts/options. Currently, there are only two scripts, but I shall work on more when I'm bored enough.

## spamresponsibly.py

This is a simple script that repeats a string n number times, depending on user input. User first enters a number, then selects a string using a single letter code. For reasons pertaining to GitHub ToS, I cannot mention the options the script gives you for the single letter codes here.

Run it in your folder of choice by using
```console
user@localmachine:~$ python3 spamresponsibly.py
```

Output spam is generated in a file called `outputtings.txt` in the working directory; user cannot specify custom filenames or other directories.

## retarded.py

This script chooses from various different copypastas, depending on user input, and copies the copypasta to the clipboard for pasting into another app. User input is a single alphabet, case-insensitive, with no error handling. Proper attribution has been given to the authors of the copypastas.
The options given to the user are

```posh
[V]elo
[C]at
[D]utch
[O]nestone
[B]engali
```

Run the script in your working directory by using
```console
user@localmachine:~$ python3 retarded.py
```
Please note that I am developing this on macOS now, so please open an issue if the code does not work on Windows. The code doesn't currently take into account GNU/Linux.
## Frequently Asked Questions (FAQ)
<strong>Q:</strong> I am new to coding and know absolutely nothing/very little about Python. I get a `python3 : The term 'python3' is not recognized as the name of a cmdlet, function, script file, or operable program` error/similar error. Help!\
<strong>A:</strong> Not to worry! This is a very common problem. This is caused by the alias `python3` not being found. Depending on your operating system, this may be due to either Python not being installed by default (Windows/macOS), Python not being added to PATH (Windows/macOS/Linux), or a version of Python that uses the `python` alias instead of `python3`. To better diagnose the issue, try to remember if you installed Python. If you are on Linux, many distros come installed with Python by default. If you are on Windows or macOS however, you will need to install Python before you can proceed. For Windows, to use the python3 alias, it is recommended to install from the Microsoft Store on Windows 10 or higher, and more advanced users can install the latest stable or nightly build from the [Python website](https://www.python.org/). Please note, that if you install from the website, you will need to check the 'Add to PATH' option while installing, and possibly restart your computer/shell/terminal before proceeding any further. macOS users should note that legacy Python 2.7 is installed by default on most macOS builds (I have not checked the developer changelog on macOS Ventura); however, this version of Python is deprecated (in plain English, not supported by the Python devs anymore), is not supported by these scripts, and for your own sanity, you should not use it. See [this](https://www.dataquest.io/blog/installing-python-on-mac/#installing-python-mac) website to know more.\
As stated on that website, if you are running a Mac with an M1 chip, or just Apple silicon in general, you're going to need to install Rosetta to install Python 3.x, to access certain features specific to the Rosetta (Intel) architecture that are simply not found on Apple silicon.\
Finally, regardless of your operating system or distribution, use the following command to check whether you have Python installed:
```console
user@localmachine:~$ python --version
```
or if you installed from the Microsoft Store or another package manager that uses the `python3` alias,
```console
user@localmachine:~$ python3 --version
```
On Linux, depending on your distribution, your package manager (apt, pacman, etc.) should prompt you to install Python if it's not already. In the case of Ubuntu/pop!\_OS you may need to add a custom PPA and then run
```console
user@localmachine:~$ sudo apt update
user@localmachine:~$ sudo apt install python3.11
```
for Python 3.11 for example. Please note that in this case your alias for Python may be different than default. Also note that you will require sudo/superuser permissions on Linux, if outside of a virtual environment, or if you want to add Python to your PATH environment variable.

<strong>Q:</strong> I am something of a noob. I copy-pasted your code and it gives me an error, something about `user@localmachine:~$`. Help!\
<strong>A:</strong> Please do not be alarmed! I put that there to get the proper formatting; however, you need to enter commands excluding the dollar sign and everything before it. You see, that is the way it looks on Linux by default, and to get the proper console formatting that GitHub offers via Markdown, I used that. So for me, for instance that would look something like this in a blank terminal window on pop!\_OS:
```console
pekoxusagikiwi@home:~$
```

<strong>Q:</strong> I am a developer for \[insert modded Discord client here]. Can I port your scripts to my own plugins/bots/self-bots/slash commands?\
<strong>A:</strong> Please note that modded Discord clients violate the [Discord ToS (terms of service)](https://discord.com/terms), as do self-bots. However, in the spirit of FOSS, you may reuse this code with proper attribution as per the license; however, you must add a disclaimer of non-liability for any damages, as well a link back to this section of my README.MD in your README.MD or other readme/license files. In the case of copypastas/other text that is not of my own creation, please also provide proper attribution to the persons involved in creating them, like I have done. Don't steal others' work!

<strong>Q:</strong> I have another question not answered here/wish to collaborate with you on a project. Where do I message?\
<strong>A:</strong> In case you have a question I have not answered here, please send an email to the email address linked in my GitHub bio, and I will try to answer it as soon as I can. Since I am a full-time university student, and also work part-time and occasionally freelance, and also because of Gmail's weird spam filters (the address in my bio is an alias for my real Gmail address), it may take longer for me to answer your query. If you wish to collaborate, I am flattered, but I am still learning how to code, so I may be more of a liability than an asset; however, if you are willing to provide training/training resources/monetary compensation + work experience, I am all ears, and the same email inbox is open for you too, naturally; however, please preface your subject line with the following tag: `[IMPORTANT/GitHub misc]` so I know it's not a query, spam or otherwise a message simply not relevant to this repository or coding in general.
