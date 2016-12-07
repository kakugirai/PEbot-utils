from setuptools import setup

setup(
    name="PEbot",
    version="0.0.1",
    py_modules=[
        "pecli",
        "botcore",
    ],
    install_requires=[
        "click",
        "pyvirtualdisplay",
        "selenium",
        "beautifulsoup4",
        "tabulate",
    ],
    entry_points='''
        [console_scripts]
        pecli=pecli:cli
    ''',
)
