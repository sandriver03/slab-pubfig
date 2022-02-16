import os
from pubfig.config import get_config
# from . import get_config


# constants
# create matplotlib style sheets
DEFAULT_AUTO_STYLE = {
    # Font
    'font.family': 'Arial',
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'xtick.direction': 'in',
    'ytick.labelsize': 8,
    'ytick.direction': 'in',
    'legend.fontsize': 9,
    'lines.markersize': 8,
    'figure.dpi': 200,
}
ALLOWED_AUTO_KEYS = [
    '_internal.classic_mode',
    'agg.path.chunksize',
    'animation.avconv_args',
    'animation.avconv_path',
    'animation.bitrate',
    'animation.codec',
    'animation.convert_args',
    'animation.convert_path',
    'animation.embed_limit',
    'animation.ffmpeg_args',
    'animation.ffmpeg_path',
    'animation.frame_format',
    'animation.html',
    'animation.html_args',
    'animation.writer',
    'axes.autolimit_mode',
    'axes.axisbelow',
    'axes.edgecolor',
    'axes.facecolor',
    'axes.formatter.limits',
    'axes.formatter.min_exponent',
    'axes.formatter.offset_threshold',
    'axes.formatter.use_locale',
    'axes.formatter.use_mathtext',
    'axes.formatter.useoffset',
    'axes.grid',
    'axes.grid.axis',
    'axes.grid.which',
    'axes.labelcolor',
    'axes.labelpad',
    'axes.labelsize',
    'axes.labelweight',
    'axes.linewidth',
    'axes.prop_cycle',
    'axes.spines.bottom',
    'axes.spines.left',
    'axes.spines.right',
    'axes.spines.top',
    'axes.titlepad',
    'axes.titlesize',
    'axes.titleweight',
    'axes.unicode_minus',
    'axes.xmargin',
    'axes.ymargin',
    'axes3d.grid',
    'backend',
    'backend.qt4',
    'backend.qt5',
    'backend_fallback',
    'boxplot.bootstrap',
    'boxplot.boxprops.color',
    'boxplot.boxprops.linestyle',
    'boxplot.boxprops.linewidth',
    'boxplot.capprops.color',
    'boxplot.capprops.linestyle',
    'boxplot.capprops.linewidth',
    'boxplot.flierprops.color',
    'boxplot.flierprops.linestyle',
    'boxplot.flierprops.linewidth',
    'boxplot.flierprops.marker',
    'boxplot.flierprops.markeredgecolor',
    'boxplot.flierprops.markerfacecolor',
    'boxplot.flierprops.markersize',
    'boxplot.meanline',
    'boxplot.meanprops.color',
    'boxplot.meanprops.linestyle',
    'boxplot.meanprops.linewidth',
    'boxplot.meanprops.marker',
    'boxplot.meanprops.markeredgecolor',
    'boxplot.meanprops.markerfacecolor',
    'boxplot.meanprops.markersize',
    'boxplot.medianprops.color',
    'boxplot.medianprops.linestyle',
    'boxplot.medianprops.linewidth',
    'boxplot.notch',
    'boxplot.patchartist',
    'boxplot.showbox',
    'boxplot.showcaps',
    'boxplot.showfliers',
    'boxplot.showmeans',
    'boxplot.vertical',
    'boxplot.whiskerprops.color',
    'boxplot.whiskerprops.linestyle',
    'boxplot.whiskerprops.linewidth',
    'boxplot.whiskers',
    'contour.corner_mask',
    'contour.negative_linestyle',
    'datapath',
    'date.autoformatter.day',
    'date.autoformatter.hour',
    'date.autoformatter.microsecond',
    'date.autoformatter.minute',
    'date.autoformatter.month',
    'date.autoformatter.second',
    'date.autoformatter.year',
    'docstring.hardcopy',
    'errorbar.capsize',
    'examples.directory',
    'figure.autolayout',
    'figure.constrained_layout.h_pad',
    'figure.constrained_layout.hspace',
    'figure.constrained_layout.use',
    'figure.constrained_layout.w_pad',
    'figure.constrained_layout.wspace',
    'figure.dpi',
    'figure.edgecolor',
    'figure.facecolor',
    'figure.figsize',
    'figure.frameon',
    'figure.max_open_warning',
    'figure.subplot.bottom',
    'figure.subplot.hspace',
    'figure.subplot.left',
    'figure.subplot.right',
    'figure.subplot.top',
    'figure.subplot.wspace',
    'figure.titlesize',
    'figure.titleweight',
    'font.cursive',
    'font.family',
    'font.fantasy',
    'font.monospace',
    'font.sans-serif',
    'font.serif',
    'font.size',
    'font.stretch',
    'font.style',
    'font.variant',
    'font.weight',
    'grid.alpha',
    'grid.color',
    'grid.linestyle',
    'grid.linewidth',
    'hatch.color',
    'hatch.linewidth',
    'hist.bins',
    'image.aspect',
    'image.cmap',
    'image.composite_image',
    'image.interpolation',
    'image.lut',
    'image.origin',
    'image.resample',
    'interactive',
    'keymap.all_axes',
    'keymap.back',
    'keymap.copy',
    'keymap.forward',
    'keymap.fullscreen',
    'keymap.grid',
    'keymap.grid_minor',
    'keymap.help',
    'keymap.home',
    'keymap.pan',
    'keymap.quit',
    'keymap.quit_all',
    'keymap.save',
    'keymap.xscale',
    'keymap.yscale',
    'keymap.zoom',
    'legend.borderaxespad',
    'legend.borderpad',
    'legend.columnspacing',
    'legend.edgecolor',
    'legend.facecolor',
    'legend.fancybox',
    'legend.fontsize',
    'legend.framealpha',
    'legend.frameon',
    'legend.handleheight',
    'legend.handlelength',
    'legend.handletextpad',
    'legend.labelspacing',
    'legend.loc',
    'legend.markerscale',
    'legend.numpoints',
    'legend.scatterpoints',
    'legend.shadow',
    'legend.title_fontsize',
    'lines.antialiased',
    'lines.color',
    'lines.dash_capstyle',
    'lines.dash_joinstyle',
    'lines.dashdot_pattern',
    'lines.dashed_pattern',
    'lines.dotted_pattern',
    'lines.linestyle',
    'lines.linewidth',
    'lines.marker',
    'lines.markeredgecolor',
    'lines.markeredgewidth',
    'lines.markerfacecolor',
    'lines.markersize',
    'lines.scale_dashes',
    'lines.solid_capstyle',
    'lines.solid_joinstyle',
    'markers.fillstyle',
    'mathtext.bf',
    'mathtext.cal',
    'mathtext.default',
    'mathtext.fallback_to_cm',
    'mathtext.fontset',
    'mathtext.it',
    'mathtext.rm',
    'mathtext.sf',
    'mathtext.tt',
    'patch.antialiased',
    'patch.edgecolor',
    'patch.facecolor',
    'patch.force_edgecolor',
    'patch.linewidth',
    'path.effects',
    'path.simplify',
    'path.simplify_threshold',
    'path.sketch',
    'path.snap',
    'pdf.compression',
    'pdf.fonttype',
    'pdf.inheritcolor',
    'pdf.use14corefonts',
    'pgf.preamble',
    'pgf.rcfonts',
    'pgf.texsystem',
    'polaraxes.grid',
    'ps.distiller.res',
    'ps.fonttype',
    'ps.papersize',
    'ps.useafm',
    'ps.usedistiller',
    'savefig.bbox',
    'savefig.directory',
    'savefig.dpi',
    'savefig.edgecolor',
    'savefig.facecolor',
    'savefig.format',
    'savefig.frameon',
    'savefig.jpeg_quality',
    'savefig.orientation',
    'savefig.pad_inches',
    'savefig.transparent',
    'scatter.marker',
    'svg.fonttype',
    'svg.hashsalt',
    'svg.image_inline',
    'text.antialiased',
    'text.color',
    'text.hinting',
    'text.hinting_factor',
    'text.latex.preamble',
    'text.latex.preview',
    'text.latex.unicode',
    'text.usetex',
    'timezone',
    'tk.window_focus',
    'toolbar',
    'verbose.fileo',
    'verbose.level',
    'webagg.address',
    'webagg.open_in_browser',
    'webagg.port',
    'webagg.port_retries',
    'xtick.alignment',
    'xtick.bottom',
    'xtick.color',
    'xtick.direction',
    'xtick.labelbottom',
    'xtick.labelsize',
    'xtick.labeltop',
    'xtick.major.bottom',
    'xtick.major.pad',
    'xtick.major.size',
    'xtick.major.top',
    'xtick.major.width',
    'xtick.minor.bottom',
    'xtick.minor.pad',
    'xtick.minor.size',
    'xtick.minor.top',
    'xtick.minor.visible',
    'xtick.minor.width',
    'xtick.top',
    'ytick.alignment',
    'ytick.color',
    'ytick.direction',
    'ytick.labelleft',
    'ytick.labelright',
    'ytick.labelsize',
    'ytick.left',
    'ytick.major.left',
    'ytick.major.pad',
    'ytick.major.right',
    'ytick.major.size',
    'ytick.major.width',
    'ytick.minor.left',
    'ytick.minor.pad',
    'ytick.minor.right',
    'ytick.minor.size',
    'ytick.minor.visible',
    'ytick.minor.width',
    'ytick.right',
]
# text font cannot be set in style sheet
DEFAULT_MANUAL_STYLE = {
    'text': {'size': 8, 'family': 'Arial'},
    'label': {'size': 12, 'weight': 'bold', 'family': 'Arial'}
}


