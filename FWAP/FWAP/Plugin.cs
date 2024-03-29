using Archipelago.MultiClient.Net.Packets;
using BepInEx;
using BepInEx.Logging;
using BepInEx5ArchipelagoPluginTemplate.Archipelago;
using BepInEx5ArchipelagoPluginTemplate.Utils;
using FWAP.Data;
using HarmonyLib;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using UnityEngine;
using static System.Collections.Specialized.BitVector32;

namespace BepInEx5ArchipelagoPluginTemplate
{
    [BepInPlugin(PluginGUID, PluginName, PluginVersion)]
    public class Plugin : BaseUnityPlugin
    {
        public const string PluginGUID = "com.yourName.projectName";
        public const string PluginName = "projectName";
        public const string PluginVersion = "0.1.0";

        public const string ModDisplayInfo = "ProjectName v0.1.0";
        private const string APDisplayInfo = "Archipelago v{ArchipelagoClient.APVersion}";
        public static ManualLogSource BepinLogger;
        public static ArchipelagoClient ArchipelagoClient;

        private void Awake()
        {
            Harmony harmony = new Harmony("2");

            //MethodInfo original = AccessTools.Method(typeof(ChestItemDrop), "giveItem");

            //MethodInfo patch = typeof(Patch).GetMethod("Prefix");

            MethodInfo original = AccessTools.Method(typeof(SwitchDatabase), "givePlayerItem");
            MethodInfo patch = AccessTools.Method(typeof(QuestPatch), "GivePlayerItemPatched");


            harmony.Patch(original, new HarmonyMethod(patch));
            //harmony.PatchAll(typeof(Patch));
            // Plugin startup logic
            BepinLogger = Logger;
            ArchipelagoClient = ClientFactory.Get();
            ArchipelagoConsole.Awake();
            

            BepinLogger.LogInfo($"{ModDisplayInfo} loaded!");
            string contents = File.ReadAllText("Prin.APFW");
            var root = JObject.Parse(contents);
            var values = root["slot_data"].ToObject<DataObject>();
            Plugin.BepinLogger.LogMessage("First " + values.locations[0] + ":" + values.items[0]);
        }

        private void OnGUI()
        {
            // show the mod is currently loaded in the corner
            GUI.Label(new Rect(16, 16, 300, 20), ModDisplayInfo);
            ArchipelagoConsole.OnGUI();

            string statusMessage;
            // show the Archipelago Version and whether we're connected or not
            if (ArchipelagoClient.Authenticated)
            {
                // if your game doesn't usually show the cursor this line may be necessary
                // Cursor.visible = false;

                statusMessage = " Status: Connected";
                GUI.Label(new Rect(16, 50, 300, 20), APDisplayInfo + statusMessage);
            }
            else
            {
                // if your game doesn't usually show the cursor this line may be necessary
                // Cursor.visible = true;

                statusMessage = " Status: Disconnected";
                GUI.Label(new Rect(16, 50, 300, 20), APDisplayInfo + statusMessage);
                GUI.Label(new Rect(16, 70, 150, 20), "Host: ");
                GUI.Label(new Rect(16, 90, 150, 20), "Player Name: ");
                GUI.Label(new Rect(16, 110, 150, 20), "Password: ");

                ArchipelagoClient.ServerData.Uri = GUI.TextField(new Rect(150, 70, 150, 20),
                    ArchipelagoClient.ServerData.Uri);
                ArchipelagoClient.ServerData.SlotName = GUI.TextField(new Rect(150, 90, 150, 20),
                    ArchipelagoClient.ServerData.SlotName);
                ArchipelagoClient.ServerData.Password = GUI.TextField(new Rect(150, 110, 150, 20),
                    ArchipelagoClient.ServerData.Password);

                // requires that the player at least puts *something* in the slot name
                if (GUI.Button(new Rect(16, 130, 100, 20), "Connect") &&
                    !ArchipelagoClient.ServerData.SlotName.IsNullOrWhiteSpace())
                {
                    ArchipelagoClient.Connect();
                }
            }
            // this is a good place to create and add a bunch of debug buttons
        }
    }
    /*[HarmonyPatch(typeof(ChestItemDrop))]
    [HarmonyPatch("giveItem")]
    class Patch
    {
        static bool Prefix(ChestItemDrop __instance)
        {
            //Debug.Log(__instance.itemName.ToString());
            //Debug.Log(__instance.name.ToString());
            //Debug.Log(__instance.tag.ToString());
            /*switch (__instance.itemName)
            {
                case "MimicKey":
                    __instance.itemName = "GhostTransform";
                    break;
                case "BlackWitchCostume":
                    __instance.itemName = "FortuneCat";
                    break;

            }
            int location = FlipwitchDictionary.locations.FirstOrDefault(x => x.Value == __instance.itemName).Key;
            //Code to check JSON goes here
            string contents = File.ReadAllText("Prin.APFW");
            var root = JObject.Parse(contents);
            var values = root["slot_data"].ToObject<DataObject>();

            if (values.locations == null) 
            {Plugin.BepinLogger.LogMessage("Is Null");} 
            else 
            {Plugin.BepinLogger.LogMessage("Isn't Null");}
            int index = values.locations.IndexOf(location);
            Plugin.BepinLogger.LogMessage(index);
            if (index == -1) 
            {
                Plugin.BepinLogger.LogMessage("Something went wrong");                
                return true;            
            }
            int item = values.items[index];
            Plugin.BepinLogger.LogMessage(item);

            __instance.itemName = FlipwitchDictionary.items[item];
            
            return true;
        }*/    


    
    class QuestPatch
    {
        [HarmonyPatch(typeof(SwitchDatabase), "givePlayerItem")]
        [HarmonyPrefix]
        static bool GivePlayerItemPatched(SwitchDatabase __instance, string __0, ref string itemName /*bool skipPopup = false, Action onPopupCloseCallback = null*/)
        {
            Plugin.BepinLogger.LogMessage(__0);
            int location = FlipwitchDictionary.locations.FirstOrDefault(x => x.Value == __0).Key;
            //Code to check JSON goes here
            string contents = File.ReadAllText("Prin.APFW");
            var root = JObject.Parse(contents);
            var values = root["slot_data"].ToObject<DataObject>();

            if (values.locations == null)
            { Plugin.BepinLogger.LogMessage("Is Null"); }
            else
            { Plugin.BepinLogger.LogMessage("Isn't Null"); }
            int index = values.locations.IndexOf(location);
            Plugin.BepinLogger.LogMessage(index + "-" + location);
            if (index == -1)
            {
                Plugin.BepinLogger.LogMessage("Something went wrong");
                return true;
            }
            int item = values.items[index];
            Plugin.BepinLogger.LogMessage(item);

            itemName = FlipwitchDictionary.items[item - 300000000];                      
                ArchipelagoClient archipelagoClient = ClientFactory.Get();
                archipelagoClient.LocationSend(location);
                archipelagoClient.SendMessage("Check please");
                archipelagoClient.SendMessage(location.ToString());
                       
            

            string progressive = GetNextProgressive(item);
            if (progressive != "")
                itemName = progressive;
            Plugin.BepinLogger.LogMessage(progressive);
            while (archipelagoClient.ReceiveNextItem())
            {
                
            }
            if (itemName == "coin")
                return false;
                //itemName = "GoblinHeadshot";
            return true;
            
        }

