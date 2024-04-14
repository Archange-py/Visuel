<p align="center" width="100%">
<img src=".\Exemples_images\logo_visuel.png" alt="Visuel">
</p>

# Visuel

###
Welcome ! This project is intended for use in conjunction with Kandinsky on a laptop or Numworks calculator. It allows you to add graphical functions, mainly around new drawing functions like line or circle drawing, but also mathematical classes like vectors or points, and much more !

## Table of Contents
***
1. [General Info](#general-info)
2. [How to use it](#how-to-use-it)
3. [Examples](#examples)
4. [More Info](#more-info)
5. [FAQs](#faqs)

## General Info
***
I strongly recommend that you test the example files on your computer, as the calculator won't have enough memory.

> To install it on the Numworks, you just need to copy and paste the code from these two files: [mathforvisuel](mathforvisuel.py), and [visuel](visuel.py) into two separate files that you'll have created beforehand on your Numworks account. Then upload them to your calculator. Finally, rename your files to mathforvisual and visual.

If you have any questions, go to the [FAQs section](#faqs), or explore all the examples [here](#examples) after visiting this [page](#how-to-use-it) to install **kandinsky** and **ion** on your computer !  

## How to use it
***
To use it properly you need to install several python packages on your computer whith the command line:

* [Kandinsky](https://github.com/ZetaMap/Kandinsky-Numworks) : `pip install kandinsky`

* [Ion](https://github.com/ZetaMap/Ion-numworks) : `pip install --pre ion-numworks`  

And python, of course, [here](https://www.python.org/downloads/) if you don't already have it.
###
>You can change the emulator's OS by pressing "_CTR+O_" to increase speed, so you can get the most out of it without seeing everything slow down !

## Examples
***
First of all, after you're on your computer, you need to start by importing it after installing it in the current directory, and write that on the first line of your project:
```
from visuel import *
from mathforvisuel import *
``` 
After that, you need to understand how this script is organized, with points and vectors for example, and how it works, with its functions. For this purpose, you have at your disposal two *Jupiter Notebook* containing everything that can be shown in writing for the file [mathforvisuel](ex_Math.ipynb), and [visuel](ex_Visuel.ipynb). Then there are plenty of example files for everything to do with graphics. You can see the results with the following images:

* **Function interpolation** : [exemple_interpolation.py](exemple_interpolation.py)  

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
            <th align="center">Example 2</th>
            <th align="center">Example 3</th>
            <th align="center">Example 4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\Exemples_images\exemple_interpolation_1.png"> </td>
            <td> <img src=".\Exemples_images\exemple_interpolation_2.png"> </td>
            <td> <img src=".\Exemples_images\exemple_interpolation_3.png"> </td>
            <td> <img src=".\Exemples_images\exemple_interpolation_4.png"> </td>
        </tr>
    </tbody>
</table>

* **Function alpha_pixel and argument "alpha" in draw function** : [exemple_alpha_layer.py](exemple_alpha_layer.py)

> We have to take a number less or equal to 0, and greater or equal to 1 for the alpha parameter

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
            <th align="center">Example 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\Exemples_images\exemple_alpha_layer_1.png"> </td>
            <td> <img src=".\Exemples_images\exemple_alpha_layer_2.png"> </td>
        </tr>
    </tbody>
</table>

* **Function plot** : [exemple_plot.py](exemple_plot.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
            <th align="center">Example 2</th>
            <th align="center">Example 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\Exemples_images\exemple_plot_1.png"> </td>
            <td> <img src=".\Exemples_images\exemple_plot_2.png"> </td>
            <td> <img src=".\Exemples_images\exemple_plot_3.png"> </td>
        </tr>
    </tbody>
</table>

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
