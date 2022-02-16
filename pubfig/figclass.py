"""
class to plot publication quality figure using matplotlib
"""
import matplotlib.pyplot as plt
import numpy as np
import os

from pubfig.config import get_config, create_project, get_projects
# from .config import get_config, create_project, get_projects
from pubfig.figsize import fig_size
from pubfig.figtool import divide_axes, add_label

import logging
log = logging.getLogger(__name__)

available_styles = get_config('STYLES')
_style_table_sheet = get_config('FIG_STYLES')
_style_table_manual = get_config('FIG_MANUALS')


class FigClass:

    def __init__(self,
                 project=None,
                 fignum=1,
                 style='default',
                 size='A4',
                 size_unit='cm',
                 canvas_format='A4',
                 ):
        """

        :param project: str, project name
        :param fignum: str or int, matplotlib figure number
        :param style: str, one of keys in available_styles
        :param size: string or (tuple, list). if string, it must be a key in FigSize.FigSize
        :param size_unit: str, 'cm' or 'inch', or anything defined in FigSize.Units
        :param canvas_format: str, must be defined in FigSize.MaxSize
        """
        self.project = project
        if project:
            self.set_project(project)
        else:
            self._project_dir = None
            self._data_dir = None

        self.fignum = fignum

        # set style
        if style in available_styles:
            self.set_style(style)
        else:
            log.info('setting style to default...')
            self.set_style('default')

        # set size
        self.set_size(size, size_unit, canvas_format)

        # data
        self.data = None
        self.data_file_name = None

        # handles
        self.figure = None      # mpl figure handle
        self.axes = []          # mpl axes handle
        self._axes_bbox = []    # bounding boxed for each axes
        self.texts = dict()     # mpl handles to added texts
        self.labels = dict()    # mpl handles to added labels

    def _init_fig(self):
        if plt.fignum_exists(self.fignum):
            plt.close(self.fignum)
        self.figure = plt.figure(self.fignum, figsize=self.size)
        self.axes = []
        self._axes_bbox = []
        self.texts = dict()
        self.labels = dict()

    def load_data(self, file_name):
        self.data_file_name = os.path.join(self._data_dir, file_name)
        self._load_data(self.data_file_name)

    def _load_data(self, file_name):
        """
        :param file_name: absolute path to the data file
        :return:
        """
        raise NotImplementedError

    def set_project(self, project_name):
        """
        :param project_name: str, project name
        :return:
        """
        if project_name not in get_projects():  # create new project
            self._project_dir = create_project(project_name)
        else:
            self._project_dir = os.path.join(get_config('BASE_DIR'), project_name)
        self._data_dir = os.path.join(self._project_dir, 'Data')

    def set_style(self, style):
        """
        :param style: style: str, one of keys in available_styles
        :return:
        """
        if style in available_styles:
            self.style = style
            self._style_sheet_dir = _style_table_sheet[style]
            self._style_manual = _style_table_manual[style]
        else:
            log.warning('style: {} not defined. no change is made')

        self.set_output_dir()

    def set_output_dir(self):
        if self.style in ('default', 'A4paper', 'presentation', 'poster'):
            self._output_dir = os.path.join(self._project_dir, 'FIG')
        else:
            self._output_dir = os.path.join(self._project_dir, 'submission_' + self.style)
            if not os.path.isdir(self._output_dir):
                log.info('Creating directory, {} for current project'.format(self._output_dir))
                os.mkdir(self._output_dir)

    def set_size(self, size, size_unit, canvas_format):
        """
        :param size: size: string or (tuple, list). if string, it must be a key in FigSize.FigSize
        :param size_unit: str, 'cm' or 'inch', or anything defined in FigSize.Units
        :param canvas_format: str, must be defined in FigSize.MaxSize
        :return:
        """
        size = fig_size(size, size_unit, canvas_format)
        self.size = size
        self.size_unit = size_unit
        self.canvas_format = canvas_format

    def divide_axes(self,
                    target=None,
                    X0=None,
                    Y0=None,
                    DivX=(1, 1),
                    DivY=(1, 1),
                    SepXs=(0.4, ),
                    SepYs=(0.6, ),
                    create_axes=True,
                    after_reset=False,
                    ):
        """
        divide figure canvas or an axes
        :param target: obj to be divided, a plt.figure.Figure or plt.axes._axes.Axes instance. if None, use plt.gcf()
                   can also be a tuple/list/numpy array of rect definition in form of [x0, y0, x_size, y_size]
                   can also be a coordinate into self.axes
        :param X0: tuple or list with 2-elements, Outer Boundary in X-Direction
        :param Y0: tuple or list with 2-elements, Outer Boundary in Y-Direction
        :param DivX: tuple or list, Vector of relative Sizes in X-Direction; can also be single number
        :param DivY: tuple or list, Vector of relative Sizes in Y-Direction; can also be single number
        :param SepXs: tuple or list, X Separation between the subplots (one less than the DivX, or single element)
        :param SepYs: tuple or list, Y Separation between the subplots (one less than the DivY, or single element)
        :param create_axes: bool, if create axes objects
        :param after_reset: bool, if apply style after resetting settings to defaults
        :return:
            None
        """
        if not target:
            if not self.figure:
                self._init_fig()
            target = self.figure

        with plt.style.context(self._style_sheet_dir, after_reset):
            re = divide_axes(target, X0, Y0, DivX, DivY, SepXs, SepYs, create_axes)
            self.axes.append(re[1])
            self._axes_bbox.append(re[0])

        return re

    def add_label(self,
                  label,
                  pos=None,
                  ref=None,
                  fontdict=None
                  ):
        """
        add subplot label
        :param label: string to be added as label
        :param pos: relative position of the label to the reference point. use figure transform system
        :param ref: reference point of the label; a mpl.figure.Figure or mpl.axes._axes.Axes instance
        :param fontdict: matplotlib font dictionary
        :return:
            None
        """
        if not ref:
            if not self.figure:
                self._init_fig()
            ref = self.figure
        if not fontdict:
            fontdict = self._style_manual['label']

        self.labels.update({label: add_label(label, pos, ref, fontdict)})
        return self.labels[label]

    def add_text(self,
                 text,
                 pos=None,
                 ref=None,
                 fontdict=None
                 ):
        """
        add subplot label
        :param text: string to be added as text
        :param pos: relative position of the label to the reference point. use figure transform system
        :param ref: reference point of the label; a mpl.figure.Figure or mpl.axes._axes.Axes instance
        :param fontdict: matplotlib font dictionary
        :return:
            None
        """
        if not ref:
            if not self.figure:
                self._init_fig()
            ref = self.figure
        if not fontdict:
            fontdict = self._style_manual['text']

        self.texts.update({text: add_label(text, pos, ref, fontdict)})
        return self.texts[text]

    def plot(self, save_format='png', save=True):
        raise NotImplementedError
