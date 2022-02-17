from requests import post as _post
from sys import argv as _argv

__all__ = ('codes', 'repeat')

logging = False
if len(_argv) > 1:
    from time import time as _time
    logging = True
    _cash_file = open('Log_%i_CashInc.log' % round(_time()), 'a')
    del _time

del _argv

codes = ['Seecashinc', 'CAPITALISTIC', 'Cashinc50k']


def repeat():
    i = 0
    while True:
        i += 1
        for n in range(len(codes)):
            a = _post(f"https://www.alegrium.com/cash/index.php/promo/code/{i}",
                      data={'PromoCodeForm[promo_code]': codes[n]})
            if 'You can only redeem the same code once' in a.text:
                if logging:
                    _cash_file.write(
                        f"User {i} has already claimed the code {codes[n]}\n"
                    )
                    _cash_file.flush()
                print("User %i has already claimed the code %s" %
                      (i, codes[n]))
            else:
                if logging:
                    _cash_file.write(
                        "Given Code {} to user {}\n".format(codes[n], i)
                    )
                    _cash_file.flush()
                print("Given Code %s to user %i" % (codes[n], i))


if __name__ == "__main__":
    repeat()
