"""
Macros for reducing boilerplate in Pants BUILD files.
"""

def multi_distribution(**kwargs):
    name = kwargs.pop("name")
    dependencies = kwargs.pop("dependencies", [])
    for interpreter in ["py36", "py37", "py38", "py39", "py310"]:
        kwargs["name"] = name + f"-{interpreter}"
        kwargs["dependencies"] = [
            (f":setup_py@interpreter_constraints={interpreter}" if dep == ":setup_py" else dep)
            for dep in dependencies
        ]
        python_distribution(**kwargs)
