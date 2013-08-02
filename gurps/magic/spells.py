from _collections import defaultdict
import csv
from math import log
from random import shuffle
import dice
import gdocs

__author__ = 'kparviainen'

CHARNAME = "Kaiuksen charru"
MAGERYLEVELS = {1: (1,0), 2: (2, 1, 1), 3: (3, 2, 1, 1, 1), 4: (4, 2, 2, 1, 1, 1, 1)}
#MYCOLLEGES = (('Communication', 2), ('Water', 1), ('Protection', 1))
#MYCOLLEGES = (('Body Control', 3), ("Movement", 2), ("Fire", 1), ("Enchantment", 1), ("Weather", 1))
#MYCOLLEGES = (('Meta',3), ('Animal', 2), ('Plant', 2), ('Protection', 1), ('Communication', 1))
#MYCOLLEGES = (('Air', 2), ('Light', 1), ('Protection', 1))
#MYCOLLEGES = (('Light', 4), ('Meta', 2), ('Mind Control', 2), ('Earth', 1),
        #('Sound', 1), ('Necromancy', 1), ('Gate', 1))
#MYCOLLEGES = (('Knowledge', 2), ('Body Control', 1), ('Fire', 1))
MYCOLLEGES = (('Illusion', 4), ('Fire', 2), ('Body Control', 2), ('Meta', 1), ('Sound', 1), ('Knowledge', 1), ('Necromancy', 1))

colleges = { 'Air': [],
             'Animal': [],
             'Body Control': [],
             'Communication': [],
             'Earth': [],
             'Enchantment': [],
             'Fire': [],
             'Food': [],
             'Gate': [],
             'Healing': [],
             'Illusion': [],
             'Knowledge': [],
             'Light': [],
             'Meta': [],
             'Mind Control': [],
             'Making': [],
             'Movement': [],
             'Necromancy': [],
             'Plant': [],
             'Protection': [],
             'Sound': [],
             'Technology': [],
             'Water': [],
             'Weather': []}

colours = {'Black': ('Earth', 'Gate', 'Light', 'Meta', 'Mind Control', 'Necromancy', 'Sound'),
           'Blue': ('Air', 'Gate', 'Meta', 'Mind Control', 'Movement', 'Water', 'Weather'),
           'Green': ('Animal', 'Communication', 'Earth', 'Illusion', 'Meta', 'Plant', 'Protection', 'Water'),
           'Red': ('Body Control', 'Fire', 'Illusion', 'Knowledge', 'Meta', 'Necromantic', 'Sound'),
           'White': ('Air', 'Communication', 'Enchantment', 'Knowledge', 'Light', 'Meta', 'Protection'),
           'Yellow': ('Animal', 'Body Control', 'Enchantment', 'Fire', 'Movement', 'Plant', 'Weather')}

with open("spells.csv") as fp:
    for spell in csv.reader(fp.readlines()):
        colleges[spell[0]].append((spell[2], spell[1]))

if __name__ == "__main__":
    spell_lists = defaultdict(list)
    for college, magery in MYCOLLEGES:
        for s in colleges[college]:
            spell, prcount = (s[0], int(s[1]))
            if prcount > 0:
                prcount = int(log(prcount,2))
            skill = 10 - prcount + magery
            roll = sum(dice.roll('3d6'))
            if roll > 17 or roll - 10 >= skill:
                # Critical failure, can not learn this spell
                print("%s failed with %d" % (spell, roll))
                continue
            elif roll <= skill:
                idx = 0
            else:
                idx = roll - skill
            spell_lists[idx].append((spell, college, -prcount))

    for v in spell_lists.values():
        shuffle(v)
    spell_list = []
    [spell_list.extend(l) for l in spell_lists.values()]
    docname = "Spellbook of %s" % CHARNAME
    with open("%s.csv" % docname, "wb") as f:
        writer = csv.writer(f)
        writer.writerow(("Position", "Spell", "College", "=COUNTIF(E2:E%d,0)" % (len(spell_list)+1),
                         "=SUM(E2:E%d)" % (len(spell_list)+1), "=ROUND(4+LOG(E1,2)-D1)"))
        for n, (name, college, bonus) in enumerate(spell_list):
            writer.writerow((n+1, name, college, bonus, None, "=SUM(E2:E%d)+1" % (n+2)))
    gdocs.upload(docname)

