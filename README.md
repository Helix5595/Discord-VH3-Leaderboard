# About This Project

This Project creates a discord bot that generates a leader board in discord for Vault Hunters Season 3. This has only been tested on Ubuntu server and not any deployment payed for services for example Apex Hosting or Shockbyte. My friends and I thought It would be cool to keep tabs on vaults run, completions, and Vault Level. We’re not very competitive, but find this intriguing to keep track of.

# Acknowledgments

Special thank you to joshglen for the help with debugging and deployment of the bot and the script. Also another special thank you to Katanitron for help with some of the script logic and debugging.

# Instructions

1.	Download the script and the bot.
2.	Edit the number of players and their ranks in the script.
3. 	Modify line 4 in the script to show more or fewer ranks as desired.
    - By default, the script shows the top 3 leveled players, excluding level 100 players who are in the level 100 club.
4.	Verify the file path to the player snapshots in line 20 of the script.
5.	Ensure that the script and the bot are in the same directory as the Server files for VaultHunters season 3 or at least in the same directory as the server files.
6.	Activate the bot by going to https://discord.com/developers/applications and creating a new application.
7.	Click on "Bot," then "Add Bot," and give it a name.
8.	Set a profile picture for the bot.
9.	Enable "Public Bot," "Presence Intent," "Server Members Intent," and "Message Content Intent" toggles.
10.	Click "Reset Token" to obtain the Discord bot token.
11.	Copy and paste the token into the bot code where it says "DISCORD_BOT_KEY_HERE," making sure to keep the apostrophes.
12.	Go to "OAuth2" in the side menu and click on "URL generator."
13.	Select "Bot" under "scopes" and choose "Administrator" under "Bot Permissions."
14.	Copy the generated link and open it in your browser to invite the bot to your desired server.
15.	If using Ubuntu server, open another screen and launch the bot program.
16.	Check for blue text, indicating that the bot is running.
17.	The bot should become active on the Discord server.
18.	Use the command `!update` to trigger the update. If the command doesn't work, ensure that the bot and the script are in the same location, not inside a folder.

# Notes
- The player snapshots (the thing the scripts get there data from) will only update after a vault and will not update with burger levels. So if you burger a level and it isn't showing run a vault then the new level will show.

## Disclaimer

This was a side project for me and there might be a more efficient way to code it or the bot. This may receive periodic updates depending on a couple of things. All previous versions of the script and bot will be kept on the github for those that are wanting to use them.
