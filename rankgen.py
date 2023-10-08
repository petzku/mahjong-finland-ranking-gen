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


outfile = "ranks.html"

with open(outfile, "w", encoding="utf-8") as fo:
    # heading part
    fo.write(
        """<tr style="height: 15.0pt;">
    <td class="xl92" style="width: 21pt; height: 15.0pt;" width="28" height="20"><strong>Sija</strong></td>
    <td class="xl91" style="width: 23pt;" width="30"><strong>↑↓</strong></td>
    <td class="xl17" style="width: 121pt;" width="170"><strong>Nimi</strong></td>
    <td class="xl91" style="width: 23pt;" width="30"><strong>ID</strong></td>
    <td class="xl17" style="width: 55pt;" width="73"><strong>Turnauksia</strong></td>
    <td class="xl17" style="width: 75pt;" width="100"><strong>Sijoituslukema</strong></td>
</tr>\n\n"""
    )

    for nth, delta, name, idn, tourns, pts in ranking:
        # format delta to up/down arrows as applicable
        if delta == "uusi":
            # new player
            muutos = '<span style="color: green;">uusi</span>'
        elif delta > 0:
            # up
            muutos = f'<span style="color: green;">↑{delta}</span>'
        elif delta < 0:
            # down
            muutos = f'<span style="color: red;">↓{-delta}</span>'
        else:
            # unchanged
            muutos = "–"

        fo.write(
            f"""<tr style="height: 15.0pt;">
    <td class="xl92" style="height: 15.0pt;" height="20"><strong>{nth}</strong></td>
    <td class="xl91">{muutos}</td>
    <td class="xl17">{name}</td>
    <td class="xl91">{idn}</td>
    <td class="xl91" style="text-align: center;">{tourns}</td>
    <td class="xl91" style="text-align: center;">{pts.replace(".", ",")}</td>
</tr>\n"""
        )
