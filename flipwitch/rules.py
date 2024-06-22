import typing
from .locations import location_table
from worlds.generic.Rules import add_rule, set_rule, forbid_item
from BaseClasses import LocationProgressType
from .regions import connect

def set_rules(self, world, player:int):
    names: typing.Dict[str, int] = {}

    #Witchy Woods
    connect(world, player, names, "Menu", "Sensei's Hut", lambda state:True)
    connect(world, player, names, "Sensei's Hut", "Sensei's Hut BBubble", lambda state:
    BBubble(state, player))
    connect(world, player, names, "Sensei's Hut", "Beatrix", lambda state:
    state.has("Fairy Bubble", player, 1))

    #Quest rewards
    connect(world, player, names, "Beatrix", "Quest Upgrade 1", lambda state:
    state.has("Completed Quests", player, 4))
    connect(world, player, names, "Quest Upgrade 1", "Quest Upgrade 2", lambda state:
    state.has("Completed Quests", player, 8))
    connect(world, player, names, "Quest Upgrade 2", "Quest Upgrade 3", lambda state:
    state.has("Completed Quests", player, 12))
    connect(world, player, names, "Quest Upgrade 3", "Quest Upgrade 4", lambda state:
    state.has("Completed Quests", player, 16))
    connect(world, player, names, "Quest Upgrade 4", "Quest Upgrade 5", lambda state:
    state.has("Completed Quests", player, 20))
    connect(world, player, names, "Quest Upgrade 5", "Quest Upgrade 6", lambda state:
    state.has("Completed Quests", player, 24))
    connect(world, player, names, "Quest Upgrade 6", "Quest Upgrade 7", lambda state:
    state.has("Completed Quests", player, 28))
    connect(world, player, names, "Quest Upgrade 7", "Quest Upgrade 8", lambda state:
    state.has("Completed Quests", player, 32))
    connect(world, player, names, "Quest Upgrade 8", "Quest Upgrade 9", lambda state:
    state.has("Completed Quests", player, 36))
    connect(world, player, names, "Quest Upgrade 9", "Quest Upgrade 10", lambda state:
    state.has("Completed Quests", player, 40))

    #Witchy Woods cont.
    connect(world, player, names, "Sensei's Hut", "Past The Hut", lambda state:True)
    connect(world, player, names, "Past The Hut", "Secret Cave", lambda state:
    BBubble(state, player))
    connect(world, player, names, "Past The Hut", "Genesis", lambda state:True)
    connect(world, player, names, "Genesis", "Genesis Promo", lambda state:
    state.has("Gacha Coin", player, 44))
    connect(world, player, names, "Genesis", "Belle", lambda state:
    state.has("Progressive Belle Item", player, 1))
    connect(world, player, names, "Genesis", "Rundown House", lambda state:True)
    connect(world, player, names, "Genesis", "Rundown House Save", lambda state: True)
    connect(world, player, names, "Rundown House Save", "Mimi", lambda state:
    state.has("Mimic Chest Key", player, 1))
    connect(world, player, names, "Rundown House Save", "Mimi Hidden Chest", lambda state:True)
    connect(world, player, names, "Mimi Hidden Chest", "Goblin Apartment", lambda state:
    state.has("Progressive Gobliana Item", player, 3))
    connect(world, player, names, "Mimi Hidden Chest", "Red Wine", lambda state:
    AFeathers(state, player))
    connect(world, player, names, "Mimi Hidden Chest", "Mimic Chest Key Room", lambda state:True)
    connect(world, player, names, "Mimic Chest Key Room", "Man Cave", lambda state:
    BBubble(state, player))
    connect(world, player, names, "Mimic Chest Key Room", "Before Great Fairy", lambda state:
    AFeathers(state, player))
    connect(world, player, names, "Mimic Chest Key Room", "Belle's Cowbell", lambda state:True)
    connect(world, player, names, "Belle's Cowbell", "Great Fairy", lambda state:
    state.has("Chaos Key Piece", player, 1))


    #Goblin Caves(WW)
    connect(world, player, names, "Belle's Cowbell", "Man Cave", lambda state:
    BBubble(state, player) and state.has("Progressive Gobliana Item", player, 1))
    connect(world, player, names, "Belle's Cowbell", "Past Man Cave", lambda state:
    BBubble(state, player))
    connect(world, player, names, "Past Man Cave", "Gerry G. Atric", lambda state:
    BBubble(state, player))
    connect(world, player, names, "Gerry G. Atric", "Hidden Alcove", lambda state:
    BBubble(state, player))
    connect(world, player, names, "Hidden Alcove", "Beside Flip Platform", lambda state:
    BubbleAndFeathers(state, player))
    connect(world, player, names, "Hidden Alcove", "Gobliana", lambda state:
    BBubble(state, player))
    connect(world, player, names, "Gobliana", "Gobliana 2", lambda state:
    BBubble(state, player) and state.has("Progressive Gobliana Item", player, 2))
    connect(world, player, names, "Gobliana", "After Chaos Fight", lambda state:
    BBubble(state, player))
    connect(world, player, names, "After Chaos Fight", "WW Boss Key Room", lambda state:
    BBubble(state, player))
    connect(world, player, names, "WW Boss Key Room", "WW Hidden Spring Room", lambda state:
    BBubble(state, player))
    connect(world, player, names, "WW Hidden Spring Room", "Fairy Chest", lambda state:
    BBubble(state, player))
    connect(world, player, names, "Fairy Chest", "Fairy Quest", lambda state:
    BBubble(state, player) and state.has("Fairy Costume", player, 1))
    connect(world, player, names, "Fairy Chest", "Goblin Queen", lambda state:
    BBubble(state, player) and GoblinQKey(state, player))
    connect(world, player, names, "Goblin Queen", "Goblin Princess", lambda state:
    BBubble(state, player) and GoblinQKey(state, player) and state.has("Goblin Costume", player, 1))
    connect(world, player, names, "Goblin Queen", "WW Post Fight", lambda state:
    BubbleAndSlime(state, player) and GoblinQKey(state, player))


    #City
    connect(world, player, names, "Goblin Queen", "Toilet", lambda state:
            BBubble(state, player))
    connect(world, player, names, "Toilet", "Toilet Coin", lambda state:
            AFeathers(state, player) or DWings(state, player))

    #Cabaret Cafe
    connect(world, player, names, "Toilet", "Cabaret Cafe Chest", lambda state:True)


    #Cabaret Cafe Gacha
    connect(world, player, names, "Cabaret Cafe Chest", "Animal Girl Gacha 1", lambda state:
            cafereq(state, player) and GachaTime(state, player, 1))
    connect(world, player, names, "Animal Girl Gacha 1", "Animal Girl Gacha 2", lambda state:
            cafereq(state, player) and GachaTime(state, player, 2))
    connect(world, player, names, "Animal Girl Gacha 2", "Animal Girl Gacha 3", lambda state:
            cafereq(state, player) and GachaTime(state, player, 3))
    connect(world, player, names, "Animal Girl Gacha 3", "Animal Girl Gacha 4", lambda state:
            cafereq(state, player) and GachaTime(state, player, 4))
    connect(world, player, names, "Animal Girl Gacha 4", "Animal Girl Gacha 5", lambda state:
            cafereq(state, player) and GachaTime(state, player, 5))
    connect(world, player, names, "Animal Girl Gacha 5", "Animal Girl Gacha 6", lambda state:
            cafereq(state, player) and GachaTime(state, player, 6))
    connect(world, player, names, "Animal Girl Gacha 6", "Animal Girl Gacha 7", lambda state:
            cafereq(state, player) and GachaTime(state, player, 7))
    connect(world, player, names, "Animal Girl Gacha 7", "Animal Girl Gacha 8", lambda state:
            cafereq(state, player) and GachaTime(state, player, 8))
    connect(world, player, names, "Animal Girl Gacha 8", "Animal Girl Gacha 9", lambda state:
            cafereq(state, player) and GachaTime(state, player, 9))
    connect(world, player, names, "Animal Girl Gacha 9", "Animal Girl Gacha 10", lambda state:
            cafereq(state, player) and GachaTime(state, player, 10))

    #Cabaret Cafe Rover
    connect(world, player, names, "Cabaret Cafe Chest", "Boned", lambda state:
            cafereq(state, player))

    #Rover q
    connect(world, player, names, "Boned", "Legendary Chewtoy", lambda state:
            cafereq(state, player) and state.has("Rover 2", player, 1)
            and state.has("Legendary Halo", player, 1))

    #Cabaret Cafe Belle
    connect(world, player, names, "Cabaret Cafe Chest", "Delicious Milk", lambda state:
            cafereq(state, player))

    #Belle q
    connect(world, player, names, "Delicious Milk", "Deluxe Milkshake", lambda state:
            cafereq(state, player) and state.has("Progressive Belle Item", player, 3))
    connect(world, player, names, "Deluxe Milkshake", "Cherry Apt Key", lambda state:
            cafereq(state, player) and state.has("Progressive Belle Item", player, 3)
            and state.has("Belle 2", player, 1))
    connect(world, player, names, "Cherry Apt Key", "Rat Problem", lambda state:
            cafereq(state, player) and state.has("Progressive Belle Item", player, 4))


    #Cabaret Cafe M&C
    connect(world, player, names, "Cabaret Cafe Chest", "Ghost Hunters", lambda state:
            cafereq(state, player))

    #M&C q
    connect(world, player, names, "Ghost Hunters", "Haunted Bathroom", lambda state:
            cafereq(state, player) and state.has("Milk & Cream 2", player, 1)
            and SForm(state, player))
    connect(world, player, names, "Haunted Bathroom", "Ectogasm", lambda state:
            cafereq(state, player) and state.has("Milk & Cream 3", player, 1)
            and state.has("Cat Costume", player, 1))

    #Cabaret Cafe M
    connect(world, player, names, "Cabaret Cafe Chest", "Jelly Mushroom", lambda state:
            cafereq(state, player) and state.has("Blue Jelly Mushroom", player, 1))

    #Cabaret Cafe BB
    connect(world, player, names, "Cabaret Cafe Chest", "Booze Bunny", lambda state:
            cafereq(state, player) and state.has("Red Wine", player, 1))

    #Cabaret Cafe HW
    connect(world, player, names, "Booze Bunny", "Help Wanted", lambda state:
            cafereq(state, player) and state.has("Rover 3", player, 1)
            and state.has("Janic 1", player, 1) and state.has("Belle 3", player, 1)
            and state.has("Milk & Cream 3", player, 1) and state.has("Merchant 1", player, 1))

    #Cabaret VIP
    connect(world, player, names, "Cabaret Cafe Chest", "VIP Chest", lambda state:
            cafereq(state, player) and state.has("Janic 2", player, 1))

    #City cont.
    connect(world, player, names, "Toilet", "Unmarked House Bubble", lambda state:True)

    #Unmarked House Gacha
    connect(world, player, names, "Unmarked House Bubble", "Angel and Demon Gacha 1", lambda state:
            GachaTime(state, player, 1))
    connect(world, player, names, "Angel and Demon Gacha 1", "Angel and Demon Gacha 2", lambda state:
            GachaTime(state, player, 2))
    connect(world, player, names, "Angel and Demon Gacha 2", "Angel and Demon Gacha 3", lambda state:
            GachaTime(state, player, 3))
    connect(world, player, names, "Angel and Demon Gacha 3", "Angel and Demon Gacha 4", lambda state:
            GachaTime(state, player, 4))
    connect(world, player, names, "Angel and Demon Gacha 4", "Angel and Demon Gacha 5", lambda state:
            GachaTime(state, player, 5))
    connect(world, player, names, "Angel and Demon Gacha 5", "Angel and Demon Gacha 6", lambda state:
            GachaTime(state, player, 6))
    connect(world, player, names, "Angel and Demon Gacha 6", "Angel and Demon Gacha 7", lambda state:
            GachaTime(state, player, 7))
    connect(world, player, names, "Angel and Demon Gacha 7", "Angel and Demon Gacha 8", lambda state:
            GachaTime(state, player, 8))
    connect(world, player, names, "Angel and Demon Gacha 8", "Angel and Demon Gacha 9", lambda state:
            GachaTime(state, player, 9))
    connect(world, player, names, "Angel and Demon Gacha 9", "Angel and Demon Gacha 10", lambda state:
            GachaTime(state, player, 10))

    #City cont.
    connect(world, player, names, "Unmarked House Bubble", "Item Shop", lambda state: True)
    connect(world, player, names, "Item Shop", "Item Shop Roof", lambda state: True)

    #Item Shop Gacha
    connect(world, player, names, "Item Shop Roof", "Monster Girl Gacha 1", lambda state:
            GachaTime(state, player, 1))
    connect(world, player, names, "Monster Girl Gacha 1", "Monster Girl Gacha 2", lambda state:
            GachaTime(state, player, 2))
    connect(world, player, names, "Monster Girl Gacha 2", "Monster Girl Gacha 3", lambda state:
            GachaTime(state, player, 3))
    connect(world, player, names, "Monster Girl Gacha 3", "Monster Girl Gacha 4", lambda state:
            GachaTime(state, player, 4))
    connect(world, player, names, "Monster Girl Gacha 4", "Monster Girl Gacha 5", lambda state:
            GachaTime(state, player, 5))
    connect(world, player, names, "Monster Girl Gacha 5", "Monster Girl Gacha 6", lambda state:
            GachaTime(state, player, 6))
    connect(world, player, names, "Monster Girl Gacha 6", "Monster Girl Gacha 7", lambda state:
            GachaTime(state, player, 7))
    connect(world, player, names, "Monster Girl Gacha 7", "Monster Girl Gacha 8", lambda state:
            GachaTime(state, player, 8))
    connect(world, player, names, "Monster Girl Gacha 8", "Monster Girl Gacha 9", lambda state:
            GachaTime(state, player, 9))
    connect(world, player, names, "Monster Girl Gacha 9", "Monster Girl Gacha 10", lambda state:
            GachaTime(state, player, 10))

    #City cont.
    connect(world, player, names, "Item Shop Roof", "Fashion Shop", lambda state:True)
    connect(world, player, names, "Fashion Shop", "Clinic", lambda state:
            state.has("Nurse Costume", player, 1))
    connect(world, player, names, "Fashion Shop", "Rover", lambda state:
            GForm(state, player))
    connect(world, player, names, "Fashion Shop", "Ancient Being Chest", lambda state:True)
    connect(world, player, names, "Ancient Being Chest", "Ancient Being", lambda state:
            state.has("Dominating Costume", player, 1))
    connect(world, player, names, "Ancient Being Chest", "Below Cemetary", lambda state:
            MScale(state, player) and ChaosKey(state, player, 1))
    connect(world, player, names, "Ancient Being Chest", "Ghost Castle Key", lambda state:
            BBubble(state, player) and ChaosKey(state, player, 1))
    connect(world, player, names, "Ancient Being Chest", "Bunny Club Quest", lambda state:
            state.has("Bunny Costume", player, 1))
    connect(world, player, names, "Ancient Being Chest", "Silky Slime Quest", lambda state:
            state.has("Silky Slime", player, 1))
    connect(world, player, names, "Ancient Being Chest", "Legs Office Key", lambda state:
            state.has("Goblin 1 Complete Flag", player, 1))
    connect(world, player, names, "Ancient Being Chest", "Emotional Baggage", lambda state:
            state.has("Progressive Gobliana Item", player, 4))
    connect(world, player, names, "Ancient Being Chest", "Dirty Debut", lambda state:
            state.has("Goblin 2", player, 1) and BubbleAndWings(state, player) and GForm(state, player))

    #Kyoni's Shop

    #Kyoni's Shop Gacha
    connect(world, player, names, "Ancient Being Chest", "Bunny Girl Gacha 1", lambda state:
            GachaTime(state, player, 1))
    connect(world, player, names, "Bunny Girl Gacha 1", "Bunny Girl Gacha 2", lambda state:
            GachaTime(state, player, 2))
    connect(world, player, names, "Bunny Girl Gacha 2", "Bunny Girl Gacha 3", lambda state:
            GachaTime(state, player, 3))
    connect(world, player, names, "Bunny Girl Gacha 3", "Bunny Girl Gacha 4", lambda state:
            GachaTime(state, player, 4))
    connect(world, player, names, "Bunny Girl Gacha 4", "Bunny Girl Gacha 5", lambda state:
            GachaTime(state, player, 5))
    connect(world, player, names, "Bunny Girl Gacha 5", "Bunny Girl Gacha 6", lambda state:
            GachaTime(state, player, 6))
    connect(world, player, names, "Bunny Girl Gacha 6", "Bunny Girl Gacha 7", lambda state:
            GachaTime(state, player, 7))
    connect(world, player, names, "Bunny Girl Gacha 7", "Bunny Girl Gacha 8", lambda state:
            GachaTime(state, player, 8))
    connect(world, player, names, "Bunny Girl Gacha 8", "Bunny Girl Gacha 9", lambda state:
            GachaTime(state, player, 9))
    connect(world, player, names, "Bunny Girl Gacha 9", "Bunny Girl Gacha 10", lambda state:
            GachaTime(state, player, 10))

    #Kyoni's Shop cont.
    connect(world, player, names, "Ancient Being Chest", "Belle's Milkshake", lambda state:
            state.has("Progressive Belle Item", player, 2) and cafereq(state, player))
    #Kyoni Quests
    connect(world, player, names, "Ancient Being Chest", "Devilicious", lambda state:
            state.has("Belle 2", player, 1) and state.has("Progressive Kyoni Item", player, 1))
    connect(world, player, names, "Devilicious", "What's a Daikon", lambda state:
            state.has("Kyoni 1", player, 1) and state.has("Progressive Kyoni Item", player, 2))

    #City cont.
    connect(world, player, names, "Ancient Being Chest", "Banana Chest", lambda state:True)
    connect(world, player, names, "Banana Chest", "Momo Pass", lambda state:True)

    #Momo quest
    connect(world, player, names, "Momo Pass", "Out of Service", lambda state:
            state.has("Momo Server Admin Password", player, 1))
    connect(world, player, names, "Out of Service", "Girl Gallery", lambda state:
            state.has("Momo Server Admin Password", player, 1))
    connect(world, player, names, "Girl Gallery", "Boy Gallery", lambda state:
            state.has("Momo Server Admin Password", player, 1) and BBubble(state, player))

    #City cont.
    connect(world, player, names, "Momo Pass", "Priestess", lambda state:
            state.has("Nun Costume", player, 1))
    connect(world, player, names, "Momo Pass", "Priest", lambda state:
            state.has("Priest Costume", player, 1))
    connect(world, player, names, "Momo Pass", "Dusty", lambda state:
            BubbleAndFeathers(state, player))
    connect(world, player, names, "Momo Pass", "Behind Alley", lambda state:
            SForm(state, player))
    connect(world, player, names, "Momo Pass", "City Chaos", lambda state:
            state.has("Abandoned Apartment Key", player, 1))
    connect(world, player, names, "Momo Pass", "Abandoned Home 02", lambda state:
            WingsAndFeathers(state, player))
    connect(world, player, names, "Momo Pass", "Abandoned Home 01", lambda state:
            GForm(state, player))
    connect(world, player, names, "Momo Pass", "Abandoned Home 6", lambda state:
            MScale(state, player))
    connect(world, player, names, "Momo Pass", "Abandoned Home Green", lambda state:
            SForm(state, player))
    connect(world, player, names, "Momo Pass", "Fungal Key", lambda state:
            state.has("Pigman Costume", player, 1))
    connect(world, player, names, "Momo Pass", "Tatil Tale", lambda state:
            state.has("Progressive Tatil Item", player, 2))
    connect(world, player, names, "Momo Pass", "Maid Contract", lambda state:
            state.has("Maid Costume", player, 1) and state.has("Pigman Costume", player, 1))
    connect(world, player, names, "Momo Pass", "Signing Bonus", lambda state:
            state.has("Maid Contract", player, 1) and state.has("Maid Costume", player, 1))
    connect(world, player, names, "Momo Pass", "Lone House", lambda state:
            AFeathers(state, player))

    #ShadySewer

    connect(world, player, names, "Momo Pass", "Pipe Chest", lambda state:
            SForm(state, player))
    connect(world, player, names, "Pipe Chest", "Side Coin", lambda state:
            SForm(state, player))
    connect(world, player, names, "Side Coin", "Side Chest", lambda state:
            FeatherAndSlime(state, player))
    connect(world, player, names, "Pipe Chest", "Sewer Shop", lambda state:
            SForm(state, player))
    connect(world, player, names, "Sewer Shop", "Sewer Gauntlet HP", lambda state:
            SForm(state, player))
    connect(world, player, names, "Sewer Gauntlet HP", "Sewer Gauntlet Chest", lambda state:
            FeatherAndSlime(state, player))
    connect(world, player, names, "Sewer Gauntlet HP", "Rat Costume Room", lambda state:
            SForm(state, player))
    connect(world, player, names, "Rat Costume Room", "Ratchel Coin", lambda state:
            SForm(state, player))
    connect(world, player, names, "Ratchel Coin", "Ratchel", lambda state:
            SForm(state, player) and state.has("Rat Costume", player, 1))
    connect(world, player, names, "Ratchel Coin", "Dr Witch", lambda state:
            SForm(state, player))
    connect(world, player, names, "Dr Witch", "Dr Witch Tutorial", lambda state:
            SForm(state, player) and MScale(state, player))


    #GhostCastle
    connect(world, player, names, "Momo Pass", "Below GC Entrance", lambda state:
            ChaosKey(state, player, 1) and GForm(state, player))
    connect(world, player, names, "Momo Pass", "Ghost Form", lambda state:
            ChaosKey(state, player, 1) and state.has("Secret Garden Key", player, 1))
    connect(world, player, names, "Momo Pass", "GC Ground Slime", lambda state:
            ChaosKey(state, player, 1) and state.has("Ghostly Castle Key", player, 1) and SForm(state, player))
    connect(world, player, names, "GC Ground Slime", "GC Raised Slime", lambda state:
            (ChaosKey(state, player, 1) and state.has("Ghostly Castle Key", player, 1) and SForm(state, player))
            and (BBubble(state, player) or AFeathers(state, player)))
    connect(world, player, names, "Ghost Form", "Ladder Coin", lambda state:
            (Ghost1(state, player) and AFeathers(state, player)) or (Ghost2(state, player) and AFeathers(state, player)))
    connect(world, player, names, "Ghost Form", "Hidden Ledge", lambda state:
            Ghost1(state, player) or Ghost2(state, player))
    connect(world, player, names, "Hidden Ledge", "GC Flip Magic Platform", lambda state:
            (Ghost1(state, player)) or (Ghost2(state, player) and BBubble(state, player)))
    connect(world, player, names, "GC Flip Magic Platform", "Panty Raid", lambda state:
            (GhostR1(state, player) and state.has("Bundle of Clothes", player, 1)) or (Ghost2(state, player)
            and state.has("Bundle of Clothes", player, 1)))
    connect(world, player, names, "GC Flip Magic Platform", "Ghost Shop", lambda state:
            GhostR1(state, player) or Ghost2(state, player))
    connect(world, player, names, "Ghost Shop", "Ghost Shop Chest", lambda state:
            (GhostR1(state, player) and AFeathers(state, player)) or (Ghost2(state, player) and AFeathers(state, player)))
    connect(world, player, names, "Ghost Shop", "Secret Garden Key", lambda state:
            GhostR1(state, player) or Ghost2(state, player))
    connect(world, player, names, "Secret Garden Key", "Ghost Thimble", lambda state:
            GhostR1(state, player) or Ghost2(state, player))
    connect(world, player, names, "Ghost Thimble", "Blind Jump", lambda state:
            Ghost3(state, player) or Ghost4(state, player))
    connect(world, player, names, "Blind Jump", "Willow", lambda state:
            Ghost3(state, player) or Ghost4(state, player))
    connect(world, player, names, "Willow", "GC Hidden Shrub", lambda state:
            Ghost3(state, player) or Ghost4(state, player))
    connect(world, player, names, "GC Hidden Shrub", "Ghost Gauntlet", lambda state:
            Ghost3(state, player) or Ghost4(state, player))
    connect(world, player, names, "Ghost Gauntlet", "Hidden Wall", lambda state:
            Ghost3(state, player) or Ghost4(state, player))
    connect(world, player, names, "Hidden Wall", "Along The Path", lambda state:
            Ghost3(state, player) or Ghost4(state, player))
    connect(world, player, names, "Along The Path", "Ghost Hidden Spring Room", lambda state:
            Ghost3(state, player) or Ghost4(state, player))
    connect(world, player, names, "Ghost Hidden Spring Room", "Behind The Vines", lambda state:
            Ghost3(state, player) or Ghost4(state, player))
    connect(world, player, names, "Behind The Vines", "Ghost Boss", lambda state:
            Ghost3(state, player) or Ghost4(state, player))
    connect(world, player, names, "Ghost Boss", "Across Boss", lambda state:
            (Ghost3(state, player) and DWings(state, player) or AFeathers(state, player))
            or (Ghost4(state, player) and DWings(state, player) or AFeathers(state, player)))

    #Jigoku
    connect(world, player, names, "Momo Pass", "J Hidden Flip Room", lambda state:
            Jig(state, player))
    connect(world, player, names, "J Hidden Flip Room", "J Slime Room", lambda state:
            Jig(state, player) and SForm(state, player))
    connect(world, player, names, "J Hidden Flip Room", "Early Ledge", lambda state:
            Jig(state, player))
    connect(world, player, names, "Early Ledge", "J Spring Room", lambda state:
            Jig(state, player))
    connect(world, player, names, "J Spring Room", "Cat Shrine", lambda state:
            Jig(state, player))
    connect(world, player, names, "Cat Shrine", "Unlucky Cat", lambda state:
            Jig(state, player) and state.has("Soul Fragment", player, 3) and state.has("Miko Costume", player, 1))
    connect(world, player, names, "Cat Shrine", "Beast Key", lambda state:
            Jig(state, player))
    connect(world, player, names, "Beast Key", "J Hidden Ledge", lambda state:
            Jig(state, player))
    connect(world, player, names, "J Hidden Ledge", "Annahell", lambda state:
            Jig(state, player) and state.has("Farmer Costume", player, 1))
    connect(world, player, names, "J Hidden Ledge", "Annahell Chest", lambda state:
            Jig(state, player))
    connect(world, player, names, "Annahell Chest", "Hidden Hole", lambda state:
            Jig(state, player))
    connect(world, player, names, "Hidden Hole", "Near Shop", lambda state:
            Jig(state, player))
    connect(world, player, names, "Near Shop", "Demon Shop", lambda state:
            Jig(state, player))
    connect(world, player, names, "Demon Shop", "Hot Guy", lambda state:
            Jig(state, player) and state.has("The Beast's Key", player, 1))
    connect(world, player, names, "Demon Shop", "Far Ledge", lambda state:
            (Jig(state, player)) and (DWings(state, player) or AFeathers(state, player)))
    connect(world, player, names, "Demon Shop", "J Hidden Flip", lambda state:
            Jig(state, player))
    connect(world, player, names, "J Hidden Flip", "Demon Wings", lambda state:
            Jig(state, player) and state.has("Collapsed Temple Key", player, 1))
    connect(world, player, names, "Demon Wings", "North Cat Shrine", lambda state:
            Jig(state, player) and state.has("Collapsed Temple Key", player, 1) and state.has("Miko Costume", player, 1))
    connect(world, player, names, "Demon Wings", "North Cat Loot", lambda state:
            Jig(state, player) and state.has("Collapsed Temple Key", player, 1))

    #Club Demon
    connect(world, player, names, "J Hidden Flip", "Club Entrance", lambda state:
            DemA(state, player) or DemD(state, player))
    connect(world, player, names, "Club Entrance", "Under The Table", lambda state:
            DemA(state, player) or DemD(state, player))
    connect(world, player, names, "Under The Table", "Bad Boy", lambda state:
            (DemA(state, player) and state.has("Progressive Letter", player, 1)) or (DemD(state, player)
            and state.has("Progressive Letter", player, 1)))
    connect(world, player, names, "Under The Table", "Club Door", lambda state:
            (DemA(state, player) and state.has("Demon Club Door Key", player, 1)) or (DemD(state, player)
            and state.has("Demon Club Door Key", player, 1)))
    connect(world, player, names, "Under The Table", "Demon Flip Chest", lambda state:
            DemA(state, player) or DemD(state, player))
    connect(world, player, names, "Demon Flip Chest", "Demon Flip Coin", lambda state:
            DemA(state, player) or DemD(state, player))
    connect(world, player, names, "Demon Flip Chest", "Demon Flip Coin", lambda state:
            DemA(state, player) or DemD(state, player))
    connect(world, player, names, "Demon Flip Coin", "Demon Thimble", lambda state:
            DemA(state, player) or DemD(state, player))
    connect(world, player, names, "Demon Thimble", "Demon Gauntlet", lambda state:
            DemA(state, player) or DemD(state, player))
    connect(world, player, names, "Demon Gauntlet", "Club Key", lambda state:
            DemA(state, player) or DemD(state, player))
    connect(world, player, names, "Club Key", "Club Cat", lambda state:
            (DemA(state, player) and state.has("Miko Costume", player, 1)) or (DemD(state, player) and
            state.has("Miko Costume", player, 1)))
    connect(world, player, names, "Club Key", "Demon Boss Key", lambda state:
            (DemA(state, player) and state.has("Secret Club Door Key", player, 1)) or (DemD(state, player)
            and state.has("Secret Club Door Key", player, 1)))
    connect(world, player, names, "Club Key", "Demon Boss", lambda state:
            (DemA(state, player) and state.has("Demon Boss Key", player, 1)) or (DemD(state, player)
            and state.has("Demon Boss Key", player, 1)))

    #Tengoku
    connect(world, player, names, "Momo Pass", "T Early Coin", lambda state:
            TenA(state, player) or TenD(state, player))
    connect(world, player, names, "T Early Coin", "T Early Chest", lambda state:
            TenA(state, player) or TenD(state, player))
    connect(world, player, names, "T Early Chest", "T Hidden Bush", lambda state:
            TenA(state, player) or TenD(state, player))
    connect(world, player, names, "T Hidden Bush", "T Hidden Flip", lambda state:
            TenA(state, player) or TenD(state, player))
    connect(world, player, names, "T Hidden Flip", "Birby", lambda state:
            TenA(state, player) or TenD(state, player))
    connect(world, player, names, "Birby", "T Hidden Chest", lambda state:
            (TenA(state, player)) or (TenD(state, player) and BBubble(state, player)))
    connect(world, player, names, "T Hidden Chest", "T Hidden Ledge", lambda state:
            (TenA(state, player)) or (TenD(state, player) and BBubble(state, player)))
    connect(world, player, names, "T Hidden Ledge", "Secret Alcove", lambda state:
            (TenA(state, player)) or (TenD(state, player) and BBubble(state, player)))

    #Angelic Hallway
    connect(world, player, names, "Secret Alcove", "Angel Start", lambda state:
            AngA(state, player) or AngD(state, player))
    connect(world, player, names, "Angel Start", "Angel Bush 1", lambda state:
            AngA(state, player) or AngD(state, player))
    connect(world, player, names, "Angel Bush 1", "Angel Bush 2", lambda state:
            (AngA(state, player)) or (AngD(state, player) and AFeathers(state, player)))
    connect(world, player, names, "Angel Bush 1", "Angel Shop", lambda state:
            AngA(state, player) or AngD(state, player))
    connect(world, player, names, "Angel Shop", "Cloudia", lambda state:
            AngA(state, player) or AngD(state, player))
    connect(world, player, names, "Cloudia", "Angel Gauntlet", lambda state:
            (AngA(state, player) and BBubble(state, player)) or (AngD(state, player)))
    connect(world, player, names, "Cloudia", "Angel Thimble", lambda state:
            AngA(state, player) or AngD(state, player))
    connect(world, player, names, "Angel Thimble", "Below Thimble", lambda state:
            AngA(state, player) or AngD(state, player))
    connect(world, player, names, "Below Thimble", "Gabrielle Room", lambda state:
            AngA(state, player) or AngD(state, player))
    connect(world, player, names, "Gabrielle Room", "Gabrielle", lambda state:
            (AngA(state, player)) and state.has("Progressive Letter", player, 2) or
            (AngD(state, player) and state.has("Progressive Letter", player, 2)))
    connect(world, player, names, "Gabrielle Room", "Angel Behind Vines", lambda state:
            (AngA(state, player) and BBubble(state, player)) or (AngD(state, player)))
    connect(world, player, names, "Gabrielle Room", "Angel Flip", lambda state:
            AngA(state, player) or AngD(state, player))
    connect(world, player, names, "Angel Flip", "Angel Feathers", lambda state:
            AngA(state, player) or AngD(state, player))
    connect(world, player, names, "Angel Feathers", "Below Boss", lambda state:
            (AngA(state, player)) or (AngD(state, player) and AFeathers(state, player)))
    connect(world, player, names, "Below Boss", "Angelica", lambda state:
            (AngA(state, player)) or (AngD(state, player) and AFeathers(state, player)))

    #Fungal Forest
    connect(world, player, names, "Momo Pass", "Fungal Thimble", lambda state:
            EFF(state, player))
    connect(world, player, names, "Fungal Thimble", "Lower Pit", lambda state:
            EFF(state, player))
    connect(world, player, names, "Lower Pit", "F Flip Coin", lambda state:
            (EFF(state, player)) and (BBubble(state, player) or DWings(state, player)))
    connect(world, player, names, "Fungal Thimble", "Fungella", lambda state:
            EFF(state, player) and state.has("Progressive Tatil Item", player, 1))
    connect(world, player, names, "Fungella", "Past Fungella", lambda state:
            EFF(state, player) and state.has("Progressive Tatil Item", player, 1))
    connect(world, player, names, "Fungal Thimble", "H Daikon", lambda state:
            EFF(state, player) and AFeathers(state, player))
    connect(world, player, names, "H Daikon", "F Past Chaos", lambda state:
            EFF(state, player) and AFeathers(state, player))

    #Fungal Forest cont.
    connect(world, player, names, "F Past Chaos", "Closed Coins", lambda state:
            DFF(state, player))
    connect(world, player, names, "Closed Coins", "Between Thorns", lambda state:
            DFF(state, player))
    connect(world, player, names, "Between Thorns", "Fungal Shop", lambda state:
            DFF(state, player))
    connect(world, player, names, "Fungal Shop", "Mushroom Guard", lambda state:
            DFF(state, player))
    connect(world, player, names, "Mushroom Guard", "Fungal Gauntlet", lambda state:
            DFF(state, player))
    connect(world, player, names, "Fungal Gauntlet", "Blue Jelly", lambda state:
            DFF(state, player))
    connect(world, player, names, "Blue Jelly", "Fungal Door", lambda state:
            DFF(state, player))
    connect(world, player, names, "Fungal Door", "Fungus Secret", lambda state:
            DFF(state, player))
    connect(world, player, names, "Fungus Secret", "Slime Form", lambda state:
            DFF(state, player) and state.has("Forgotten Fungal Door Key", player, 1))
    connect(world, player, names, "Fungus Secret", "SCKey", lambda state:
            DFF(state, player))


    #Slime Citadel
    connect(world, player, names, "SCKey", "Slime Entrance", lambda state:
            SCAcc(state, player))
    connect(world, player, names, "Slime Entrance", "Slime Secret", lambda state:
            SCAcc(state, player))
    connect(world, player, names, "Slime Secret", "Lone Room", lambda state:
            SCAcc(state, player))
    connect(world, player, names, "Lone Room", "Silky Chest", lambda state:
            SCAcc(state, player))
    connect(world, player, names, "Silky Chest", "Silky Stone", lambda state:
            SCAcc(state, player) and state.has("Alchemist Costume", player, 1))
    connect(world, player, names, "Silky Chest", "Small Detour", lambda state:
            SCAcc(state, player))
    connect(world, player, names, "Small Detour", "Sub Key", lambda state:
            SCAcc(state, player))
    connect(world, player, names, "Sub Key", "Across Key", lambda state:
            SCAcc(state, player))
    connect(world, player, names, "Across Key", "Slime Thimble", lambda state:
            SCAcc(state, player))
    connect(world, player, names, "Slime Thimble", "Slime Gauntlet", lambda state:
            SCAcc(state, player))
    connect(world, player, names, "Slime Gauntlet", "Near Stone", lambda state:
            SCAcc(state, player))
    connect(world, player, names, "Near Stone", "Secret Spring Coin", lambda state:
            SCAcc(state, player))
    connect(world, player, names, "Secret Spring Coin", "Secret Spring Stone", lambda state:
            SCAcc(state, player) and state.has("Alchemist Costume", player, 1))
    connect(world, player, names, "Secret Spring Coin", "Hidden Tunnel", lambda state:
            SCAcc(state, player))
    connect(world, player, names, "Hidden Tunnel", "Slime Shop", lambda state:
            SCAcc(state, player))
    connect(world, player, names, "Slime Shop", "Slurp", lambda state:
            Pslurp(state, player))
    connect(world, player, names, "Slurp", "Slurp Stone", lambda state:
            Pslurp(state, player) and state.has("Alchemist Costume", player, 1))
    connect(world, player, names, "Slime Shop", "Natasha", lambda state:
            SCAcc(state, player) and state.has("Alchemist Costume", player, 1) and state.has("Summon Stone", player, 3))
    connect(world, player, names, "Slime Shop", "Slime Boss", lambda state:
            SCAcc(state, player) and state.has("Slime Boss Key", player, 1))

    #Umi Umi
    connect(world, player, names, "Momo Pass", "Umi Early", lambda state:
            (UmiR(state, player)) and (AFeathers(state, player) or DWings(state, player)))
    connect(world, player, names, "Momo Pass", "Umi Save", lambda state:
            UmiR(state, player))
    connect(world, player, names, "Umi Save", "Angler Chest", lambda state:
            UmiR(state, player))
    connect(world, player, names, "Angler Chest", "Umi Flip 1", lambda state:
            UmiR(state, player) and BubbleAndFeathers(state, player))
    connect(world, player, names, "Angler Chest", "Corner", lambda state:
            UmiR(state, player))
    connect(world, player, names, "Corner", "Dagger", lambda state:
            UmiR(state, player))
    connect(world, player, names, "Dagger", "Umi Flip 2", lambda state:
            (UmiR(state, player)) and (BBubble(state, player) or AFeathers(state, player)))
    connect(world, player, names, "Umi Flip 2", "Mermaid Chest", lambda state:
            (UmiR(state, player)) and (BBubble(state, player) or AFeathers(state, player)))
    connect(world, player, names, "Mermaid Chest", "Umi Chaos", lambda state:
            (UmiR(state, player)) and (BBubble(state, player) or AFeathers(state, player)))
    connect(world, player, names, "Umi Chaos", "Above Save", lambda state:
            (UmiR(state, player)) and (BBubble(state, player) or AFeathers(state, player)))
    connect(world, player, names, "Above Save", "Octpath", lambda state:
            (UmiR(state, player)) and (BBubble(state, player) or AFeathers(state, player)))
    connect(world, player, names, "Octpath", "Octrina", lambda state:
            UmiR(state, player) and BubbleAndFeathers(state, player))
    connect(world, player, names, "Octrina", "Water Gauntlet", lambda state:
            (UmiR(state, player)) and (BBubble(state, player) or AFeathers(state, player)))
    connect(world, player, names, "Water Gauntlet", "Frog Path", lambda state:
            UmiR(state, player) and BBubble(state, player))
    connect(world, player, names, "Dagger", "Keroku", lambda state:
            UmiR(state, player) and state.has("Angler Costume", player, 1) and state.has("Frog Boss Key", player, 1))
    connect(world, player, names, "Dagger", "Frog Boss", lambda state:
            UmiR(state, player) and state.has("Frog Boss Key", player, 1))

    #Castle Chaos
    connect(world, player, names, "Momo Pass", "Castle Outside", lambda state:
            ChaosKey(state, player, 6))
    connect(world, player, names, "Castle Outside", "Castle Early", lambda state:
            ChaosKey(state, player, 6))
    connect(world, player, names, "Castle Early", "GFP", lambda state:
            ChsB(state, player))
    connect(world, player, names, "GFP", "GCP", lambda state:
            ChsB(state, player) and GForm(state, player))
    connect(world, player, names, "GCP", "JP", lambda state:
            ChsB(state, player))
    connect(world, player, names, "JP", "Near Chaos", lambda state:
            ChsB(state, player))
    connect(world, player, names, "Near Chaos", "Chaos Shop", lambda state:
            ChsB(state, player))
    connect(world, player, names, "Chaos Shop", "SCP", lambda state:
            ChsBS(state, player))
    connect(world, player, names, "SCP", "FP", lambda state:
            ChsBS(state, player))
    connect(world, player, names, "FP", "Big Jump", lambda state:
            ChsWing(state, player))
    connect(world, player, names, "Big Jump", "Pandora", lambda state:
            ChsBS(state, player))
    connect(world, player, names, "FP", "Chaos Queen", lambda state:
            ChsBS(state, player))
    connect(world, player, names, "Chaos Queen", "Ending", lambda state:True)



    world.completion_condition[player] = lambda state: state.has("Ending", player, 1)


    #Item shortcuts

    def BBubble(state, player):
        return state.has("Bewitched Bubble", player, 1)

    def AFeathers(state, player):
        return state.has("Angel Feathers", player, 1)

    def DWings(state, player):
        return state.has("Demon Wings", player, 1)

    def GForm(state, player):
        return state.has("Ghost Form", player, 1)

    def SForm(state, player):
        return state.has("Slime Form", player, 1)

    def MScale(state, player):
        return state.has("Mermaid Scale", player, 1)

    def BubbleAndFeathers(state, player):
        return BBubble(state, player) and AFeathers(state, player)

    def BubbleAndWings(state, player):
        return BBubble(state, player) and DWings(state, player)

    def BubbleAndSlime(state, player):
        return BBubble(state, player) and SForm(state, player)

    def BubbleAndGhost(state, player):
        return BBubble(state, player) and GForm(state, player)

    def WingsAndFeathers(state, player):
        return DWings(state, player) and AFeathers(state, player)

    def FeatherAndSlime(state, player):
        return AFeathers(state, player) and SForm(state, player)

    def GachaTime(state, player, amount):
        return state.has("Gacha Coin", player, amount)

    def ChaosKey(state, player, amount):
        return state.has("Chaos Key Piece", player, amount)

    def GoblinQKey(state, player):
        return state.has("Goblin Queen Key", player, 1)

    def GardenKey(state, player):
        return state.has("Secret Garden Key", player, 1)

    def GhostKey(state, player):
        return state.has("Ghostly Castle Key", player, 1)

    def RoseKey(state, player):
        return state.has("Rose Garden Key", player, 1)

    def CitaKey(state, player):
        return state.has("Slime Citadel Key", player, 1)

    def cafereq(state, player):
        return state.has("Belle 1", player, 1) and state.has("Rover 1", player, 1) and state.has("Milk & Cream 1", player, 1)

    def Ghost1(state, player):
        return ChaosKey(state, player, 1) and GhostKey(state, player) and BBubble(state, player)

    def GhostR1(state, player):
        return ChaosKey(state, player, 1) and GhostKey(state, player) and BBubble(state, player) and RoseKey(state, player)

    def Ghost2(state, player):
        return ChaosKey(state, player, 1) and GardenKey(state, player) and GForm(state, player)

    def Ghost3(state, player):
        return ChaosKey(state, player, 1) and GhostKey(state, player) and BBubble(state, player) and RoseKey(state, player) and GForm(state, player)

    def Ghost4(state, player):
        return ChaosKey(state, player, 1) and GForm(state, player) and GardenKey(state, player) and BBubble(state, player)

    def Jig(state, player):
        return BBubble(state, player) and GForm(state, player)

    def DemD(state, player):
        return BBubble(state, player) and GForm(state, player) and DWings(state, player)

    def DemA(state, player):
        return BBubble(state, player) and GForm(state, player) and AFeathers(state, player)

    def TenD(state, player):
        return ChaosKey(state, player, 1) and DWings(state, player) and GForm(state, player)

    def TenDB(state, player):
        return ChaosKey(state, player, 1) and DWings(state, player) and GForm(state, player) and BBubble(state, player)

    def TenA(state, player):
        return ChaosKey(state, player, 1) and AFeathers(state, player) and GForm(state, player)

    def AngD(state, player):
        return DWings(state, player) and GForm(state, player) and BBubble(state, player)

    def AngA(state, player):
        return AFeathers(state, player) and GForm(state, player)

    def EFF(state, player):
        return ChaosKey(state, player, 1) and GForm(state, player)

    def DFF(state, player):
        return ChaosKey(state, player, 1) and GForm(state, player) and AFeathers(state, player) and BBubble(state, player)

    def SCAcc(state, player):
        return ChaosKey(state, player, 1) and GForm(state, player) and AFeathers(state, player) and BBubble(state, player) and SForm(state, player) and CitaKey(state, player)

    def Pslurp(state, player):
        return SCAcc(state, player) and state.has("Slimy Sub Boss Key", player, 1)

    def UmiR(state, player):
        return ChaosKey(state, player, 1) and MScale(state, player) and GForm(state, player)

    def ChsB(state, player):
        return ChaosKey(state, player, 6) and BBubble(state, player)

    def ChsBS(state, player):
        return ChsB(state, player) and SForm(state, player)

    def ChsWing(state, player):
        return ChsB(state, player) and WingsAndFeathers(state, player)