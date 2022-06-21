import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stega-saurus-py",
    version="0.0.1a2",
    author="Greg Allan",
    author_email="gregallandev@gmail.com",
    description="A steganography CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gregmallan/stega-saurus",
    project_urls={
        "Bug Tracker": "https://github.com/gregmallan/stega-saurus/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
    ],
    package_dir={"": "stega"},
    packages=setuptools.find_packages(where="stega"),
    python_requires=">=3.7.2",
    install_requires=[
        "Pillow>=8.4.0,<8.5",
        "typer>=0.4.1,<0.5",
    ],
    extras_require={
        "dev": [
            "pytest>=7.1.2,<7.2",
            "pytest-cov>=3.0.0,<3.1",
        ]
    }
)
