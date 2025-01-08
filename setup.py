# setup.py
from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
def read_requirements():
    with open('requirements.txt') as req_file:
        return req_file.read().splitlines()

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
    install_requires=read_requirements(),  # Dynamically read requirements
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)