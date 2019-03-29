import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uipath_scaffold",
    version="0.0.7",
    author="Christian Blandford",
    author_email="christianblandford@me.com",
    description="CLI tool for running UiPath Scaffold Generators.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/christianblandford/UiPath-Scaffold",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "console_functions >= 0.0.8"
    ],
)
