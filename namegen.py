PARTS = {
        "high fantasy": (
            ("a", "e", "i", "o", "u", "y", "ee", "ei", "ie", "ou", "a", "ay",
                "eu", "oi", "ou"),
            ("b", "d", "f", "k", "ch", "g", "l", "ll", "m", "mm", "n", "nn",
                "p", "r", "s", "t", "tt")),
        "dwarven": (
            ("sk", "gn", "gr", "sc", "th", "gl", "g", "br", "w", "b", "tr",
                "kn", "kl", "bl", ""),
            ("a", "e", "i", "o", "u", "y", "ei", "oi", "ai", "ou"),
            ("mm", "n", "ll", "th", "ck", "r", "t", "ng", "nt")),
        "tavern": (
            ("golden", "hanged", "smiling", "red", "green", "blue", "silver",
                "happy", "broken", "round", "thin", "black", "white", 
                "old", "pretty", "wooden", "strong", "sunny", "mended", 
                "healthy", "holy", "dead", "angry", "sick", "mad", "crazy",
                "warm", "hot", "dark", "lost"),
            ("rat", "donkey", "monkey", "ass", "gentleman", "lady", "girl", 
                "boy", "pig", "table", "barrel", "drum", "bottle", "horse",
                "shoe", "cross", "well", "tree", "fox", "scout", "sailor",
                "innkeeper", "vicar", "ghost", "stag", "crown", "fence",
                "maid", "rooster", "bull", "hammer", "axe", "sickle", "door",
                "trumpet", "whistle", "bard", "druid", "warrior", "mage", 
                "thief", "rogue", "traveler", "stranger", "hag", "witch",
                "wizard", "king", "prince", "baron", "duke", "duchess",
                "joker", "garden", "horse", "mount", "elf", "dwarf", "troll"),
            (" ", ), (" and " ,), ("the ",), ("two ", "three ", "twin ",
                "double "), ("s",)),
        "places": (
            ("old", "sunny", "red", "green", "up", "west", "east", "north",
            "south", "dark", "bright", "cold", "warm", "wake", "wet", "dry", 
            "bridge", "sand", "stone", "way", "bay", "moon", "spring", "summer",
            "winter", "fall", "beach", "river", "sun", "petti", "crow", "craw",
            "oak", "pine", "spruce", "palm", "elm", "birch", "maple", "dead"),
            ("vale", "creek", "field", "crest", "lake", "cross", "cliff", 
                "cove", "brook", "spring", "marsh", "swamp", "port", 
                "bridge", "stone", "wall", "town", "beach", "pier", 
                "sands", "peak", "mount", "wood", "woods"),
            ("dur", "brent", "dun", "war", "wan", "bur", "bent", "gris", "den",
                "balt", "wan", "win", "wol", "bul", "chris", "malt", "bolt",
                "man", "lond", "gil", "nor", "cant", "rom", "dorn", "cray",
                "born", "wilt", "wil", "bin", "till", "ill", "bill", "chil",
                "mill", "chur", "elms", "star", "car", "cad"),
            ("wick", "rick", "ham", "chester", "more", "on", "ford", "slow",
            "caster", "bury", "shire", "burn", "way", "slough", "marsh", 
            "ville", "bridge", "stone", "wall", "hill", "pool", "fall",
            "slough", "mouth", "wich", "head", "holm", "helm", "kirk"), (" ",))}

NAME_TYPES = {
        "dwarven": ((0, 1, 2), (0, 1, 2, 1)),
        "high fantasy": [],
        "tavern": ((0, 2, 1), (0, 2, 1), (0, 2, 1), (4, 0, 2, 1),
            (4, 1, 3, 1), (1, 3, 1),
            (4, 1, 3, 4, 1), (4, 5, 1, 6)),
        "places": ((0, 1), (0 ,3), (2, 3), (2, 3, 4, 1))}

SURNAMES = {
        "dwarven": (
            ("iron", "steel", "stone", "tunnel", "oaken", "timber", "flint",
            "iron", "copper", "coal", "mine", "crafts", "strong", "strong",
            "strong", "hard", "master", "thunder", "fire", "hammer",
            "power", "might", "granite", "gold", "silver", "ruby"),
        ("head", "arm", "leg", "fist", "hand", "shield", "hammer", "helm",
            "shaft", "axe", "beard", "nose", "mind", "shanks", "shin", "heel")),
        "high fantasy": (),
        "human": PARTS['places'][2:4]}


# Gernerate all sorts of alternating types for high fantasy names
for i in range(3, 7):
    NAME_TYPES["high fantasy"] += (tuple([(x + 1) % 2 for x in range(i)]),)
    NAME_TYPES['high fantasy'] += (tuple([x % 2 for x in range(i)]),)


from random import sample
import optparse

def generate(t, count):
    ret = []
    for n in range(count):
        name = ""
        name_type = sample(NAME_TYPES[t], 1)[0]

        for i in name_type:
            name += (sample(PARTS[t][i], 1)[0])

        if t == "dwarven":
            name += " %s%s" % (sample(SURNAMES[t][0], 1)[0], 
                    sample(SURNAMES[t][1], 1)[0])
        
        ret.append(name.title())
    return ret

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-n", "--count", dest="ncount", type=int, help="Generate NUMBER names",
            metavar="NUMBER", default="5")
    opts, args = parser.parse_args()
    for nametype in NAME_TYPES.keys():
        print "\n\n-- %s ---:" % nametype.title()
        names = generate(nametype, opts.ncount)
        for name in names:
            print "\t" + name

