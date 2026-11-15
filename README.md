# Party Feud

A Family Feud-style party game you run from a laptop and show on a TV. One window is the game board for the room, a second window is the host's screen with every answer and all the controls. It has buzzer lockout, strikes and steals, double and triple rounds, and a Fast Money round that both teams get to play.

It's a single web page. No install, no account, no server.

**Play it:** https://jgruber92.github.io/party-feud/

Made for a Friendsgiving and shared for other game nights. Not affiliated with the TV show. The survey answers and point values are made up.

## Setting up for game night

1. Plug the laptop into the TV and set the TV as an **extended display**, not a mirror. (Mac: System Settings → Displays → set the TV to "Extended display".)
2. In Chrome, open the game link and drag that window onto the TV. Press **F** for fullscreen. This is the **board**.
3. Open a **second Chrome window** (Cmd+N) on the laptop and go to the same link with `#host` on the end:
   `https://jgruber92.github.io/party-feud/#host`
   This is the **host screen**. It should say "TV is showing: Main game" with a green dot.
4. Set the Mac's sound output to the TV (speaker icon in the menu bar) so the dings and buzzers play through the TV. Sounds come from the host window, so there's nothing to click on the TV.
5. Click on the host window. Your keys and the buzzers land there.

Both windows must be in the **same browser on the same laptop**. That's how they stay in sync. If the host screen shows a red "TV window isn't connected" banner, that's what to check.

## Your game's name

Open **Setup** and type a **Game title**, like "Friendsgiving Feud" or "Super Bowl Feud". It shows at the top of the TV, with the last word in the accent color.

## Buzzers

Any buzzer set that plugs in by USB and **acts like a keyboard** works (each button sends a key press). Open **Setup** (press S), click **Set buzzer** for each team, and press that team's button. No buzzers yet? The defaults are **Z** for the left team and **/** for the right team.

## Running a round

The host screen has a step-by-step box that tells you what to press next. The short version:

| Key | What it does |
| --- | --- |
| **Enter** | Show the question on the TV and arm the buzzers |
| **1–8** | Flip that answer (you can see them all on the host screen) |
| **X** | Strike. On the third strike the other team gets one guess to steal |
| **← / →** | The left or right team plays the round (after the face-off) |
| **[ / ]** | Give the pot to the left or right team (usually automatic) |
| **R** | Re-arm the buzzers for a new face-off |
| **N / P** | Next or previous round |
| **U** | Undo |
| **S** | Setup (team names, buzzers, questions) |
| **F** | Fullscreen |
| **M** | Sound on or off |

**Steals happen on their own.** After the third strike, if the stealing team's guess is on the board, press its number and they take the whole pot. If it isn't, press X and the first team keeps it.

Rounds 1–3 are single points, 4–5 double, 6 and later triple. First team to 300 wins (you can change that in Setup).

## Fast Money

Switch the "On the TV" toggle at the top of the host screen to **Fast Money**. Each team sends two players. Player 1 gets 20 seconds for 5 questions, player 2 gets 25 seconds for the same 5 (player 1's answers are covered on the TV). Each team gets its own 5 questions.

- **Enter** starts the clock. Read the question on your screen.
- **1–8** records which survey answer they gave, **0** for a pass, or type an answer that isn't on the list. Each answer jumps you to the next question while the clock keeps running, and the clock stops on its own after the 5th.
- **D** plays the "already said that" buzzer.
- **Enter** or **Space** then reveals the next answer, then its points. Your screen shows the question again so you can say "When we asked…, you said…"
- **T** pauses or restarts the clock if you need to.

Reach 200 and the TV throws confetti. Fall short and it lets them down gently.

**Moving along:** press **N** (or the big **Next** button) to go from team 1 player 1, to player 2, to team 2 player 1, to player 2. The host screen shows where you are.

**Head-to-head rounds:** when both teams have played, the TV announces who won the Fast Money round and keeps a running "rounds won" count. Press **N** again to start the next round with 10 new questions. The sample set has two rounds; load more in Setup for more.

## Making your own questions with AI

Open **Setup** and use **Load a new question set**:

1. Click **Copy prompt for Claude** and paste it into Claude (or another AI chat). Replace the bracketed part with your theme, inside jokes, or who's coming.
2. Copy the whole reply, paste it into the box, and press **Load questions**.

That loads 10 main game questions and 20 Fast Money questions (two Fast Money rounds) in one go. You can also edit questions by hand in Setup. The format is a question line, then one answer per line ending with its points, with a blank line between questions:

```
Name something you bring to a tailgate
Beer 35
Grill 22
Chairs 18
```

Your questions, team names and scores are saved in that browser, so they're still there next time you open the page.

## Editing the game

The source is `src/game.html`. After changing it, rebuild the playable page:

```bash
python3 build.py
```

That writes `index.html`, which is what GitHub Pages serves. You can also just double-click `index.html` to play offline.

## License

MIT. Use it, change it, share it.
