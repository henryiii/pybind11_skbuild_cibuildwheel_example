from skbuild import setup

setup(
    name="cli11",
    version="1.2.3",
    description="a minimal example package (with pybind11)",
    author="Henry Schreiner",
    license="MIT",
    packages=["cli11"],
    package_dir={"": "src"},
    cmake_install_dir="src/cli11",
    python_requires=">=3.7",
    extras_require={"test": ["pytest"]},
)