# styles
# custom styles
def get_predefined_styles():
    FigStyles = \
        {
            'default': {},

            'manuscript': {
                'stylesheet': {
                    'axes.labelsize': 10,
                },
                'manual': {
                    'text': {'fontsize': 7}
                }
            },

            'A4paper': {},

            'poster': {
                'stylesheet': {
                    'axes.labelsize': 18,
                    'axes.titlesize': 22,
                    'xtick.labelsize': 14,
                    'ytick.labelsize': 14,
                    'legend.fontsize': 16,
                    'lines.linewidth': 2.5,
                },
                'manual': {
                    'text': {'fontsize': 14},
                    'label': {'fontsize': 22}
                },
            },

            'presentation': {
                'stylesheet': {
                    'axes.labelsize': 14,
                    'axes.titlesize': 20,
                    'xtick.labelsize': 12,
                    'ytick.labelsize': 12,
                    'legend.fontsize': 14,
                    'lines.linewidth': 2.5,
                },
                'manual': {
                    'text': {'fontsize': 12},
                    'label': {'fontsize': 20}
                },
            },

            'jneurosci': {
                'stylesheet': {
                },
                'manual': {
                    'text': {'fontsize': 10},
                    'label': {'fontsize': 12}
                },
            },

            'neuron': {
                'stylesheet': {
                    'axes.labelsize': 8,
                    'legend.fontsize': 8,
                    'lines.linewidth': 1,
                },
                'manual': {
                    'text': {'fontsize': 7},
                    'label': {'fontsize': 11}
                },
            },

            'pnas': {
                'stylesheet': {
                },
                'manual': {
                },
            },

            'jnphys': {
                'stylesheet': {
                },
                'manual': {
                },
            },

            'plos': {
                'stylesheet': {
                },
                'manual': {
                },
            },
        }

    return FigStyles


