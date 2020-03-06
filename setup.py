from setuptools import setup


#with open("README.md", "r") as fh:
#    long_description = fh.read()

setup(
    name = "wasserbombenspiel",
    version = "0.0.1",
    description = "wasserbombenspiel",
    #long_description= long_description,
    url = "https://github.com/maxmay12/python",
    author = "Max May",
    author_email = "m.may@example.com",
    #license = "GPLv3",
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        # Pick your license as you wish
        #'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        #"Operating System :: POSIX :: Linux",
    ],
    install_requires = ["pgzero"],
    packages = ["images"],
    package_data = {"images" : ["*.png*"]},
    scripts = ["wasserbombenspiel.py"]
)
