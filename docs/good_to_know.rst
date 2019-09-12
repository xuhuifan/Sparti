Good to know
============

Here we describe some important concepts related to Sparti. These will help in understanding
the literature of spatial partition inference.


Sparti models
----------

There are six models in Sparti: Infinite Relational Model, Bayesian Additive Regression Trees, the Mondrian Process, the Binary Space Partitioning-Tree Process, the Rectangular Bounding Process and Scalable Deep Generative Relational Model. 

provides a convenient syntax of combining these operations into a network that is called
an `ElfiModel`_, where each node represents an operation. Basically, the `ElfiModel`_ is a
description of how different quantities needed in the inference are to be generated. The
structure of the network is a `directed acyclic graph (DAG)`_.

.. _`directed acyclic graph (DAG)`: https://en.wikipedia.org/wiki/Directed_acyclic_graph

.. _`ElfiModel`: api.html#elfi.ElfiModel



