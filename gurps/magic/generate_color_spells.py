from xml.etree.ElementTree import parse
import re
from collections import defaultdict as ddict
from random import choice
import csv
import sys

MAXCOST = 60

root = parse("library.xml").getroot()
library = {}
for _ in ("advantage", "skill", "spell"):
    library["%ss" % _] = root.find("%s_list" % _).getchildren()


SPELLS = {}
lens = ddict(int)
COLORS = ('Black', 'Gray', 'White', 'Yellow', 'Red', 'Purple', 'Blue', 'Green',
    'Brown')

for spell in library["spells"]:
   SPELLS[spell.find("name").text] = spell

if __name__ == "__main__":
    writer = csv.writer(open("color_spells.csv", "wb"))
    writer.writerow(["Name", "Prereqs"] + list(COLORS) + ["ref"])
    with open("colors.csv") as fp:
            for spell in csv.reader(fp.readlines()):
                new = list()
                if len(spell) == 0: continue
                name = spell[0]
                if name.endswith(" (VH)"):
                    name = name[:-5]
                if name.endswith("/TL"):
                    name = name[:-3]
                try:
                    ref = SPELLS[name].find("reference").text
                except KeyError:
                    sys.stderr.write("%s not found!\n" % name)
                    continue
                new.append(name)
                new.append(spell[1])
                for _ in COLORS:
                    if _ in spell[5:8] or "All" in spell[5:8]:
                        new.append("1")
                    elif ("(%s)" % _) in spell[5:8]:
                        new.append("-1")
                    else:
                        new.append("")
                if len(spell) > 8:
                    spell[8] = ref
                elif len(spell) == 5:
                    spell = spell + ["","",""]
                    spell.append(ref)
                new.append(ref)
                print new
                writer.writerow(new)

