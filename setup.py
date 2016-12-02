from setuptools import setup

setup(
    name="PEbot",
    version="0.0.1",
    py_modules=[
        "pecli",
        "botcore",
    ],
    install_requires=[
        "Click",
        "selenium",
        "beautifulsoup4",
    ],
    entry_points='''
        [console_scripts]
        pecli=pecli:cli
    ''',
)

