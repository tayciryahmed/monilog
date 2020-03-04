from setuptools import setup, find_packages

import monilog

with open('README.md') as f:
    long_description = f.read()


setup(name='monilog',
      version='0.1.0',
      description='HTTP log monitoring',
      long_description=long_description,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approvec :: MIT License',
          'Programming Language :: Python :: 3.7',
          'Topic :: HTTP log monitoring',
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