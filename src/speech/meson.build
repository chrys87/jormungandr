
compiler = meson.get_compiler('cpp')
boost_dep = [
    compiler.find_library('boost_system'),
    compiler.find_library('boost_filesystem'),
    compiler.find_library('boost_locale'),
]

# seems to be needed as hack
compiler = meson.get_compiler('cpp')
if compiler.has_argument('-permissive')
    # boost 1.64, the version we test against, doesn't work with -permissive
    add_project_arguments('-permissive', language: 'cpp')
endif

# create node objects
node_lib = shared_library('node', '../node/node.cpp')

# compile generic speech node
speech_generic = executable('generic', 'generic/generic.cpp', dependencies : [boost_dep], link_with: [node_lib])

test('Test speech_node', speech_generic)
