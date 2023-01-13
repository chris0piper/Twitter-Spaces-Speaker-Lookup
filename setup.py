import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Twitter-Spaces-Speaker-Lookup",
    version="0.0.6",
    author="Example Author",
    author_email="chris0piper@gmail.com",
    description="Program to monitor twitter spaces for when a given user speaks in or hosts a twitter space.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chris0piper/Twitter-Spaces-Speaker-Lookup",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)