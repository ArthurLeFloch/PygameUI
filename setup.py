from setuptools import setup

setup(
    name='PygameUI',
    version='1.0.0',
    author='Arthur Le Floch',
    author_email='alf.github@gmail.com',
    description='Pygame UI',
    long_description='UI controls for Pygame (Button, ImageButton, CheckBox, Slider, Text)',
    url='https://github.com/ArthurLeFloch/PygameUI',
    packages=[''],
    package_dir={'': 'src'},
    install_requires=[
        'pygame'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL v3.0',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
