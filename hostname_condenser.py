#!/usr/bin/env python3

"""A module for generating a list of condensed hostnames.

A module for generating a list of condensed hostnames, where condensing is
moving part of the full hostname into the top-level directory (TLD).

An example is if the hostname was "egg": this could also be represented as
"e.gg", which would form part of a larger URI.
"""

import argparse

class HostnameCondenserError(Exception):
    """The generic base exception used by the hostname_condenser module."""

class TLDProcessingError(HostnameCondenserError):
    """Raise when the list of TLDs cannot be processed."""

def get_top_level_domains(file_path):
    """Get the top level domains from a specified file.

    Args:
        file_path (str): The path to a file containing one top level domain per
            line and optional comments (lines starting with a "#").

    Returns:
        A list of top level domains.

    Raises:
        TLDProcessingError: When top level domains cannot be read from
            file_path.
    """
    try:
        with open(file_path, "r") as top_level_domains_file_handle:
            top_level_domains = [line.rstrip().lower() for line in
                                 top_level_domains_file_handle.readlines()
                                 if not line.startswith("#")]
            return top_level_domains
    except Exception as exc:
        exception_message = "Could not read TLDs from file: " + file_path
        raise TLDProcessingError(exception_message) from exc

def get_default_top_level_domains():
    """Get the default top level domains from an inbuilt file.

    Returns:
        A list of top level domains.

    Raises:
        TLDProcessingError: When top level domains cannot be read from the
        inbuilt file.
    """
    top_level_domains_file_path = r"data\tlds-alpha-by-domain.txt"

    return get_top_level_domains(top_level_domains_file_path)

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
    if top_level_domains is None:
        top_level_domains = get_default_top_level_domains()

    matching_top_level_domains = [top_level_domain for top_level_domain in
                                  top_level_domains if
                                  hostname[1:].lower() \
                                  .endswith(top_level_domain)]

    return [hostname.replace(tld, "") + "." + tld
            for tld in matching_top_level_domains]

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="Generate a list of "
                                                 "condensed hostnames.")

    PARSER.add_argument("hostname",
                        help="A hostname to condense.")
    PARSER.add_argument("-tlds",
                        "--tld_file_path",
                        default=None,
                        help="The path to a file containing one top level "
                             "domain per line and optional comments (lines "
                             "starting with a \"#\").")

    ARGS = PARSER.parse_args()

    condensed_hostnames = []

    if ARGS.tld_file_path is not None:
        condensed_hostnames = condense_hostname(ARGS.hostname,
                                                ARGS.tld_file_path)
    else:
        condensed_hostnames = condense_hostname(ARGS.hostname)

    if condensed_hostnames:
        for condensed_hostname in condensed_hostnames:
            print(condensed_hostname)
    else:
        print("No matches found for hostname \"{0}\"".format(ARGS.hostname))
