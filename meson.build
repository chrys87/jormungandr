# https://github.com/mesonbuild/meson/blob/master/test%20cases/frameworks/1%20boost/meson.build
project(
    'jormungandr', 'cpp',
    version: '0.0.1',
    meson_version: '>= 0.40.0',
    #default_options : ['cpp_std=c++14']
)

add_project_arguments(
    ['-DBOOST_LOG_DYN_LINK'],
    language : 'cpp'
)

subdir('src')
