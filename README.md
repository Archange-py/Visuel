<p align="center" width="100%">
<img src=".\pictures\logo\logo_visuel.png" alt="Visuel">
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
I recommend that you test the sample files on your computer, as you may be able to increase the speed.

To install it on the Numworks, we have the choice :  
1. Just follow this link to the [Numworks website](https://numworks.com)  

2. you just need to copy and paste the code from this file: [visuel](visuel.py) into a new script on your Numworks account. Then upload them to your calculator. 

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

* **Function draw_lines** : [example_lines.py](example_lines.py)

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


* **Function draw_ellipses and fill_ellipses** : [example_ellipse.py](example_ellipse.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
            <th align="center">Example 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\example_ellipses_1.png"> </td>
            <td> <img src=".\pictures\example_ellipses_2.png"> </td>
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

## More Info
***
Extensions will soon be available. They including another graphics tool and a tool already present on Numworks.

<table>
    <thead>
        <tr>
            <th align="center">Grapher</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\pictures\grapher_pictures\example_1.png"> </td>
        </tr>
    </tbody>
</table>

## FAQs
***
A list of frequently asked questions (for the moment there is none).
