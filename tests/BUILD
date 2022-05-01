python_test_utils(
    name="test_utils",
    sources=["conftest.py", "optional.py", "util.py"],
)

file(
    name="toml",
    source="empty.toml",
)

python_tests(
    name="tests",
    dependencies=[
        ":test_utils",
        ":toml",
        "tests/data"
    ],
)
