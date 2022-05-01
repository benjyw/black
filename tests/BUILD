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
        ":test_utils",
        ":toml",
        "tests/data"
    ],
)
