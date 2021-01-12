# Baseball-Cases

I was approached one day by a client who requested a particular Baseball simulation. The objective was to acquire a distribution of "game states" via Monte Carlo-ish simulation with N number of runs.

It turns out that particular "game states" of Baseball exist. An example of this "game state" is having one player on first base and nobody on second or third (kudos for making "Who's On First" jokes as you read this). There are a finite number of game states that can emerge after the pitcher throws the ball (<b>IMPORTANT</b>: this does <i>NOT</i> include stealing bases... yet). I'll enumerate them explicitly below:

<ul>
<li>
<a id = "1">1.</a>
Batter gets a strike.
</li>

<li>
<a id = "2">2.</a>
Batter goes to first, first goes to second.
</li>

<li>
<a id = "3">3.</a>
Batter goes to second, first goes to third.
</li>

<li>
<a id = "4">4.</a>
Batter goes to third, first goes home (1 point).
</li>

<li>
<a id = "5">5.</a>
Batter hits a home run, first goes home (2 points).
</li>

<li>
<a id = "6">6.</a>
Batter goes to first, first goes to third.
</li>

<li>
<a id = "7">7.</a>
Batter goes to first, first goes home (1 point).
</li>

<li>
<a id = "8">8.</a>
Batter goes to second, first goes home (1 point).
</li>
</ul>

After one of the above valid events (valid for the explicit example aforementioned) occurs, another game state emerges. In other words, these games states are emergent in the game of Baseball.

The question then is to figure out which game state is the most common. One way to answer this question is by using Monte Carlo simulations. My client gave me a list of all the game states labeled with a number from 1-25 (where state 1 is 0 outs and empty bases and state 25 is 3 outs without regard to the bases). Included in this list was all the possible game states one could travel to from the given game state. For example, all the possible accessible game states from state 1 are 2 (batter goes to first), 9 (strike out), 3 (batter goes to second), and 1 again. (You might've noticed that there is no way to access the "batter goes to third" game state. That's correct. Again, this is what the client provided to me.)

The approach was to simply construct a DataFrame using Pandas and traverse it, incrementing a counter every time a particular cell was reached. That was easy enough to set up as it only requires turning a CSV file into a Pandas DF. The rest of the iteration can be understood from the code.
