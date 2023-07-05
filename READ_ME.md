# A bout This Project

This Project creates a discord bot that generates a leader board in discord for Vault Hunters Season 3. This has only been tested on Ubuntu server and not any deployment payed for services for example Apex Hosting or Shockbyte. My friends and I thought It would be cool to keep tabs on vaults run, completions, and Vault Level. We’re not very competitive, but find this intriguing to keep track of.

# Acknowledgments

Special thank you to joshglen for the help with debugging and deployment of the bot and the script. Also another special thank you to Katanitron for help with some of the script logic and debugging.

# Instructions

	•	Download the script and the bot.
	•	Edit the number of players and their ranks in the script.
	•	By default, the script shows the top 3 leveled players, excluding level 100 players who are in the level 100 club.
	•	Modify line 4 in the script to show more or fewer ranks as desired.
	•	Verify the file path to the player snapshots in line 20 of the script.
	•	Ensure that the script and the bot are in the same directory as the Server files for VaultHunters season 3 or at least in the same directory as the server files.
	•	Activate the bot by going to https://discord.com/developers/applications and creating a new application.
	•	Click on "Bot," then "Add Bot," and give it a name.
	•	Set a profile picture for the bot.
	•	Enable "Public Bot," "Presence Intent," "Server Members Intent," and "Message Content Intent" toggles.
	•	Click "Reset Token" to obtain the Discord bot token.
	•	Copy and paste the token into the bot code where it says "DISCORD_BOT_KEY_HERE," making sure to keep the apostrophes.
	•	Go to "OAuth2" in the side menu and click on "URL generator."
	•	Select "Bot" under "scopes" and choose "Administrator" under "Bot Permissions."
	•	Copy the generated link and open it in your browser to invite the bot to your desired server.
	•	If using Ubuntu server, open another screen and launch the bot program.
	•	Check for blue text, indicating that the bot is running.
	•	The bot should become active on the Discord server.
	•	Use the command "!update" to trigger the update. If the command doesn't work, ensure that the bot and the script are in the same location, not inside a folder.


### Disclaimer

This was a side project for me and there might be a more efficient way to code it or the bot. This may receive periodic updates depending on a couple of things. All previous versions of the script and bot will be kept on the github for those that are wanting to use them.
