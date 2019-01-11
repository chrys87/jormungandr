project('jormungandr', 'cpp',        version: '0.1.0',
  meson_version: '>= 0.40.0',
)

subdir('src')

cxx = meson.get_compiler('cpp')

boost_dep = [
    cxx.find_library('boost_system'),
    cxx.find_library('boost_filesystem'),
    cxx.find_library('boost_locale'),
]

node_lib = shared_library('node', 'src/node/node.cpp')
speech_generic = executable('generic', 'src/speech/generic/generic.cpp', dependencies : [boost_dep], link_with: [node_lib])
