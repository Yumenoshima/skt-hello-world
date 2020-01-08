import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='print-hello-world',  
    version='0.0.1',
    scripts=['print-hello-world'],
    author="Hans Maulloo",
    author_email="askyourkode@gmail.com",
    description="Prints hello world!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/askyourkode/print-hello-world",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
    ],
)