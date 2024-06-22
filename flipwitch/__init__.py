import math
import os
import json
from typing import Any, ClassVar, Dict, List, Optional, Set, Tuple, Mapping
from BaseClasses import Item, ItemClassification, MultiWorld, Tutorial
from worlds.AutoWorld import WebWorld, World
from .items import item_table, ItemData, FlipWitchItem
from .locations import location_table
from .regions import create_regions
from .rules import set_rules
from .options import FlipWitchOptions

class FlipWitchWeb(WebWorld):
    theme = "dirt"
    setup = Tutorial(
        "multiworld setup guide",
        "guide",
        "english",
        "setup_en.md",
        "setup/en",
        ["Prin"]
    )
    tutorials = [setup]

class FlipWitchWorld(World):
    """
    HeeHee Stinky
    """
    game = "FlipWitch"
    topology_present = True
    options: FlipWitchOptions
    options_dataclass = FlipWitchOptions
    web: ClassVar[WebWorld] = FlipWitchWeb()
    item_name_to_id = {**item_table}
    for key, value in item_name_to_id.items():
        item_name_to_id[key] = value+300000000
    location_name_to_id = location_table
    for key, value in location_name_to_id.items():
        location_name_to_id[key] = value+300000000

    def __int__(self, world:MultiWorld, player:int):
        super().__init__(world, player)
        self.game = "FlipWitch"

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def set_rules(self):
        set_rules(self, self.multiworld, self.player)

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        classification = ItemClassification.progression
        item = FlipWitchItem(name, classification, item_id, self.player)
        return item

    def create_item_junk(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        classification = ItemClassification.filler
        item = FlipWitchItem(name, classification, item_id, self.player)
        return item

    def create_items(self):
        GhostForm = self.create_item("Ghost Form")
        FortuneCat = self.create_item("Fortune Cat")
        MimicKey = self.create_item("Mimic Chest Key")
        BWC = self.create_item("Black Witch Costume")
        SDagger = self.create_item("Sacrificial Dagger")
        TSV = self.create_item("Toxic Slime Vial")
        HauntedScythe = self.create_item("Haunted Scythe")
        MagicalMushroom = self.create_item("Magical Mushroom")
        GoblinBomb = self.create_item("Goblin Bomb")
        MoonRing = self.create_item("Ring Of The Moon")
        HarpyFeather = self.create_item("Harpy Feather")
        DisarmingBell = self.create_item("Disarming Bell")
        SlimeForm = self.create_item("Slime Form")
        SlimeSentry = self.create_item("Slime Sentry")
        FrillyPanties = self.create_item("Frilly Panties")
        DemonicCuff = self.create_item("Demonic Cuff")
        MagneticHairpin = self.create_item("Magnetic Hairpin")
        CursedTalisman = self.create_item("Cursed Talisman")
        PortablePortal = self.create_item("Portable Portal")
        SunRing = self.create_item("Ring Of The Sun")
        StarBracelet = self.create_item("Star Bracelet")
        YFT = self.create_item("Yellow Frog Talisman")
        BFT = self.create_item("Blue Frog Talisman")
        MindMushroom = self.create_item("Mind Mushroom")
        HeartNecklace = self.create_item("Heart Necklace")
        Flutterknife = self.create_item("Flutterknife Garter")
        GenderBubble = self.create_item("Bewitched Bubble")
        TeleportCrystal = self.create_item("Goblin Crystal")
        DemonForm = self.create_item("Demon Wings")
        AngelForm = self.create_item("Angel Feathers")
        MermaidScale = self.create_item("Mermaid Scale")
        RWC = self.create_item("Red Wizard Costume")
        NunCostume = self.create_item("Nun Costume")
        PriestCostume = self.create_item("Priest Costume")
        MikoCostume = self.create_item("Miko Costume")
        FarmerCostume = self.create_item("Farmer Costume")
        CatCostume = self.create_item("Cat Costume")
        GoblinCostume = self.create_item("Goblin Costume")
        MaidCostume = self.create_item("Maid Costume")
        PigmanCostume = self.create_item("Pigman Costume")
        BunnyCostume = self.create_item("Bunny Costume")
        RatCostume = self.create_item("Rat Costume")
        NurseCostume = self.create_item("Nurse Costume")
        AnglerCostume = self.create_item("Angler Costume")
        DominatingCostume = self.create_item("Dominating Costume")
        PostmanCostume = self.create_item("Postman Costume")
        FairyCostume = self.create_item("Fairy Costume")
        AlchemistCostume = self.create_item("Alchemist Costume")
        RundownKey = self.create_item("Rundown House Key")
        GhostlyKey = self.create_item("Ghostly Castle Key")
        BeastKey = self.create_item("The Beast's Key")
        SecretClubKey = self.create_item("Secret Club Door Key")
        SlimeCitadelKey = self.create_item("Slime Citadel Key")
        FrogKey = self.create_item("Frog Boss Key")
        GoblinQueenKey = self.create_item("Goblin Queen Key")
        RoseKey = self.create_item("Rose Garden Key")
        TempleKey = self.create_item("Collapsed Temple Key")
        DemonBossKey = self.create_item("Demon Boss Key")
        SlimySubBossKey = self.create_item("Slimy Sub Boss Key")
        ChaosKey = self.create_item("Chaos Sanctum Key")
        ApartmentKey = self.create_item("Abandoned Apartment Key")
        GardenKey = self.create_item("Secret Garden Key")
        DemonClubKey = self.create_item("Demon Club Door Key")
        FungalKey = self.create_item("Forgotten Fungal Door Key")
        SlimeBossKey = self.create_item("Slime Boss Key")
        GoldCoin = self.create_item("Gold Coins")
        ServerPassword = self.create_item("Momo Server Admin Password")
        BundleofClothes = self.create_item("Bundle of Clothes")
        Halo = self.create_item("Legendary Halo")
        SilkySlime = self.create_item("Silky Slime")
        Wine = self.create_item("Red Wine")
        JellyMushroom = self.create_item("Blue Jelly Mushroom")
        MaidContract = self.create_item("Maid Contract")
        DeedToForest = self.create_item("Deed to Fungal Forest")
        for i in range(6):
            self.multiworld.itempool+=[self.create_item("Chaos Key Piece")]
        for i in range(2):
            self.multiworld.itempool+=[self.create_item("Progressive Letter")]
        for i in range(4):
            self.multiworld.itempool+=[self.create_item("Progressive Belle Item")]
        for i in range(4):
            self.multiworld.itempool+=[self.create_item("Progressive Gobliana Item")]
        for i in range(2):
            self.multiworld.itempool+=[self.create_item("Progressive Kyoni Item")]
        for i in range(2):
            self.multiworld.itempool+=[self.create_item("Progressive Tatil Item")]
        for i in range(10):
            self.multiworld.itempool+=[self.create_item("Peachy Peach")]
        for i in range(3):
            self.multiworld.itempool+=[self.create_item("Soul Fragment")]
        for i in range(3):
            self.multiworld.itempool+=[self.create_item("Summon Stone")]
        for i in range(10):
            self.multiworld.itempool+=[self.create_item("Health Upgrade")]
        for i in range(10):
            self.multiworld.itempool+=[self.create_item("Mana Upgrade")]
        for i in range(2):
            self.multiworld.itempool+=[self.create_item("Peachy Peach Upgrade")]
        for i in range(2):
            self.multiworld.itempool+=[self.create_item("Wand Upgrade")]
        for i in range(44):
            self.multiworld.itempool+=[self.create_item("Gacha Coin")]
        for i in range(10):
            self.multiworld.itempool += [self.create_item("Progressive Animal Girl Gacha")]
        for i in range(10):
            self.multiworld.itempool+=[self.create_item("Progressive Bunny Girl Gacha")]
        for i in range(10):
            self.multiworld.itempool += [self.create_item("Progressive Angels & Demons Gacha")]
        for i in range(10):
            self.multiworld.itempool += [self.create_item("Progressive Monster Girl Gacha")]
        for i in range(226):
            self.multiworld.itempool+=[self.create_item_junk("Gold Coins")]
        FairyBubble = self.create_item("Fairy Bubble")
        SpecialGacha = self.create_item("Special Promo Gacha")

        #Questlist = list(quest_table.keys())[list(quest_table.values())]
        Questlist = dict((v, k) for k, v in location_table.items())
        for i in range(40):
            self.multiworld.get_location(Questlist.get(300001001 + i),self.player).place_locked_item(self.create_item("Completed Quests"))
        self.multiworld.get_location("Belle 1 Complete Flag", self.player).place_locked_item(self.create_item("Belle 1"))
        self.multiworld.get_location("Belle 2 Complete Flag", self.player).place_locked_item(self.create_item("Belle 2"))
        self.multiworld.get_location("Belle 3 Complete Flag", self.player).place_locked_item(self.create_item("Belle 3"))
        self.multiworld.get_location("Goblin 1 Complete Flag", self.player).place_locked_item(self.create_item("Goblin 1"))
        self.multiworld.get_location("Goblin 2 Complete Flag", self.player).place_locked_item(self.create_item("Goblin 2"))
        self.multiworld.get_location("Rover 1 Complete Flag", self.player).place_locked_item(self.create_item("Rover 1"))
        self.multiworld.get_location("Rover 2 Complete Flag", self.player).place_locked_item(self.create_item("Rover 2"))
        self.multiworld.get_location("Rover 3 Complete Flag", self.player).place_locked_item(self.create_item("Rover 3"))
        self.multiworld.get_location("Merchant 1 Complete Flag", self.player).place_locked_item(self.create_item("Merchant 1"))
        self.multiworld.get_location("Milk & Cream 1 Complete Flag", self.player).place_locked_item(self.create_item("Milk & Cream 1"))
        self.multiworld.get_location("Milk & Cream 2 Complete Flag", self.player).place_locked_item(self.create_item("Milk & Cream 2"))
        self.multiworld.get_location("Milk & Cream 3 Complete Flag", self.player).place_locked_item(self.create_item("Milk & Cream 3"))
        self.multiworld.get_location("Janic 1 Complete Flag", self.player).place_locked_item(self.create_item("Janic 1"))
        self.multiworld.get_location("Janic 2 Complete Flag", self.player).place_locked_item(self.create_item("Janic 2"))
        self.multiworld.get_location("Kyoni 1 Complete Flag", self.player).place_locked_item(self.create_item("Kyoni 1"))

        self.multiworld.get_location("Ending", self.player).place_locked_item(self.create_item("Ending"))
        self.multiworld.itempool+=[GhostForm, FortuneCat, MimicKey, BWC, SDagger, TSV, HauntedScythe, MagicalMushroom,
                                   GoblinBomb, MoonRing, HarpyFeather, DisarmingBell, SlimeForm, SlimeSentry,
                                   FrillyPanties, DemonicCuff, MagneticHairpin, CursedTalisman, PortablePortal, SunRing,
                                   StarBracelet, YFT, BFT, MindMushroom, HeartNecklace, Flutterknife, GenderBubble,
                                   TeleportCrystal, DemonForm, AngelForm, MermaidScale, RWC, NunCostume, PriestCostume,
                                   MikoCostume, FarmerCostume, CatCostume, GoblinCostume, MaidCostume, PigmanCostume,
                                   BunnyCostume, RatCostume, NurseCostume, AnglerCostume, DominatingCostume,
                                   PostmanCostume, FairyCostume, AlchemistCostume, RundownKey, GhostlyKey, BeastKey,
                                   SecretClubKey, SlimeCitadelKey, FrogKey, GoblinQueenKey, RoseKey, TempleKey,
                                   DemonBossKey, SlimySubBossKey, ChaosKey, ApartmentKey, GardenKey, DemonClubKey,
                                   FungalKey, SlimeBossKey, GoldCoin, ServerPassword,
                                   BundleofClothes, Halo, SilkySlime, Wine, JellyMushroom, MaidContract,
                                   DeedToForest, FairyBubble, SpecialGacha, ]

    def fill_slot_data(self):
        locations = []
        items = []
        for i in self.multiworld.get_locations():
            locations += [self.location_name_to_id[i.name]]
            items += [self.item_name_to_id[i.item.name]]
        slot_data = \
        {
            "locations": locations,
            "items": items,
        }
        return slot_data

    def generate_output(self, output_directory: str):
        data = {
            "slot_data": self.fill_slot_data(),
            "location_to_item": {self.location_name_to_id[i.name]: self.item_name_to_id[i.item.name] for i in
                                 self.multiworld.get_locations()},
            "data_package": {
                "data": {
                    "games": {
                        self.game: {
                            "item_name_to_id": self.item_name_to_id,
                            "location_name_to_id": self.location_name_to_id
                        }
                    }
                }
            }
        }
        filename = f"{self.multiworld.get_out_file_name_base(self.player)}.apfw"
        with open(os.path.join(output_directory, filename), 'w') as f:
            json.dump(data, f)