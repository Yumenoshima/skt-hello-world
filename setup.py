import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='skt-hello-world',
    version='0.0.1',
    scripts=['skt-hello-world'],
    author="Yumenoshima",
    author_email="skt.tofuya@gmail.com",
    description="Prints skt hello world!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yumenoshima/skt-hello-world",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
    ],
)