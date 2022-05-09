python_sources(dependencies=[":scm_version"])

setuptools_scm_version(
    name="scm_version",
    write_to="src/_black_version.py",
    write_to_template='version = "{version}"\n',
)

python_requirement(
    name="extra-d",
    requirements=["aiohttp>=3.7.4"],
)

python_requirement(
    name="extra-jupyter",
    requirements=["ipython>=7.8.0", "tokenize-rt>=3.2.0"],
)
