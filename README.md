<p align="center" width="100%">
<img src=".\pictures\logo\logo_visuel.png" alt="Visuel">
</p>

# Visuel

###
Welcome ! This project is intended for use in conjunction with Kandinsky on a laptop or Numworks calculator. It allows you to add graphical functions, mainly around new drawing functions like line or circle drawing, but also mathematical classes like vectors or points, and much more !

> Visual on the Numworks calculator will soon be available after a code refactoring to adapt it to micropython. The extensions are almost finished and will also undergo a reduction in memory size and a refactoring to adapt them in the same way.

## Table of Contents
***
1. [General Info](#general-info)
2. [How to use it](#how-to-use-it)
3. [Examples](#examples)
3. [Tree Fractals](#tree-fractals)
5. [More Info](#more-info)
6. [FAQs](#faqs)

## General Info
***
I recommend that you test the sample files on your computer, as you may be able to increase the speed.

To install it on the Numworks, we have the choice :  
1. Just follow this link to the [Numworks website](https://my.numworks.com/python/archange/visuel)  

2. you just need to copy and paste the code from this file: [visuel](visuel.py) into a new script on your Numworks account. Then upload them to your calculator. 

On your laptop, you can use this [file](visuel_for_computer.py). If you have any questions, go to the [FAQs section](#faqs), or explore all the examples [here](#examples) after visiting this [page](#how-to-use-it) to install **kandinsky** and **ion** on your computer !  

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
```
from visuel import *
``` 
After that, you need to understand how this script is organized, with points and vectors for example, and how it works, with its functions. For this purpose, you have at your disposal one *Jupiter Notebook* containing everything that can be shown in writing for the file [visuel_example](visuel_example.ipynb). Then there are plenty of example files for everything to do with graphics. You can see the results with the following images :

* **Function interpolation** : [example_interpolation.py](example_interpolation.py)  

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

* **Function expend** : [example_vectoriel_geometry](example_vectoriel_geometry.py)

* **Function findWithPoint** : [example_findwithpoint.py](example_findwithpoint.py)  

* **Function findWithAngle** : [example_findwithangle.py](example_findwithangle.py)  


* **Function alpha_pixel and argument "alpha" in draw function** : [example_alpha_layer.py](example_alpha_layer.py)

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

* **Function scatter** : [example_scatter.py](example_scatter.py)

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

* **Function plot** : [example_plot.py](example_plot.py)

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

* **Function set_lines** : [example_lines.py](example_lines.py)

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

* **Function draw_points** : [example_point.py](example_point.py)

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

* **Function draw_croix** : [example_croix.py](example_croix.py)

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

* **Function draw_arrows** : [example_arrows.py](example_arrows.py)

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

* **Function draw_vector** : [example_vectors.py](example_vectors.py)

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

* **Function draw_droite** : [example_droite.py](example_droite.py)

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

* **Function fill_triangles** : [example_triangle.py](example_triangle.py)

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

* **Function draw_polygone and fill_polygone** : [example_polygone.py](example_polygone.py)

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

* **Function draw_circle and fill_circle** : [example_cercle.py](example_cercle.py)

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

* **Function bezier curve** : [example_bezier_curve](example_bezier_curve.py)

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
            <td> <img src=".\pictures\example_bezier_N_curve.png"> </td>
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

* **Function draw_quadratic** : [example_quadratic_bezier_curve.py](example_quadratic_bezier_curve.py)  

> Just on laptop !

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_bezier_quadratic_curve.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_cubic** : [example_cubic_bezier_curve.py](example_cubic_bezier_curve.py)

> Just on laptop too !

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_bezier_cubic_curve.png"> </td>
        </tr>
    </tbody>
</table>

## Tree Fractals
The link to the example script: [example_fractal.py](example_fractale.py)
***

> Don't forget to install the lines extension ([here](ext_lines.py)) in your calculator !

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

## More Info
***
Extensions will soon be available. They including another graphics tool and a tool already present on Numworks.

* **Extension Lines** : [lines_example.py](lines_example.py)

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


* **Extension Ellipses** : [example_ellipse.py](ext_ellipses.py)

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

* **Extension Turtle** : [turtle_example.py](turtle_example.py)

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

<table>
    <thead>
        <tr>
            <th align="center">[Preview] Grapher</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\grapher_pictures\example_1.png"> </td>
        </tr>
        <tr>
            <td> <img src=".\pictures\grapher_pictures\example_2.png"> </td>
        </tr>
    </tbody>
</table>

## FAQs
***
A list of frequently asked questions (for the moment there is none).
