import shutil
from pathlib import Path
from setuptools import setup, Extension

name = 'cdmapi'
src = 'cdmapi_src'
setup(
    name=name,
    version="1.0.0",
    ext_modules=[
        Extension(
            name=name,
            sources=[
                f'{src}/bind.cpp',
                f'{src}/codelift.cpp'
            ],
            extra_objects=[f'{src}/cryptlib.lib'],

            # to use for any python version
            py_limited_api=True,
            define_macros=[('Py_LIMITED_API', None)]
        )
    ]
)


for folder in ('build', 'cdmapi.egg-info'):
    if Path(folder).exists():
        print(f'Deleting {folder} folder and files')
        shutil.rmtree(folder)


dist = Path('dist')
if dist.exists():
    try:
        whl = next(dist.glob('*.whl'))
        whl.rename(whl.name)
        dist.rmdir()
    except StopIteration:
        pass
