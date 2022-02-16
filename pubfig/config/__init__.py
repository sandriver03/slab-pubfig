import logging
import os

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def load_settings():
    # Load the default settings
    from . import settings

    # Load the computer-specific settings, saved as separate file in Config, with name [CompName_config]
    import getpass
    compname = os.environ['COMPUTERNAME']
    username = getpass.getuser()
    custom_setting_name = compname + '_' + username + '.config'
    try:
        import json
        with open(os.path.join(settings.SETTING_DIR, custom_setting_name), 'r') as fh:
            extra_settings = json.load(fh)
        # extra_settings is a dictionary
        # Update the setting defaults with the computer-specific settings
        for k, v in extra_settings.items():
            setattr(settings, k, v)
    except FileNotFoundError:
        log.debug('No custom settings defined, use default settings')
    except IOError:
        log.debug('Custom setting file: {} cannot be read',
                  os.path.join(settings.SETTING_DIR, custom_setting_name))
    # Load user-specific settings in Config, with name
    return settings


_settings = load_settings()


def set_config(setting, value):
    '''
    Set value of setting
    '''
    setattr(_settings, setting, value)


def get_config(setting=None):
    '''
    Get value of setting
    '''
    if setting is not None:
        return getattr(_settings, setting)
    else:
        setting_names = [s for s in dir(_settings) if s.upper() == s]
        setting_values = [getattr(_settings, s) for s in setting_names]
        return dict(zip(setting_names, setting_values))


def get_settings():
    '''
    Get all settings
    '''
    setting_names = [s for s in dir(_settings) if s.upper() == s]
    setting_values = [getattr(_settings, s) for s in setting_names]
    return dict(zip(setting_names, setting_values))


def get_user_settings():
    """
    get user specific settings
    :return:
        dict
    """
    vals = get_settings()
    from . import settings
    dks = [k for k in vals.keys() if k not in dir(settings) or vals[k] != getattr(settings, k)]
    s_settings = {k: vals[k] for k in dks}
    return s_settings


def save_settings():
    """
    save current settings to hard drive with json
    :return:
        None
    """
    s_settings =get_user_settings()

    import os, getpass, json
    compname = os.environ['COMPUTERNAME']
    username = getpass.getuser()
    custom_setting_name = compname + '_' + username + '.config'
    with open(os.path.join(get_config('SETTING_DIR'), custom_setting_name), 'r') as fh:
        json.dump(s_settings, fh)


def get_projects():
    """
    get the name of existing projects
    :return:
    """
    path = get_config('BASE_DIR')
    return [f.name for f in os.scandir(path) if f.is_dir()]


def create_project(project_name):
    """
    create dir for a new project
    :param project_name: str, name of the project
    :return:
        abs path to project folder
    """
    pjs = get_projects()
    if project_name in pjs:
        raise ValueError('Project with name: {} already exists'.format(project_name))
    path = os.path.join(get_config('BASE_DIR'), project_name)
    log.info('Creating project directory, {}'.format(path))
    os.makedirs(path, )
    for nm in get_config('SUB_DIRS'):
        os.makedirs(os.path.join(path, nm))
    return path


# check to see if the dirs exist; create dir if it does not exist
if not os.path.isdir(get_config('BASE_DIR')):
    log.info('Creating base directory, {}'.format(get_config('BASE_DIR')))
    os.mkdir(get_config('BASE_DIR'))

if not os.path.isdir(get_config('STYLE_DIR')):
    log.info('Creating style sheet directory, {}'.format(get_config('STYLE_DIR')))
    os.mkdir(get_config('STYLE_DIR'))


# work on default styles
from .styles import check_saved_styles, get_saved_styles, get_saved_manuals
if check_saved_styles():
    from .styles import get_predefined_styles, _save_default_styles
    _save_default_styles(check_saved_styles(),
                         get_predefined_styles(),
                         get_config('STYLE_DIR'),
                         )

# register available styles in _settings
setattr(_settings, 'FIG_STYLES', get_saved_styles())
setattr(_settings, 'FIG_MANUALS', get_saved_manuals())
setattr(_settings, 'STYLES', tuple(get_config('FIG_STYLES').keys()))
