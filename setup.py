from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ckanext-demo',
    version=version,
    description='Demo extension for CKAN',
    long_description='',
    classifiers=[],
    keywords='',
    author='Open Knowledge Foundation',
    author_email='info@okfn.org',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.demo'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points=\
    """
    [ckan.plugins]
    demo=ckanext.demo.plugin:DemoPlugin
    """,
)
