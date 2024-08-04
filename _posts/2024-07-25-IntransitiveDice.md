---
title: 'Intransitive Dice: How to express mathematics'
date: 2024-07-25
permalink: /posts/2024/07/IntransitiveDice/
tags:
  - Easy
  - Probability
  - Analytical
---

How to discuss a intransitive dice problem in a mathematical way and what can we prove about it?

I've recentently took part in a work that discusses the problem of intransitive dice and I wnated to share some of the insights we had and how we dealt with the problem. We did arrive in some interesting results but left a lot of questions untouched. In sharing this, I hope to leave the door for someone else who's intesrested to use from our work and advanced it. You can check the mathematical details directly at [Intransitive Dice](/publication/CLT-Intransitive-Dice).


Paper, Rock, Scissors
---------------------

<img src="/images/posts/IntransitiveDices/Comparing.png" alt="Comparing two dices"
  title="Comparing two dices" style="float:right; width: 40%; margin=10px;"/>

Here is a far fetched question you may have encountered before: Can we play rock, paper or scissors with dice? On the first level, this question is asking us if we can have a set of three dice such that each die beat each other circularly. In other words, if we have three dice, A, B and C, can we have a set such that A beats B, B beats C and C beats A? This hints us at a set of intransitive dice; and I'll say now that they do exist. But first, we need to know how to compare dice. Suppose two dice A and B such as the ones in the image. A has faces 1, 2, 4 and B has faces 1, 2, 3. We will say that A beats B if, from the nine possible outcomes of throwing both dice, A wins B more times than B wins over A. Otherwise, we say that B beats A. In this case, A beats B four out of nine times and B beats A three out of nine times - the rest of outcomes are ties. We say, in this case, that \\( A \triangleright B\\). So ok, to prove this first affirmation - that such intransitive set exists - we only need an example. Consider the following set

<p style="text-align:center">
<img src="/images/posts/IntransitiveDices/ExemploTres.png" alt="Example"
  title="Comparing two dices" style="block; width: 70%; margin=10px;"/>
</p>

Here, it is still easy enough to see, by going over all possible outcomes, that \\(A \triangleright B \triangleright C \triangleright A\\). Which means that we have an intransitive set of three dice. This is enough to assert about the existence of an intransitive set. However, there is still an alternative interpretation to the rock, paper and scissors question: Is there a set of three dice such that A always beats B, B always beats C and C always beats A? This is a bit trickier. Of course we can see that, for dice with three side, this can not be the case. But what if we take dice with infinetely many faces? Are you sure this is still the case? Well, if you are, congratulations. We indeed can not have such set of dice. This results follows directly from the fact that if \\(p(A)\\) is a realization of the random variable that represents the face of dice A, then for an arbitrary \\(\epsilon > 0\\), if

$$
\mathbb{P}(p(A) > p(B)) = 1 - \epsilon, 
$$ 

and

$$
\mathbb{P}(p(B) > p(C)) = 1 - \epsilon,
$$

we must have that

$$
\mathbb{P}(p(A) > p(C)) < 2\epsilon.
$$

which is a shame. However, we can still do some interesting things. There is an alternative game of rock, paper and scissors called rock, paper, scissors, lizard, Spock. In this game, we have five elements and the rules are the following: Rock crushes scissors, scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock. Well.... ok, some weird rules. We can still have a set of dice that emulates the behaviour of those characters, although not deterministicaly. This is illustrated in the image below.

<p style="text-align:center">
<img src="/images/posts/IntransitiveDices/PedraPapelTesoura.png" alt="Rock Paper Scissors"
  title="Area Estimation" style="display: block; width: 100%; margin=10px;"/>
</p>

The dice are getting complicated
---------------------------

Maybe you trusted me when I said the former dice had the properties I said they would have. Maybe you checked this result, however I wouldn't assume so. The dice are getting complicated and counting all possible encounters is getting out of hand. Suppose for example the following set of dice

<p style="text-align:center">
<img src="/images/posts/IntransitiveDices/Example.png" alt="Example of cicle"
  title="Example of cicle" style="width: 60%; margin=10px;"/>
</p>

Howto check if it is intransitive? Counting encounters by hand would be hellish. Well, a way to do it is to simulate the dice. 

