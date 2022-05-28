import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyInfo-Nexachromic",
    version="0.0.1",
    author="Nexachromic",
    author_email="nexachromic.djs@gmail.com",
    description="A package to guide developers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nexachromic-djs/PyInfo",
    project_urls="https://github.com/Nexachromic-djs/PyInfo",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: Windows",
    ],
    package_dir={"": "PyInfo"},
    packages=setuptools.find_packages(where="PyInfo"),
    python_requires=">=3.6",
)
