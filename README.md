# JamBot-Slack-Bot
A bot I made for slack

#Description
This is a template for anyone who wishes to make a bot for the Slack chat client. It comes with Wolfram query functionality built in. SOME ASSEMBLY REQUIRED. You will need to aquire your own tokens.

#Use
In order to use this bot you need to have a team chat registered with Slack (Slack.com). After you succesfully set that up, you need to add a Custom Integration to your slack chat. This can be accomplished by logging into your slack chat, clicking your Team name in the upper left hand of the chat (In a web browser) and clicking "Apps and Integrations" in the drop down menu that appears. 

A new tab or window will open and take you to the Slack App Directory. From here you must click the "Configure" button in the upper right. Then click the "Custom Integrations" tab. Then click on "Bots" and click "Add Integration". Follow the steps as prompted on the screen and you will be given a Bot Token. 

That token goes in the "bot.py" file where the comment says "YOUR TOKEN GOES HERE"

After you get your bot token, you will need your Wolfram API token. To do this simply sign up at http://products.wolframalpha.com/api/ and register a new application. Once this is completed, Wolfram will give you their API token. Free use of the Wolfram API is limited to 2000 API calls a month. This token goes in the "wolframquery.py" file where the comment says "YOUR TOKEN GOES HERE"

Once you have all of that set up you should be able to run the bot. 

#####NOTE: you will have to invite your bot to the channels you want the bot to respond in. You can do this with the "@<botname>" command within slack.

Commands are issued with a "?" flag. 

In order to query wolfram alpha, for example, you would type "?wa Miles to Inches" and the bot will reply with wolfram's answer.