        static string GetNextProgressive(long item)
        {
            int count = ClientFactory.Get().GetItemQuantity(item);
            Plugin.BepinLogger.LogMessage(count.ToString());
            Plugin.BepinLogger.LogMessage(item.ToString());
            //int count = 1;
            switch (item)
            {
                case 300000080:
                    if (count == 0)
                    {                        ;
                        return "GoblinHeadshot";
                    }

                    else if (count == 1)
                    {                        
                        return "GoblinBusinessCard";
                    }

                    else if (count == 2)
                    {
                        return "GoblinApartmentKey"; //Fix name 
                    }

                    else if (count == 3)
                    {
                        return "GoblinModelLuggage"; //Fix name?
                    }

                    break;

                case 300000082:
                    if (count == 0) {return "HellishDango";} //name

                    else if (count == 1) { return "HeavenlyDaikon"; } //name

                    break;

                case 300000076:
                    if (count == 0) { return "Cowbell"; }

                    else if (count == 1) { return "DeliciousMilk"; } //Fix Name

                    else if (count == 2) { return "DeluxeMilkshake"; } //Fix Name
                    
                    else if (count == 3) { return "CherryAptKey"; } //Fix Name

                    break;

                case 300000088:
                    if (count == 0) { return "AngelLetter";}

                    else if (count == 1) { return "DemonLetter";} //name?

                    break;

                case 300000095:
                    if (count == 0) { return "FungalKey"; } //right item?

                    else if (count == 1) { return "FungalDeed"; } //name

                    break;

                case 300000101:
                    if (count == 0) { return "playerWandLevel"; } //name and number

                    else if (count == 1) { return "playerWandLevel"; }

                    break;
            }
            return "";
        }
    }

    public class Shuffle
    {
        List<string> items = new List<string> { "GhostTransform", "FortuneCat" };
        List<string> chest = new List<string> { "ww_mimic", "ww_coins_savestatue" };
        public void findchests()
        {
            GameObject.FindObjectsOfType(Type.GetType("ChestItemDrop", false, true));
        }


    }
    public class DataObject
    {
        public List<int> locations { get; set; }
        public List<int> items { get; set; }
    }

    public static class ClientFactory
    {
        public static ArchipelagoClient Client;

        public static ArchipelagoClient Get()
        {
            if (Client == null)
                Client = new ArchipelagoClient();
            return Client;
        }
    
    }
}