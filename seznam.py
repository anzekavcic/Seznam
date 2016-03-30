seznam = []

pozdrav = raw_input("Ali zelis dodati kaj na seznam? DA / NE: ")
if pozdrav == "DA":
    item = raw_input("Kaj pa? ")
    seznam.append(item)
elif pozdrav == "NE":
    print "Seznam vsebuje: ", seznam