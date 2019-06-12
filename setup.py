import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='turtlepro',
    version='0.1.0',
    packages=['turtlepro'],
    license='MIT',
    author='Zach Bateman',
    description='Higher-level interface to the Python turtle',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zachbateman/turtlepro.git',
    download_url='https://github.com/zachbateman/turtlepro/archive/v_0.1.0.tar.gz',
    keywords=['TURTLE', 'DRAWING', 'PRO', 'PLOT', 'GRAPH'],
    install_requires=[],
    classifiers=['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   ]
)