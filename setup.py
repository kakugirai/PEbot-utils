from setuptools import setup

setup(
    name="PEbot CLI",
    version="0.0.1",
    py_modules=["bot_cli"],
    install_requires=[
        "Click",
    ],
    entry_points='''
        [console_scripts]
        bot_cli=bot_cli:cli
    ''',
)

