#!/usr/bin/env python3

"""A module for generating a list of condensed hostnames.

A module for generating a list of condensed hostnames, where condensing is
moving part of the full hostname into the top-level directory (TLD).

An example is if the hostname was "egg": this could also be represented as
"e.gg", which would form part of a larger URI.
"""
