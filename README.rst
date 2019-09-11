**************************
PartiP - stochastic Partition Process inference
**************************

.. image:: https://img.shields.io/pypi/v/sphinx_rtd_theme.svg
   :target: https://pypi.python.org/pypi/sphinx_rtd_theme
   :alt: Pypi Version
.. image:: https://travis-ci.org/readthedocs/sphinx_rtd_theme.svg?branch=master
   :target: https://travis-ci.org/readthedocs/sphinx_rtd_theme
   :alt: Build Status
.. image:: https://img.shields.io/pypi/l/sphinx_rtd_theme.svg
   :target: https://pypi.python.org/pypi/sphinx_rtd_theme/
   :alt: License
.. image:: https://readthedocs.org/projects/sphinx-rtd-theme/badge/?version=latest
  :target: http://sphinx-rtd-theme.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

PartiP is a statistical software package for stochastic partition process inference such as inference methods for `the Mondrian Process`_ , `the Binary Space Partitioning-Tree Process`_ , `the Rectangular Bounding Process`_ . Currently, Markov chain Monte Carlo method is the main strategy for the inference. More advanced and scalable inference, such as Variational AutoEncoding method should come in the near future.

.. _the Mondrian Process: https://papers.nips.cc/paper/3622-the-mondrian-process
.. _the Binary Space Partitioning-Tree Process: http://proceedings.mlr.press/v84/fan18b
.. _the Rectangular Bounding Process: https://papers.nips.cc/paper/7989-rectangular-bounding-process

ELFI is licensed under BSD3_. The source is in GitHub_.

.. _BSD3: https://opensource.org/licenses/BSD-3-Clause
.. _GitHub: https://github.com/elfi-dev/elfi


Currently implemented PartiP models:
----------------------------------

- Infinite Relational Model (For relational data only.)
- Bayesian Additive Regression Tree (For regression tree only.)
- the Mondrian Process
- the Binary Space Partitioning-Tree Process
- the Rectangular Bounding Process

PartiP currently can be applied in the following two tasks:
- Relational modelling
- Regression Tree (including classification and regression)

Additionally, PartiP integrates tools for visualization, model comparison, diagnostics and post-processing.


Installation
----------------------------------

This theme is distributed on PyPI_ and can be installed with ``pip``:

.. code:: console

   pip install partip

To use the theme in your Sphinx project, you will need to add the following to
your ``conf.py`` file:

.. code:: python

    import sphinx_rtd_theme

    extensions = [
        ...
        "sphinx_rtd_theme",
    ]

    html_theme = "sphinx_rtd_theme"

For more information read the full documentation on `installing the theme`_

.. _PyPI: https://pypi.python.org/pypi/sphinx_rtd_theme
.. _installing the theme: https://sphinx-rtd-theme.readthedocs.io/en/latest/installing.html

Configuration
----------------------------------

This theme is highly customizable on both the page level and on a global level.
To see all the possible configuration options, read the documentation on
`configuring the theme`_.

.. _configuring the theme: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html

Contributing
----------------------------------

If you would like to help modify or translate the theme, you'll find more
information on contributing in our `contributing guide`_.

.. _contributing guide: https://sphinx-rtd-theme.readthedocs.io/en/latest/contributing.html
