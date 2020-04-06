import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pydeezer",
    version="0.0.1", 
    author="Aaron Gonzales", 
    author_email="aaroncgonzales.dev@gmail.com",
    description="A package to search and download musics on Deezer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chr1st-oo/pydeezer",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
