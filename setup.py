# setup.py

from setuptools import setup, find_packages

setup(
    name='quakeflowplot',
    version='0.0.0',
    packages=["quakeflowplot"],
    description='help with visualization of quakeflow results',
    author='Junhao Song',
    author_email='sjh2015@mail.ustc.edu.cn',
    url='https://github.com/jhsong-seis/quakeflowplot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
