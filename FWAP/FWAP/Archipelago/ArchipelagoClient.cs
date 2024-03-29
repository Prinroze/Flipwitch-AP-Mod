using System;
using System.Linq;
using System.Threading;
using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Helpers;
using Archipelago.MultiClient.Net.MessageLog.Messages;
using Archipelago.MultiClient.Net.Models;
using Archipelago.MultiClient.Net.Packets;
using BepInEx5ArchipelagoPluginTemplate.Utils;
using Newtonsoft.Json;


namespace BepInEx5ArchipelagoPluginTemplate.Archipelago
{
    public class ArchipelagoClient
    {
        public const string APVersion = "0.4.4";
        private const string Game = "FlipWitch";

        public static bool Authenticated;
        private bool attemptingConnection;

        public static ArchipelagoData ServerData = new ArchipelagoData();
        private DeathLinkHandler DeathLinkHandler;
        private ArchipelagoSession session;
        public int Slot;

        /// <summary>
        /// call to connect to an Archipelago session. Connection info should already be set up on ServerData
        /// </summary>
        /// <returns></returns>
        public void Connect()
        {
            if (Authenticated || attemptingConnection) return;

            try
            {
                session = ArchipelagoSessionFactory.CreateSession(ServerData.Uri);
                SetupSession();
            }
            catch (Exception e)
            {
                Plugin.BepinLogger.LogError(e);
            }

            TryConnect();
        }

        /// <summary>
        /// add handlers for Archipelago events
        /// </summary>
        private void SetupSession()
        {
            session.MessageLog.OnMessageReceived += OnMessageReceived;
            session.Items.ItemReceived += OnItemReceived;
            session.Socket.ErrorReceived += OnSessionErrorReceived;
            session.Socket.SocketClosed += OnSessionSocketClosed;
        }

        /// <summary>
        /// attempt to connect to the server with our connection info
        /// </summary>
        private void TryConnect()
        {
            LoginResult loginResult = null;
            try
            {
                // it's safe to thread this function call but unity notoriously hates threading so do not use excessively
                            loginResult = session.TryConnectAndLogin(
                            Game,
                            ServerData.SlotName,
                            ItemsHandlingFlags.AllItems, // TODO make sure to change this line
                            new Version(APVersion),
                            password: ServerData.Password,
                            requestSlotData: false // ServerData.NeedSlotData
                        );
            }
            catch (Exception e)
            {
                Plugin.BepinLogger.LogError(e);
                HandleConnectResult(new LoginFailure(e.ToString()));
                attemptingConnection = false;
            }
            if (loginResult is LoginSuccessful success) 
            {
                Slot = success.Slot;
            }
        }

        /// <summary>
        /// handle the connection result and do things
        /// </summary>
        /// <param name="result"></param>
        private void HandleConnectResult(LoginResult result)
        {
            string outText;
            if (result.Successful)
            {
                var success = (LoginSuccessful)result;

                ServerData.SetupSession(success.SlotData, session.RoomState.Seed);
                Authenticated = true;                
                DeathLinkHandler = new DeathLinkHandler(session.CreateDeathLinkService(), ServerData.SlotName);
#if NET35
                session.Locations.CompleteLocationChecksAsync(null, ServerData.CheckedLocations.ToArray());
#else
                session.Locations.CompleteLocationChecksAsync(ServerData.CheckedLocations.ToArray());
#endif
                outText = $"Successfully connected to {ServerData.Uri} as {ServerData.SlotName}!";

                Plugin.BepinLogger.LogMessage(outText);
            }
            else
            {
                var failure = (LoginFailure)result;
                outText = $"Failed to connect to {ServerData.Uri} as {ServerData.SlotName}.";
                outText = failure.Errors.Aggregate(outText, (current, error) => current + $"\n    {error}");

                Plugin.BepinLogger.LogError(outText);

                Authenticated = false;
                Disconnect();
            }

            ArchipelagoConsole.LogMessage(outText);
            attemptingConnection = false;
        }

        /// <summary>
        /// something we wrong or we need to properly disconnect from the server. cleanup and re null our session
        /// </summary>
        private void Disconnect()
        {
            Plugin.BepinLogger.LogDebug("disconnecting from server...");
#if NET35
            session?.Socket.Disconnect();
#else
            session?.Socket.DisconnectAsync();
#endif
            session = null;
            Authenticated = false;
        }

        /// <summary>
        /// we received and need to handle a message from the server
        /// </summary>
        /// <param name="message">the received server message</param>
        private void OnMessageReceived(LogMessage message)
        {
            Plugin.BepinLogger.LogMessage(message);
            ArchipelagoConsole.LogMessage(message.ToString());
        }

        public void SendMessage(string message)
        {
            session.Socket.SendPacketAsync(new SayPacket { Text = message });
        }

        /// <summary>
        /// we received an item so reward it here
        /// </summary>
        /// <param name="helper">item helper which we can grab our item from</param>
        private void OnItemReceived(ReceivedItemsHelper helper)
        {
            var receivedItem = helper.DequeueItem();

            if (helper.Index < ServerData.Index) return;

            ServerData.Index++;
            Plugin.BepinLogger.LogMessage($"Received Item: {JsonConvert.SerializeObject(receivedItem)}");
            string name = session.Items.GetItemName(receivedItem.Item);
            Plugin.BepinLogger.LogMessage($"Receiving item ID {receivedItem.Item}.  Name is {name}.  Slot is {receivedItem.Player}.  Location is {receivedItem.Location}.");
            // TODO reward the item here
            // if items can be received while in an invalid state for actually handling them, they can be placed in a local
            // queue to be handled later
        }

        /// <summary>
        /// something went wrong with our socket connection
        /// </summary>
        /// <param name="e">thrown exception from our socket</param>
        /// <param name="message">message received from the server</param>
        private void OnSessionErrorReceived(Exception e, string message)
        {
            Plugin.BepinLogger.LogError(e);
            ArchipelagoConsole.LogMessage(message);
        }

        /// <summary>
        /// something went wrong closing our connection. disconnect and clean up
        /// </summary>
        /// <param name="reason"></param>
        private void OnSessionSocketClosed(string reason)
        {
            Plugin.BepinLogger.LogError($"Connection to Archipelago lost: {reason}");
            Disconnect();
        }

        public void LocationSend(int location) 
        {
            session.Locations.CompleteLocationChecks(location);
        }

        public int GetItemQuantity(long item)
        {            
            int counter = 0;
            foreach(NetworkItem networkitem in session.Items.AllItemsReceived) 
            {
                Plugin.BepinLogger.LogMessage("Test1");
                Plugin.BepinLogger.LogMessage(networkitem.Item);
                if (networkitem.Item == item)
                    counter++;
            }
            Plugin.BepinLogger.LogMessage("Test2");
            return counter;
        }
        
        public bool ReceiveNextItem()
        {
            if (!session.Items.Any()) return false;
            NetworkItem networkItem = session.Items.DequeueItem();
            Plugin.BepinLogger.LogMessage($"Received Item: {JsonConvert.SerializeObject(networkItem)}");
            string name = session.Items.GetItemName(networkItem.Item);
            Plugin.BepinLogger.LogMessage($"Receiving item ID {networkItem.Item}.  Name is {name}.  Slot is {networkItem.Player}.  Location is {networkItem.Location}.");
            return true;
        }
                    
    }
}