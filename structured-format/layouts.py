from collections import namedtuple
from typing import Callable, List, Generic, TypeVar


class Layout:
    pass


T = TypeVar('T')


class State(Generic[T]):
    format_lst: 'List[Layout]'
    result: T


class Empty(Layout):
    pass


_leaf = namedtuple('Leaf', {
    'left_pad': bool,
    'obj': object,
    'right_pad': bool
})


class Terminal(_leaf, Layout):
    pass


_combined = namedtuple(
    'Combined', {
        'left_pad': bool,
        'fst': Layout,
        'mid_pad': bool,
        'snd': Layout,
        'right_pad': bool
    })


class Combined(_combined, Layout):
    pass


_monitor = namedtuple('Minitor',
                      {'map': Callable[[State[Layout]], State[Layout]]})


class Monitor(_monitor, Layout):
    pass


_group = namedtuple('Group', {'group_id': int, 'layout': Layout})


class Group(_group, Layout):
    pass

