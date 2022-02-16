This package is designed to plot complex publication-ready figures composed of multiple subplots with uneven splitting of the canvas. The plotting is based on matplotlib.

## Getting Started

### Requirement
Python >= 3.7 with Numpy, Matplotlib

### Installation
Install the package using the following command:
```commandline
   #ToDO
```


## Core ideas and classes

The core of this toolbox is the function divide_axes. It can be used to divide (and further subdivide) any matplotlib axes object. See the provided examples for the usage.

The FigClass class provides a wrapper that wrap all the information about one figure in a single place.

The `Config` module is used to define some globals and constants, e.g. where to located the data by default, and predefined formats for different journals/presentations/posters.


## Examples

Below we demonstrate the usage of the core funciton, `divide_axes`:
```
    from pubfig import divide_axes
    import matplotlib.pyplot as plt
```
The function can work with either a matplotlib figure, or an axes. Below we use it to divide a figure:
```
    fig = plt.figure()
    # divide the figure into 3 column, 1 row; the 3 columns have ratio of 1:2:1
    boxes, axes = divide_axes(fig, DivX=[1, 2, 1], DivY=1)
```
The axes returned are indexed as [row][column], i.e. here we have 1 row and 3 columns, and the middle axes can be accessed by axes[0][1].
We can use the function to further divide the axes. E.g. we can divide the 2nd axes into 2 rows and 2 columns, equally spaced:
```
    new_boxes, new_axes = divide_axes(axes[0][1], DivX=2, DivY=2)
```
The new_axes with be 2 rows, 2 columns list, each element is the corresponding new axes.

See the `example` folder for further example. The examples are used to demonstrate how to divide axes; data associated is not provided. However, one example of the plotted figure can be seen in `Figure_1.png`


## Possible issues

Currently only tested on Windows system. The settings in the `Config` probably need to be modified/added for it to work also in iOS and Linux.


## Feedback and feature request

Please contact me, or even better in case of feature request: implement them yourself!
