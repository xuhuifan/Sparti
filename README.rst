**************************
Sparti - Spatial partition inference
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

Sparti is a statistical software package for spatial partition inference such as inference methods for `the Mondrian Process`_ , `the Binary Space Partitioning-Tree Process`_ , `the Rectangular Bounding Process`_ . Currently, Markov chain Monte Carlo method is the main strategy for the inference. More advanced and scalable inference, such as Variational AutoEncoding method should come in the near future.

.. _the Mondrian Process: https://papers.nips.cc/paper/3622-the-mondrian-process
.. _the Binary Space Partitioning-Tree Process: http://proceedings.mlr.press/v84/fan18b
.. _the Rectangular Bounding Process: https://papers.nips.cc/paper/7989-rectangular-bounding-process

Sparti is licensed under BSD3_. The source is in GitHub_.

.. _BSD3: https://opensource.org/licenses/BSD-3-Clause
.. _GitHub: https://github.com/elfi-dev/elfi


Currently implemented Sparti models:
----------------------------------

- Infinite Relational Model (For relational data only.)
- Bayesian Additive Regression Tree (For regression tree only.)
- the Mondrian Process
- the Binary Space Partitioning-Tree Process
- the Rectangular Bounding Process

Currently, Sparti can be applied in the following two tasks (More tasks are under exploration.) 

- Relational modelling
- Regression Tree (including classification and regression)


Additionally, Sparti integrates tools for visualization, model comparison, diagnostics and post-processing.


Installation
----------------------------------

This theme is distributed on PyPI_ and can be installed with ``pip``:

.. code:: console

   pip install sparti


Example Usage
----------------------------------

.. code:: python

    import sparti
    import numpy as np
    
    xdata = np.random.rand(100, 2)
    ydata = np.random.rand(100)
    sparti.BSPF(xdata, ydata)


