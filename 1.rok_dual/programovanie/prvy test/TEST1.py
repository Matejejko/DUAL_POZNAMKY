import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, "sk_SK")

dnes = datetime.now()
fomatovanyCas = dnes.strftime("Dnes je %A, %d. %B %Y\n")

print(fomatovanyCas)