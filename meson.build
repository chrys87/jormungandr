project('jormungandr', ['cpp', 'c'],        version: '0.1.0',
  meson_version: '>= 0.40.0',
)

linkdep = dependency('boost', modules : ['thread', 'system', 'locale'])


subdir('src')
node = shared_library('node', 'src/node/node.cpp')
speech_generic = executable('generic', 'src/speech/generic/generic.cpp', link_with : node)