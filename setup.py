import os 
from setuptools import setup, find_packages
import monilog

def read(file):
    return open(os.path.join(os.path.dirname(__file__), file)).read()


setup(name='monilog',
      version='0.1.1',
      description='HTTP log monitoring',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
      ],
      keywords='HTTP log monitoring',
      url='https://tayciryahmed.github.io/monilog/',
      author='Taycir Yahmed',
      author_email='taycir.yahmed@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points={
          'console_scripts': ['monitoring=monilog.bin.run_monitoring:run',
                              'log_generator=monilog.bin.run_log_generator:run'],
      },
      zip_safe=False)
