from setuptools import setup
from Cython.Build import cythonize

def job_():
    setup(ext_modules=cythonize("cythoncollatzwhileloop.pyx"),)

if __name__ == '__main__':
    job_()

