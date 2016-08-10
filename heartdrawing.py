stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
loot = ["gold coin", "gold coin", "dagger", "ruby", "gold coin"]


def inventory_listing(stuff):
    totalitems = 0
    print("Inventory\n----------------\n")
    for k, v in stuff.items():
        print(k + ": " + str(v) + " unit(s)")
        totalitems += v
    print("\n-----------------\nTotal: " + str(totalitems))


def addtoinv(inventory, loot):
    for item in loot:
        inventory.setdefault(item, 0)
        inventory[item] += 1

addtoinv(stuff, loot)
inventory_listing(stuff)
