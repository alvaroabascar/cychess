import glob
import os
import subprocess
import sys

import Cython
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
from Cython.Build import cythonize

MOD_NAMES = [
    'chess.piece',
    'chess.piece_properties'
]


def generate_cython(root, source):
    print('Cythonizing sources')
    p = subprocess.call([sys.executable,
                         os.path.join(root, 'bin', 'cythonize.py'),
                         source], env=os.environ)
    if p != 0:
        raise Exception('Running cythonize failed.')


def setup_package():
    root = os.path.abspath(os.path.dirname(__file__))
    pyx_files = glob.glob('chess/**/*.pyx', recursive=True)
    extensions = []
    for mod in MOD_NAMES:
        cpp_file = mod.replace('.', '/') + '.cpp'
        extensions.append(Extension(
            mod,
            [cpp_file],
            language='c++'))

    extensions = cythonize(extensions)

    generate_cython(root, 'chess')

    setup(
        name="chess",
        ext_modules=cythonize(extensions),
        cmdclass={'build_ext': build_ext},
        packages=['my_package', 'my_package.inner_package']
    )


if __name__ == '__main__':
    setup_package()
