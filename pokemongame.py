pokelist = ["audino", "bagon", "baltoy", "banette", "bidoof", "braviary",
            "bronzor", "carracosta", "charmeleon", "cresselia", "croagunk",
            "darmanitan", "deino", "emboar", "emolga", "exeggcute", "gabite",
            "girafarig", "gulpin", "haxorus", "heatmor", "heatran", "ivysaur",
            "jellicent", "jumpluff", "kangaskhan", "kricketune", "landorus",
            "ledyba", "loudred", "lumineon", "lunatone", "machamp",
            "magnezone", "mamoswine", "nosepass", "petilil", "pidgeotto",
            "pikachu", "pinsir", "poliwrath", "poochyena", "porygon2",
            "porygonz", "registeel", "relicanth", "remoraid", "rufflet",
            "sableye", "scolipede", "scrafty", "seaking", "sealeo", "silcoon",
            "simisear", "snivy", "snorlax", "spoink", "starly", "tirtouga",
            "trapinch", "treecko", "tyrogue", "vigoroth", "vulpix", "wailord",
            "wartortle", "whismur", "wingull", "yamask"]


def firstchar(list):
    firstcharlist = []
    for word in list:
        firstcharlist.append(word[0])
    print(firstcharlist)
    return firstcharlist


def lastchar(list):
    lastcharlist = []
    for word in list:
        lastcharlist.append(word[-1])
    print(lastcharlist)
    return lastcharlist


def gamegenerator(list):
    firstcharlist = firstchar(list)
    lastcharlist = lastchar(list)
    for word in list:
        worklist = list[:]
        indexpointer = list.index(word)
        
