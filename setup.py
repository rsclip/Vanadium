import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vanadium",
    version="0.0.2.1",
    author="Cyclip",
    author_email="gdneop@gmail.com",
    description="A python module for small things; so you don't have to reinvent the wheel",

    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cyclip/Vanadium",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
