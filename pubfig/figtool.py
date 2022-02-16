"""
core tools to plot the figure
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def divide_axes(target=None,
                X0=None,
                Y0=None,
                DivX=(1, 1),
                DivY=(1, 1),
                SepXs=(0.4, ),
                SepYs=(0.6, ),
                create_axes=True,
                ):
    """
    divide figure canvas or an axes
    :param target: obj to be divided, a plt.figure.Figure or plt.axes._axes.Axes instance. if None, use plt.gcf()
                   can also be a tuple/list/numpy array of rect definition in form of [x0, y0, x_size, y_size]
    :param X0: tuple or list with 2-elements, Outer Boundary in X-Direction
    :param Y0: tuple or list with 2-elements, Outer Boundary in Y-Direction
    :param DivX: tuple or list, Vector of relative Sizes in X-Direction; can also be single number
    :param DivY: tuple or list, Vector of relative Sizes in Y-Direction; can also be single number
    :param SepXs: tuple or list, X Separation between the subplots (one less than the DivX, or single element)
    :param SepYs: tuple or list, Y Separation between the subplots (one less than the DivY, or single element)
    :param create_axes: bool, if create axes objects
    :return:
        list of bounding boxes and axes handles
    """
    # set defaults
    if not target and create_axes:
        target = plt.gcf()
    # get figure handle
    if target:
        if isinstance(target, mpl.figure.Figure):
            fg_h = target
        elif isinstance(target, mpl.axes._axes.Axes):
            fg_h = target.figure
    if isinstance(target, mpl.figure.Figure) and create_axes:
        target.clf()
    if isinstance(target, mpl.axes._axes.Axes) and create_axes:
        target.remove()

    if not X0:
        if isinstance(target, mpl.figure.Figure):
            X0 = (0.1, 0.85)
        else:
            X0 = (0, 1)
    if not Y0:
        if isinstance(target, mpl.figure.Figure):
            Y0 = (0.1, 0.85)
        else:
            Y0 = (0, 1)

    if isinstance(target, mpl.axes._axes.Axes):
        axes_rect = target._position.bounds
    elif isinstance(target, (tuple, list, np.ndarray)):
        axes_rect = target
    elif isinstance(target, mpl.figure.Figure):
        axes_rect = (0, 0, 1, 1)
    # adjust X0, Y0 based on axes_rect
    X0 = (axes_rect[0] + X0[0] * axes_rect[2], ) + (X0[1] * axes_rect[2], )
    Y0 = (axes_rect[1] + Y0[0] * axes_rect[3], ) + (Y0[1] * axes_rect[3], )

    # check input parameters
    # if DivX or DivY is just one number, consider it the number of divisions
    if isinstance(DivX, (int, float)):
        DivX = (1, ) * int(DivX)
    elif DivX.__len__() == 1 and DivX[0] > 1:
        DivX = (1, ) * int(DivX[0])
    if isinstance(DivY, (int, float)):
        DivY = (1, ) * int(DivY)
    elif DivY.__len__() == 1 and DivY[0] > 1:
        DivY = (1, ) * int(DivY[0])
    # If SepXs or SepYs is just one number, use it for all separations
    if isinstance(SepXs, (int, float)):
        SepXs = (SepXs, ) * (DivX.__len__() - 1)
    elif SepXs.__len__() == 1 and DivX.__len__() > 2:
        SepXs = SepXs * (DivX.__len__() - 1)
    if isinstance(SepYs, (int, float)):
        SepYs = (SepYs, ) * (DivY.__len__() - 1)
    elif SepYs.__len__() == 1 and DivY.__len__() > 2:
        SepYs = SepYs * (DivY.__len__() - 1)

    # set Seps to 0 if there is only 1 division
    if len(DivX) == 1:
        SepXs = [0]
    if len(DivY) == 1:
        SepYs = [0]

    # convert to np arrays
    DivX = np.array(DivX)
    DivY = np.array(DivY)
    SepXs = np.array(SepXs)
    SepYs = np.array(SepYs)
    X0 = np.array(X0)
    Y0 = np.array(Y0)

    # calculation
    NX = sum(DivX) + sum(SepXs)  # total length before normalization
    NY = sum(DivY) + sum(SepYs)
    DivX_N = DivX / NX * X0[1]     # actual relative size
    SepXs_N = SepXs / NX * X0[1]
    DivY_N = DivY / NY * Y0[1]
    SepYs_N = SepYs / NY * Y0[1]
    Divs_C = [[0 for i in range(DivX.size)] for j in range(DivY.size)]
    Ax_H = [[0 for i in range(DivX.size)] for j in range(DivY.size)]
    for iy in range(DivY.size):   # should flip y so it goes from top to bottom
        for ix in range(DivX.size):
            Divs_C[iy][ix] = \
            [
                X0[0] + sum(DivX_N[:ix]) + sum(SepXs_N[:ix]),
                Y0[0] + sum(DivY_N[iy+1:]) + sum(SepYs_N[iy:]),
                DivX_N[ix],
                DivY_N[iy]
             ]

    if create_axes:
        for iy in range(DivY.size):
            for ix in range(DivX.size):
                Ax_H[iy][ix] = fg_h.add_axes(Divs_C[iy][ix])

    return Divs_C, Ax_H


def add_label(s, pos=None, ref=None, fontdict=None):
    """
    add subplot label
    :param s: string to be added as label
    :param pos: relative position of the label to the reference point. use figure transform system
    :param ref: reference point of the label; a mpl.figure.Figure or mpl.axes._axes.Axes instance
    :param fontdict: matplotlib font dictionary
    :return:
        handle to the label added
    """
    if not pos and not ref:
        raise ValueError('One of the input pos or ref must be provided')
    if not ref:
        ref = plt.gcf()
    if isinstance(ref, mpl.figure.Figure):
        if not pos:
            final_pos = (0.05, 0.9)
        else:
            final_pos = pos
        fg_h = ref
    elif isinstance(ref, mpl.axes._axes.Axes):
        if not pos:
            pos = (-0.05, 0.02)
        # calculate position of the label in figure coordinate
        ax_pos = ref._position.bounds
        final_pos = (ax_pos[0] + pos[0], ax_pos[1] + ax_pos[3] + pos[1])
        fg_h = ref.figure

    # add text using figure coordinate
    return plt.text(final_pos[0], final_pos[1], s, fontdict=fontdict,
                    ha='left', va='center', transform=fg_h.transFigure)
