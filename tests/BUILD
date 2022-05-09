python_test_utils(
    name="test_utils",
    sources=["conftest.py", "optional.py", "util.py"],
)

files(
    name="toml",
    sources=["*.toml"],
)

python_tests(
    name="tests",
    dependencies=[
        "//:test_format_files",
        ":test_utils",
        ":toml",
        "src:extra-d",
        "src:extra-jupyter",
        "tests/data"
    ],
    interpreter_constraints=parametrize(
        py36=[">=3.6.2,<3.7"],
        py37=["==3.7.*"],
        py38=["==3.8.*"],
        py39=["==3.9.*"],
        py310=["==3.10.*"],
    ),
)
