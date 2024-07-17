---
title: 'What is the BuddhaBrot after all?'
date: 2024-07-17
permalink: /posts/2024/07/BudahBrot/
tags:
  - Easy
  - Mandelbrot
  - Artsy
---

I do not understand the BuddhaBrot set, but look at it.

<p style="text-align:center">
  <img src="/images/posts/BuddhaBrot/b1.png" width="30%" />
  <img src="/images/posts/BuddhaBrot/b2.png" width="30%" />
  <img src="/images/posts/BuddhaBrot/b3.png" width="30%" />
</p>

Well, there is much to cover until we get to the BuddhaBrot set. We need to first understand and learn how to simulate the Mandelbrot set. Which is interesting by itself. There is much to be said about its connections with other sets, fractal theory, and even chaos in general, particularly the relation to the logistic map. I will not, however, talk about many of those, as I said, I do not understand the BuddhaBrot set. Nevertheless, I feel compelled to it. There is something to be said about the other driving forces of a mathematician. Beauty, sometimes, is enough.

<img src="/images/posts/BuddhaBrot/butterfly.jpeg" width="100%" />

The Mandelbrot Set
=====

<img src="/images/posts/BuddhaBrot/Mandelbrot.png"
 alt="Mandelbrot Set"
 style="float: right; width: 30%; margin-left: 10px;"
 />

We shall then start at the Mandelbrot set. This is nothing more than a set of complex numbers bounded by some rule. This is done in the same way we could define a circle in the plane, that is, the set

$$
\{z \in \mathbb{C} : |z| \leq 1\}
$$

is the unit circle. In a similar sense, the Mandelbrot set is defined as the set of complex numbers \\(c\\) for which the sequence is defined by if

$$
z_{n+1} = z_n^2 + c
$$

is bounded. That is, if you iterate on \\(z_n\\), you will get an finite number when \\(n\\) goes to infinity. If you then plot this set of points you end up with what we call the Mandelbrot set. 


<img src="/files/posts/BuddhaBrot/gifMandelbrot.gif"
 alt="Mandelbrot Set Gif"
 style="float: left; width: 30%; margin-right: 10px;"
 onmouseover="this.src='/files/posts/BuddhaBrot/gifMandelbrot.gif'"
 />

There are some considerations if we wish to simulate it. We, of course, do not iterate every point of the grid to infinity. Among those arbitrary points of the grid we choose to iterate, we say that they diverge if, after a certain threshold, they have an absolute value greater than 2. Selecting a threshold is a matter of art and intent. We also choose to color the set (mainly its borders) by how many iterations it took to ‘diverge’. That is, for those who don’t diverge, we will plot the threshold value, and for the rest, we will plot the number of iterations it took to surpass the radius defined previously. If you’re anything like me, you already defied some definitions here: What happens if we use something other than \\(z^2\\)? What is the set appearance for different constants \\(c\\). I won't explicitly answer those, but the GIF answers one of them. Feel free to explore, the code necessary to do it is in [Mandelbrot](/files/posts/BuddhaBrot/Mandelbrot.py). Here are some close-ups of the Mandelbrot set.

<p style="text-align:center">
  <img src="/images/posts/BuddhaBrot/Mz1.png" width="30%" />
  <img src="/images/posts/BuddhaBrot/Mz3.png" width="30%" />
  <img src="/images/posts/BuddhaBrot/Mz2.png" width="30%" />
</p>

The amount of programming it takes to simulate the Mandelbrot is minimal. But somehow, this is a very interesting mathematical object. Mainly, we will discuss it as a fractal. A fractal is a set with a fractal dimension. Well, that doesn’t help very much. How can something have a fractal dimension? We know about lines with dimension 1, and we know about planes with 2 dimensions. How can some objects have 1.4 dimensions? Well, first, we need to be sure about the meaning of a line having 1 dimension or the plane having 2. We could talk about the orthogonal basis, but that’s too sophisticated. Another way to define dimensions is using self-similarity.

