from distutils.core import setup

setup(
    name="HIV-AIDS-Diagnoses-Analysis",
    version="0.1.0",
    description="Data analysis.",
    author="Lokesh Dondapati",
    author_email="ldondapa@mail.yu.edu",
    license="MIT",
    url='https://github.com/LokeshDondapati/HIV-AIDS-Diagnoses-Analysis',

    packages=["Diagnoses_Analysis"],
    install_requires=[
        "matplotlib>=3.0.2",
        "numpy>=1.15.2",
        "pandas>=0.23.4",
        "seaborn>=0.11.0",
        "black>=23.11.0,"
    ],
)
