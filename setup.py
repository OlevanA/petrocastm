# setup.py
from setuptools import setup, find_packages

setup(
    name='PetroCast',
    version='0.1.0',
    author='Ole van Allen',
    author_email='ole.allen@inn.no',
    license='MIT',
    description='Forecasting Fossil Fuel extraction',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/OlevanA/PetroCast',  # URL of your project's repository
    packages=find_packages(),  # Automatically find packages in your directory
    install_requires=[
        # Add your project requirements here, for example:
        'numpy',
        'pandas',
        'matplotlib',
        'scipy',
        'pylint',


    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
