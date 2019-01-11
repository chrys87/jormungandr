project(
  'jormungandr', 'cpp',
  version: '0.1.0',
  meson_version: '>= 0.40.0',
  default_options : ['cpp_std=c++11']
)

add_project_arguments(
  ['-DBOOST_LOG_DYN_LINK'],
  language : 'cpp'
)

subdir('src')

# why this doesnt work on ArchLinux?
#boost_dep = dependency('boost')
#if not boost_dep.found()
#    error('MESON: boost not found.')
#endif

compiler = meson.get_compiler('cpp')
boost_dep = [
    compiler.find_library('boost_system'),
    compiler.find_library('boost_filesystem'),
    compiler.find_library('boost_locale'),
]

compiler = meson.get_compiler('cpp')
if compiler.has_argument('-permissive')
  # boost 1.64, the version we test against, doesn't work with -permissive
  add_project_arguments('-permissive', language: 'cpp')
endif

node_lib = shared_library('node', 'src/node/node.cpp')

speech_generic = executable('generic', 'src/speech/generic/generic.cpp', dependencies : [boost_dep], link_with: [node_lib])
