geostates
=========

[![pypi](https://img.shields.io/pypi/v/geostates.svg)](https://pypi.org/project/geostates)
[![downloads](https://static.pepy.tech/badge/geostates)](https://pepy.tech/project/geostates)
[![License:MIT](https://img.shields.io/badge/License-MIT-lightgray.svg?style=flt-square)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6812430.svg)](https://doi.org/10.5281/zenodo.6812430)

Geostates is a Python package for quickly plotting choropleth maps of the United States.

Installation
------------

**PyPI**

To install geostates run: ``pip install geostates``.


Dev roadmap
-----------

The current version of geostates only allows for plotting choropleth maps of the United States using a very specific
set of shapefiles. In the future, the goal is to add:

- Ability to plot United States maps with county-level data.
- Add support for Congressional Districts, Metropolitan Statistical Areas, and Zip Code Areas to individual state
 plots.
- Add support for plotting categorical data for United States maps.
- Add features for plotting political science maps (ie. Electoral College maps, etc.).

How to contribute
-----------------

You can contribute to the geostates package by installing it and giving it a try. You can also file issues on the 
issue tracker or submit a pull request if you would like to make any improvements.

Acknowledgements
----------------

- This package's core functionality relies substantially on the [geopandas](https://geopandas.org/en/stable/) package.
- The idea to use inset axes for this package came from Cimbali. A helpful explanation on utilizing segmented
colormaps came from JohanC. As mentioned in the comments, the function for discretizing matplotlib colormaps was
inspired by an example provided in Jake VanderPlas' [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/).

 