<img src="/images/posts/BuddhaBrot/Mz4.png"
 alt="Zoom of Mandelbrot"
 style="float: block; width: 100%;"/>

If we take a line and divide it into 2 equal parts, we get 2 lines. Each of those can be scaled by 2 to get the original line. If we, instead, divide it into 3 parts, we should scale each of those parts by 3 to get the original line. That is, diving by \\(N\\) demands a scale of \\(N\\). What about a square? We now can't divide the square by 2 or 3 self-similar parts. But we can divide it by 4, and each of those squares must be scaled by 2 to get the original square. Generally, we can divide by parts, and each of those must be scaled by \\(N\\) to get the original square. This introduces the idea that those objects have different dimensions. Dimension is simply the exponent of the scale factor. That is, a line is of dimension 1, a square is of dimension 2. What about the following set?

<img src="/images/posts/BuddhaBrot/serpiensky.png"
 alt="Serpiensky Triangle"
 style="float: right; width: 50%;"/>

This is the Serpiensky Triangle, a fractal of dimension 1.58. Actually, producing this set is very interesting. We start with 3 points in the complex plane. We then choose a random point on the plane and plot it. We select one of the 3 points at random and plot the point in the middle of the line between the random point and the chosen point. Repeat this process. Somehow, this generates this fractal.

How do we calculate its dimension?

$$
\text{dimension} = \frac{\log(\text{#self-similar pieces})}{\log(\text{scale factor})}
$$

In this case

$$
\text{dimension} = \frac{\log(3)}{\log(2)} = 1.58
$$

The Mandelbrot set has dimension 2 somehow, this is just so interesting.

The Buddhabrot Set
=====

We have so far overlooked a set of numbers complementary to the Mandelbrot set. This is the Buddhabrot set. This set is defined by the set of complex numbers \\(c\\) for which the sequence is defined by

$$
z_{n+1} = z_n^2 + c
$$

diverges. We won't plot the set, however. What is the path of the diverging points? The density of those paths is represented in the Buddhabrot visualization. In this way, we simply get random points in the complex plane and iterate them. If they diverge, we plot the path they take. There are some optimizations to be made, like excluding points that are obviously inside the Mandelbrot set. The code to do this is in [Buddhabrot](/files/posts/BuddhaBrot/Buddhabrot.py) and the plot file is the [Plot](/files/posts/BuddhaBrot/plotBuddha.py). There is no secret to this part.

Some Artistic Liberties
-----

Clearly, a 2D array with numbers doesn’t transform itself in these cool pictures simply plotting the numbers. You can simply plot it with a nice colormap, this will be fine. However, if you’re trying to add a little more flare to the image, here’s what you can do: Firstly, get comfortable with the variables in the generation process, those are going to define which characteristics will be clear in your plot. Mainly, worry about the quantity of points you’re using and how many iterations you’re recording. As the points diverge, if you record long paths, you will see some semi-stable orbits highlighted. If you record short paths, you will get a more blurry image.

<p style="text-align:center">
  <img src="/images/posts/BuddhaBrot/baseR.png" width="30%" />
  <img src="/images/posts/BuddhaBrot/baseB.png" width="30%" />
  <img src="/images/posts/BuddhaBrot/baseG.png" width="30%" />
</p>

The second step is composing. We will generate an RGB image composing the three channels, each with any characteristic of the Buddhabrot set you choose to highlight. Then, in any editing software, you will superpose those images and merge them with one of the many blending modes. With this, you can create any of these images.

<p style="text-align:center">
  <img src="/images/posts/BuddhaBrot/b21.png" width="30%" />
  <img src="/images/posts/BuddhaBrot/b22.png" width="30%" />
  <img src="/images/posts/BuddhaBrot/b23.png" width="30%" />
</p>

I do not understand the Buddhabrot set, but look at it. This time, beauty is enough.