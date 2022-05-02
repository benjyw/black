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
)
