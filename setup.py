import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("qanom/version.txt", "r") as f:
    version = f.read().strip()

setuptools.setup(
    name="roleQGeneration",
    version=version,
    author="Valentina Py",
    url="https://github.com/rubenwol/RoleQGeneration",
    packages=setuptools.find_packages(),
    install_requires=[
        'spacy==2.3.2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
