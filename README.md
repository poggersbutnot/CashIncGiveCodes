# Info  <img align="right" src="https://cdn.discordapp.com/avatars/523597014030876672/c764dea3c375986b8d58915d49fe99b8.png"/>
[![poggersbutnot](https://cdn.discordapp.com/avatars/523597014030876672/c764dea3c375986b8d58915d49fe99b8.png)
*Will give almost the entire player-base 3 promotion codes. (I already gave it to 50 users.. lol)*

## Changing ID Limit

```bash
range(1200000)
```

You can change the ID limit by changing the range.

```python
def repeat():
    for i in range(1200000): #Edit this
```

## Code Features
The code checks if your updated to it's latest version, if not. It will send you to this github page for you to consider updating to the latest version:

```python
from requests import get
from webbrowser import open
from sys import exit

QIU = False #quit_if_update

print(get('https://raw.githubusercontent.com/poggersbutnot/CashIncGiveCodes/main/updates').text.replace('\n', ''))
ver = """1.1
"""
if ver != get('https://raw.githubusercontent.com/poggersbutnot/CashIncGiveCodes/main/version').text:
    print("New update available...")
    print("Update "+ get('https://raw.githubusercontent.com/poggersbutnot/CashIncGiveCodes/main/version').text.replace('\n', '') + " is availible.")
    open("https://github.com/poggersbutnot/CashIncGiveCodes")
    if QIU is True:
        exit()
    else:
        pass
    if ver.replace('.', '') > get('https://raw.githubusercontent.com/poggersbutnot/CashIncGiveCodes/main/version').text.replace('.', ''):
        print("So u decided to change the version, but WHY.")
    else:
        pass
else:
    pass
```

## Questions
> Do You Still Mod PG3D?
- Yes, i still do. Im just modding other games, to.
> Is it fast?
- Im gonna be honest, no. Not really, as it has to do *post()* 3 times until it switches to another user.
> Was this hard to make?
- ~~No lol it was easy asf~~

## Game Link
[Cash Inc](https://play.google.com/store/apps/details?id=com.alegrium.cong2&hl=en&gl=US)
    
 

