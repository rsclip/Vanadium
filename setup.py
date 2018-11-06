import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vanadium",
    version="0.0.1",
    author="Cyclip",
    author_email="gdneop@gmail.com",
    description="A python module for small things; so you don't have to reinvent the wheel",
    maintainer = "Cyclip"
    maintainer_email = "gdneop@gmail.com"

    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cyclip/Vanadium",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
        "Natural Language :: English
        "Intended Audience :: Developers"
        "Developement Status :: 2 - Pre-Alpha",
    ],

    install_requires=[
        'random'
        'base64'
        'hashlib'
        'threading'
        'requests'
        'pathlib'
        'smtplib'
        'sys'
        'inspect'
        'subprocess'
        'ctypes'
)
