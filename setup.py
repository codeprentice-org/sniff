import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sniffpy",
    version="1.0.0",
    author="Codeprentice",
    author_email="nb2838@columbia.edu",
    description="A package for mime-sniffing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codeprentice-org/sniffpy",
    download_url='https://github.com/woberton/sniffpy/archive/1.0.0.tar.gz',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
