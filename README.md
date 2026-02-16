<p>
  <img src="imgs/dashboard.png">
</p>

<p>
  <img src="imgs/plot1.png">
</p>
<h2>Plot 1: Stacked Bar Chart — Coin Flips: Heads vs Tails</h2>

<h3>Purpose:</h3>
<p>
This plot compares the total number of heads and tails between old coins and new coins, broken down by denomination.
</p>

<h3>How it works:</h3>
<ul>
<li>There are two main categories:
    <ul>
        <li>Old Coin</li>
        <li>New Coin</li>
    </ul>
</li>

<li>Each category has two stacked bars:
    <ul>
        <li>Left bar = Heads</li>
        <li>Right bar = Tails (lighter color)</li>
    </ul>
</li>

<li>Each bar is stacked into denominations:
    <ul>
        <li>1 Peso</li>
        <li>5 Peso</li>
        <li>10 Peso</li>
        <li>Others</li>
    </ul>
</li>
</ul>

<h3>What it shows:</h3>
<ul>
<li>The total height of each stacked bar represents the total number of flips.</li>
<li>The colored segments show how much each denomination contributed.</li>
<li>Heads and tails counts are very close, indicating a fair coin toss simulation.</li>
</ul>

<h3>Interpretation:</h3>
<p>
Since heads and tails totals are nearly equal, this supports the probability theory that:
</p>

<p align="center">
P(Heads) ≈ 0.5 &nbsp;&nbsp;&nbsp; and &nbsp;&nbsp;&nbsp; P(Tails) ≈ 0.5
</p>

<hr>

<p>
  <img src="imgs/plot2.png">
</p>

<h2>Plot 2: Pie Chart — Combined Heads and Tails</h2>

<h3>Purpose:</h3>
<p>
This plot shows the overall percentage of heads and tails from all 15 groups combined.
</p>

<h3>How it works:</h3>

<p>Uses total counts calculated by:</p>

<pre><code>full_heads = total_flip_result(..., heads=True)
full_tails = total_flip_result(..., tails=True)
</code></pre>

<p>
Displays percentage of heads and tails.
</p>

<h3>What it shows:</h3>

<p>Example result:</p>

<ul>
<li>Heads: 50.1%</li>
<li>Tails: 49.9%</li>
</ul>

<h3>Interpretation:</h3>

<p>
This confirms that the coin toss simulation behaves like a fair random process.
</p>

<p>
The closer the result is to 50%–50%, the more it follows theoretical probability.
</p>

<hr>

<p>
  <img src="imgs/plot33.png">
</p>

<h2>Plot 3: Horizontal Bar Chart — Wood vs Tiles Comparison</h2>

<h3>Purpose:</h3>

<p>
This compares heads and tails counts between:
</p>

<ul>
<li>Wood coins (Old coins)</li>
<li>Tile coins (New coins)</li>
</ul>

<p>
for each denomination.
</p>

<h3>How it works:</h3>

<p>For each denomination:</p>

<ul>
<li>Wood Heads</li>
<li>Wood Tails</li>
<li>Tiles Heads</li>
<li>Tiles Tails</li>
</ul>

<p>
are shown side by side.
</p>

<h3>What it shows:</h3>

<ul>
<li>Comparison of old vs new coin fairness</li>
<li>Comparison of heads vs tails balance per denomination</li>
</ul>

<h3>Interpretation:</h3>

<p>
If wood and tile coins have similar heads/tails counts, both coin types behave fairly.
</p>

<p>
No significant bias is observed.
</p>

<hr>

<p>
  <img src="imgs/plot4.png">
</p>

<h2>Plot 4: Line Chart — Cumulative Heads Over Time</h2>

<h3>Purpose:</h3>

<p>
This shows how the number of heads increases over time as more flips occur.
</p>

<h3>How it works:</h3>

<p>Uses cumulative sum:</p>

<pre><code>np.cumsum(...)
</code></pre>

<p>
Each line represents a coin type and denomination.
</p>

<ul>
<li>Solid lines = Wood coins</li>
<li>Dashed lines = Tile coins</li>
</ul>

<h3>What it shows:</h3>

<ul>
<li>The number of heads increases steadily over flips</li>
<li>The lines appear approximately linear</li>
</ul>

<h3>Interpretation:</h3>

<p>
This demonstrates the <b>Law of Large Numbers</b>.
</p>

<p>
As the number of flips increases, the observed results approach expected probability.
</p>

<p>
The steady growth confirms randomness without bias.
</p>

<hr>

<h2>Explanation of Key Functions in the Code</h2>

<h3>total_flip_result()</h3>

<p><b>Purpose:</b><br>
Calculates total heads or tails across all 15 groups.
</p>

<p>Uses:</p>

<pre><code>.iloc[-1]
</code></pre>

<p>
This gets the final cumulative count.
</p>

<hr>

<h3>result_per_coin()</h3>

<p><b>Purpose:</b><br>
Adds flip counts from multiple groups.
</p>

<p>Example:</p>

<pre><code>new1_heads = result_per_coin(df1, df2, df3)
</code></pre>

<hr>

<h3>concat_df()</h3>

<p><b>Purpose:</b><br>
Combines multiple flip series and computes cumulative heads or tails over time.
</p>

<p>Uses:</p>

<pre><code>np.cumsum()
</code></pre>

<p>
This produces the cumulative line plot.
</p>

<hr>

<h2>Overall Interpretation of the Experiment</h2>

<ul>
<li>Heads and tails occur with nearly equal probability</li>
<li>Old coins and new coins behave similarly</li>
<li>Different denominations show no significant bias</li>
<li>Results follow expected probability theory</li>
</ul>

<p>
This confirms that the coin toss simulation produces fair and random outcomes.
</p>

<hr>

<h2>Scientific Conclusion</h2>

<p>
The results of the coin toss simulation across 15 groups confirm that the probability of obtaining heads or tails is approximately equal. All visualizations, including stacked bar charts, pie charts, comparison charts, and cumulative line plots, support the theoretical expectation of a fair coin. As the number of flips increases, the observed outcomes converge toward a 50/50 distribution, demonstrating the Law of Large Numbers. No significant bias was observed between old and new coins or between different denominations.
</p>
