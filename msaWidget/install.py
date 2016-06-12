#!/usr/bin/env python

import argparse
from os.path import dirname, abspath, join

try:
    from inspect import signature
except ImportError:
    from funcsigs import signature


def install(enable=False, **kwargs):
    """
    Install the msaWidget nbextension assets

    Parameters
    ----------
    **kwargs: keyword arguments
        Other keyword arguments passed to the install_nbextension command
    """
    from notebook.nbextensions import install_nbextension

    directory = join(dirname(abspath(__file__)), 'static', 'msaWidget')

    kwargs = {k: v for k, v in kwargs.items() if not (v is None)}

    kwargs["destination"] = "msaWidget"
    install_nbextension(directory, **kwargs)


if __name__ == '__main__':
    from notebook.nbextensions import install_nbextension

    install_kwargs = list(signature(install_nbextension).parameters)

    parser = argparse.ArgumentParser(
        description="Installs msaWidget nbextension")

    default_kwargs = dict(
        action="store",
        nargs="?"
    )

    store_true_kwargs = dict(action="store_true")

    store_true = ["symlink", "overwrite", "quiet", "user"]

    [parser.add_argument(
        "--{}".format(arg),
        **(store_true_kwargs if arg in store_true else default_kwargs)
        )
        for arg in install_kwargs]

    install(**parser.parse_args().__dict__)
