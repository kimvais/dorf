from xml.etree.ElementTree import parse
import re
from collections import defaultdict as ddict
from random import choice

MAXCOST = 60

root = parse("library.xml").getroot()
library = {}
for _ in ("advantage", "skill", "spell"):
    library["%ss" % _] = root.find("%s_list" % _).getchildren()

DATA = { 'Advantage': ddict(list),
        'Disadvantage': ddict(list),
        'Perk': ddict(list),
        'Quirk': ddict(list),
        'Power': ddict(list),
        'Cinematic': ddict(list),
        'Attribute': ddict(list),
        'Language': ddict(list)
        }

for a in library['advantages']:
    name = a.find('name').text

    try:
        categories = [_.text for _ in a.find('categories').findall('category')]
    except:
        categories = list()
    try:
        types = re.findall(r'\w+', a.find('type').text)
    except:
        types = list()

    try:
        cost = int(a.find('base_points').text)
    except:
        cost = 0

    try:
        levelcost = int(a.find('points_per_level').text)
    except:
        levelcost = 0

    try:
        ref = a.find('reference').text
    except:
        ref = ""

    for cat in categories:
        for typ in types:
            try:
                DATA[cat][typ].append((name, cost, levelcost, ref))
            except KeyError:
                print cat, typ

if __name__ == "__main__":
    cost = 0
    while cost < MAXCOST:
        t = choice(('Mental', 'Physical'))
        disari = choice(DATA['Disadvantage'][t])
        cost -= sum(disari[1:3])
        print disari
