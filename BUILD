pex_binary(
    name="fuzz",
    dependencies=[":fuzz_py"],
    entry_point="fuzz.py",
)

python_sources(
    sources=["fuzz.py"],
    name="fuzz_py",
)

python_sources(
    sources=["setup.py"],
    name="setup_py",
)

python_requirements(
    name = "requirements",
)

resources(
    name="build_resources",
    sources=["pyproject.toml", "README.md", "CHANGES.md"],
)

python_distribution(
    name = "dist",
    dependencies=[
        ":build_resources",
        ":setup_py",
        "src/black",
    ],
    provides=python_artifact(
        name="black",
        version="9.9.9",
    ),
    wheel_config_settings={"--global-option": ["--python-tag", "py37.py38.py39"]},
    generate_setup = False,
)

files(
    name="test_format_files",
    sources=[
        "src/black/__init__.py",
        "src/black/__main__.py",
        "src/black/brackets.py",
        "src/black/cache.py",
        "src/black/comments.py",
        "src/black/concurrency.py",
        "src/black/const.py",
        "src/black/debug.py",
        "src/black/files.py",
        "src/black/linegen.py",
        "src/black/lines.py",
        "src/black/mode.py",
        "src/black/nodes.py",
        "src/black/numerics.py",
        "src/black/output.py",
        "src/black/parsing.py",
        "src/black/report.py",
        "src/black/rusty.py",
        "src/black/strings.py",
        "src/black/trans.py",
        "src/blackd/__init__.py",
        "src/blib2to3/pygram.py",
        "src/blib2to3/pytree.py",
        "src/blib2to3/pgen2/conv.py",
        "src/blib2to3/pgen2/driver.py",
        "src/blib2to3/pgen2/grammar.py",
        "src/blib2to3/pgen2/literals.py",
        "src/blib2to3/pgen2/parse.py",
        "src/blib2to3/pgen2/pgen.py",
        "src/blib2to3/pgen2/tokenize.py",
        "src/blib2to3/pgen2/token.py",
        "setup.py",
        "tests/test_black.py",
        "tests/test_blackd.py",
        "tests/test_format.py",
        "tests/optional.py",
        "tests/util.py",
        "tests/conftest.py",
    ]
)
