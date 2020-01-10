import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wordsearchutils",
    version="1.0.1",
    author="David Bootle",
    author_email="davidtbootle@gmail.com",
    description="A library to solve word searches.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheWeirdSquid/wordsearchutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