<img src="/images/posts/IntransitiveDices/HistogramaExemplo.png" alt="Example Simulation"
  onmouseover="this.src='/files/posts/IntransitiveDice/ABCDices.gif'"
  onmouseout="this.src='/images/posts/IntransitiveDices/HistogramaExemplo.png'"
  title="Example Simulation" style="float:right; width: 50%; margin=10px;"/>

We can throw the dice a large number of times and count the number of times each dice wins over the other. This is illustrated in the simulation below. I don't think this will be enough to convince you of the intransitivity of the set of dice, much less of the results I want to show you next. Although this will be an usefull tool, I promise we won't relie on it. We need some mathematical language as to model this dice and its interactions. With this tool, I hope to be able to clarify when does these sets of dice exists and how many of them there are. This is the goal of the next sections.

Words or how to express dice set
=======

We first set the model of dice we want to consider. We will consider sets of fair dice, that is, dice which the faces are equally likely to be thrown.  Also, we won't allow for faces to be shared between two dice neither for a die to have repeating faces. The restriction of no
repeated faces is of particular interest since it enables the use the here denominated string representation.

A little note on fair dice
---------------------------

Although we are considering fair dice, it is not difficult to adapt some results for unfair dice. This is because we can think of the weights of faces as a repetition. If a die with three faces a, b and c has weights 1, 1.2 and 1.5 we can think of it, without loss of generality, as a die with with 10 a's + 12 b's + 15 c's, all equally likely to be thrown. 

<p style="text-align:center">
<img src="/images/posts/IntransitiveDices/weights.png" alt="Example of weighted dice"
  title="Example of weighted dice" style="width: 80%; margin=10px;"/>
</p>


<img src="/images/posts/IntransitiveDices/weightsTable.png" alt="weights table"
  title="weights table" style="float: right; width: 40%; margin=10px;"/>

With this idea we can actually prove the existence (or non existence) of all sets of intransitive dice with weighted faces. If \\(m\\) is the number of dice and \\(n\\) the number of faces, we can prove the existence of sets of intransitive dice for all \\(m\\) and \\(n\\) except for the case where \\(n = 1, 2, 3\\), when it does not exist a set of intransitive dice. Those cases are illustrades in the table to the right.

Getting back on strings
---------------------------

Suppose that \\(D^{(1)}, D^{(2)}, \dots, D^{(m)}\\) are honest \\(n\\)-sided dice such that there are no repeating values on the faces through all dice. Therefore, it is possible to sort all the faces of the dice by its value and create a descending sequence that is given by some permutation of the faces of \\(D^{(1)}, D^{(2)}, \dots, D^{(m)}\\). This process can generate a unique string that represents the set of dice. This process, for three 4-sided dice, is represented in the following figure. 

<p style="text-align:center">
<img src="/images/posts/IntransitiveDices/Palavras.png" alt="Words"
  title="Words representation" style="width: 80%; margin=10px;"/>
</p>

Note that this sequence makes explicit that, when comparing the faces of the dice, one only cares about the relative position of the value in this sequence created. Therefore it is possible to exchange values by some symbolic representation of the dice the value belongs to without losing the information necessary to compare the dice. With the string, to compare die \\(D^{(2)}\\) to \\(D^{(1)}\\) is to sum how many letters \\(s^{(1)}\\) are to the right of every letter \\(s^{(2)}\\). The result is how many possible victories \\(D^{(2)}\\) has over \\(D^{(1)}\\). This relation \\(D^{(1)} \triangleright D^{(2)}\\) has a natural translation when comparing strings; therefore, the same notation may also be used in this context.

In the depiction, the obtained string uses a, b, and c to represent values of the respective  A, B, and C die. This gives \\(abccabbcaabc\\). It is possible to extend this process to any number of dice with any number of faces, given that they fulfill the requirement of not repeating values between them or in themselves.
            
To compare only two dice of the string, it is enough to remove all letters that are not representative of the dice of interest, and without loss, one can compare the two within the sub-sequence created. In the example given, to compare the dice A and B, analyze the sub-sequence generated by removing the c's: \\( ab\textcolor{red}{c}\textcolor{red}{c}abb\textcolor{red}{c}aab\textcolor{red}{c}\\) \\(\to\\) \\(ababbaab\\). Again, the problem is resolved by comparing the relative position of the letter in the string. Sum how many b's are to the right of every a to obtain the number of victories of a over b and vice-versa.

This is enough to understand what follows.

