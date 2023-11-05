# TempleBot
TempleBot is a discord bot inspired by TempleOS made by Terry A. Davis. <br>
Since his works were dedicated to the public domain, this code has been also made public. <br>
Feel free to change my (horrible) code. <br>

If you don't want to self-host this bot, you can invite it to your server [here](https://discord.com/api/oauth2/authorize?client_id=1168260312307351584&permissions=100352&scope=bot). <br>
<br>
## Commands
| Command                     | Arguments                        | Example       | Example Output                                               | Behaviour                                                                                                   |
|:---------------------------:|:--------------------------------:|:-------------:|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------:|
| t!num                       | $NUM (default: 10)               | t!num 20      | 4                                                            | This command generates a random number.                                                                     |
| t!feel                      | none.                            | t!feel        | :)                                                           | This command displays a random emotion.                                                                     |
| t!gw (or t!God, t!words)    | $NUM (default: 10)               | t!gw 5        | requirements lament sources occasioned listing               | This command generates God Words.                                                                           |
| t!happy                     | $NUM (default: 10)               | t!happy 5     | no_way_dude hooah I_donno wot look_out                       | This command generates Happy God Words.                                                                     |
| !recipe                     | $NUM (default: 10)               | t!recipe 5    | coulis, Chinese_dates, preserves, white_chocolate, pompano,  | Generates a "recipe" of $NUM elements.                                                                      |
| t!bible (or t!oracle)       | $QUOTE (if not provided, random) | t!bible Ge1:1 | Ge1:1 In the beginning God created the heaven and the earth. | This command searches the Bible for $QUOTE. If not provided, it will get a random quote from the KJV Bible. |
| t!godmusic                  | none.                            | t!godmusic    | Bot sends a WAV file.                                        | This command generates a piano song based on random number generation.                                      |
| t!elephant                  | none.                            | t!elephant    | Bot sends an elephant picture.                               | This command fetches a random elephant picture from reddit.                                                 |
| t!help                      | none.                            | t!help        | Bot sends a video.                                           | This command sends out a video of terry davis.                                                              |
| t!goddrawing (or t!drawing) | none.                            | t!drawing     | Bot sends an image.                                          | This command generates a drawing using the Pillow library and a random number generator.                    |

## Hosting
This bot already includes the keep_alive function for **FREE** Repl.it hosting, so the only thing you need to do is setup Uptimerobot and upload the files onto your repl project.
