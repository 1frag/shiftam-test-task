from setuptools import find_packages, setup

setup(
    name='shiftam_test_task',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='==3.10'
)
