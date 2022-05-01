python_test_utils(
    name="test_utils",
    sources = ["conftest.py", "optional.py"],
)

python_tests(
    name="tests",
    dependencies = [
        ":test_utils",
        "tests/data"
    ],
)
