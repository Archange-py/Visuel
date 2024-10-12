<p align="center" width="100%">
<img src=".\pictures\assets\logo\logo_visuel.png" alt="Visuel">
</p>

# Visuel

###
Welcome ! This project is intended for use in conjunction with Kandinsky on a laptop or Numworks calculator. It allows you to add graphical functions, mainly around new drawing functions like line or circle drawing, but also mathematical classes like vectors or points, and much more !

## Table of Contents
***
1. [General Info](#general-info)
2. [How to use it](#how-to-use-it)
3. [Examples](#examples)
3. [Tree Fractals](#tree-fractals)
5. [Extensions](#extensions)
6. [QR-Codes](#qr-codes)
7. [FAQs](#faqs)

## General Info
***
I recommend that you test the sample files on your computer, as you may be able to increase the speed.

To install it on the Numworks, we have the choice :  
1. Just follow this link to the [Numworks website](https://my.numworks.com/python/archange/visuel)  

2. you just need to copy and paste the code from this file: [visuel](visuel.py) into a new script on your Numworks account. Then upload them to your calculator. 

> Here's an example of what you can do with the calculator, using the [example file](visuel_first_example.py). Click [here](https://my.numworks.com/python/archange/example_visuel) to see it on the Numworks website.  

<p align="center" width="100%">
<img src=".\pictures\example_visuel.png" alt="Visuel">
</p>

If you have any questions, go to the [FAQs section](#faqs), or explore all the examples [here](#examples) after visiting this [page](#how-to-use-it) to install **kandinsky** and **ion** on your computer !  

## How to use it
***
To use it properly you need to install several python packages on your computer whith the command line:

* [Kandinsky](https://github.com/ZetaMap/Kandinsky-Numworks) :  
```
pip install kandinsky
```

* [Ion](https://github.com/ZetaMap/Ion-numworks) :  
```
pip install --pre ion-numworks
```

And python, of course, [here](https://www.python.org/downloads/) if you don't already have it.
###
>You can change the emulator's OS by pressing "_CTR+O_" to increase speed, so you can get the most out of it without seeing everything slow down !

## Examples
***
First of all, after you're on your computer, you need to start by importing it after installing it in the current directory, and write that on the first line of your project:
```Python
from visuel import *
``` 
After that, you need to understand how this script is organized, with points and vectors for example, and how it works, with its functions. For this purpose, you have at your disposal one *Jupiter Notebook* containing everything that can be shown in writing for the file [visuel_example](visuel_example.ipynb). Then there are plenty of example files for everything to do with graphics. You can see the results with the following images :

* **Function interpolation** : [example_interpolation.py](\examples\example_interpolation.py)  

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
            <td> <img src=".\pictures\example_interpolate_1.png"> </td>
            <td> <img src=".\pictures\example_interpolate_2.png"> </td>
            <td> <img src=".\pictures\example_interpolate_3.png"> </td>
            <td> <img src=".\pictures\example_interpolate_4.png"> </td>
        </tr>
    </tbody>
</table>

* **Function expend** : [example_vectoriel_geometry](\examples\example_vectoriel_geometry.py)

* **Function findWithPoint** : [example_findwithpoint.py](\examples\example_findwithpoint.py)

* **Function alpha_pixel and argument "alpha" in draw function** : [example_alpha_layer.py](\examples\example_alpha_layer.py)

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
            <td> <img src=".\pictures\example_alpha_layer_1.png"> </td>
            <td> <img src=".\pictures\example_alpha_layer_2.png"> </td>
        </tr>
    </tbody>
</table>

* **Function scatter** : [example_scatter.py](\examples\example_scatter.py)

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
            <td> <img src=".\pictures\example_scatter_1.png"> </td>
            <td> <img src=".\pictures\example_scatter_2.png"> </td>
            <td> <img src=".\pictures\example_scatter_3.png"> </td>
        </tr>
    </tbody>
</table>

* **Function plot** : [example_plot.py](\examples\example_plot.py)

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
            <td> <img src=".\pictures\example_plot_1.png"> </td>
            <td> <img src=".\pictures\example_plot_2.png"> </td>
            <td> <img src=".\pictures\example_plot_3.png"> </td>
        </tr>
    </tbody>
</table>

* **Function set_lines** : [example_lines.py](\examples\example_lines.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_lines.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_points** : [example_point.py](\examples\example_point.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_points.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_croix** : [example_croix.py](\examples\example_croix.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_croix.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_arrows** : [example_arrows.py](\examples\example_arrows.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_arrows.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_vector** : [example_vectors.py](\examples\example_vectors.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_vectors.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_droite** : [example_droite.py](\examples\example_droite.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
            <th align="center">Example 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_droite_1.png"> </td>
            <td> <img src=".\pictures\example_droite_2.png"> </td>
        </tr>
    </tbody>
</table>

* **Function fill_triangles** : [example_triangle.py](\examples\example_triangle.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_triangles.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_polygone and fill_polygone** : [example_polygone.py](\examples\example_polygone.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_polygones.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_circle and fill_circle** : [example_cercle.py](\examples\example_cercle.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_cercle.png"> </td>
        </tr>
    </tbody>
</table>

* **Function bezier curve** : [example_bezier_curve](\examples\example_bezier_curve.py)

<table>
    <thead>
        <tr>
            <th align="center">Examples</th>
            <th align="center">Examples</th>
            <th align="center">Examples</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_bezier_curve.png"> </td>
            <td> <img src=".\pictures\example_bezier_curve_2.png"> </td>
            <td> <img src=".\pictures\example_bezier_curve_3.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_bezier_curve_4.png"> </td>
            <td> <img src=".\pictures\example_bezier_curve_5.png"> </td>
            <td> <img src=".\pictures\example_bezier_curve_6.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_bezier_curve_7.png"> </td>
            <td> <img src=".\pictures\example_bezier_curve_8.png"> </td>
            <td> <img src=".\pictures\example_bezier_curve_9.png"> </td>
        </tr>
    </tbody>
</table>

## Tree Fractals
The link to the example script: [example_fractal.py](fractal_example.py)  
And the source script: [fractal.py](fractal.py)  
***

> Don't forget to install the lines extension ([here](ext_lines.py)) in your computer !

<table>
    <thead>
        <tr>
            <th align="center">Basics Tree</th>
            <th align="center">Palmier</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_basic_tree_1.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_palm_red_yellow_1.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_basic_tree_2.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_palm_red_yellow_2.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_basic_tree_black_1.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_palm_black_1.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_basic_tree_black_2.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_palm_black_2.png"> </td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th align="center">Cyan Tree</th>
            <th align="center">Cyan Tree</th>
            <th align="center">Cyan Tree</th>
            <th align="center">Cyan Tree</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_magenta_1.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_magenta_2.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_magenta_3.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_magenta_4.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_magenta_thickness_1.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_magenta_thickness_2.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_magenta_thickness_3.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_magenta_thickness_4.png"> </td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th align="center">Magenta Tree</th>
            <th align="center">Magenta Tree</th>
            <th align="center">Magenta Tree</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_cyan_angle_1.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_cyan_angle_2.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_cyan_angle_3.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_cyan_angle_4.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_cyan_angle_5.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_cyan_angle_6.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_cyan_angle_7.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_cyan_angle_8.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_cyan_angle_9.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_cyan_angle_10.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_cyan_angle_11.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_cyan_angle_12.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_cyan_angle_13.png"> </td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th align="center">Examples Trees</th>
            <th align="center">Examples Trees</th>
            <th align="center">Examples Trees</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_tree_blue.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_tree_cyan.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_tree_fushia.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_tree_green.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_tree_magenta.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_tree_orange.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_tree_pink.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_tree_purple.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_tree_red.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_tree_yellow.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_tree_white.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_thickness_purple.png"> </td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th align="center">Angle Tree </th>
            <th align="center">Angle Tree </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\fractal_pictures\fractale_h_magenta_purple.png"> </td>
            <td> <img src=".\pictures\fractal_pictures\fractale_h_black.png"> </td>
        </tr>
    </tbody>
</table>

## Extensions
***
Here are some extensions designed to work with the calculator. However, the latest extension, Grapher, will only work on a computer. They include a number of extra features, notably a reproduction of the turtle module, and another, much simpler one, of the matplotlib.pyplot module. I'll let you discover them with some beautiful images!

> You need to copy and paste the code from the extension files into a new file created on the Numworks website.

* **Extension Lines** : [lines_example.py](\extensions\lines_example.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\lines_pictures\example_lines.png"> </td>
        </tr>
    </tbody>
</table>


* **Extension Ellipses** : [example_ellipse.py](\extensions\ext_ellipses.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
            <th align="center">Example 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\ellipses_pictures\example_ellipses_1.png"> </td>
            <td> <img src=".\pictures\ellipses_pictures\example_ellipses_2.png"> </td>
        </tr>
    </tbody>
</table>

* **Extension Turtle** : [turtle_example.py](\extensions\turtle_example.py)

> The turtle extension has both a compact and a non-compact file for use on the computer.

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\turtle_pictures\example_1_flocon_1.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\pictures\turtle_pictures\example_1_flocon_2.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\pictures\turtle_pictures\example_1_flocon_3.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\pictures\turtle_pictures\example_1_flocon_4.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\pictures\turtle_pictures\example_1_flocon_5.png"> </td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th align="center">Example 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\.\pictures\turtle_pictures\example_2.png"> </td>
        </tr>
    </tbody>
</table>

* **Extension Grapher** : [grapher_example.ipynb](\extensions\grapher_example.ipynb)  

<table>
    <thead>
        <th>Keys</th>
        <th>Short</th>
    </thead>
    <tbody>
        <tr>
            <td>Arrows [Up, Down, Right, Left]</td>
            <td>allows you to move around the grapher</td>
        </tr>
        <tr>
            <td>'Maj'+'=' or '+'</td>
            <td>zoom in or out</td>
        </tr>
        <tr>
            <td>'Maj'+'à' or '0'</td>
            <td>refocuses the graphic</td>
        </tr>
        <tr>
            <td>'Ctr'+'o'</td>
            <td>changes the emulator, thus increasing speed</td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th align="center">Examples :</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\.\extensions\grapher_pictures\example_fonction_axes_1.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\.\extensions\grapher_pictures\example_fonction_axes_poo_1.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\.\extensions\grapher_pictures\example_fonction_axes_2.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\.\extensions\grapher_pictures\example_fonction_axes_poo_2.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\.\extensions\grapher_pictures\example_fonction_axes_poo_3.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\.\extensions\grapher_pictures\example_fonction_axes_poo_4.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\.\extensions\grapher_pictures\example_fonction_axes_poo_5.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\.\extensions\grapher_pictures\example_fonction_axes_poo_6.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\.\extensions\grapher_pictures\example_fonction_scatter_and_points_2.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\.\extensions\grapher_pictures\example_fonction_plot_and_lines_1.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\.\extensions\grapher_pictures\example_fonction_vector_1.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\.\extensions\grapher_pictures\example_fonction_droite_1.png"> </td>
        </tr>
    </tbody>
</table>

## QR-Codes
***
Here are two QR codes to easily find the Visuel library on GitHub and on the official Numworks website. Use them without restriction!

* The GitHub'link: ![Github](.\pictures\assets\QR_codes\qr_code_site_github_2.png)

* The Numworks'link: ![Github](.\pictures\assets\QR_codes\qr_code_site_numworks_2.png)


## FAQs
***
A list of frequently asked questions (for the moment there is none).
