tidyTestFileContents = "def testMe(a,b):\n    return a+b\n"
tidyWithTestCaseContents = "def testMe(a,b):\n    return a+b\n\n\ntestMe(1, 2)\n"

defaultFinalizerResults = ({
    0: {'Line': 1, 'globals': {}, 'locals': {}},
    1: {'Line': 5, 'globals': {}, 'locals': {}},
    2: {'Line': 1, 'globals': {}, 'locals': {'a': 1, 'b': 2}},
    3: {'Line': 2, 'globals': {}, 'locals': {'a': 1, 'b': 2}},
    4: {'Line': 2, 'globals': {}, 'locals': {'__return__': 3, 'a': 1, 'b': 2}},
    5: {'Line': 5, 'globals': {}, 'locals': {}}
}, ['a', 'b'], [])

defaultMungerResults = {
    '__lineNo__': [(0, 1), (1, 5), (2, 1), (3, 2), (4, 2), (5, 5)],
    '__return__': [(0, 'myNaN'),
                   (1, 'myNaN'),
                   (2, 'myNaN'),
                   (3, 'myNaN'),
                   (4, 3),
                   (5, 'myNaN')],
    'a': [(0, 'myNaN'), (1, 'myNaN'), (2, 1), (3, 1), (4, 1), (5, 'myNaN')],
    'b': [(0, 'myNaN'), (1, 'myNaN'), (2, 2), (3, 2), (4, 2), (5, 'myNaN')]
}

unfinalizedLoggerResults = [{'event': 'step_line',
  'func_name': '<module>',
  'globals': {},
  'heap': {},
  'line': 1,
  'ordered_globals': [],
  'stack_to_render': [],
  'stdout': ''},
 {'event': 'step_line',
  'func_name': '<module>',
  'globals': {'testMe': ['REF', 1]},
  'heap': {1: ['FUNCTION', 'testMe(a, b)', None]},
  'line': 5,
  'ordered_globals': ['testMe'],
  'stack_to_render': [],
  'stdout': ''},
 {'event': 'call',
  'func_name': 'testMe',
  'globals': {'testMe': ['REF', 1]},
  'heap': {1: ['FUNCTION', 'testMe(a, b)', None]},
  'line': 1,
  'ordered_globals': ['testMe'],
  'stack_to_render': [{'encoded_locals': {'a': 1, 'b': 2},
                       'frame_id': 1,
                       'func_name': 'testMe',
                       'is_highlighted': True,
                       'is_parent': False,
                       'is_zombie': False,
                       'ordered_varnames': ['a', 'b'],
                       'parent_frame_id_list': [],
                       'unique_hash': 'testMe_f1'}],
  'stdout': ''},
 {'event': 'step_line',
  'func_name': 'testMe',
  'globals': {'testMe': ['REF', 1]},
  'heap': {1: ['FUNCTION', 'testMe(a, b)', None]},
  'line': 2,
  'ordered_globals': ['testMe'],
  'stack_to_render': [{'encoded_locals': {'a': 1, 'b': 2},
                       'frame_id': 1,
                       'func_name': 'testMe',
                       'is_highlighted': True,
                       'is_parent': False,
                       'is_zombie': False,
                       'ordered_varnames': ['a', 'b'],
                       'parent_frame_id_list': [],
                       'unique_hash': 'testMe_f1'}],
  'stdout': ''},
 {'event': 'return',
  'func_name': 'testMe',
  'globals': {'testMe': ['REF', 1]},
  'heap': {1: ['FUNCTION', 'testMe(a, b)', None]},
  'line': 2,
  'ordered_globals': ['testMe'],
  'stack_to_render': [{'encoded_locals': {'__return__': 3, 'a': 1, 'b': 2},
                       'frame_id': 1,
                       'func_name': 'testMe',
                       'is_highlighted': True,
                       'is_parent': False,
                       'is_zombie': False,
                       'ordered_varnames': ['a', 'b', '__return__'],
                       'parent_frame_id_list': [],
                       'unique_hash': 'testMe_f1'}],
  'stdout': ''},
 {'event': 'return',
  'func_name': '<module>',
  'globals': {'testMe': ['REF', 1]},
  'heap': {1: ['FUNCTION', 'testMe(a, b)', None]},
  'line': 5,
  'ordered_globals': ['testMe'],
  'stack_to_render': [],
  'stdout': ''}]

unpickledFinalResults = {
 'args': [],
 'returnVars': [],
 'trace': {'__lineNo__': [(0, 1), (1, 5), (2, 1), (3, 2), (4, 2), (5, 5)],
           '__return__': [(0, 'myNaN'),
                          (1, 'myNaN'),
                          (2, 'myNaN'),
                          (3, 'myNaN'),
                          (4, 3),
                          (5, 'myNaN')],
           'a': [(0, 'myNaN'),
                 (1, 'myNaN'),
                 (2, 1),
                 (3, 1),
                 (4, 1),
                 (5, 'myNaN')],
           'b': [(0, 'myNaN'),
                 (1, 'myNaN'),
                 (2, 2),
                 (3, 2),
                 (4, 2),
                 (5, 'myNaN')]}}