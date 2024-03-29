using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FWAP.Data
{
    public static class FlipwitchDictionary
    {
        public static Dictionary<int, string> locations = new Dictionary<int, string>
        {
            { 300000001, "BlackWitchCostume"},
            { 300000184, "MimicKey"},
            { 300000023, "GoblinBomb"},
            { 300000035, "MagneticHairpin"},
            { 300000243, "FlutterknifeGarter"},
            { 300000305, "SacrificialDagger"},
            { 300000333, "HarpyFeather"},
            { 300000029, "GoblinCrystal"},            
            { 300000176, "GhostTransform"},
            { 300000253, "AngelJump"},
            { 300000276, "SlimeTransform"},
            { 300000155, "MermaidScale"},
            { 300000017, "Cowbell"},
            { 300000180, "CatGirlsClothes"},
            { 300000079, "HellishDango"},
            { 300000238, "LegendaryHalo"},
            { 300000010, "Wine"},
            { 300000273, "GlassWand"},
            { 300000281, "SilkySlime"},
            { 300000141, "MaidContract"},
            { 300000064, "BunnyCostume"},
            { 300000149, "RatCostume"}, //testing chest 2
            { 300000302, "AnglerCostume"},
            { 300000018, "RundownHouseKey"}, //need switch? "ww_rundownhousekey"
            { 300000134, "AbandonedApartmentKey"}, //need switch? "sc_abandonedapartmentkey"
            { 300000030, "GoblinBossKey"}, //need switch? "ww_goblinbosskey"
            { 300000077, "GhostCastleKey"}, //need switch? "sc_ghostcastlekey"
            { 300000162, "RoseGardenKey"}, //need switch? "gc_rosegardenkey"
            { 300000169, "SecretGardenKey"}, //need switch? "gc_secretgardenkey"
            { 300000194, "DemonSubBossKey"}, //need switch? "j_demonsubbosskey"
            { 300000222, "DemonBossKey"}, //need switch? "j_demonbosskey"
            { 300000202, "CollapsedTempleKey"}, //need switch? "j_collapsedtemplekey"
            { 300000219, "ClubDoor1Key"}, //need switch? "j_clubdoor1key" ClubDoor or SecretClubDoor?
            { 300000213, "ClubDoor2Key"}, //need switch? "j_clubdoor2key" ClubDoor or SecretClubDoor?
            { 300000274, "ForgottenFungalDoorKey"}, //need switch? "ff_forgotten_fungal_key"
            { 300000277, "SlimeCitadelKey"}, //need switch? "ff_slime_citadel_key"
            { 300000284, "SlimySubBossKey"}, //need switch? "sc_slimysubbosskey"
            { 300000295, "SlimeBossKey"}, //need switch? "sc_slimebosskey"
            { 300000311, "FrogBossKey"}, //need switch? "uu_frog_boss_key"
            { 300000329, "ChaosSanctumKey"}, //need switch? "cc_chaossanctumkey"
            { 300000032, "ChaosKey1"},
            { 300000181, "ChaosKey2"},
            { 300000223, "ChaosKey3"},
            { 300000256, "ChaosKey4"},
            { 300000315, "ChaosKey5"},
            { 300000298, "ChaosKey6"},
            { 300000004, "PeachyPeach"},
            
        };
        public static Dictionary<int, string> items = new Dictionary<int, string>
        {
            { 1, "MimicKey" },
            { 2, "GhostTransform" },
            { 3, "BlackWitchCostume" },
            { 4, "FortuneCat" },
            { 6, "SacrificialDagger" },
            { 8, "HauntedScythe" },
            { 9, "MagicalMushroom" },
            { 10, "GoblinBomb" },
            { 11, "RingofMoon" },
            { 12, "HarpyFeather" },
            { 13, "DisarmingBell" },
            { 14, "SlimeTransform" },
            { 15, "SlimySentry" },
            { 16, "FrillyPanties" },
            { 17, "DemonicCuff" },
            { 18, "MagneticHairpin" },
            { 19, "CursedTalisman" },
            { 20, "PortablePortal" },
            { 21, "RingofSun" },
            { 22, "StarBracelet" },
            { 23, "FirstFrogTalisman" }, //yellow?
            { 24, "MindMushroom" },
            { 25, "HeartNecklace" },
            { 26, "FlutterknifeGarter" },
            { 27, "SecondFrogTalisman" }, //blue?
            { 28, "ChaosKey1" }, //How many do I add?
            { 34, "BewitchedBubble" },
            { 35, "GoblinCrystal" },
            { 36, "DemonDash" },
            { 37, "AngelJump" },
            { 38, "MermaidScale" },
            { 39, "RedWizardCostume" },
            { 40, "NunCostume" },
            { 41, "PriestCostume" },
            { 42, "MikoCostume" },
            { 43, "FarmerCostume" },
            { 44, "CatCostume" },
            { 45, "GoblinCostume" },
            { 46, "MaidCostume" },
            { 47, "PigCostume" },
            { 48, "BunnyCostume" },
            { 49, "RatCostume" },
            { 50, "NurseCostume" },
            { 51, "AnglerCostume" },
            { 52, "PoliceCostume" },
            { 53, "PostmanCostume" },
            { 54, "FairyCostume" },
            { 55, "AlchemistCostume" },
            { 56, "RundownHouseKey" },
            { 68, "AbandonedApartmentKey"},
            { 62, "GoblinBossKey" },
            { 57, "GhostCastleKey" },
            { 63, "RoseGardenKey" },
            { 69, "SecretGardenKey" },
            { 58, "DemonSubBossKey" },
            { 65, "DemonBossKey" },
            { 64, "CollapsedTempleKey" },
            { 70, "ClubDoor1Key" },
            { 59, "ClubDoor2Key" },
            { 71, "ForgottenFungalDoorKey" },
            { 60, "SlimeCitadelKey" },
            { 66, "SlimySubBossKey" },
            { 72, "SlimeBossKey" },
            { 61, "FrogBossKey" },
            { 67, "ChaosSanctumKey" },
            { 73, "PeachyPeach" },
            { 74, "GachaCoin" }, //or GachaToken, find that out
            { 75, "coin" }, //GoldCoins 
            { 102, "FairyBubble" },
            { 76, "Cowbell" },
            { 80, "GoblinHeadshot" }, //GoblinModelQuest1 - switch name
            { 78, "MomoBotAdminPassword" },
            { 79, "CatGirlsClothes" },
            { 82, "HellishDango" },
            { 88, "AngelLetter" },
            { 87, "LegendaryHalo" },
            { 92, "Wine" },
            { 95, "FungalKey" },
            { 93, "GlassWand" },
            { 90, "SilkySlime" },
            { 94, "MaidContract" },
            { 84, "SoulFragment1" }, //3 of these same name numbered different, switch unknown atm
            { 96, "SummonStone1" }, //3 of these same name numbered different, double check name. Switch Driven name is "PhiloStone"            
            { 99, "hpUpgradeLevel" }, //10 of these?
            { 100, "mpUpgradeLevel" }, //10 of these?
            { 101, "playerWandLevel" }, //Doublecheck this one, and 2 of these?
            { 144, "HealStrengthLevel" }, //Doublecheck this one, and 2 of these?
            { 110, "GachaMachine" }, //Doublecheck this one, Animal Girls. Collection = AnimalGirls (GachaCollections). Combine with Promotion? Could be "AnimalGirls_0"
            { 120, "GachaMachine (1)" }, //Doublecheck this one, Bunny Girls. Collection = Bunnys (GachaCollections). Could be "Bunnys_0"
            { 130, "GachaMachine (2)" }, //Doublecheck this one, Angel & Demon Girls. Collection = AngelsAndDemons (GachaCollections). Could be "AngelsAndDemons_0"
            { 140, "GachaMachine (3)" }, //Doublecheck this one, Monster Girls. Collection = Monsters (GachaCollections). Could be "Monsters_0"
            { 143, "GachaMachine" }, //Doublecheck this one, Promotion. Collection = Promotion (GachaCollections). Could be "Promotion_0"
        };

    }
}
