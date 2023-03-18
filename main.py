# **--coding: utf-8; --**
# :author: couriourc

from vaspy.electro import DosX


def vasp_start(DOS_SUM):
    dos = DosX(filename=DOS_SUM)
    dos.plotsum(0, (1, 100))


if __name__ == '__main__':
    from os.path import abspath, join

    parameters_prefix = abspath('./parameters')
    DOS_SUM = join(parameters_prefix, "DOS_SUM")
    vasp_start(DOS_SUM)
