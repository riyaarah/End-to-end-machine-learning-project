from setuptools import find_packages, setup

setup(
name='mlproject',
version='0.1.0',
author='Riya',
author_email='riyaarah@gmail.com',
packages=find_packages(),
install_requires=['pandas', 'numpy', 'scikit-learn', 'flask','seaborn']
)