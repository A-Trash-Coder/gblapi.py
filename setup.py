import setuptools

with open("README.md", "r") as fh:
    long_desc = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="gblpyapi",
    version="0.1.9",
    packages= ["glennbotlist"],
    url="https://glennbotlist.xyz",
    license="MIT",
    author="CoderLamar420",
    author_email="gavynlamar@gmail.com",
    description="glennbotlist.xyz API Wrapper in Python",
    long_desciption=long_desc,
    long_description_content_type="text/markdown",
    requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)