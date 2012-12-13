"""
Flask Redisession
-----------------

A simple extension to provide Redis Session support to flask

Links
`````
"""

from setuptools import setup

setup(
	name='Flask-Redisession',
	version='0.1',
	url='http://github.com/petermelias/flask-redisession',
	license='BSD',
	author='Peter M. Elias',
	author_email='petermelias@gmail.com',
	description='A simple extension to drop in redis session support for Flask.',
	long_description=__doc__,
	py_modules=['flask_redisession'],
	zip_safe=False,
	include_package_data=True,
	platforms='any',
	install_requires=[
		'Flask',
		'Werkzeug',
		'redis'
	],
	classifiers=[
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
		'Topic :: Software Development :: Libraries :: Python Modules'
	],
	test_suite='tests'
)