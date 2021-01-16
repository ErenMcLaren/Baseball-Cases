# Baseball-Cases

I was approached one day by a client who requested a particular Baseball simulation. The objective was to acquire a distribution of "game states" via Monte Carlo-ish simulation with N number of runs.

It turns out that there are particular "game states" in Baseball. An example of a "game state" is having one player on first base and nobody on second or third with two outs total (kudos for making "Who's On First" jokes as you read this). There are a finite number of game states that can emerge after the pitcher throws the ball (<b>IMPORTANT</b>: this does <i>NOT</i> include stealing bases or pitching balls yet). I'll enumerate the possibilities explicitly below:

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

I ended up sending these results to my client:

||2|3|4|5|6|7|8|9|10|11|12|
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|1|29069|58213|87050|115615|144968|173948|144954|116058|86528|58248|29023|
|2|8346|16606|24827|32967|41537|49304|41103|33053|24751|16333|8359|
|3|1702|3504|5317|6995|8750|10454|8634|7130|5301|3512|1804|
|4|0|0|0|0|0|0|0|0|0|0|0|
|5|1915|3773|5771|7676|9427|11346|9458|7589|5731|3792|1918|
|6|1262|2592|3798|5168|6369|7667|6406|5185|3822|2562|1224|
|7|632|1401|2023|2654|3343|3909|3271|2717|2017|1343|694|
|8|629|1319|1961|2545|3418|4024|3343|2621|1904|1317|652|
|9|19668|39523|58488|79019|98449|118159|97899|78800|59069|39545|19687|
|10|10465|21272|31404|42193|52659|63372|52918|42215|31561|21379|10605|
|11|2529|5133|7641|10023|12509|15104|12607|10059|7547|5038|2510|
|12|0|0|0|0|0|0|0|0|0|0|0|
|13|3730|7337|11074|14708|18657|22283|18302|14759|11154|7344|3585|
|14|2430|4909|7554|10100|12445|15024|12385|10069|7223|5069|2489|
|15|1391|2602|4133|5365|6841|8178|6707|5553|4119|2696|1385|
|16|1547|3266|4990|6581|7935|9822|8115|6522|4943|3249|1510|
|17|13808|27441|41645|55164|68954|82748|68887|55591|41243|27673|13971|
|18|11209|22635|33653|44979|55936|67110|55721|44273|33557|22180|11039|
|19|2800|5573|8450|11456|14148|16942|14250|11462|8604|5740|2864|
|20|208|428|639|844|1094|1291|1096|853|643|430|206|
|21|5065|10258|15123|20115|25128|30449|25156|20252|15352|10187|5196|
|22|3490|6886|10540|13841|17265|20770|17157|13726|10347|6950|3461|
|23|1918|3805|5826|7697|9713|11392|9555|7613|5755|3855|1924|
|24|2509|5135|7926|10406|13080|15742|13090|10402|7897|5219|2652|


