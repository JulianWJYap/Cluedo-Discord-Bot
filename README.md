A simple bot to assist in simulating a Cluedo Game, based on the Cluedo Card Game.

The expected environment to use this bot is a special cluedo discord channel where players can facilitate the game (Example, a #cluedo channel. 

Using /cluedo will start a game by shuffling and sending the cards to all players mentioned. 
/cluedo @username @username

The objective of the game is to be the first to guess the Suspect, Weapon, Location.
Each player will be DMed the cards that are NOT including the real suspect, weapon, location.
Each turn the player can ask someone to show them one of two cards or make the final guess. Getting the guess wrong will eliminate the player.
In the cluedo channel, the players can converse to ask the player to show a card, the card can be sent to the player by using DMing to the cluedo bot with /clue_send, which will pass the message to the other player.

Example: /clue_send @username I have a Knife!

Once a player makes a guess, they can use the /get_answer command at the cluedo channel to show a spoiler tagged answer. The guessing player should open the spoiler message to check if they were wrong. 
If the guess was wrong the game continues. 
