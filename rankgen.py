vanha_file = "vanha.csv"
uusi_file = "uusi.csv"

with open(vanha_file, encoding="utf-8") as fo:
    vanha = {}
    for line in fo.readlines():
        nth, name, idn, turn, pts = line.strip().split("\t")
        vanha[name] = int(nth)

with open(uusi_file, encoding="utf-8") as fo:
    uusi = []
    for line in fo.readlines():
        nth, name, idn, turn, pts = line.strip().split("\t")
        uusi.append(
            (
                int(nth),
                name,
                idn,
                turn,
                pts,
            )
        )

ranking = []
for nth, name, i, t, p in uusi:
    if name in vanha:
        delta = vanha[name] - nth
    else:
        delta = "uusi"

    ranking.append((nth, delta, name, i, t, p))

outfile = "ranks.md"
with open(outfile, "w", encoding="utf-8") as fo:
    fo.write("Sija | ↑↓ | Nimi | ID | Turnauksia | Sijoituslukema\n")
    fo.write("-----|----|------|----|------------|---------------\n")

    fo.writelines("{} | {} | {} | {} | {} | {}\n".format(*data) for data in ranking)
