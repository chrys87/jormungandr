compiler = meson.get_compiler('cpp')
boost_dep = [
    compiler.find_library('boost_system'),
    compiler.find_library('boost_filesystem'),
    compiler.find_library('boost_locale'),
    compiler.find_library('boost_thread'),
]


thread_dep = dependency('threads')

# seems to be needed as hack
compiler = meson.get_compiler('cpp')
if compiler.has_argument('-permissive')
    # boost 1.64, the version we test against, doesn't work with -permissive
    add_project_arguments('-permissive', language: 'cpp')
endif

# create node objects
node_lib = shared_library('node', '../../node/node.cpp', dependencies : [boost_dep, thread_dep])

# compile generic speech node
OutputNode = executable('OutputNode', 'OutputNode.cpp', dependencies : [boost_dep, thread_dep], link_with: [node_lib])

test('Test OutputNode', OutputNode)
 
