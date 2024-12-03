import setuptools
import os
from subprocess import check_output

command = "git describe --tags --dirty"
version_format = ("{tag}.dev{commitcount}+{gitsha}",)


def format_version(version, fmt):
    parts = version.split("-")
    assert len(parts) in (3, 4)
    dirty = len(parts) == 4
    tag, count, sha = parts[:3]
    if count == "0" and not dirty:
        return tag
    return fmt.format(tag=tag, commitcount=count, gitsha=sha.lstrip("g"))


version = check_output(command.split()).decode("utf-8").strip()


with open("README.rst", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    install_requires = fh.read().split("\n")

setuptools.setup(
    name="simple_nexus_dashboard",
    version=version,
    author="Wilhelm Putz",
    author_email="wilhelm.putz@cancom.com",
    description="Simple REST-client for Cisco Nexus Dashboard",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/jinjamator/simple_nexus_dashboard",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={"": ["*"]},
    install_requires=install_requires,
    license="ASL V2",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    zip_safe=False,
)
