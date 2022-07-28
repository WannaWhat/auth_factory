from enum import Enum


# Base class for all cryptography algorithms
class BaseAlgorithm(object):
    name = ''
    func = None
    algorithms_enum_join_on_supported = {}
    algorithms_enum = None

    # Create Enum and asocial array for enum value == some algorithm
    def __new__(cls, *args, **kwargs):
        enum_alg_dict = {}
        cls.algorithms_enum_join_on_supported = {}
        for i in cls.__subclasses__():
            enum_alg_dict[i.__name__] = i.name
            cls.algorithms_enum_join_on_supported[i.__name__] = i
        if not enum_alg_dict:
            raise ValueError('No items for enum')
        cls.algorithms_enum = Enum('hash_algorithms_enum', enum_alg_dict)
        return cls

    # Join enum name: str with algorithm class
    @classmethod
    def algorithm_enum_name_join(cls, enum_name: str):
        enum_value = cls.algorithms_enum(enum_name)
        return cls.algorithm_enum_value_join(enum_value)

    # Join enum value: Enum with algorithm class
    @classmethod
    def algorithm_enum_value_join(cls, enum_value: Enum):
        if enum_value.name in cls.algorithms_enum_join_on_supported:
            return cls.algorithms_enum_join_on_supported[enum_value.name]
        return None


class AlgorithmTypesEnum(str, Enum):
    HASH_SUM = 'hash_sum'
    ASYMMETRIC = 'asymmetric'
    SYMMETRIC = 'symmetric'


# AlgorithmParentClass for isolation memory from base class
class AlgorithmParentClass(BaseAlgorithm):
    pass
