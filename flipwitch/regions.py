from BaseClasses import MultiWorld, Region, Entrance
from worlds.AutoWorld import World
import typing
from .locations import location_table, FlipWitchLocation

def create_regions(world:MultiWorld, player:int):
    #menu
    menu = Region("Menu", player, world)

    #Witchy Woods

    #senseihut
    senseihut = Region("Sensei's Hut", player, world)
    senseihut.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], senseihut) for loc_name in
                          get_array([1])]
    #senseihutbubble
    senseihutbubble = Region("Sensei's Hut BBubble", player, world)
    senseihutbubble.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], senseihutbubble) for
                                loc_name in get_array([2])]
    #beatrix
    beatrix = Region("Beatrix", player, world)
    beatrix.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], beatrix) for loc_name in
                          get_array([3, 1034])]
    #questupgrade1
    questupgrade1 = Region("Quest Upgrade 1", player, world)
    questupgrade1.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], questupgrade1) for loc_name
                              in get_array([37])]
    #questupgrade2
    questupgrade2 = Region("Quest Upgrade 2", player, world)
    questupgrade2.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], questupgrade2) for
                                loc_name in get_array([38])]
    #questupgrade3
    questupgrade3 = Region("Quest Upgrade 3", player, world)
    questupgrade3.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], questupgrade3) for
                                loc_name in get_array([39])]
    #questupgrade4
    questupgrade4 = Region("Quest Upgrade 4", player, world)
    questupgrade4.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], questupgrade4) for
                                loc_name in get_array([40])]
    #questupgrade5
    questupgrade5 = Region("Quest Upgrade 5", player, world)
    questupgrade5.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], questupgrade5) for
                                loc_name in get_array([41])]
    #questupgrade6
    questupgrade6 = Region("Quest Upgrade 6", player, world)
    questupgrade6.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], questupgrade6) for
                                loc_name in get_array([42])]
    #questupgrade7
    questupgrade7 = Region("Quest Upgrade 7", player, world)
    questupgrade7.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], questupgrade7) for
                                loc_name in get_array([43])]
    #questupgrade8
    questupgrade8 = Region("Quest Upgrade 8", player, world)
    questupgrade8.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], questupgrade8) for
                                loc_name in get_array([44])]
    #questupgrade9
    questupgrade9 = Region("Quest Upgrade 9", player, world)
    questupgrade9.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], questupgrade9) for
                                loc_name in get_array([45])]
    #questupgrade10
    questupgrade10 = Region("Quest Upgrade 10", player, world)
    questupgrade10.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], questupgrade10) for
                                loc_name in get_array([46])]
    #pastthehut
    pastthehut = Region("Past The Hut", player, world)
    pastthehut.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], pastthehut) for loc_name in
                             get_array([4])]
    #secretcave
    secretcave = Region("Secret Cave", player, world)
    secretcave.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], secretcave) for loc_name in
                             get_array([11, 12])]
    #genesis
    genesis = Region("Genesis", player, world)
    genesis.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], genesis) for loc_name in
                          get_array([6])]
    #genesispromo
    genesispromo = Region("Genesis Promo", player, world)
    genesispromo.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], genesispromo) for loc_name
                               in get_array([7])]
    #belle
    belle = Region("Belle", player, world)
    belle.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], belle) for loc_name in
                        get_array([8, 1001, 2001])]
    #rundownhouse
    rundownhouse = Region("Rundown House", player, world)
    rundownhouse.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], rundownhouse) for loc_name
                               in get_array([18, 19])]
    #rundownhousesave
    rundownhousesave = Region("Rundown House Save", player, world)
    rundownhousesave.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], rundownhousesave) for
                                   loc_name in get_array([9])]
    #mimi
    mimi = Region("Mimi", player, world)
    mimi.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], mimi) for loc_name in
                     get_array([14, 1016])]
    #mimihiddenchest
    mimihiddenchest = Region("Mimi Hidden Chest", player, world)
    mimihiddenchest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], mimihiddenchest) for
                                  loc_name in get_array([13])]
    #goblinapartment
    goblinapartment = Region("Goblin Apartment", player, world)
    goblinapartment.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], goblinapartment) for
                                loc_name in get_array([15])]
    #redwine
    redwine = Region("Red Wine", player, world)
    redwine.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], goblinapartment) for loc_name in
                        get_array([10])]
    #mimicchestkeyroom
    mimicchestkeyroom = Region("Mimic Chest Key Room", player, world)
    mimicchestkeyroom.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], mimicchestkeyroom) for loc_name in
                        get_array([183, 184])]
    #bellescowbell
    bellescowbell = Region("Belle's Cowbell", player, world)
    bellescowbell.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bellescowbell) for
                                loc_name in get_array([17])]
    #mancave
    mancave = Region("Man Cave", player, world)
    mancave.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], mancave) for loc_name in
                        get_array([21])]
    #beforegreatfairy
    beforegreatfairy = Region("Before Great Fairy", player, world)
    beforegreatfairy.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], beforegreatfairy) for loc_name in
                       get_array([20])]
    #greatfairy
    greatfairy = Region("Great Fairy", player, world)
    greatfairy.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], greatfairy) for loc_name in
                 get_array([47])]
    #pastmancave
    pastmancave = Region("Past Man Cave", player, world)
    pastmancave.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], pastmancave) for loc_name in
                  get_array([22])]
    #gerrygatric
    gerrygatric = Region("Gerry G. Atric", player, world)
    gerrygatric.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], gerrygatric) for loc_name in
                  get_array([23])]
    #hiddenalcove
    hiddenalcove = Region("Hidden Alcove", player, world)
    hiddenalcove.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], hiddenalcove) for loc_name in
                   get_array([24])]
    #flipplatform
    flipplatform = Region("Beside Flip Platform", player, world)
    flipplatform.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], flipplatform) for loc_name in
                   get_array([25])]
    #gobliana
    gobliana = Region("Gobliana", player, world)
    gobliana.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], gobliana) for loc_name in
                    get_array([26])]
    #gobliana2
    gobliana2 = Region("Gobliana 2", player, world)
    gobliana2.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], gobliana2) for loc_name in
                    get_array([27, 1004, 2004])]
    #afterchaosfight
    afterchaosfight = Region("After Chaos Fight", player, world)
    afterchaosfight.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], afterchaosfight) for loc_name in
                  get_array([28])]
    #bosskeyroom
    wwbosskeyroom = Region("WW Boss Key Room", player, world)
    wwbosskeyroom.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], wwbosskeyroom) for loc_name in
                        get_array([29, 30, 31])]
    #wwhiddenspringroom
    wwhiddenspringroom = Region("WW Hidden Spring Room", player, world)
    wwhiddenspringroom.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], wwhiddenspringroom) for loc_name in
                      get_array([36])]
    #fairychest
    fairychest = Region("Fairy Chest", player, world)
    fairychest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], fairychest) for loc_name in
                   get_array([35])]
    #fairyquest
    fairyquest = Region("Fairy Quest", player, world)
    fairyquest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], fairyquest) for loc_name in
                   get_array([34, 1035])]
    #goblinqueen
    goblinqueen = Region("Goblin Queen", player, world)
    goblinqueen.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], goblinqueen) for loc_name in
                   get_array([32, 33])]
    #goblinprincess
    goblinprincess = Region("Goblin Princess", player, world)
    goblinprincess.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], goblinprincess) for loc_name in
                    get_array([185, 1019])]
    #WWpostfight
    wwpostfight = Region("WW Post Fight", player, world)
    wwpostfight.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], wwpostfight) for loc_name in
                       get_array([186])]


    #City


    #toilet
    toilet = Region("Toilet", player, world)
    toilet.locations+=[FlipWitchLocation(player, loc_name, location_table[loc_name], toilet) for loc_name in
             get_array([48, 49])]
    #toiletcoin
    toiletcoin = Region("Toilet Coin", player, world)
    toiletcoin.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], toiletcoin) for loc_name in
               get_array([50])]
    #cabaretcafechest
    cabaretcafechest = Region("Cabaret Cafe Chest", player, world)
    cabaretcafechest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], cabaretcafechest) for loc_name in
                   get_array([51])]
    #animalgirlgacha1
    animalgirlgacha1 = Region("Animal Girl Gacha 1", player, world)
    animalgirlgacha1.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], animalgirlgacha1) for
                                   loc_name in get_array([94])]
    #animalgirlgacha2
    animalgirlgacha2 = Region("Animal Girl Gacha 2", player, world)
    animalgirlgacha2.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], animalgirlgacha2) for
                                   loc_name in get_array([95])]
    #animalgirlgacha3
    animalgirlgacha3 = Region("Animal Girl Gacha 3", player, world)
    animalgirlgacha3.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], animalgirlgacha3) for
                                   loc_name in get_array([96])]
    #animalgirlgacha4
    animalgirlgacha4 = Region("Animal Girl Gacha 4", player, world)
    animalgirlgacha4.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], animalgirlgacha4) for
                                   loc_name in get_array([97])]
    #animalgirlgacha5
    animalgirlgacha5 = Region("Animal Girl Gacha 5", player, world)
    animalgirlgacha5.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], animalgirlgacha5) for
                                   loc_name in get_array([98])]
    #animalgirlgacha6
    animalgirlgacha6 = Region("Animal Girl Gacha 6", player, world)
    animalgirlgacha6.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], animalgirlgacha6) for
                                   loc_name in get_array([99])]
    #animalgirlgacha7
    animalgirlgacha7 = Region("Animal Girl Gacha 7", player, world)
    animalgirlgacha7.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], animalgirlgacha7) for
                                   loc_name in get_array([100])]
    #animalgirlgacha8
    animalgirlgacha8 = Region("Animal Girl Gacha 8", player, world)
    animalgirlgacha8.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], animalgirlgacha8) for
                                   loc_name in get_array([101])]
    #animalgirlgacha9
    animalgirlgacha9 = Region("Animal Girl Gacha 9", player, world)
    animalgirlgacha9.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], animalgirlgacha9) for
                                   loc_name in get_array([102])]
    #animalgirlgacha10
    animalgirlgacha10 = Region("Animal Girl Gacha 10", player, world)
    animalgirlgacha10.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], animalgirlgacha10) for
                                   loc_name in get_array([103])]
    #boned
    boned = Region("Boned", player, world)
    boned.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], boned)
                                  for loc_name in get_array([52, 1007, 2007])]
    #legendarychewtoy
    legendarychewtoy = Region("Legendary Chewtoy", player, world)
    legendarychewtoy.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], legendarychewtoy)
                                for loc_name in get_array([53, 1008, 2008])]
    #deliciousmilk
    deliciousmilk = Region("Delicious Milk", player, world)
    deliciousmilk.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], deliciousmilk)
                        for loc_name in get_array([54])]
    #deluxemilkshake
    deluxemilkshake = Region("Deluxe Milkshake", player, world)
    deluxemilkshake.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], deluxemilkshake)
                                for loc_name in get_array([55, 1002, 2002])]
    #cherryaptkey
    cherryaptkey = Region("Cherry Apt Key", player, world)
    cherryaptkey.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], cherryaptkey)
                                for loc_name in get_array([56])]
    #ratproblem
    ratproblem = Region("Rat Problem", player, world)
    ratproblem.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ratproblem)
                                for loc_name in get_array([57, 1003, 2003])]
    #ghosthunters
    ghosthunters = Region("Ghost Hunters", player, world)
    ghosthunters.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ghosthunters)
                                for loc_name in get_array([58, 1011, 2011])]
    #hauntedbathroom
    hauntedbathroom = Region("Haunted Bathroom", player, world)
    hauntedbathroom.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], hauntedbathroom)
                                for loc_name in get_array([59, 1012, 2012])]
    #ectogasm
    ectogasm = Region("Ectogasm", player, world)
    ectogasm.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ectogasm)
                                for loc_name in get_array([60, 1020])]
    #jellymushroom
    jellymushroom = Region("Jelly Mushroom", player, world)
    jellymushroom.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], jellymushroom)
                                for loc_name in get_array([61, 1009, 2009])]
    #boozebunny
    boozebunny = Region("Booze Bunny", player, world)
    boozebunny.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], boozebunny)
                                for loc_name in get_array([62, 1013, 2013])]
    #helpwanted
    helpwanted = Region("Help Wanted", player, world)
    helpwanted.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], helpwanted)
                                for loc_name in get_array([63, 1014, 2014])]
    #vipchest
    vipchest = Region("VIP Chest", player, world)
    vipchest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], vipchest)
                                for loc_name in get_array([64, 1021])]
    #unmarkedhousebubble
    unmarkedhousebubble = Region("Unmarked House Bubble", player, world)
    unmarkedhousebubble.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], unmarkedhousebubble) for
                                   loc_name in get_array([65])]
    #angelndemongacha1
    angelndemongacha1 = Region("Angel and Demon Gacha 1", player, world)
    angelndemongacha1.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelndemongacha1)
                                      for loc_name in get_array([114])]
    #angelndemongacha2
    angelndemongacha2 = Region("Angel and Demon Gacha 2", player, world)
    angelndemongacha2.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelndemongacha2)
                                    for loc_name in get_array([115])]
    #angelndemongacha3
    angelndemongacha3 = Region("Angel and Demon Gacha 3", player, world)
    angelndemongacha3.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelndemongacha3)
                                    for loc_name in get_array([116])]
    #angelndemongacha4
    angelndemongacha4 = Region("Angel and Demon Gacha 4", player, world)
    angelndemongacha4.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelndemongacha4)
                                    for loc_name in get_array([117])]
    #angelndemongacha5
    angelndemongacha5 = Region("Angel and Demon Gacha 5", player, world)
    angelndemongacha5.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelndemongacha5)
                                    for loc_name in get_array([118])]
    #angelndemongacha6
    angelndemongacha6 = Region("Angel and Demon Gacha 6", player, world)
    angelndemongacha6.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelndemongacha6)
                                    for loc_name in get_array([119])]
    #angelndemongacha7
    angelndemongacha7 = Region("Angel and Demon Gacha 7", player, world)
    angelndemongacha7.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelndemongacha7)
                                    for loc_name in get_array([120])]
    #angelndemongacha8
    angelndemongacha8 = Region("Angel and Demon Gacha 8", player, world)
    angelndemongacha8.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelndemongacha8)
                                    for loc_name in get_array([121])]
    #angelndemongacha9
    angelndemongacha9 = Region("Angel and Demon Gacha 9", player, world)
    angelndemongacha9.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelndemongacha9)
                                    for loc_name in get_array([122])]
    #angelndemongacha10
    angelndemongacha10 = Region("Angel and Demon Gacha 10", player, world)
    angelndemongacha10.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelndemongacha10)
                                    for loc_name in get_array([123])]
    #itemshop
    itemshop = Region("Item Shop", player, world)
    itemshop.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], itemshop)
                                    for loc_name in get_array([66, 67, 68, 69])]
    #itemshoproof
    itemshoproof = Region("Item Shop Roof", player, world)
    itemshoproof.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], itemshoproof)
                            for loc_name in get_array([70])]
    #monstergirlgacha1
    monstergirlgacha1 = Region("Monster Girl Gacha 1", player, world)
    monstergirlgacha1.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], monstergirlgacha1)
                            for loc_name in get_array([124])]
    #monstergirlgacha2
    monstergirlgacha2 = Region("Monster Girl Gacha 2", player, world)
    monstergirlgacha2.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], monstergirlgacha2)
                                    for loc_name in get_array([125])]
    #monstergirlgacha3
    monstergirlgacha3 = Region("Monster Girl Gacha 3", player, world)
    monstergirlgacha3.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], monstergirlgacha3)
                                    for loc_name in get_array([126])]
    #monstergirlgacha4
    monstergirlgacha4 = Region("Monster Girl Gacha 4", player, world)
    monstergirlgacha4.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], monstergirlgacha4)
                                    for loc_name in get_array([127])]
    #monstergirlgacha5
    monstergirlgacha5 = Region("Monster Girl Gacha 5", player, world)
    monstergirlgacha5.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], monstergirlgacha5)
                                    for loc_name in get_array([128])]
    #monstergirlgacha6
    monstergirlgacha6 = Region("Monster Girl Gacha 6", player, world)
    monstergirlgacha6.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], monstergirlgacha6)
                                    for loc_name in get_array([129])]
    #monstergirlgacha7
    monstergirlgacha7 = Region("Monster Girl Gacha 7", player, world)
    monstergirlgacha7.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], monstergirlgacha7)
                                    for loc_name in get_array([130])]
    #monstergirlgacha8
    monstergirlgacha8 = Region("Monster Girl Gacha 8", player, world)
    monstergirlgacha8.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], monstergirlgacha8)
                                    for loc_name in get_array([131])]
    #monstergirlgacha9
    monstergirlgacha9 = Region("Monster Girl Gacha 9", player, world)
    monstergirlgacha9.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], monstergirlgacha9)
                                    for loc_name in get_array([132])]
    #monstergirlgacha10
    monstergirlgacha10 = Region("Monster Girl Gacha 10", player, world)
    monstergirlgacha10.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], monstergirlgacha10)
                                    for loc_name in get_array([133])]
    #fashionshop
    fashionshop = Region("Fashion Shop", player, world)
    fashionshop.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], fashionshop)
                            for loc_name in get_array([71, 72])]
    #clinic
    clinic = Region("Clinic", player, world)
    clinic.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], clinic)
                            for loc_name in get_array([73, 1017])]
    #rover
    rover = Region("Rover", player, world)
    rover.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], rover)
                            for loc_name in get_array([74, 1006, 2006])]
    #ancientbchest
    ancientbchest = Region("Ancient Being Chest", player, world)
    ancientbchest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ancientbchest)
                            for loc_name in get_array([75])]
    #ancientbeing
    ancientbeing = Region("Ancient Being", player, world)
    ancientbeing.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ancientbeing)
                            for loc_name in get_array([76, 1018])]
    #belowcemetary
    belowcemetary = Region("Below Cemetary", player, world)
    belowcemetary.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], belowcemetary)
                               for loc_name in get_array([78])]
    #ghostcastlekey
    ghostcastlekey = Region("Ghost Castle Key", player, world)
    ghostcastlekey.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ghostcastlekey)
                                for loc_name in get_array([77])]
    #bunnyclubq
    bunnyclubq = Region("Bunny Club Quest", player, world)
    bunnyclubq.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bunnyclubq)
                                 for loc_name in get_array([80, 1040])]
    #silkyslimeq
    silkyslimeq = Region("Silky Slime Quest", player, world)
    silkyslimeq.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], silkyslimeq)
                                for loc_name in get_array([81, 1039])]
    #legsofficekey
    legsofficekey = Region("Legs Office Key", player, world)
    legsofficekey.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], legsofficekey)
                                for loc_name in get_array([82])]
    #emotionalbaggage
    emotionalbaggage = Region("Emotional Baggage", player, world)
    emotionalbaggage.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], emotionalbaggage)
                                for loc_name in get_array([83, 1005, 2005])]
    #dirtydebut
    dirtydebut = Region("Dirty Debut", player, world)
    dirtydebut.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], dirtydebut)
                                for loc_name in get_array([84, 1033])]
    #bunnygirlgacha1
    bunnygirlgacha1 = Region("Bunny Girl Gacha 1", player, world)
    bunnygirlgacha1.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bunnygirlgacha1)
                                for loc_name in get_array([104])]
    #bunnygirlgacha2
    bunnygirlgacha2 = Region("Bunny Girl Gacha 2", player, world)
    bunnygirlgacha2.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bunnygirlgacha2)
                                  for loc_name in get_array([105])]
    #bunnygirlgacha3
    bunnygirlgacha3 = Region("Bunny Girl Gacha 3", player, world)
    bunnygirlgacha3.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bunnygirlgacha3)
                                  for loc_name in get_array([106])]
    #bunnygirlgacha4
    bunnygirlgacha4 = Region("Bunny Girl Gacha 4", player, world)
    bunnygirlgacha4.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bunnygirlgacha4)
                                  for loc_name in get_array([107])]
    #bunnygirlgacha5
    bunnygirlgacha5 = Region("Bunny Girl Gacha 5", player, world)
    bunnygirlgacha5.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bunnygirlgacha5)
                                  for loc_name in get_array([108])]
    #bunnygirlgacha6
    bunnygirlgacha6 = Region("Bunny Girl Gacha 6", player, world)
    bunnygirlgacha6.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bunnygirlgacha6)
                                  for loc_name in get_array([109])]
    #bunnygirlgacha7
    bunnygirlgacha7 = Region("Bunny Girl Gacha 7", player, world)
    bunnygirlgacha7.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bunnygirlgacha7)
                                  for loc_name in get_array([110])]
    #bunnygirlgacha8
    bunnygirlgacha8 = Region("Bunny Girl Gacha 8", player, world)
    bunnygirlgacha8.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bunnygirlgacha8)
                                  for loc_name in get_array([111])]
    #bunnygirlgacha9
    bunnygirlgacha9 = Region("Bunny Girl Gacha 9", player, world)
    bunnygirlgacha9.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bunnygirlgacha9)
                                  for loc_name in get_array([112])]
    #bunnygirlgacha10
    bunnygirlgacha10 = Region("Bunny Girl Gacha 10", player, world)
    bunnygirlgacha10.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bunnygirlgacha10)
                                  for loc_name in get_array([113])]
    #bellesmilkshake
    bellesmilkshake = Region("Belle's Milkshake", player, world)
    bellesmilkshake.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bellesmilkshake)
                                   for loc_name in get_array([85])]
    #devilicious
    devilicious = Region("Devilicious", player, world)
    devilicious.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], devilicious)
                                   for loc_name in get_array([86, 1015, 2015])]
    #whatsadaikon
    whatsadaikon = Region("What's a Daikon", player, world)
    whatsadaikon.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], whatsadaikon)
                              for loc_name in get_array([87, 1022])]
    #bananachest
    bananachest = Region("Banana Chest", player, world)
    bananachest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bananachest)
                              for loc_name in get_array([250])]
    #momopass
    momopass = Region("Momo Pass", player, world)
    momopass.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], momopass)
                              for loc_name in get_array([91])]
    #outofservice
    outofservice = Region("Out of Service", player, world)
    outofservice.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], outofservice)
                              for loc_name in get_array([92])]
    #girlgallery
    girlgallery = Region("Girl Gallery", player, world)
    girlgallery.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], girlgallery)
                              for loc_name in get_array([248, 1023])]
    #boygallery
    boygallery = Region("Boy Gallery", player, world)
    boygallery.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], boygallery)
                              for loc_name in get_array([249, 1024])]
    #priestess
    priestess = Region("Priestess", player, world)
    priestess.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], priestess)
                              for loc_name in get_array([89, 1025])]
    #priest
    priest = Region("Priest", player, world)
    priest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], priest)
                                for loc_name in get_array([90, 1026])]
    #dusty
    dusty = Region("Dusty", player, world)
    dusty.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], dusty)
                              for loc_name in get_array([88, 1027])]
    #behindalley
    behindalley = Region("Behind Alley", player, world)
    behindalley.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], behindalley)
                              for loc_name in get_array([93])]
    #citychaos
    citychaos = Region("City Chaos", player, world)
    citychaos.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], citychaos)
                              for loc_name in get_array([79])]
    #abandonedhome02
    abandonedhome02 = Region("Abandoned Home 02", player, world)
    abandonedhome02.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], abandonedhome02)
                              for loc_name in get_array([134])]
    #abandonedhome01
    abandonedhome01 = Region("Abandoned Home 01", player, world)
    abandonedhome01.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], abandonedhome01)
                                  for loc_name in get_array([135])]
    #abandonedhome6
    abandonedhome6 = Region("Abandoned Home 6", player, world)
    abandonedhome6.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], abandonedhome6)
                                  for loc_name in get_array([136])]
    #abandonedhomegreen
    abandonedhomegreen = Region("Abandoned Home Green", player, world)
    abandonedhomegreen.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], abandonedhomegreen)
                                  for loc_name in get_array([137])]
    #fungalkey
    fungalkey = Region("Fungal Key", player, world)
    fungalkey.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], fungalkey)
                                  for loc_name in get_array([139])]
    #tatiltale
    tatiltale = Region("Tatil Tale", player, world)
    tatiltale.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], tatiltale)
                            for loc_name in get_array([140, 1028])]
    #maidcontract
    maidcontract = Region("Maid Contract", player, world)
    maidcontract.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], maidcontract)
                            for loc_name in get_array([141])]
    #signingbonus
    signingbonus = Region("Signing Bonus", player, world)
    signingbonus.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], signingbonus)
                               for loc_name in get_array([142, 1029])]
    #lonehouse
    lonehouse = Region("Lone House", player, world)
    lonehouse.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], lonehouse)
                               for loc_name in get_array([138])]
    #pipechest
    pipechest = Region("Pipe Chest", player, world)
    pipechest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], pipechest)
                               for loc_name in get_array([143])]
    #sidecoin
    sidecoin = Region("Side Coin", player, world)
    sidecoin.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], sidecoin)
                             for loc_name in get_array([144])]
    #sidechest
    sidechest = Region("Side Chest", player, world)
    sidechest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], sidechest)
                             for loc_name in get_array([145])]
    #sewershop
    sewershop = Region("Sewer Shop", player, world)
    sewershop.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], sewershop)
                             for loc_name in get_array([153, 154, 332])]
    #sewergauntlethp
    sewergauntlethp = Region("Sewer Gauntlet HP", player, world)
    sewergauntlethp.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], sewergauntlethp)
                             for loc_name in get_array([151])]
    #sewergauntletchest
    sewergauntletchest = Region("Sewer Gauntlet Chest", player, world)
    sewergauntletchest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], sewergauntletchest)
                                for loc_name in get_array([152])]
    #ratcostumeroom
    ratcostumeroom = Region("Rat Costume Room", player, world)
    ratcostumeroom.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ratcostumeroom)
                                for loc_name in get_array([148, 149, 150])]
    #ratchelcoin
    ratchelcoin = Region("Ratchel Coin", player, world)
    ratchelcoin.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ratchelcoin)
                              for loc_name in get_array([146])]
    #ratchel
    ratchel = Region("Ratchel", player, world)
    ratchel.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ratchel)
                              for loc_name in get_array([147, 1030])]
    #drwitch
    drwitch = Region("Dr Witch", player, world)
    drwitch.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], drwitch)
                              for loc_name in get_array([155, 156])]
    #drwitchtutorial
    drwitchtutorial = Region("Dr Witch Tutorial", player, world)
    drwitchtutorial.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], drwitchtutorial)
                               for loc_name in get_array([157])]
    #belowgcentrance
    belowgcentrance = Region("Below GC Entrance", player, world)
    belowgcentrance.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], belowgcentrance)
                                  for loc_name in get_array([158])]
    #ghostform
    ghostform = Region("Ghost Form", player, world)
    ghostform.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ghostform)
                                  for loc_name in get_array([176])]
    #gcgroundslime
    gcgroundslime = Region("GC Ground Slime", player, world)
    gcgroundslime.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], gcgroundslime)
                                  for loc_name in get_array([159, 160])]
    #gcraisedslime
    gcraisedslime = Region("GC Raised Slime", player, world)
    gcraisedslime.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], gcraisedslime)
                                  for loc_name in get_array([161])]
    #laddercoin
    laddercoin = Region("Ladder Coin", player, world)
    laddercoin.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], laddercoin)
                                  for loc_name in get_array([164])]
    #hiddenledge
    hiddenledge = Region("Hidden Ledge", player, world)
    hiddenledge.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], hiddenledge)
                                  for loc_name in get_array([165])]
    #gcflipmagicplatform
    gcflipmagicplatform = Region("GC Flip Magic Platform", player, world)
    gcflipmagicplatform.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], gcflipmagicplatform)
                                  for loc_name in get_array([162])]
    #pantyraid
    pantyraid = Region("Panty Raid", player, world)
    pantyraid.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], pantyraid)
                                  for loc_name in get_array([166, 1010, 2010])]
    #ghostshop
    ghostshop = Region("Ghost Shop", player, world)
    ghostshop.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ghostshop)
                                  for loc_name in get_array([167])]
    #ghostshopchest
    ghostshopchest = Region("Ghost Shop Chest", player, world)
    ghostshopchest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ghostshopchest)
                                  for loc_name in get_array([168])]
    #secretgardenkey
    secretgardenkey = Region("Secret Garden Key", player, world)
    secretgardenkey.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], secretgardenkey)
                                  for loc_name in get_array([169])]
    #ghostthimble
    ghostthimble = Region("Ghost Thimble", player, world)
    ghostthimble.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ghostthimble)
                                  for loc_name in get_array([177, 178, 179])]
    #blindjump
    blindjump = Region("Blind Jump", player, world)
    blindjump.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], blindjump)
                                  for loc_name in get_array([163])]
    #willow
    willow = Region("Willow", player, world)
    willow.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], willow)
                                  for loc_name in get_array([180])]
    #gchiddenshrub
    gchiddenshrub = Region("GC Hidden Shrub", player, world)
    gchiddenshrub.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], gchiddenshrub)
                                  for loc_name in get_array([175])]
    #ghostgauntlet
    ghostgauntlet = Region("Ghost Gauntlet", player, world)
    ghostgauntlet.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ghostgauntlet)
                                  for loc_name in get_array([240])]
    #hiddenwall
    hiddenwall = Region("Hidden Wall", player, world)
    hiddenwall.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], hiddenwall)
                                  for loc_name in get_array([170])]
    #alongthepath
    alongthepath = Region("Along The Path", player, world)
    alongthepath.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], alongthepath)
                                  for loc_name in get_array([171])]
    #ghosthiddenspringroom
    ghosthiddenspringroom = Region("Ghost Hidden Spring Room", player, world)
    ghosthiddenspringroom.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ghosthiddenspringroom)
                                  for loc_name in get_array([172])]
    #behindthevines
    behindthevines = Region("Behind The Vines", player, world)
    behindthevines.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], behindthevines)
                                  for loc_name in get_array([173])]
    #ghostboss
    ghostboss = Region("Ghost Boss", player, world)
    ghostboss.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ghostboss)
                                  for loc_name in get_array([181, 182])]
    #acrossboss
    acrossboss = Region("Across Boss", player, world)
    acrossboss.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], acrossboss)
                                  for loc_name in get_array([174])]
    #jhiddenfliproom
    jhiddenfliproom = Region("J Hidden Flip Room", player, world)
    jhiddenfliproom.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], jhiddenfliproom)
                                  for loc_name in get_array([187])]
    #jslimeroom
    jslimeroom = Region("J Slime Room", player, world)
    jslimeroom.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], jslimeroom)
                                  for loc_name in get_array([188])]
    #earlyledge
    earlyledge = Region("Early Ledge", player, world)
    earlyledge.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], earlyledge)
                                  for loc_name in get_array([189])]
    #jspringroom
    jspringroom = Region("J Spring Room", player, world)
    jspringroom.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], jspringroom)
                                  for loc_name in get_array([190, 191])]
    #catshrine
    catshrine = Region("Cat Shrine", player, world)
    catshrine.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], catshrine)
                                  for loc_name in get_array([192])]
    #unluckycat
    unluckycat = Region("Unlucky Cat", player, world)
    unluckycat.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], unluckycat)
                                  for loc_name in get_array([193, 1036])]
    #beastkey
    beastkey = Region("Beast Key", player, world)
    beastkey.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], beastkey)
                                  for loc_name in get_array([194])]
    #jhiddenledge
    jhiddenledge = Region("J Hidden Ledge", player, world)
    jhiddenledge.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], jhiddenledge)
                                  for loc_name in get_array([195])]
    #annahell
    annahell = Region("Annahell", player, world)
    annahell.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], annahell)
                                  for loc_name in get_array([196, 1031])]
    #annahellchest
    annahellchest = Region("Annahell Chest", player, world)
    annahellchest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], annahellchest)
                                  for loc_name in get_array([197])]
    #hiddenhole
    hiddenhole = Region("Hidden Hole", player, world)
    hiddenhole.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], hiddenhole)
                                  for loc_name in get_array([198])]
    #nearshop
    nearshop = Region("Near Shop", player, world)
    nearshop.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], nearshop)
                                  for loc_name in get_array([199])]
    #demonshop
    demonshop = Region("Demon Shop", player, world)
    demonshop.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], demonshop)
                                  for loc_name in get_array([200, 201])]
    #hotguy
    hotguy = Region("Hot Guy", player, world)
    hotguy.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], hotguy)
                                  for loc_name in get_array([202])]
    #farledge
    farledge = Region("Far Ledge", player, world)
    farledge.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], farledge)
                                  for loc_name in get_array([203])]
    #Jhiddenflip
    jhiddenflip = Region("J Hidden Flip", player, world)
    jhiddenflip.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], jhiddenflip)
                                  for loc_name in get_array([204])]
    #demonwings
    demonwings = Region("Demon Wings", player, world)
    demonwings.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], demonwings)
                                  for loc_name in get_array([205, 206])]
    #northcatshrine
    northcatshrine = Region("North Cat Shrine", player, world)
    northcatshrine.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], northcatshrine)
                                  for loc_name in get_array([207])]
    #northcatloot
    northcatloot = Region("North Cat Loot", player, world)
    northcatloot.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], northcatloot)
                                  for loc_name in get_array([208, 209])]
    #clubentrance
    clubentrance = Region("Club Entrance", player, world)
    clubentrance.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], clubentrance)
                                  for loc_name in get_array([210])]
    #undertable
    undertable = Region("Under The Table", player, world)
    undertable.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], undertable)
                                  for loc_name in get_array([211])]
    #badboy
    badboy = Region("Bad Boy", player, world)
    badboy.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], badboy)
                                  for loc_name in get_array([212])]
    #clubdoor
    clubdoor = Region("Club Door", player, world)
    clubdoor.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], clubdoor)
                                  for loc_name in get_array([213])]
    #demonflipchest
    demonflipchest = Region("Demon Flip Chest", player, world)
    demonflipchest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], demonflipchest)
                                  for loc_name in get_array([214])]
    #demonflipcoin
    demonflipcoin = Region("Demon Flip Coin", player, world)
    demonflipcoin.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], demonflipcoin)
                                  for loc_name in get_array([215])]
    #demonthimble
    demonthimble = Region("Demon Thimble", player, world)
    demonthimble.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], demonthimble)
                                  for loc_name in get_array([216, 217])]
    #demongauntlet
    demongauntlet = Region("Demon Gauntlet", player, world)
    demongauntlet.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], demongauntlet)
                                  for loc_name in get_array([218])]
    #clubkey
    clubkey = Region("Club Key", player, world)
    clubkey.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], clubkey)
                                  for loc_name in get_array([219, 220])]
    #clubcat
    clubcat = Region("Club Cat", player, world)
    clubcat.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], clubcat)
                                  for loc_name in get_array([221])]
    #demonbosskey
    demonbosskey = Region("Demon Boss Key", player, world)
    demonbosskey.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], demonbosskey)
                                  for loc_name in get_array([222])]
    #demonboss
    demonboss = Region("Demon Boss", player, world)
    demonboss.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], demonboss)
                                  for loc_name in get_array([223, 224])]
    #tearlycoin
    tearlycoin = Region("T Early Coin", player, world)
    tearlycoin.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], tearlycoin)
                                  for loc_name in get_array([225])]
    #tearlychest
    tearlychest = Region("T Early Chest", player, world)
    tearlychest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], tearlychest)
                                  for loc_name in get_array([226])]
    #thiddenbush
    thiddenbush = Region("T Hidden Bush", player, world)
    thiddenbush.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], thiddenbush)
                                  for loc_name in get_array([227])]
    #thiddenflip
    thiddenflip = Region("T Hidden Flip", player, world)
    thiddenflip.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], thiddenflip)
                                  for loc_name in get_array([228])]
    #birby
    birby = Region("Birby", player, world)
    birby.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], birby)
                                  for loc_name in get_array([333])]
    #thiddenchest
    thiddenchest = Region("T Hidden Chest", player, world)
    thiddenchest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], thiddenchest)
                                  for loc_name in get_array([229])]
    #thiddenledge
    thiddenledge = Region("T Hidden Ledge", player, world)
    thiddenledge.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], thiddenledge)
                                  for loc_name in get_array([230])]
    #secretalcove
    secretalcove = Region("Secret Alcove", player, world)
    secretalcove.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], secretalcove)
                                  for loc_name in get_array([231])]
    #angelstart
    angelstart = Region("Angel Start", player, world)
    angelstart.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelstart)
                                  for loc_name in get_array([232])]
    #angelbush1
    angelbush1 = Region("Angel Bush 1", player, world)
    angelbush1.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelbush1)
                                  for loc_name in get_array([233])]
    #angelbush2
    angelbush2 = Region("Angel Bush 2", player, world)
    angelbush2.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelbush2)
                                  for loc_name in get_array([234])]
    #angelshop
    angelshop = Region("Angel Shop", player, world)
    angelshop.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelshop)
                                  for loc_name in get_array([235, 236, 237])]
    #cloudia
    cloudia = Region("Cloudia", player, world)
    cloudia.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], cloudia)
                                  for loc_name in get_array([238])]
    #angelgauntlet
    angelgauntlet = Region("Angel Gauntlet", player, world)
    angelgauntlet.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelgauntlet)
                                for loc_name in get_array([239])]
    #angelthimble
    angelthimble = Region("Angel Thimble", player, world)
    angelthimble.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelthimble)
                                for loc_name in get_array([241, 242, 243])]
    #belowthimble
    belowthimble = Region("Below Thimble", player, world)
    belowthimble.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], belowthimble)
                                for loc_name in get_array([244])]
    #gabrielleroom
    gabrielleroom = Region("Gabrielle Room", player, world)
    gabrielleroom.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], gabrielleroom)
                                for loc_name in get_array([245, 247])]
    #gabrielle
    gabrielle = Region("Gabrielle", player, world)
    gabrielle.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], gabrielle)
                                for loc_name in get_array([246, 1032])]
    #angelbehindvines
    angelbehindvines = Region("Angel Behind Vines", player, world)
    angelbehindvines.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelbehindvines)
                                for loc_name in get_array([251])]
    #angelflip
    angelflip = Region("Angel Flip", player, world)
    angelflip.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelflip)
                                for loc_name in get_array([252])]
    #angelfeathers
    angelfeathers = Region("Angel Feathers", player, world)
    angelfeathers.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelfeathers)
                                for loc_name in get_array([253])]
    #belowboss
    belowboss = Region("Below Boss", player, world)
    belowboss.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], belowboss)
                                for loc_name in get_array([254, 255])]
    #angelica
    angelica = Region("Angelica", player, world)
    angelica.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], angelica)
                                for loc_name in get_array([256, 257])]
    #fungalthimble
    fungalthimble = Region("Fungal Thimble", player, world)
    fungalthimble.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], fungalthimble)
                                for loc_name in get_array([258, 259])]
    #lowerpit
    lowerpit = Region("Lower Pit", player, world)
    lowerpit.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], lowerpit)
                                for loc_name in get_array([260])]
    #Fflipcoin
    fflipcoin = Region("F Flip Coin", player, world)
    fflipcoin.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], fflipcoin)
                                for loc_name in get_array([261])]
    #fungella
    fungella = Region("Fungella", player, world)
    fungella.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], fungella)
                                for loc_name in get_array([262])]
    #pastfungella
    pastfungella = Region("Past Fungella", player, world)
    pastfungella.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], pastfungella)
                                for loc_name in get_array([263])]
    #hdaikon
    hdaikon = Region("H Daikon", player, world)
    hdaikon.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], hdaikon)
                                for loc_name in get_array([264])]
    #fpastchaos
    fpastchaos = Region("F Past Chaos", player, world)
    fpastchaos.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], fpastchaos)
                                for loc_name in get_array([265])]
    #closedcoins
    closedcoins = Region("Closed Coins", player, world)
    closedcoins.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], closedcoins)
                                for loc_name in get_array([266])]
    #betweenthorns
    betweenthorns = Region("Between Thorns", player, world)
    betweenthorns.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], betweenthorns)
                                for loc_name in get_array([267])]
    #fungalshop
    fungalshop = Region("Fungal Shop", player, world)
    fungalshop.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], fungalshop)
                                for loc_name in get_array([268, 269, 270])]
    #mushroomguard
    mushroomguard = Region("Mushroom Guard", player, world)
    mushroomguard.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], mushroomguard)
                                for loc_name in get_array([271])]
    #fungalgauntlet
    fungalgauntlet = Region("Fungal Gauntlet", player, world)
    fungalgauntlet.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], fungalgauntlet)
                                for loc_name in get_array([272])]
    #bluejelly
    bluejelly = Region("Blue Jelly", player, world)
    bluejelly.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bluejelly)
                                for loc_name in get_array([273])]
    #fungaldoor
    fungaldoor = Region("Fungal Door", player, world)
    fungaldoor.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], fungaldoor)
                                for loc_name in get_array([274])]
    #fungussecret
    fungussecret = Region("Fungus Secret", player, world)
    fungussecret.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], fungussecret)
                                for loc_name in get_array([275])]
    #slimeform
    slimeform = Region("Slime Form", player, world)
    slimeform.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], slimeform)
                                for loc_name in get_array([276])]
    #sckey
    sckey = Region("SCKey", player, world)
    sckey.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], sckey)
                                for loc_name in get_array([277])]
    #slimeentrance
    slimeentrance = Region("Slime Entrance", player, world)
    slimeentrance.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], slimeentrance)
                                for loc_name in get_array([278])]
    #slimesecret
    slimesecret = Region("Slime Secret", player, world)
    slimesecret.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], slimesecret)
                                for loc_name in get_array([279])]
    #loneroom
    loneroom = Region("Lone Room", player, world)
    loneroom.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], loneroom)
                                for loc_name in get_array([280])]
    #silkychest
    silkychest = Region("Silky Chest", player, world)
    silkychest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], silkychest)
                                for loc_name in get_array([281])]
    #silkystone
    silkystone = Region("Silky Stone", player, world)
    silkystone.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], silkystone)
                                for loc_name in get_array([282, 1037])]
    #smalldetour
    smalldetour = Region("Small Detour", player, world)
    smalldetour.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], smalldetour)
                                for loc_name in get_array([283])]
    #subkey
    subkey = Region("Sub Key", player, world)
    subkey.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], subkey)
                                for loc_name in get_array([284])]
    #acrosskey
    acrosskey = Region("Across Key", player, world)
    acrosskey.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], acrosskey)
                                for loc_name in get_array([285])]
    #slimethimble
    slimethimble = Region("Slime Thimble", player, world)
    slimethimble.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], slimethimble)
                                for loc_name in get_array([286, 287])]
    #slimegauntlet
    slimegauntlet = Region("Slime Gauntlet", player, world)
    slimegauntlet.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], slimegauntlet)
                                for loc_name in get_array([288])]
    #nearstone
    nearstone = Region("Near Stone", player, world)
    nearstone.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], nearstone)
                                for loc_name in get_array([289])]
    #secretspringcoin
    secretspringcoin = Region("Secret Spring Coin", player, world)
    secretspringcoin.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], secretspringcoin)
                                for loc_name in get_array([290])]
    #secretspringstone
    secretspringstone = Region("Secret Spring Stone", player, world)
    secretspringstone.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], secretspringstone)
                                for loc_name in get_array([291])]
    #hiddentunnel
    hiddentunnel = Region("Hidden Tunnel", player, world)
    hiddentunnel.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], hiddentunnel)
                                for loc_name in get_array([292])]
    #slimeshop
    slimeshop = Region("Slime Shop", player, world)
    slimeshop.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], slimeshop)
                                for loc_name in get_array([293, 294])]
    #slurp
    slurp = Region("Slurp", player, world)
    slurp.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], slurp)
                                for loc_name in get_array([295])]
    #slurpstone
    slurpstone = Region("Slurp Stone", player, world)
    slurpstone.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], slurpstone)
                                for loc_name in get_array([296])]
    #natasha
    natasha = Region("Natasha", player, world)
    natasha.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], natasha)
                                for loc_name in get_array([297])]
    #slimeboss
    slimeboss = Region("Slime Boss", player, world)
    slimeboss.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], slimeboss)
                                for loc_name in get_array([298, 299])]
    #umiearly
    umiearly = Region("Umi Early", player, world)
    umiearly.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], umiearly)
                                for loc_name in get_array([300])]
    #umisave
    umisave = Region("Umi Save", player, world)
    umisave.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], umisave)
                                for loc_name in get_array([301])]
    #anglerchest
    anglerchest = Region("Angler Chest", player, world)
    anglerchest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], anglerchest)
                                for loc_name in get_array([302])]
    #umiflip1
    umiflip1 = Region("Umi Flip 1", player, world)
    umiflip1.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], umiflip1)
                                for loc_name in get_array([303])]
    #corner
    corner = Region("Corner", player, world)
    corner.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], corner)
                                for loc_name in get_array([304])]
    #dagger
    dagger = Region("Dagger", player, world)
    dagger.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], dagger)
                                for loc_name in get_array([305])]
    #umiflip2
    umiflip2 = Region("Umi Flip 2", player, world)
    umiflip2.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], umiflip2)
                                for loc_name in get_array([306])]
    #mermaidchest
    mermaidchest = Region("Mermaid Chest", player, world)
    mermaidchest.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], mermaidchest)
                                for loc_name in get_array([307])]
    #umichaos
    umichaos = Region("Umi Chaos", player, world)
    umichaos.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], umichaos)
                                for loc_name in get_array([308])]
    #abovesave
    abovesave = Region("Above Save", player, world)
    abovesave.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], abovesave)
                                for loc_name in get_array([309])]
    #octpath
    octpath = Region("Octpath", player, world)
    octpath.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], octpath)
                                for loc_name in get_array([310])]
    #octrina
    octrina = Region("Octrina", player, world)
    octrina.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], octrina)
                                for loc_name in get_array([311])]
    #watergauntlet
    watergauntlet = Region("Water Gauntlet", player, world)
    watergauntlet.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], watergauntlet)
                                for loc_name in get_array([312])]
    #frogpath
    frogpath = Region("Frog Path", player, world)
    frogpath.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], frogpath)
                                for loc_name in get_array([313])]
    #keroku
    keroku = Region("Keroku", player, world)
    keroku.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], keroku)
                                for loc_name in get_array([314, 1038])]
    #frogboss
    frogboss = Region("Frog Boss", player, world)
    frogboss.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], frogboss)
                                for loc_name in get_array([315, 316])]
    #castleoutside
    castleoutside = Region("Castle Outside", player, world)
    castleoutside.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], castleoutside)
                                for loc_name in get_array([317])]
    #castleearly
    castleearly = Region("Castle Early", player, world)
    castleearly.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], castleearly)
                                for loc_name in get_array([318])]
    #gfp
    gfp = Region("GFP", player, world)
    gfp.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], gfp)
                                for loc_name in get_array([319])]
    #gcp
    gcp = Region("GCP", player, world)
    gcp.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], gcp)
                                for loc_name in get_array([320])]
    #jp
    jp = Region("JP", player, world)
    jp.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], jp)
                                for loc_name in get_array([321])]
    #nearchaos
    nearchaos = Region("Near Chaos", player, world)
    nearchaos.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], nearchaos)
                                for loc_name in get_array([322])]
    #chaosshop
    chaosshop = Region("Chaos Shop", player, world)
    chaosshop.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], chaosshop)
                                for loc_name in get_array([323, 324])]
    #scp
    scp = Region("SCP", player, world)
    scp.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], scp)
                                for loc_name in get_array([325])]
    #fp
    fp = Region("FP", player, world)
    fp.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], fp)
                                for loc_name in get_array([326])]
    #bigjump
    bigjump = Region("Big Jump", player, world)
    bigjump.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], bigjump)
                                for loc_name in get_array([327, 328])]
    #pandora
    pandora = Region("Pandora", player, world)
    pandora.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], pandora)
                                for loc_name in get_array([329, 330])]
    #chaosqueen
    chaosqueen = Region("Chaos Queen", player, world)
    chaosqueen.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], chaosqueen)
                                for loc_name in get_array([331])]
    #ending
    ending = Region("Ending", player, world)
    ending.locations += [FlipWitchLocation(player, loc_name, location_table[loc_name], ending) for loc_name in
                         get_array([5])]



    #Put all new regions in square brackets
    regions = [menu, senseihut, senseihutbubble, beatrix, questupgrade1, questupgrade2, questupgrade3, questupgrade4,
               questupgrade5, questupgrade6, questupgrade7, questupgrade8, questupgrade9, questupgrade10, pastthehut,
               secretcave, genesis, genesispromo, belle, rundownhouse, rundownhousesave, mimi, mimihiddenchest,
               goblinapartment, mimicchestkeyroom, bellescowbell, redwine, mancave, beforegreatfairy, greatfairy,
               pastmancave, gerrygatric, hiddenalcove, flipplatform, gobliana, gobliana2, afterchaosfight,
               wwbosskeyroom, wwhiddenspringroom, fairyquest, fairychest, goblinqueen, goblinprincess, wwpostfight,
               toilet, toiletcoin, cabaretcafechest, animalgirlgacha1, animalgirlgacha2, animalgirlgacha3,
               animalgirlgacha4, animalgirlgacha5, animalgirlgacha6, animalgirlgacha7, animalgirlgacha8, animalgirlgacha9,
               animalgirlgacha10, boned, legendarychewtoy, deliciousmilk, deluxemilkshake, cherryaptkey, ratproblem,
               ghosthunters, hauntedbathroom, ectogasm, jellymushroom, boozebunny, helpwanted, vipchest,
               unmarkedhousebubble, angelndemongacha1, angelndemongacha2, angelndemongacha3,
               angelndemongacha4, angelndemongacha5, angelndemongacha6, angelndemongacha7, angelndemongacha8,
               angelndemongacha9, angelndemongacha10, itemshop, itemshoproof, monstergirlgacha1, monstergirlgacha2,
               monstergirlgacha3, monstergirlgacha4, monstergirlgacha5, monstergirlgacha6, monstergirlgacha7,
               monstergirlgacha8, monstergirlgacha9, monstergirlgacha10, fashionshop, clinic, rover, ancientbchest,
               ancientbeing, belowcemetary, ghostcastlekey, bunnyclubq, silkyslimeq, legsofficekey, emotionalbaggage,
               dirtydebut, bunnygirlgacha1, bunnygirlgacha2, bunnygirlgacha3, bunnygirlgacha4, bunnygirlgacha5, bunnygirlgacha6,
               bunnygirlgacha7, bunnygirlgacha8, bunnygirlgacha9, bunnygirlgacha10, bellesmilkshake, devilicious,
               whatsadaikon, bananachest, momopass, outofservice, girlgallery, boygallery, priestess, priest, dusty, citychaos,
               behindalley, abandonedhome02, abandonedhome01, abandonedhome6, abandonedhomegreen, lonehouse, fungalkey, tatiltale, maidcontract,
               signingbonus, pipechest, sidecoin, sidechest, sewershop, sewergauntlethp, sewergauntletchest,
               ratcostumeroom, ratchelcoin, ratchel, drwitch, drwitchtutorial, belowgcentrance, ghostform, gcgroundslime,
               gcraisedslime, laddercoin, hiddenledge, gcflipmagicplatform, pantyraid, ghostshop, ghostshopchest,
               secretgardenkey, ghostthimble, blindjump, willow, gchiddenshrub, ghostgauntlet, hiddenwall, alongthepath,
               ghosthiddenspringroom, behindthevines, ghostboss, acrossboss, jhiddenfliproom, jslimeroom, earlyledge,
               jspringroom, catshrine, unluckycat, beastkey, jhiddenledge, annahell, annahellchest, hiddenhole, nearshop,
               demonshop, hotguy, farledge, jhiddenflip, demonwings, northcatshrine, northcatloot, clubentrance, undertable,
               badboy, clubdoor, demonflipchest, demonflipcoin, demonthimble, demongauntlet, clubkey, clubcat, demonbosskey,
               demonboss, tearlycoin, tearlychest, thiddenbush, thiddenflip, birby, thiddenchest, thiddenledge, secretalcove,
               angelstart, angelbush1, angelbush2, angelshop, cloudia, angelgauntlet, angelthimble, belowthimble, gabrielleroom,
               gabrielle, angelbehindvines, angelflip, angelfeathers, belowboss, angelica, fungalthimble, lowerpit, fflipcoin,
               fungella, pastfungella, hdaikon, fpastchaos, closedcoins, betweenthorns, fungalshop, mushroomguard, fungalgauntlet,
               bluejelly, fungaldoor, fungussecret, slimeform, sckey, slimeentrance, slimesecret, loneroom, silkychest, silkystone,
               smalldetour, subkey, acrosskey, slimethimble, slimegauntlet, nearstone, secretspringcoin, secretspringstone,
               hiddentunnel, slimeshop, slurp, slurpstone, natasha, slimeboss, umiearly, umisave, anglerchest, umiflip1, corner,
               dagger, umiflip2, mermaidchest, umichaos, abovesave, octpath, octrina, watergauntlet, frogpath, keroku, frogboss,
               castleoutside, castleearly, gfp, gcp, jp, nearchaos, chaosshop, scp, fp, bigjump, pandora, chaosqueen, ending,]
    world.regions.extend(regions)

def connect_regions(world: MultiWorld, player:int, source:str, target:str, rule = None):
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)
    connection = Entrance(player, '', sourceRegion)
    if rule:
        connection.access_rule = rule

    sourceRegion.exits.append(connection)
    connection.connect(targetRegion)

def connect(world: World, player: int, used_names: typing.Dict[str, int], source: str, target: str,
            rule: typing.Optional[typing.Callable] = None):
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)

    if target not in used_names:
        used_names[target] = 1
        name = target
    else:
        used_names[target] += 1
        name = target + (' ' * used_names[target])

    connection = Entrance(player, name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)

def get_array(array):
    res = dict()
    for i in array:
        for key, val in location_table.items():
            if int(val)== i+ 300000000:
                res[key]= val
    return res