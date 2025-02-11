# setup.py

from setuptools import setup

setup(
    name='quakeflowplot',
    version='0.0.0',
    packages=["quakeflowplot"],
    description='help with visualization of quakeflow results',
    author='Junhao Song',
    author_email='sjh2015@mail.ustc.edu.cn',
    url='https://github.com/jhsong-seis/quakeflowplot',
    python_requires=['matplotlib', 'pandas', 'numpy'],
)
