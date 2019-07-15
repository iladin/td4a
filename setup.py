from setuptools import setup

setup(name='td4a',
      version='1.7',
      description='A browser based jinja template renderer',
      url='http://github.com/cidrblock/td4a',
      author='Bradley A. Thornton',
      author_email='brad@thethorntons.net',
      license='MIT',
      include_package_data=True,
      packages=[
          'td4a'
      ],
      scripts=['td4a-server'],
      install_requires=[
          'ansible==2.8.2',
          'Flask==1.1.1',
          'netaddr==0.7.19',
          'Twisted==19.2.1',
          'requests==2.22.0',
          'ruamel.yaml==0.15.35',
          'genson==1.1.0',
          'jsonschema==3.0.1'
      ],
      zip_safe=False)