When does it exist?
=======

We first try to determine when does such a set exists. We need to establish a few results before we can answer this question. I won't mathematically prove the results as it is already well established in our work, I will however give a general idea.

1. **Symmetry**: If the string representing the set of dice is symmetric, then, no dice beats any other and they all tie. This is very natural because if a string is symmetric, it can be written as the concatenation of a string and what we call it's inverse. This means that the number of victories of one die over the other is the same as the number of victories of the other die over the first. Therefore, they tie.

2. **Extension on the number of faces**: If we have a set of dice that is intransitive, then we can add two faces to each of the dice and still have an intransitive set. This is because we can add two extra letters of each die concatenating a neutral string to the main word. Note that a neutral string is composed of this two extra letters of each die.

3. **Extension on the number of dice**: If we have a set of dice that is intransitive, then we can add a dice to the set and still have an intransitive set. This is because we can add a new letter in the string (other die) to the rigth of every 'a', for example. In this way, this new letter will have the same relation as 'A' to the rest of the set but will loose to 'A'. Creating, thus, a new intransitive set. 

4. **Non-existence**: there are no intransitive sets of three dice with two faces. This is straightforward to see.

<img src="/images/posts/IntransitiveDices/BaseExistencia.png" alt="Existence Examples"
  title="Existence Example" style="float: left; width: 60%; margin=10px;"/>

We now only need two examples to deermine the existence of sets of intransitive dice for all number of faces and all number of dice. Using the image displayed with examples, we can see that there is a set with three dice with three faces. This is enough to prove that there is a set of three-sided intransitive dice for all possible number of dice using the result 3. We can also use the result 2 to prove that all set of odd-sided intransitive dice must exist, for every number of dice. In the same manner, we use the second example to show that all sets of even-sided intransitive dice must exist, for every number of dice. This is enough to prove the existence of all sets of intransitive dice but the ones with two faces.

<img src="/images/posts/IntransitiveDices/tableExistencia.png" alt="Existence"
  title="Existence" style="float: right; width: 40%; margin=10px;"/>

We therefore show, using simple techniques, that there are sets of intransitive dice for all possible number of dice and faces, except for the case where the dice have two faces. This is a very interesting result and comes directly from the representation we choose to use. This is one of the many advantages of a good model or representation when trying to prove a result in mathematics. However, we do not stop here. We can also determine how many sets of intransitive dice there are for each number of dice and faces. This is the goal of the next section.

How many are there?
=======

This is harder. To count how many strings can be classified as intransitive, we would have to identify some properties in the strings that we couldn't so far see. So far as we know, this isn't straightforward. However, we do have some results in this direction. To get a feeling of the behaviour of the number of intransitive sets, we can simulate the number of intransitive sets for a given number of dice and faces. This is only possible for sets with few faces as the number of possible outcomes quickly gets out of hand. The table shows how many intransitive sets \\(I(n)\\) ouof the total amount of sets \\(D(n)\\) of three dice with a given number of faces we can have up to 10 faces.

<img src="/images/posts/IntransitiveDices/RatioIntransitivee.png" alt="Quantidade"
  title="Quantidade" style="float: right; width: 50%; margin=10px;"/>

This give us two main informations about the sequence \\(I(n)/D(n)\\): Firstly that it decreases fast as the number of faces increment. Secondly that it has two distinct curves of behaviour that seem to converge, one for the dice with odd-number of faces and other for the dice with even-number of faces. This is mostly bacause of the symmetry properties of a string that can't express in odd-faced dice. Iw we wish to see how this behaviour extends to larger number of faces, we can't compute deterministically the quantities. We will have to perform a stochastic orientered simulation of these dice. This is easy enough if we know how to mount and compare strings. Using this idea we extract the following curve.

<p style="text-align:center">
<img src="/images/posts/IntransitiveDices/curves.jpg" alt="Curves"
  title="Curves" style="width: 90%; margin=10px;"/>
</p>

This strongly suggests that the ratio of intransitive sets to the total amount of sets of dice with a given number of faces converges to zero. Mathematically we can show that \\(I(m+n) \geq I(m)I(n)\\) by a combinatorial argument. This gives us, by feketes lemma, that 

$$
\lim_{n \to \infty} \frac{\log(I(n))}{n} = L
$$

or equivalently that

$$
I(n) = e^{nL + o(n)}
$$  

