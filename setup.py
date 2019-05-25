from setuptools import setup

version = "1.0.0.0"

setup(
    name='Sanic-OpenTracing',
    version=version,
    license='MIT',
    author='Harsha Narayana',
    author_email='harsha2k4@gmail.com',
    description='OpenTracing support for Sanic applications',
    long_description='OpenTracing support for Sanic applications',
    packages=['sanic_opentracing'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'sanic',
        'opentracing',
        'jaeger-client'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)