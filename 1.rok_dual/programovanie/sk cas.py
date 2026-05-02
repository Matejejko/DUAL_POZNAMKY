import datetime, locale

locale.setlocale(locale.LC_TIME, "sk_SK")
dnesny_den = datetime.datetime.now().strftime("%A")

print("Dnes je " + dnesny_den)