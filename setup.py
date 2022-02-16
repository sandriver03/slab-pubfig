from setuptools import setup, find_packages
import re

with open('README.md') as f:
    readme = f.read()

# extract version
with open('pubfig/__init__.py') as file:
    for line in file.readlines():
        m = re.match("__version__ *= *['\"](.*)['\"]", line)
        if m:
            version = m.group(1)

setup(name='slab-pubfig',
      version=version,
      description='Matplotlib based plotting tool for publication-ready figures',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='https://github.com/sandriver03/Slab-pubfig.git',
      author='Chao Huang',
      author_email='c.huang03@gmail.com',
      license='MIT',
      python_requires='>=3.7',
      # install_requires=["matplotlib < 3.5"],
      packages=find_packages(),
      zip_safe=False)
