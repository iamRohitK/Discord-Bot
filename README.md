# Introduction

* This Discord Bot is basically an **Encourage Bot**
* As the name suggests, the bot responds with a **message of encouragement** whenever someone sends a message containing **sad words**

## Features of this bot

* It can give a random inspirational quote using [zenquotes.io API](https://zenquotes.io/api) when user types **$inspire** into the chat
* User will be able to add encouraging messages (by just typing **$new "message"** into the chat) for the bot to use and the user-submitted messages will be stored in the Repl.it database using Database class of [replit](https://pypi.org/project/replit/) library
* It will respond with an encouragement message whenever someone sends a message containing a sad word
* User can delete encouraging message just by typing **$del "index"** into the chat
* It shows a list of user-submitted messages right from Discord just by typing **$list** into the chat
* Can turn off and on whether the bot responds to sad words just by typing **$responding true** or **$responding false**
* When responding is off, the bot will not gonna respond with message of encouragement