import setuptools
with open("README.md", "r", encoding="utf8") as fh:
    long_desc = fh.read()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="gblpyapi",
    version="0.2.0",
    packages= ["glennbotlist"],
    url="https://glennbotlist.xyz",
    license="MIT",
    author="A Trash Coder",
    author_email="gavynlamar@gmail.com",
    description="glennbotlist.xyz API Wrapper in Python",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)