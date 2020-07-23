import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fishfinder-sdstolworthy", # Replace with your own username
    version="0.0.1",
    author="sdstolworthy",
    author_email="sdstolworthy@gmail.com",
    description="A simple application to find a cheap plane",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sdstolworthy/fishfinder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)