import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="url_benchmark",
    version="0.0.1",
    author="Denis Yarats",
    author_email="denisyarats@cs.nyu.edu",
    description="A library for unsupervised reinforcement learning benchmark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rll-research/url_benchmark.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
)
