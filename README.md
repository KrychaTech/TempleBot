# TempleBot
TempleBot is a discord bot inspired by TempleOS made by Terry A. Davis. <br>
Since his works were dedicated to the public domain, this code has been also made public. <br>
Feel free to change my (horrible) code. <br>

As of january 3th 2024, repl.it has removed legacy website hosting, moving it into a paid feature called "Deployments". as such, if you wish to use this bot you must self host it yourself.
<br>
## Commands
| Command                     | Arguments                        | Example       | Example Output                                                                                                                        | Behaviour                                                                                                   |
|:---------------------------:|:--------------------------------:|:-------------:|:-------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------:|
| t!num                       | $NUM (default: 10)               | t!num 20      | 4                                                                                                                                     | This command generates a random number.                                                                     |
| t!feel                      | none.                            | t!feel        | :)                                                                                                                                    | This command displays a random emotion.                                                                     |
| t!gw (or t!God, t!words)    | $NUM (default: 10)               | t!gw 5        | requirements lament sources occasioned listing                                                                                        | This command generates God Words.                                                                           |
| t!happy                     | $NUM (default: 10)               | t!happy 5     | no_way_dude hooah I_donno wot look_out                                                                                                | This command generates Happy God Words.                                                                     |
| !recipe                     | $NUM (default: 10)               | t!recipe 5    | coulis, Chinese_dates, preserves, white_chocolate, pompano,                                                                           | Generates a "recipe" of $NUM elements.                                                                      |
| t!bible (or t!oracle)       | $QUOTE (if not provided, random) | t!bible Ge1:1 | Ge1:1 In the beginning God created the heaven and the earth.                                                                          | This command searches the Bible for $QUOTE. If not provided, it will get a random quote from the KJV Bible. |
| t!godmusic                  | none.                            | t!godmusic    | Bot sends a WAV file.                                                                                                                 | This command generates a piano song based on random number generation.                                      |
| t!elephant                  | none.                            | t!elephant    | Bot sends an elephant picture.                                                                                                        | This command fetches a random elephant picture from reddit.                                                 |
| t!help                      | none.                            | t!help        | Bot sends a video.                                                                                                                    | This command sends out a video of terry davis.                                                              |
| t!goddrawing (or t!drawing) | none.                            | t!drawing     | Bot sends an image.                                                                                                                   | This command generates a drawing using the Pillow library and a random number generator.                    |
| t!joke                      | none.                            | t!joke        | What's it like to be kissed by a vampire? It's a pain in the neck.                                                                    | This command fetches a random joke using the JokeAPI library.                                               |
| t!quote                     | none.                            | t!quote       | You will be the victim of a bizarre joke.                                                                                             | This command fetches a random fortune.                                                                      |
| t!tadquote                  | none.                            | t!tadquote    | "The CIA must surrender to the IRA in the WWI French rail car. Then, the whole world will build God's temple like the Contact movie." | This command fetches a random (clean) Terry A. Davis Quote.                                                 |

## Hosting
This bot already includes the keep_alive function for **FREE** Repl.it hosting, so the only thing you need to do is setup Uptimerobot and upload the files onto your repl project.
**Update: repl.it has removed legacy hosting, as such this is no longer available. If you wish to run the code now, delete the webserver.py file and remove the keep_alive function from the main file.**

## Output of the command t!drawing
![drawing 1](god-drawing.png)
