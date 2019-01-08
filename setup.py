from setuptools import setup

setup(name='yoga', version='0.1', description='the flexible automation framework',
      url='https://bitbucket.org/infinityworksconsulting/yoga',
      author='Bianca Linscott',
      packages=['yoga'],
      package_data={'yoga': ['resources/*', 'remote/*', 'data/*']},
      install_requires=[
        'Appium-Python-Client==0.28',
        'selenium==3.14.0',
        'urllib3==1.23',
        'colorama==0.3.9',
        'sauceclient==1.0.0',
        'requests==2.19.1',
        'pytest==3.7.3',
        'assertpy==0.14',
        'pdbpp==0.9.3',
        'boto==2.49.0',
        'PyMySQL==0.9.3'
      ],
      setup_requires=["pytest-runner"],
      tests_require=["pytest"]
      )