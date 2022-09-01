from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Simple Loading/Progress Bar for python'
LONG_DESCRIPTION = 'Simple package which you can use anywhere, where you need a loading or progress bar'

setup(
    name="simple-bar",
    version=VERSION,
    author="4yub1k (Salah Ud Din)",
    author_email="<salahuddin@protonmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    install_requires=[], 
    keywords=['python', 'loading', 'progress', 'progress bar', 'upload bar'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)