This, plus knowing the expression for \\(D(n)\\) gives us the following result

$$
\frac{I(n)}{D(n)} = (k + o(1))e^{-n(L - 3\log(3) + o(1))}
$$

where \\(L\\) determines the decaiment of the expression. The deterministic simulations gives us \\( L \leq 3,23 \leq 3 \log(3)\\). Stochastically, it goes to \\(3\log(3)\\) when we grow the number of faces. A later analysis indeed shown that \\(L = 3\log(3)\\) for the surprise of no one but to our satisfaction.

A note on random graphs
-----------------------

Someone may have noted at this point that the diagrams we used to represent the set of dice can be interpret as directed graphs. This is very interesting and a questions that might pop up is: Can we represent any graph with a set of dice: The answer is yes and the explication is surprisingly simple. Lets create a random graph such as the one below. 

<p style="text-align:center">
<img src="/images/posts/IntransitiveDices/graph.png" alt="graph"
  title="graph" style="width: 80%; margin=10px;"/>
</p>

The way we interpret the graph is: Every node is a die and every edge is a relation of victory of one die over the other. When there is a directed edge from node A to node B, it means that A beats B. If there isn's an edge, this means the dice tie.

The proof is by procedure. We take a symmetric string such that it has the same number of dice as the graph has of nodes. At this point, we have no edges. To generate an edge we can concatenate a symmetric string to the main string and swap the position of the letters of the two nodes we want the relation to change. This can always be done leaving the two letter in the middle of the symmetric string concatenated. In this manner, we don't change the relation of the other dice. This is enough to show that we can represent any graph with a set of dice. An open question, however, would be the minimum number of faces we need to represent a graph with a set of dice. 

 <hr style="height:1px;border-width:0;color:gray;background-color:gray">

A central limit theorem for intransitive dice
====================

This section is here to simply enunciate the main result of our work that was: A central limit theorem for the vector of normalized victories of a die against the next one in the list when the faces of a die are i.i.d. random variables and all dice are independent. This is a very elegant and interesting result that I definetely won't go into detail in this post. However I do feel you can get an idea for the result by the simple enunciation of it. The main corollary of the central limit theorem is that, for the dice we considered,

$$
\lim_{n\to\infty}\frac{I(n)}{D(n)} = p(X, Y, Z>0)+p(X, Y, Z<0) \le p((X, Y, Z)\in G^c) = 0.
$$

Let me explain. First, the variables \\(X, Y, Z\\) are the normalized victories of a die against the next one. This means that it keeps, respectively, how many more victories A has over B, B has over C and C has over A. If \\(X\\) is positive, it means that A has more victories over B than B has over A. The same goes for \\(Y\\) and \\(Z\\). The set \\(G^c\\) is such that

$$
(x, y, z) \in G^c \Leftrightarrow x + y + z \neq 0.
$$

The corollary then is saying to us that the probability of the sets being intransitive is less than, or equal, the probability of the set of dice belonging to the set \\(G^c\\). With three dice this corresponds to two octants of the space of the variables \\(X, Y, Z\\). In fact, our main theorem shows that the mulvariate distribution converges to the plane \\(x + y + z = 0\\) with distribution

$$
\frac{1}{3\pi} e^{-\frac{2}{9} (x^2 + y^2 + z^2-xy-yz-zx)},
$$

as the number of faces grows, as shown in the image below. With this, we can say that the probability of the set of dice being intransitive goes to zero when the number of faces grows.

<p style="text-align:center">
<img src="/images/posts/IntransitiveDices/Octantes.png" alt="Octantes"
  onmouseover="this.src='/files/posts/IntransitiveDice/Octantes.gif'"
  onmouseout="this.src='/images/posts/IntransitiveDices/Octantes.png'"
  title="Simulation Octantes" style="width: 50%"/>
<img src="/images/posts/IntransitiveDices/hyperplane.png" alt="Hyperplane"
  title="Hyperplane" style="width: 40%"/>
</p>

The same idea is confirmed in the simulations performed. This can be seen in the GIF above.

<hr style="height:1px;border-width:0;color:gray;background-color:gray"> 

If you speak Portuguese, you can also watch the video below as a complement to this post.

<iframe width="560" height="315" src="https://www.youtube.com/embed/fHEBWL0weVk?si=ymxzfrxzZuzFXN0E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>