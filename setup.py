from setuptools import setup, find_packages

setup(
    name='silverpy',
    version='1.0.0',
    description='An easy-to-use Silverpop Engage Library.',
    long_description=(open('README.md').read()),
    url='https://github.com/kevinwaddle/silverpy',
    license='',
    author='Nicholas Santos',
    author_email='nicholas.santos@dedsert.com',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
