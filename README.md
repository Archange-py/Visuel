<p align="center" width="100%">
<img src=".\Exemples_images\Logo Visuel.png" alt="Visuel-4">
</p>

# Visuel - 4

###
Welcome ! This project is intended to be used in conjunction with Numworks on a laptop, as an additional package. Following my dismay when I realized that the kandinsky module only offered a certain number of restricted possibilities, I told myself that I needed a package that would allow me to add a number of new drawing functions, as well as classes for visualizing RGB images, and even making animations an your laptop !

## Table of Contents
***
1. [General Info](#general-info)
2. [How to use it](#how-to-use-it)
3. [Examples](#examples)
4. [More Info](#more-info)
5. [FAQs](#faqs)

## General Info
***
I strongly recommend that you use this script on your computer and not on your calculator, because it's far too heavy and still very slow.   
Version 5 will be an optimized version of version 4 and will be made especially for the Numworks. In the meantime, check out version 4 anyway. 🙃  
>⚠️ **So don't download it to your *calculator*, download it to your *computer* !**  

If you have any questions, go to the [FAQs section](#faqs), or explore all the examples [here](#examples) after visiting this [page](#how-to-use-it) to install **kandinsky** and **ion** !  


## How to use it
***
To use it properly you need to install several python packages on your computer whith the command line:
* [Kandinsky](https://github.com/ZetaMap/Kandinsky-Numworks) -> `pip install kandinsky`
* [Ion](https://github.com/ZetaMap/Ion-numworks) -> `pip install --pre ion-numworks`  

And python, of course, [here](https://www.python.org/downloads/) if you don't already have it.
###
>You can change the emulator's OS by pressing "_CTR+O_" to increase speed, so you can get the most out of it without seeing everything slow down !

## Examples
***
First of all, after you're on your computer, you need to start by importing it after installing it in the current directory, and write : `from visuel_4 import *` on the first line of your project.  
After that, you need to understand how this script is organized, with points and vectors for example, and how it works, with its functions. For this purpose, you have at your disposal a *Jupiter Notebook* containing everything that can be shown in writing [here](exemple_visuel_4.ipynb). Then there are a lot of example files for everything to do with the screen, and just after, you can see the result with screenshots here

I will show you several examples what you can do with :  

* Function interpolation : [exemple_interpolation.py](exemple_interpolation.py)
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_interpolation_1.png" alt="dash" style="width: 60%; min-width: 100px; display: block; margin: auto;">
</p>
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_interpolation_2.png" alt="dash" style="width: 60%; min-width: 100px; display: block; margin: auto;">
</p>
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_interpolation_3.png" alt="dash" style="width: 60%; min-width: 100px; display: block; margin: auto;">
</p>
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_interpolation_4.png" alt="dash" style="width: 60%; min-width: 100px; display: block; margin: auto;">
</p>

* Function alpha_pixel and argument "alpha" in draw function : [exemple_alpha_layer.py](exemple_alpha_layer.py)

> We have to take a number less or equal to 0, and greater or equal to 1 for the alpha parameter

<p align="center" width="100%">
<img src=".\Exemples_images\exemple_alpha_layer_1.png" alt="dash" style="width: 60%; min-width: 100px; display: block; margin: auto;">
</p>
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_alpha_layer_2.png" alt="dash" style="width: 60%; min-width: 100px; display: block; margin: auto;">
</p>

* Function plot : [exemple_plot.py](exemple_plot.py)

<p align="center" width="100%">
<img src=".\Exemples_images\exemple_plot_1.png" alt="dash" style="width: 60%; min-width: 100px; display: block; margin: auto;">
</p>
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_plot_2.png" alt="dash" style="width: 60%; min-width: 100px; display: block; margin: auto;">
</p>
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_plot_3.png" alt="dash" style="width: 60%; min-width: 100px; display: block; margin: auto;">
</p>

* Draw dash : [exemple_point.py](exemple_point.py)
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_point.png" alt="dash" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>

* Draw line : [exemple_line.py](exemple_line.py)
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_ligne.png" alt="line" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>

* Draw arrow : [exemple_fleche.py](exemple_fleche.py)  
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_fleche.png" alt="arrow" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>

* Draw vecteur : [exemple_vecteur.py](exemple_vecteur.py)  
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_vecteur.png" alt="vecteur" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>

* Draw line : [exemple_droite.py](exemple_droite.py)  
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_droite_1.png" alt="line" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_droite_2.png" alt="line" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>

* Draw cercle : [exemple_cercle.py](exemple_cercle.py)  
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_cercle_1.png" alt="cercle" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_cercle_2.png" alt="cercle" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>

* Draw triangle : [exemple_triangle.py](exemple_triangle.py)  
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_triangle.png" alt="triangle" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>

* Draw polygone : [exemple_polygone.py](exemple_polygone.py)  
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_polygone_1.png" alt="plygone" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_polygone_2.png" alt="point" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>

* Draw figure : [exemple_figure.py](exemple_figure.py)  
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_figure_1.png" alt="figure" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_figure_2.png" alt="figure" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>

* Draw graph : [exemple_graph.py](exemple_graph.py)  
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_graph.png" alt="graph" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>

> The shortest path is shown in green

* Image : [exemple_image.py](exemple_image.py)  
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_image.png" alt="image" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>

* Animation : [exemple_animation.py](exemple_droite.py)  
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_animation.png" alt="animation" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>


* Function add : [exemple_func_add.py](exemple_func_add.py)  
<p align="center" width="100%">
<img src=".\Exemples_images\exemple_func_add.png" alt="func_add" style="width: 60%; min-width: 600px; display: block; margin: auto;">
</p>

> Normally, these are both animated examples, but I'll just show you one static image.

## More Info
***
Version 5 is currently being created, so that it can be used on the Numworks, which unfortunately cannot be done with version 4 because it is too heavy and runs far too slowly.

###
Here's a quick summary of the changes that V-5 will bring :  
- [x] separation of "image" and "visual" sections
- [ ] new drawing functions, like ellipsis, bezier curve...
- [ ] code refactoring
- [ ] optimization of code and reduction of the number of lines

## FAQs
***
A list of frequently asked questions  
1. **Why can't I put this script on my Numworks?**  
Because it takes up too much space and RAM memory. Execution of the files provided as examples takes a long time, compared with execution on a computer, for example.  

2. **When will version 5 be available?**  
I don't know yet, because I need :
* *Refactor* and *clean up* a lot of code
* *updating* and *adding functionalities*
* reduce *code size*
