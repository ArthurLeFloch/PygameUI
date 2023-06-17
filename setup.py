from setuptools import setup

setup(
    name='pygame_ui_controls',
    version='1.0.0',
    author='Arthur Le Floch',
    author_email='alf.github@gmail.com',
    description='Pygame UI controls',
    long_description='UI controls for Pygame (Button, ImageButton, CheckBox, Slider, Text)',
    url='https://github.com/ArthurLeFloch/PygameUI',
    packages=[''],
    package_dir={'': 'src'},
    install_requires=[
        'pygame'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
