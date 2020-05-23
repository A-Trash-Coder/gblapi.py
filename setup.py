import setuptools
with open("README.md", "r", encoding="utf8") as fh:
    long_desc = fh.read()

setuptools.setup(
    name="gblpyapi",
    version="0.2.2",
    packages= ["glennbotlist"],
    url="https://glennbotlist.xyz",
    license="MIT",
    author="A Trash Coder",
    author_email="gavynlamar@gmail.com",
    description="glennbotlist.xyz API Wrapper in Python",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    install_requires=['aiohttp'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)