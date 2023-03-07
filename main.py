# **--coding: utf-8; --**
# :author: couriourc

from vaspy.incar import InCar
from vaspy.atomco import PosCar


# 1. DFT+U：由于对电子之间的相互作用考虑的不充分，LDA和GGA对一些电子高度局域并且强关联体系并不是很适用例如，金属氧化物，稀土元素及其化合物，
# 故而Anisimov等人对其进行修正，在LDA或者GGA的能量泛函中加入Hubbard参数U，即DFT+U方法。
# U就是自旋相反电子的强关联排斥能，在Hubbard模型一级近似下，U考虑了同一个原子上自旋相反的局域电子之间的库伦排斥，从而导致能带的“重正化”。
# 通常U值是一个经验性参数，对于相同元素的不同晶体配位环境，U值通常也不同，需要查找相关文献上U值的使用，
# 以及多次测试U值的大小来确定最适宜的U值。
# 通常测试U是否合适主要看以下一些信息：磁矩是否与实验值吻合，磁基态是否和实验吻合，
# 绝缘（半导）体系的磁转变（通常为Curie或者Néel温度）温度是否和实验值吻合（金属体系通过Heisenberg Model预测转变温度，通常会高估），
# 能带定性上是否和实验吻合（不要追求能隙吻合，LDA和GGA本来就低估能隙）。
# 如果是自己预测的体系，建议不同的U值都测试一遍，看看U值对关心的性质影响是否很大。
def get_u():
    ...
    return


def get_parameter():
    ...
    from os.path import abspath, join
    parameter_dir = abspath('./parameters')
    incar = InCar(join(parameter_dir, 'INCAR'))
    poscar = InCar(join(parameter_dir, 'POSCAR'))

    return incar, poscar


def main():
    ...


if __name__ == '__main__':
    main()
