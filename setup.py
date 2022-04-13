import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = "0.0.1"

setuptools.setup(
    name="RoleQGeneration",
    version=version,
    author="Valentina Py",
    url="https://github.com/rubenwol/RoleQGeneration",
    packages=['RoleQGeneration'],
    install_requires=[
        'spacy',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
