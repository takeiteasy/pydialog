from setuptools import setup, find_packages, Extension

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pydialog",
    version="0.1.0",
    author="George Watson",
    author_email="gigolo@hotmail.co.uk",
    description="Python bindings for osdialog",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/takeiteasy/pydialog",
    include_dirs="osdialog",
    ext_modules=[Extension("pydialog",
                           sources=["pydialog.c", "osdialog.c", "osdialog_mac.m"],
                           extra_link_args=["-framework", "Cocoa"])],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)