# **--coding: utf-8; --**
# :author: couriourc

from vaspy.electro import DosX


def vasp_start(INCAR, POSCAR, OUTCAR, DOSCAR):
    dos = DosX(filename=DOSCAR)
    dos.plotsum(0, (1, 100))


if __name__ == '__main__':
    from os.path import abspath, join

    parameters_prefix = abspath('./parameters')
    INCAR = join(parameters_prefix, "INCAR")
    POSCAR = join(parameters_prefix, "POSCAR")
    OUTCAR = join(parameters_prefix, "OUTCAR")
    DOSCAR = join(parameters_prefix, "DOSCAR")

    vasp_start(
        INCAR, POSCAR, OUTCAR, DOSCAR
    )
