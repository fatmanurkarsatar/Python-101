#sets

meyveler = { "elma","kiraz","kavun","üzüm" }
sebzeler = { "bezelye","soğan"}


sonuc = meyveler
# sonuc = meyveler[0] indekslenemez
sonuc = "elma" in meyveler
meyveler.add("çilek")
meyveler.update(["vişne","karpuz"])


sonuc = len(meyveler)
# meyveler.remove("karpuzz") #keyError
# meyveler.discard('karpuz')

# sonuc = meyveler.pop()
# meyveler.clear()

sonuc = meyveler.union(sebzeler)
# sonuc = meyveler

# for x in meyveler:
#     print(x)


print(sonuc)