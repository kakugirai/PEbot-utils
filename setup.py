from setuptools import setup

setup(
    name="pecli",
    version="0.0.1",
    description="A CLI tool to check, register and cancel PE class in SFC",
    url="https://github.com/kakugirai/PEbot-utils",
    author="Girai Kaku",
    author_email="kakugirai@gmail.com",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    py_modules=[
        "pecli",
        "botcore",
    ],
    install_requires=[
        "click",
        "inquirer",
        "pyvirtualdisplay",
        "lxml",
        "selenium",
        "beautifulsoup4",
        "tabulate",
    ],
    entry_points='''
        [console_scripts]
        pecli=pecli:cli
    ''',
)
