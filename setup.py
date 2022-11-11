from setuptools import setup, find_packages

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="PetroGeoSim",
    packages=find_packages(exclude=["docs*", "examples*", "tests*"]),
    version="0.9",
    url="https://github.com/sup3r-g/PetroGeoSim",
    license="GNU GPLv3",
    author="sup3r-g",
    description="Estimation of reservoir reserves using Monte Carlo method",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    python_requires=">=3.10",
    install_requires=["joblib", "matplotlib", "numpy", "scipy"],
    extras_require={},
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "License :: GNU General Public License v3.0",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Development Status :: 4 - Beta",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
