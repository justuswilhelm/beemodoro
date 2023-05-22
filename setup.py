from setuptools import setup

setup(
    author='Justus Perlwitz',
    author_email='hello@justus.pw',
    description='Beeminder Pomodoro Timer',
    entry_points={
        'console_scripts': [
            'beemodoro = beemodoro:main',
            'track_goal = beemodoro.track_goal:main',
        ],
    },
    install_requires=['requests==2.31.0'],
    license='MIT',
    name='beemodoro',
    packages=['beemodoro'],
    url='https://github.com/justuswilhelm/beemodoro',
    version='1.3.0',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
