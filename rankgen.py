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
        # format delta to up/down arrows
        if delta > 0:
            # up
            muutos = f"↑{delta}"
        elif delta < 0:
            # down
            muutos = f"↓{-delta}"
        else:
            # unchanged
            muutos = "–"
    else:
        muutos = "uusi"

    ranking.append((nth, muutos, name, i, t, p))

outfile = "ranks.md"
with open(outfile, "w", encoding="utf-8") as fo:
    fo.write("Sija | ↑↓ | Nimi | ID | Turnauksia | Sijoituslukema\n")
    fo.write("-----|----|------|----|------------|---------------\n")

    fo.writelines("{} | {} | {} | {} | {} | {}\n".format(*data) for data in ranking)
