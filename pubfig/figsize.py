"""
options to be configured to each figure
"""
MAXSIZE = {
    'A4': (8.27, 11.69),
    'A3': (11.69, 16.53),
    'custom': None,
}

FIGSIZE = {
    'A4': (8.27, 11.69),
    'A3': (11.69, 16.53),
    }

Units = ('cm', 'inch')


# figure size
# matplotlib seems only use inch
def cm2inch(*tupl):
    inch = 2.54
    if isinstance(tupl[0], (tuple, list)):
        return tuple(i/inch for i in tupl[0])
    else:
        return tuple(i/inch for i in tupl)


def fig_size(size, unit='cm', paper_format='A4'):
    """
    check if the required size of the figure can fit into the paper format
    :param size: string or (tuple, list). if str, it must be a key in FigSize
    :param unit: unit of the size
    :param paper_format: string, paper format for the figure
    :return:
        tuple, figure size in inches
    """
    if isinstance(size, str):
        fsize = FIGSIZE[size]
    elif isinstance(size, (tuple, list)):
        if unit == 'cm':
            fsize = cm2inch(size)
        elif unit == 'inch':
            fsize = size
        else:
            raise ValueError('Unit: {} not known')
    else:
        raise ValueError('input size must be a tuple, list or string')

    if MAXSIZE[paper_format]:
        if fsize[0] > MAXSIZE[paper_format][0] or fsize[1] > MAXSIZE[paper_format][1]:
            raise ValueError('Specified figure size: {} is larger than allowed by the paper format: {}: {}'.
                             format(size, paper_format, MAXSIZE[paper_format]))
    return fsize
