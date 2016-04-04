izdelki_in_cene = {"mleko": float(1.25), "kruh": float(2.50), "jajca": float(3.35), "moka":float(0.95), "sladkor":float(0.80)}
def e_blagajna(item):
    for izdelek, cena in izdelki_in_cene.iteritems():
        if item == izdelek:
            return cena
    print "Izdelek ni na voljo"
item = raw_input("Kateri izdelek te zanima? ")
print "Cena izdleka je: " , e_blagajna(item)