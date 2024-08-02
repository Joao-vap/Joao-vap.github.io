---
title: 'The Voyager and our Golden Record'
date: 2024-07-15
permalink: /posts/2024/07/VoyagerGoldenRecord/
tags:
  - Basics
  - Voyager
  - Golden Record
---

I can't get over the Voyager mission. 


Context 
====

Ok, maybe I should start with some context of what I'm talking about. The Voyager mission consisted of two spacecraft launched by NASA in the 1970s. On paper, the main mission was to explore Jupiter and Saturn by hovering close by. Voyager 2 extended its route to Uranus and Neptune and is still the only spacecraft to have approached those planets. This, by itself, is already pretty impressive and a major achievement for NASA and all of humanity. More details can be found on [NASA's website](https://voyager.jpl.nasa.gov/mission/). However, that part of the mission won't be the focus of this post. 

<img src="/images/posts/Voyager/voyager.png"
     alt="Artistic Conception of Voyager"
     width="50%"
     style="float: right; margin-right: 5px;" />

There are some monumental moments that mark history. Legend has it that one of them was produced by the brilliant Carl Sagan. Once the Voyager 1 mission had surpassed Pluto’s orbit, it turned around its cameras and took pictures of the solar system as seen by an outsider. It is said that it was Sagan who was responsible for that decision. Either way, it produced one of the most impressive media I’ve seen, a picture that has been called the ["pale blue dot"](https://science.nasa.gov/mission/voyager/voyager-1s-pale-blue-dot/)  in reference to the appearance of the Earth from the spacecraft perspective. This picture, as discussed in the incredible documentary ‘Cosmos’, by Sagan itself, was intended to give perspective on the magnitude of our planet (and ourselves) in the infinitude of the Cosmos.

Today, those spacecraft are still traveling and making sporadic contact with us. They are, as of now, the furthest from Earth that any man-made object has ever been, and they are still distancing themselves. Someday they will no longer be in contact or active, but they will still be wandering the Cosmos. This is the intent. Intentionally I have not, so far, commented on the most interesting aspect of this mission: [The Golden Record](https://voyager.jpl.nasa.gov/golden-record/). This is a vinyl that accompanies the spacecraft, containing recordings of sounds and images of Earth and its inhabitants. Why? The hope is that the spacecrafts survive traveling in space for an enormous amount of time, convering a long distamce. By cointaining in themselves a snapshot of our planet, they could then be found by some other civilization that would be able to learn about us. If you’re not familiar with the Golden Record, one of your questions may be how such a civilization would go about interpreting a mysterious object from space. This is what they tried to solve with the instructions on the record’s cover. Of course, such instructions couldn’t be done in written language, so they used a mix of depictions of mathematical and physical concepts that we think are natural for any scientifically driven civilization to stumble upon. There are many assumptions made here. Firstly, we suppose that whoever finds it will be interested in the object at all. This is because we like to think that they should; we would be, wouldn’t we? The second assumption is that those concepts are universal and should compose the basic understanding of every scientific community in any corner of the universe.

<img src="/images/posts/Voyager/VoyagerCoverDiagram.jpg"
     alt="Golden Record Cover"
     width="65%"
     style="float: left; margin-left: 3px;" />

Decoding
=====

The cover then describes how the information is encoded. The main idea is: Images are codified in audio in such a way that it has the profile shown in the upper right corner of the image displayed (courtesy of NASA). Each image using 512 lines of resolution. The separation between frames is done by a prominent negative value, and between images, we have the zig-zag patterns. I haven’t found one good source as to how to decode the audio in its entirety. I think I am then responsible to write a short how-to and make the source code avaible. However, there is a very good blog post done by [Ron Barry](https://boingboing.net/2017/09/05/how-to-decode-the-images-on-th.html), where he goes through the process of understanding the cover and plotting some images. But of course, I’m not satisfied with manually selecting the sections of the audio for each of the images and reconstructing them according to the cover; that would take me an hour! I have therefore spent a few days automating this process in a sometimes reliable program. Isn’t generalizing the instinct of every mathematician? ;)

<p style="text-align:center">
  <audio controls="1" controlslist="nodownload nofullscreen noremoteplayback" src="/files/posts/Voyager/Voyager-Golden-Record.mp3">
    Your browser does not support the audio element.
  </audio>
</p>

As far as I know, this is the only recording available on the internet of the Golden Record. And it's kind of bad. First, it is sped up 2x from the intended record velocity. Second, the microphone used introduces a lot of noise and artifacts into the audio. As an example, the zig-zag pattern appears somehow damped; this may manifest in weird ways on the image. However, it is not incapacitating and we may continue.

<p style="text-align:center">
  <img src="/images/posts/Voyager/Voyager-zig-zag.png"
       alt="Golden Record Audio"
       width="70%"/>
</p>

Our first challenge is to identify the zig-zag regions and separate the recording into sections, one for each of the images that it should contain. One possible approach is to identify the main frequencies in each region, as the images sections will have a wider range than the separators. However, a more direct way is to check for the density of peaks above a certain threshold (arbitrary and empirical). This is because the separators have, in general, a higher intensity than the images, although they are not consistent. Using this density approach we can damp the noise.

If we divide the recording into sections of short length (also arbitrary and empirical), we can determine the densities of the high peaks in each of those sections. This would be enough. However, if we then group these sections and calculate the 'densities of sections determined to have higher densities of high peaks', we can determine regions of high densities with more consistency. This double-density approach is a good way to avoid false positives. This is what is done in [Audio -> txt](/files/posts/Voyager/audio_to_txt.py). We could of course apply more layers and do the density of the densities of densities... I think I lost myself, you get the idea. Note that there are two channels in the audio, and it is necessary to apply the same approach to both. We get the following (very good may I add) division:

<p style="text-align:center">
  <img src="/images/posts/Voyager/Voyager-divided.png"
       alt="Golden Record Audio Divided"
       width="100%"/>
</p>

For the last stretch, we need a way to display each image. The idea is quite simple and based on how the images are encoded. We need to find the first big valley in our data, which is the beginning of an image line. By the end, we should encounter 512 of those lines, but generally, we can’t count on that. The cuts we made are imperfect, and we may be missing a line or two or the valleys may be ill defined. Starting from the first identified valley, we can find the next one knowing the mean distance we expect and looking for a valley around that point. All points inbetween will be one line of our matrix. There is something we should notice. As we’re dealing with imprecise data, we may have some lines with more points than others. That will be a problem when plotting the matrix. We can, however, compete with the lines in an arbitrary empty space, so we have a margin to wobble around. I found that 1100 points (enough for a double line) is a nice enough number to use. All of this process is done in [txt -> Img](/files/posts/Voyager/txt_to_image.py). After this, we can plot the matrix, and we should have the image. Such images are shown (with cutted borders) below.

<p>
<p style="text-align:center">
  <img src="/images/posts/Voyager/Voyager-rocket.png" width="30%" />
  <img src="/images/posts/Voyager/Voyager-concha.png" width="30%" />
  <img src="/images/posts/Voyager/Voyager-earth.png" width="30%" />
</p>
<p style="text-align:center">
  <img src="/images/posts/Voyager/Voyager-inside.png" width="30%" />
  <img src="/images/posts/Voyager/Voyager-men.png" width="30%" />
  <img src="/images/posts/Voyager/Voyager-text.png" width="30%" />
</p>
</p>

There are some pictures that appear three times, indicating RGB channels. If we want, we can compose those pictures and have colorful images! Anyway, all the code and results are available on my [GitHub](https://github.com/Joao-vap/Decoding_Golden-Record_Images/tree/main).

Tying the knot
=====

Sometimes I do wonder about the work that was put into the Golden Record. That is, a team of really invested people took uncountable hours to work on the instructions and the recording. For what? Really, how likely is it that someone encounters these spacecraft? I mean, Sagan itself has made a point about the size of our universe in comparison to what we have influenced. Suppose you agree with the argument that there should be another civilization somewhere. Even more, you are prepared to say that there should be some other civilization that is as curious and alone as we are, craving a message. Honestly, I can consider that. I even find it likely for some form of life to be in the Cosmos somewhere, looking for signs of company. After all, for us to be alone would be a mathematical wonder.

Even then, what is the chance that our tiny piece of metal gets in the hands of such a life form? Even if it is going straight to somewhere it can be found, how long until this happens? The Cosmos is vast, and we are small. No, we can’t think of the Golden Record as a message to someone out there, nor directly or mainly, at least. I think all the people involved in the project knew this, I know this. The Golden Record is a message to oneself. It is an exercise to categorically explicit what is valuable to us. To understand what would be our image to an imaginary outer civilization; it is a way to reflect not on the distant unknown but on the close-known self.

In more than one way, I can’t stop coming back to this concept. It is no coincidence that I’ve chosen this to be the first post on the blog. In a less subtle way, I guess this text itself is one of the records I’m putting on this Golden Blog. There is no instruction to read through this, I wouldn't know how to make those. I can only hope I use a common language that we both understand. Regardless of who is going to be the decoder of the message, and for all of those I wish the best of luck, this, in itself, will hold all that is dear and personal to me. I truy hope, however, that we don't live on a mathematical wonder.