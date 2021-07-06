from requests import post, get
from threading import Thread
from webbrowser import open
from sys import exit

QIU = False #quit_if_update
codes = ['Seecashinc','CAPITALISTIC', 'Cashinc50k']

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

def repeat():
    for i in range(1200000):
        a = post('https://www.alegrium.com/cash/index.php/promo/code/'+ str(i), data={'PromoCodeForm[promo_code]': codes[0]})
        b = post('https://www.alegrium.com/cash/index.php/promo/code/'+ str(i), data={'PromoCodeForm[promo_code]': codes[1]})
        c = post('https://www.alegrium.com/cash/index.php/promo/code/'+ str(i), data={'PromoCodeForm[promo_code]': codes[2]})
        if 'You can only redeem the same code once' in a.text:
            print("User "+ str(i) + " has already claimed this code: ", str(codes[0]))
        else:
            print("Given Code "+ codes[0] + " to ID:", str(i))
        if 'You can only redeem the same code once' in b.text:
            print("User "+ str(i) + " has already claimed this code: ", str(codes[1]))
        else:
            print("Given Code "+ codes[1] + " to ID:", str(i))
        if 'You can only redeem the same code once' in c.text:
            print("User "+ str(i) + " has already claimed this code: ", str(codes[2]))
        else:
            print("Given Code "+ codes[2] + " to ID:", str(i))

if __name__ == "__main__":
    for i in range(1):
       Thread(target=repeat).start()
