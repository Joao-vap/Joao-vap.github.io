---
title: 'N-dimensional Spheres: Monte Carlo Estimation'
date: 2024-07-19
permalink: /posts/2024/07/MonteCarlo/
tags:
  - Medium
  - Monte Carlo
  - Numerical
---

What is the volume of an n-dimensional sphere?

Let's start on the basics. Consider the famous 2-dimensional sphere, the circle. We know that its area is given by the formula

$$
A = \pi r^2
$$

where \\(r\\) is the radius of the circle. The volume (in this case the area, of course) of a circle depends therefore on its radius squared and is proportional to \\(\pi\\). To simplify the discussion, and without loss of generality, let's consider spheres with radius 1. The volume of a 2-dimensional sphere is then \\(\pi\\). Of course we could perform the integration in polar coordinates 

$$
V_2 = \int_0^{2\pi} \int_0^1 r dr d\theta = \pi
$$

to determine the volume. This is easy enough, and we could, equivalently, perform it for 1 and 3-dimensional spheres, whose volumes are

$$
V_1 = \int_{-1}^1 dx = 2
$$

and

$$
V_3 = \int_0^{2\pi} \int_0^\pi \int_0^1 r^2 \sin(\theta) dr d\theta d\phi = \frac{4}{3}\pi
$$

respectively. But what about higher dimensions? We won't perform the integration for those spheres, not analytically at least. Instead, we will use an numerical approach.

Estimating Volumes
===========

<img src="/images/posts/MonteCarlo/gridIlustration.png" alt="Illustration Grid Method"
  title="Illustration Grid Method" style="float:right; width: 40%; margin=10px;"/>

Let's take the 2-dimensional case for the sake of visualization. We can of course determine the area of the unit circle by the following procedure: Divide the unit square into a equally divided grid of \\(N \times N\\) points, and count the number of points that fall inside the circle. The ratio of points inside the circle to the total number of points give us an estimate of the area of the circle, that is

$$
\frac{N_{\text{inside}}}{N_{\text{total}}} = \frac{A_{\text{circle}}}{A_{\text{square}}}
$$

where we know \\(A_{\text{square}} = 4\\). This estimative takes the computing of \\(N^2\\) points. More generally, in \\(D\\) dimensions, it would take \\(N^D\\) points. Let's check how precise it is and how much time it takes to compute its estimation.

<p style="text-align:center">
<img src="/images/posts/MonteCarlo/graphsGrid.png" alt="Area Estimation"
  title="Area Estimation" style="display: block; width: 100%; margin=10px;"/>
</p>

In the top row we see the estimated volume of the 2-dimensional sphere for a progression of values of \\(N\\) and the respective time it took to estimate it. Here, the measure of time is not that important and is mostly affected by the computer fluctuations in computing. Nevertheless we can see the value approaching \\(pi\\) is a somewhat monotonous manner. Where things get interesting is when we extend to higher dimensions. The bottom row shows the estimated volume of the n-dimensional unit sphere for \\(N = 100\\) and the respective time it took to estimate it. First, as one could expect, the volume increases up to the fourth dimension. Furthermore, we can also more clearly see that times gets progressively impeditive. This is beacuse the amount of computing grows exponentially with the dimension. Ok, time is definitely a problem. The way to solve this problem is to use the Monte Carlo method.

Monte Carlo Method
===========

The idea behind the Monte Carlo method is to sample estochastically the space of interest based on some distribution. In this way we can numerically integrate some function of interest by using the resulting samples. A bit more formally the Monte Carlo method is of help to calculating the following expectation value

$$
\mu = E[f(x)] = \int f(x) p(x) dx
$$

where \\(f(x)\\) is some function of interest and \\(x\\) is a random variable based on some distribution of interest. If for some reason we can't perform the integral analytically, be that because of the complexity or randomness of the system at hand, we can use the Monte Carlo method to estimate the expectation value. Of course, if you can sample the variable \\(x\\) from the distribution you can simply calculate

$$
\mu \approx \frac{1}{N} \sum_{i=1}^N f(x_i)
$$

where \\(x_i\\) are independent and identically distributed samples from the distribution of interest. To prove the conversion is a matter of fundamental statistics, it relies heavily on the law of large numbers. This simple idea is very powerfull and allows us to sample from some very complex distributions asociated for example with the solution for coupled differential equations or the partition function of a system of particles. To illustrate this idea, let's return to the simulation of the volume of the unit sphere. Hovewer we will now sample uniformly from the unit cube and count how many of the points fall inside the unit sphere. As before, the ratio of points inside the sphere to the total number of points gives us an estimate of the volume of the sphere. For this visualization, I'll run the Monte Caro method untill I get an as good estimation of the volume and regster the amount of samples it took to get there. The results of the ratio of poins needed before and with this method are shown in the following figure for some dimensions.

<p style="text-align:center">
<img src="/images/posts/MonteCarlo/Comparison.png" alt="Volume Comparison"
  title="Volume Estimation" style="display: block; width: 100%; margin=10px;"/>
</p>

The main point is that we need to use a incredible smaller quantity of points to get the same precision. This idea can be explored to overcome the problem of the dimensionality increase of complexity in our program. All results can be replicated with the following (not very organized) code resource [Sphere Volume](/files/posts/MonteCarlo/SphereVolum.py). The Monte Carlo method returns the following results for the volumes of the unit spheres

<img src="/images/posts/MonteCarlo/SphereVolumes.png" alt="Volume Estimation d-dimensions"
  title="Volume Estimation" style="display: block; width: 100%; margin=10px;"/>

Well, first of all, my choosing of the quantity of points was half-arbitrary. I was interested in the general behavior of the curve and you may guess why now. There is a peak in the volumes of the n-dimensional unit spheres. This is weird but not too much. You can think of it as the effect of the volume of the cube that contains the sphere simply growing faster than the volume of the sphere. This is the effect of the high-dimensionality. I've been holding on to this, but there is a explicit formula for the volume of the n-dimensional sphere. It is given by

$$
V_n = \frac{\pi^{n/2}}{\Gamma(n/2 + 1)}
$$

where \\(\Gamma\\) is the gamma function. With this we can be more explicit about this volume and calculate the curve to be 

<img src="/images/posts/MonteCarlo/SphereVolumesExplicit.png" alt="Volume Estimation d-dimensions"
  title="Volume Estimation" style="display: block; width: 100%; margin=10px;"/>

where we can clearly see the peak to be in \\(n = 5\\). This always baffled me. I may just enjoy too much maximums in these 'natural' situations. Nature and Mathematics are usually so equal on its dimensions, I find it amusing when it decides to have some weird behavior. 
