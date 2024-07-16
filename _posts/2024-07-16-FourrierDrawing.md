---
title: 'The drawings of Fourrier'
date: 2024-07-16
permalink: /posts/2024/07/FourrierDrawing/
tags:
  - Medium
  - Fourrier
  - Artsy
---

I don't know for how long I've been obsessed with the Fourries Series.

<img src="/images/posts/Fourrier/eu.png"
 alt="Fourrier Drawing"
 style="float: right; width: 30%;"/>

There is something ming boggling about the theory behind Fourrier Series, and more generally, the Fourrier Transform. It is a simple and elegant theory that allows us to represent functions in terms of the frequencies of oscilating basis that compose them. I cannot overstate how many application this theory has. We will, however, use it do draw some fun pictures. To get there, let's very briefly go through the theory, although in our application we will simply use a python library. Maybe next time we can implement it with a fun twist: The Fast Fourrier Transform. More importantly, as I would never make a bettet job than 3Blue1Brown in the theory aspect, I will leave the following important links if you're interested.

- [Fourrier Series](https://www.youtube.com/watch?v=r6sGWTCMz2k&list=PLZHQObOWTQDN52m7Y21ePrTbvXkPaWVSg)
- [Fourrier Transform](https://www.youtube.com/watch?v=spUNpyF58BY&list=PLZHQObOWTQDN52m7Y21ePrTbvXkPaWVSg&index=6)

With the context set, let's work some background on the math. Don't worry too much about this section, I just want to set some context.

Fourrier Series
====

Consider a function \\(f(x)\\) defined in the interval \\([-T, T]\\). We say that

\\[ f(x) = \frac{a_0}{2} + \sum_{k=1}^{\infty} a_k \cos\left(\frac{\pi k x}{T}\right) + b_k \sin\left(\frac{\pi k x}{T}\right) \\]

is the Fourrier Series of \\(f(x)\\) in the interval \\([-T, T]\\). The coefficients \\(a_k\\) and \\(b_k\\) say how much of the frequency \\(k\\) is in the function \\(f(x)\\), note that every different frequency is orthogonal to each other. This is simply representing the function in term of its geometric components. Similar in a way to a Taylor Series, wich expands the function in a polynomial basis. Notice that the resulting function is periodic with period \\(2T\\) because of the properties of the sines and cosines. How do we get the value of the coeficients? 

Fact is that we can find the coefficients by multiplying both sides of the Fourrier Series by \\(\cos\left(\frac{\pi l x}{T}\right)\\) or \\(\sin\left(\frac{\pi l x}{T}\right)\\) and integrating over the interval \\([-T, T]\\). This has a nice interpretation. When we integrate the function multiplied by alternating cosines and sines, we know to expect something other than zero if the function alternates signs along with the cosine or sine. Otherwise, it would generally go to zero as we integrate the interval. As of this scenario This is beacause the area would be positive, of course. This is equivalent to say that the function has a component of that frequency, or that is expressed with non zero coeficient in that basis vector.

We then know that multiplying the function by those sines and cosines we would be filtering orthogonal vectors, that is, frequencies. We wont go through the details of the calculations, but it is elucidative to see how it is done. For that, we have should remember the propeties of the trigonometric functions. That is

$$ 
 \int_{-T}^{T} \cos\left(\frac{\pi k x}{T}\right) \cos\left(\frac{\pi l x}{T}\right) dx = \begin{cases} 0 & \text{if } k \neq l \\ T & \text{if } k = l \end{cases}
$$

$$ 
 \int_{-T}^{T} \sin\left(\frac{\pi k x}{T}\right) \sin\left(\frac{\pi l x}{T}\right) dx = \begin{cases} 0 & \text{if } k \neq l \\ T & \text{if } k = l \end{cases}
$$

e

$$ 
 \int_{-T}^{T} \cos\left(\frac{\pi k x}{T}\right) \sin\left(\frac{\pi l x}{T}\right) dx = 0
$$

Therefore, multiplying both sides of the Fourrier Series by \\(\cos\left(\frac{\pi l x}{T}\right)\\) and integrating over the interval \\([-T, T]\\) we get

$$ 
 \begin{eqnarray}
  \int_{-T}^{T} f(x) \cos\left(\frac{\pi l x}{T}\right) dx &=& \frac{a_0}{2} \int_{-T}^{T}  \cos\left(\frac{\pi l x}{T}\right) dx  \\
  &+& \sum_{k=1}^{\infty} a_k \int_{-T}^{T} \cos\left(\frac{\pi k x}{T}\right) \cos\left(\frac{\pi l x}{T}\right) dx \\
  &+& \sum_{k=1}^{\infty} b_k \int_{-T}^{T} \sin\left(\frac{\pi k x}{T}\right) \cos\left(\frac{\pi l x}{T}\right) dx
  \end{eqnarray}
$$

The first and third terms of the right hand side are always zero. The second term however is equal to \\(a_l T\\) only when \\(l = k\\). Therefore, we get

$$
a_k = \frac{1}{T} \int_{-T}^{T} f(x) \cos\left(\frac{\pi k x}{T}\right) dx \ \ \text{,for} \ n \neq 0
$$

The same can be done for the sine, and we get

$$
b_k = \frac{1}{T} \int_{-T}^{T} f(x) \sin\left(\frac{\pi k x}{T}\right) dx \ \ \text{,for} \ n \neq 0
$$

The coefficient \\(a_0\\) is given by

$$
a_0 = \frac{1}{T} \int_{-T}^{T} f(x) dx
$$

We have now a way to find the coefficients of the Fourrier Series. We can decompose any function in terms of its frequencies.

Note about the discrete
====

<img src="/images/posts/Fourrier/angela.png"
 alt="Fourrier Drawing"
 style="float: right; width: 30%;"/>

We neew to have some care if we want to be precise in this case. Naturally, we are testing for a finite number of frequencies. This means that if we were, for example, expressing a cosine function with a frequency that is not being used for the composition, this would be expressed as a distribution of frequencies around the one we are testing. When using discrete data, we cannot either identify frequencies that are higher than the so called Nyquist frequency. That is, the sampling rate of the data used. This is natural as the detail of those oscillations would e lost inbetween the data points. The Nyquist theorem is a highly important theorem in signal processing and deserves much more thought than I am giving here, however, it won't be our focus.

A complex extension
====

Assume a time series that takes values in the complex plane. We can extend the Fourrier Series to complex numbers. That is, we can write

$$
f(x) = \sum_{n=-\infty}^{\infty} c_n e^{i \frac{2 \pi n x}{T}}
$$

where the coefficients are given by

$$
c_n = \frac{1}{T} \int_{-T}^{T} f(x) e^{-i \frac{2 \pi n x}{T}} dx
$$

 <img src="/images/posts/Fourrier/paulita1.png"
 alt="Fourrier Drawing"
 style="float: left; width: 30%;"/>

The idea is the same as we discussed previously. We are representing the function in terms of its frequencies. The difference is that now we are using complex exponentials and summing over the negative frequencies as well. This is a natural way to represent a complex time series. Now we can take any arbitrary curve (well, maybe not any, but all we're dealing) and write it in term of its frequencies.

Wen we talk about these complex time series, as these that are illustrating the post, we say we want to decompose its frequecies components. What does that mean visually? The links I've exposed in the begining of the text say this too well. We can think of the complex numbers as vectors in the complex plane. The complex exponential is a vector that rotates in the complex plane. The frequency of the complex exponential is the frequency of the rotation. The coefficients \\(c_n\\) are the amplitudes of the rotations. The Fourrier Series is then a sum of rotations of different frequencies and amplitudes. In te end, we have a multitude of rotating vectors that write our curve. This is simply beautiful.

Going beyond and having fun
====

If we can choose an arbitrary curve, nothing stop us from having fun with it. The idea for this post is to draw photographs and do some cool art.

<img src="/images/posts/Fourrier/ambos.png"
 alt="Fourrier Drawing"
 style="display: block;
 margin: auto; width: 90%;"/>

The first challenge is to get a complex time series from the picture we start with. The first aspect of the project is then to have an appropriate picture. This, for me, was solved drawing my own pictures. There is a change you can do this to some easy simple pictures, I have tried some and had some success but this will depend highly on the next step. The process now depends on your image. If you have a png or anything like it, we will need to extract by force the series. This is, at least for me, a hard task. The idea is to first diminish the quality of the picture so that we can start to see the single pictures in the curve. This is beacause now we can interpret the points/pixels as data from a time series. However the points are not ordered, it is not yet a time series. This is the hard part. A way to order would be to interpret those points as vertices of a graph and then find the shortest path that connects all the vertices (or at least most of them). This is basically the Traveling Salesman Problem. A highly non-trivial problem that you can try and find partial solutions around. If that's to much, for some curves it is possible to just find the closest point untill the last one. This won't suffice for most curves. If youre doing your own drawings, you can facilitate the process separating it into pieces and then tying them together afterwards. This is what I do when I want to intersect curves.

The other option is to know the order of the points. We will use SVGs files.

Inserting SVGs and Finishing up
====

SVGs are vectorial images. This means that the image is decomposed in many components. Those components can be mathematical curves, lines, circles, etc. An exemple of a SVG file is the following where I (very skyllfully may I add ;) ) drew a person holding a board.

<p style="text-align:center">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" > 
<circle cx="50" cy="50" r="10" stroke="black" stroke-width="3"/>
<line x1="30" y1="100" x2="30" y2="70" style="stroke:black;stroke-width:2" />
<line x1="30" y1="100" x2="50" y2="70" style="stroke:black;stroke-width:2" />
<line x1="70" y1="100" x2="50" y2="70" style="stroke:black;stroke-width:2" />
<line x1="50" y1="130" x2="50" y2="50" style="stroke:black;stroke-width:2" />
<line x1="50" y1="130" x2="30" y2="160" style="stroke:black;stroke-width:2" />
<line x1="50" y1="130" x2="70" y2="160" style="stroke:black;stroke-width:2" />
<ellipse cx="80" cy="75" rx="15" ry="75" style="fill:white;stroke:black;stroke-width:2" />
</svg>
</p>

The elements of the image are as follows:

<pre>
〈svg xmlns="http://www.w3.org/2000/svg" version="1.1" 〉 
〈circle cx="50" cy="50" r="10" stroke="black" stroke-width="3"/〉
〈line x1="30" y1="100" x2="30" y2="70" style="stroke:black;stroke-width:2" /〉
〈line x1="30" y1="100" x2="50" y2="70" style="stroke:black;stroke-width:2" /〉
〈line x1="70" y1="100" x2="50" y2="70" style="stroke:black;stroke-width:2" /〉
〈line x1="50" y1="130" x2="50" y2="50" style="stroke:black;stroke-width:2" /〉
〈line x1="50" y1="130" x2="30" y2="160" style="stroke:black;stroke-width:2" /〉
〈line x1="50" y1="130" x2="70" y2="160" style="stroke:black;stroke-width:2" /〉
〈ellipse cx="80" cy="75" rx="15" ry="75" style="fill:white;stroke:black;stroke-width:2" /〉
〈/svg〉
</pre>

Here I didn't use very complex elements, but as long as they are in the SVG format, we can extract the points from the curves. A full guide of the elements can be found on [Mozilla Guide](https://developer.mozilla.org/en-US/docs/Web/SVG/Element). This is the best way to get the time series. We can just extract the points from the curves cause we know how to construct these objects.

 <img src="/images/posts/Fourrier/JIP.svg"
 alt="Fourrier Drawing"
 style="display: block;
 margin: auto; width: 70%;"/>

From that on the program is very easy. We first take the elements on te SVG and extract points from the construction of each of those in order. The interpretation of the elements can be done with a parser from a python library named svgpathtools. This is done in [Svg -> Path](/files/posts/Fourrier/svgPathToSeries.py).

<img src="/files/posts/Fourrier/JIP.gif"
 alt="Fourrier Drawing"
 style="display: block;
 margin: auto; width: 50%;"/>

 The only thing remaining now is to take the time series and apply the Fourrier Transform. This is done in [Fourrier Transform](/files/posts/Fourrier/FourrierTransform.py). We won't go through the implementation of the series calculation. Instead, we will use numpy to that for us better than I ever could. In this way we get a function of sines and cosines that render such as the GIF displayed above.

Some Results
====

For completness, here are some of the images shown and it's series. Have fun with it!

<p style="text-align:center">
<p style="text-align:center">
  <img src="/images/posts/Fourrier/feu.png" width="30%" />
  <img src="/images/posts/Fourrier/fpaulina.png" width="30%" />
  <img src="/images/posts/Fourrier/fangela.png" width="30%" />
</p>
<p style="text-align:center">
  <img src="/images/posts/Fourrier/fambos.png" width="90%" />
</p>
<p style="text-align:center">
  <img src="/images/posts/Fourrier/JIP.png" width="90%" />
</p>
</p>