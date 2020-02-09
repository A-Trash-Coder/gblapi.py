import setuptools

setuptools.setup(
    name="gblpyapi",
    version="0.1.0",
    packages= ["glennbotlist"],
    url="https://glennbotlist.xyz",
    license="MIT",
    author="CoderLamar420",
    author_email="gavynlamar@gmail.com",
    description="glennbotlist.xyz API Wrapper in Python",
    long_desciption=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)