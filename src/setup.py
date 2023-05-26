from setuptools import setup

setup(name='routes',
      version='0.1',
      packages=['routes'],
      entry_points={
          'console_scripts': [
              'test_exec = User.interfaces.routes:main'
          ]
      }
      )