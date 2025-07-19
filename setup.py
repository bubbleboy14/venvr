from setuptools import setup

setup(
    name='venvr',
    version="0.1.5.1",
    author='Mario Balibrera',
    author_email='mario.balibrera@gmail.com',
    license='MIT License',
    description='Virtual ENVironment manageR',
    long_description='classes and functions for interacting with virtual environments',
    packages=[
        'venvr'
    ],
    zip_safe = False,
    install_requires = [
        "fyg >= 0.1.7.2"
    ],
    entry_points = '''
        [console_scripts]
        venvr = venvr:invoke
    ''',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