def get_saved_styles():
    s_dir = get_config('STYLE_DIR')
    files = os.listdir(s_dir)
    style_files = [f for f in files if os.path.isfile(os.path.join(s_dir, f)) and f.endswith('.stylelib')]

    return {s.split('.stylelib')[0]: os.path.join(s_dir, s) for s in style_files}


def get_saved_manuals():
    s_dir = get_config('STYLE_DIR')
    files = os.listdir(s_dir)
    manual_config = [f for f in files if os.path.isfile(os.path.join(s_dir, f))
                     and f.endswith('.manual')]
    import json
    manual_dict = {}
    for name in manual_config:
        with open(os.path.join(s_dir, name), 'r') as f:
            manual_dict.update({name.split('.manual')[0]: json.load(f)})

    return manual_dict


def check_saved_styles():
    # check if all predefined styles are already saved as stylesheet
    style_names = get_saved_styles().keys()
    default_style_names = get_predefined_styles().keys()

    return set(default_style_names) - set(style_names)


def save_style(style_name, style_dict, path=None, overwrite=True):
    """
    save style as style sheet. it will overwrite existing one with same name if already exist
    :param style_name: str, name of the style to be saved
    :param style_dict: dictionary of style configurations to be saved
    :param path: str or path, default to get_config('STYLE_DIR')
    :param overwrite: Bool, if overwrite existing style definition
    :return:
    """
    if not overwrite and style_name in get_saved_styles().keys():
        raise ValueError('Style with name: {} already exist'.format(style_name))

    default_style = {
        'stylesheet': DEFAULT_AUTO_STYLE.copy(),
        'manual': DEFAULT_MANUAL_STYLE.copy(),
    }
    if not path:
        path = get_config('STYLE_DIR')
    # save style sheet
    current_style = default_style.copy()
    if 'stylesheet' in style_dict.keys():
        for k, v in style_dict['stylesheet'].items():
            if k in ALLOWED_AUTO_KEYS:
                current_style['stylesheet'].update({k: v})
    with open(os.path.join(path, style_name + '.stylelib'), 'w') as f:
        for k, v in current_style['stylesheet'].items():
            f.write(r"""{}: {}""".format(k, v) + '\n')
    if 'manual' in style_dict.keys():
        for k, v in style_dict['manual'].items():
            current_style['manual'].update({k: v})
    # save manual configurations as json file
    import json
    with open(os.path.join(path, style_name + '.manual'), 'w') as f:
        json.dump(current_style['manual'], f)


def _save_default_styles(style_names, style_dicts, path=None, overwrite=True):
    """
        save default styles as style sheet. it will overwrite existing one with same name if already exist
        :param style_names: list or tuple of str, name of the style to be saved
        :param style_dicts: list or tuple of dictionary of style configurations to be saved
        :param path: str or path, default to get_config('STYLE_DIR')
        :param overwrite: Bool, if overwrite existing style definition
        :return:
    """
    for name in style_names:
        if name in style_dicts.keys():
            try:
                save_style(name, style_dicts[name], path, overwrite)
            except ValueError:
                pass
