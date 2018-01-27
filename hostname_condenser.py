#!/usr/bin/env python3

"""A module for generating a list of condensed hostnames.

A module for generating a list of condensed hostnames, where condensing is
moving part of the full hostname into the top-level directory (TLD).

An example is if the hostname was "egg": this could also be represented as
"e.gg", which would form part of a larger URI.
"""


def condense_hostname(hostname, top_level_domains=None):
    """Takes a hostname and an optional list of top-level domains and generates
    possible hostname-TLD combinations.

    Args:
        hostname(str): The hostname to condense.
        top_level_domains(iterable): The top-level domains to use when
        condensing the hostname or None to use the inbuilt list.

    Returns:
        A list of valid hostname/TLD combinations.
    """
