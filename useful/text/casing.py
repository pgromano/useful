import re


__all__ = [
    "camel_to_global",
    "camel_to_kebab",
    "camel_to_pascal",
    "camel_to_snake",
    "global_to_camel",
    "global_to_kebab",
    "global_to_pascal",
    "global_to_snake",
    "kebab_to_camel",
    "kebab_to_global",
    "kebab_to_pascal",
    "kebab_to_snake",
    "pascal_to_camel",
    "pascal_to_global",
    "pascal_to_kebab",
    "pascal_to_snake",
    "snake_to_camel",
    "snake_to_global",
    "snake_to_kebab",
    "snake_to_pascal",
]


RE_IS_GLOBAL = re.compile(r"^[A-Z]+(?:_[A-Z]+)*$")
RE_IS_SNAKE = re.compile(r"^[a-z]+(?:_[a-z]+)*$")
RE_IS_KEBAB = re.compile(r"^[a-z]+(?:-[a-z]+)*$")
RE_IS_PASCAL = re.compile(r"^[A-Z][a-z]*(?:[A-Z][a-z]*)*$")
RE_IS_CAMEL = re.compile(r"^[a-z]+(?:[A-Z][a-z]*)*$")


def _is_global(string: str):
    return True if RE_IS_GLOBAL.match(string) else False


def _is_snake(string: str):
    return True if RE_IS_SNAKE.match(string) else False


def _is_kebab(string: str):
    return True if RE_IS_KEBAB.match(string) else False


def _is_pascal(string: str):
    return True if RE_IS_PASCAL.match(string) else False


def _is_camel(string: str):
    return True if RE_IS_CAMEL.match(string) else False


def infer_casing(string: str):
    if len(string) == 0:
        raise ValueError("Cannot infer casing from empty string!")

    if _is_snake(string):
        return "snake"
    elif _is_pascal(string):
        return "pascal"
    elif _is_global(string):
        return "global"
    elif _is_camel(string):
        return "camel"
    elif _is_kebab(string):
        return "kebab"
    else:
        raise ValueError(f"Could not infer casing for givin string `{string}`")


def camel_to_global(string: str):
    """Convert Camel to Global Case

    The following code takes a string input and will attempt to
    convert it to global casing, assuming it is originally in
    camel case. We use the Python PEP8 convention that global and
    constant variables should be snake cased in all caps. For example,
    "thisIsAnExample" would return "THIS_IS_AN_EXAMPLE".

    Parameters
    ----------
    string : str
        A camel case string

    Returns
    -------
    str
        A snake case string
    """
    return camel_to_snake(string).upper()


def camel_to_kebab(string: str):
    """Convert Camel to Kebab Case

    The following code takes a string input and will attempt to convert it to
    kebab casing, assuming it is originally in camel case. For example,
    "thisIsAnExample" would return "this-is-an-example".

    Parameters
    ----------
    string : str
        A camel case string

    Returns
    -------
    str
        A kebab case string
    """
    return snake_to_kebab(camel_to_snake(string))


def camel_to_pascal(string: str):
    """Convert Camel to Pascal Case

    The following code takes a string input and will attempt to convert it to
    pascal casing, assuming it is originally in camel case. For example,
    "thisIsAnExample" would return "this-is-an-example".

    Parameters
    ----------
    string : str
        A camel case string

    Returns
    -------
    str
        A pascal case string
    """
    return string[0].upper() + string[1:]


def camel_to_snake(string: str):
    """Convert Camel to Snake Case

    The following code takes a string input and will attempt to convert it to
    snake casing, assuming it is originally in camel case. For example,
    "thisIsAnExample" would return "this-is-an-example".

    Parameters
    ----------
    string : str
        A camel case string

    Returns
    -------
    str
        A snake case string
    """
    return pascal_to_snake(string)


def global_to_camel(string: str):
    """Convert Global to Camel Case

    The following code takes a string input and will attempt to
    convert it to camel casing, assuming it is originally in
    global case. We use the Python PEP8 convention that global and
    constant variables should be camel cased in all caps. For example,
    "THIS_IS_AN_EXAMPLE" would return "thisIsAnExample".

    Parameters
    ----------
    string : str
        A global case string

    Returns
    -------
    str
        A camel case string
    """
    return snake_to_camel(string.lower())


def global_to_kebab(string: str):
    """Convert Global to Kebab Case

    The following code takes a string input and will attempt to
    convert it to kebab casing, assuming it is originally in
    global case. We use the Python PEP8 convention that global and
    constant variables should be kebab cased in all caps. For example,
    "THIS_IS_AN_EXAMPLE" would return "this-is-an-example".

    Parameters
    ----------
    string : str
        A global case string

    Returns
    -------
    str
        A kebab case string
    """
    return snake_to_kebab(string.lower())


def global_to_pascal(string: str):
    """Convert Global to Pascal Case

    The following code takes a string input and will attempt to
    convert it to pascal casing, assuming it is originally in
    global case. We use the Python PEP8 convention that global and
    constant variables should be pascal cased in all caps. For example,
    "THIS_IS_AN_EXAMPLE" would return "ThisIsAnExample".

    Parameters
    ----------
    string : str
        A global case string

    Returns
    -------
    str
        A pascal case string
    """
    return snake_to_pascal(string.lower())


def global_to_snake(string: str):
    """Convert Global to Snake Case

    The following code takes a string input and will attempt to
    convert it to snake casing, assuming it is originally in
    global case. We use the Python PEP8 convention that global and
    constant variables should be snake cased in all caps. For example,
    "THIS_IS_AN_EXAMPLE" would return "this_is_an_example".

    Parameters
    ----------
    string : str
        A global case string

    Returns
    -------
    str
        A snake case string
    """
    return string.lower()


def kebab_to_camel(string: str):
    """Convert Kebab to Camel Case

    The following code takes a string input and will attempt to
    convert it to camel casing, assuming it is originally in
    kebab case. We use the Python PEP8 convention that camel and
    constant variables should be snake cased in all caps. For example,
    "ThisIsAnExample" would return "thisIsAnExample".

    Parameters
    ----------
    string : str
        A pascal case string

    Returns
    -------
    str
        A snake case string
    """

    return snake_to_camel(kebab_to_snake(string))


def kebab_to_global(string: str):
    """Convert Kebab to Camel Case

    The following code takes a string input and will attempt to
    convert it to camel casing, assuming it is originally in
    kebab case. We use the Python PEP8 convention that camel and
    constant variables should be snake cased in all caps. For example,
    "ThisIsAnExample" would return "thisIsAnExample".

    Parameters
    ----------
    string : str
        A pascal case string

    Returns
    -------
    str
        A snake case string
    """

    return snake_to_global(kebab_to_snake(string))


def kebab_to_pascal(string: str):
    """Convert Kebab to Camel Case

    The following code takes a string input and will attempt to
    convert it to camel casing, assuming it is originally in
    kebab case. We use the Python PEP8 convention that camel and
    constant variables should be snake cased in all caps. For example,
    "ThisIsAnExample" would return "thisIsAnExample".

    Parameters
    ----------
    string : str
        A pascal case string

    Returns
    -------
    str
        A snake case string
    """

    return snake_to_pascal(kebab_to_snake(string))


def kebab_to_snake(string: str):
    """Convert Kebab to Camel Case

    The following code takes a string input and will attempt to
    convert it to camel casing, assuming it is originally in
    kebab case. We use the Python PEP8 convention that camel and
    constant variables should be snake cased in all caps. For example,
    "ThisIsAnExample" would return "thisIsAnExample".

    Parameters
    ----------
    string : str
        A pascal case string

    Returns
    -------
    str
        A snake case string
    """
    return string.replace("-", "_")


def pascal_to_camel(string: str):
    """Convert Pascal to Camel Case

    The following code takes a string input and will attempt to
    convert it to camel casing, assuming it is originally in
    pascal case. We use the Python PEP8 convention that camel and
    constant variables should be snake cased in all caps. For example,
    "ThisIsAnExample" would return "thisIsAnExample".

    Parameters
    ----------
    string : str
        A pascal case string

    Returns
    -------
    str
        A snake case string
    """
    return string[0].lower() + string[1:]


def pascal_to_global(string: str):
    """Convert Pascal to Global Case

    The following code takes a string input and will attempt to
    convert it to global casing, assuming it is originally in
    pascal case. We use the Python PEP8 convention that global and
    constant variables should be snake cased in all caps. For example,
    "ThisIsAnExample" would return "THIS_IS_AN_EXAMPLE".

    Parameters
    ----------
    string : str
        A pascal case string

    Returns
    -------
    str
        A snake case string
    """
    return pascal_to_snake(string).upper()


def pascal_to_kebab(string: str):
    """Convert Pascal to Kebab Case

    The following code takes a string input and will attempt to
    convert it to kebab casing, assuming it is originally in
    pascal case. We use the Python PEP8 convention that kebab and
    constant variables should be snake cased in all caps. For example,
    "ThisIsAnExample" would return "this-is-an-example".

    Parameters
    ----------
    string : str
        A pascal case string

    Returns
    -------
    str
        A snake case string
    """
    return snake_to_kebab(pascal_to_snake(string))


def pascal_to_snake(string: str):
    """Convert Pascal to Snake Case

    The following code takes a string input and will attempt to
    convert it to snake casing, assuming it is originally in
    pascal case. For example, "ThisIsAnExample" would return
    "this_is_an_example".

    Parameters
    ----------
    string : str
        A pascal case string

    Returns
    -------
    str
        A snake case string
    """
    new_string = "".join(
        "_" + char.lower() if char.isupper() else char for char in string
    )
    if new_string[0] == "_":
        new_string = new_string[1:]
    return new_string


def snake_to_camel(string: str):
    """Convert Snake to Camel Case

    The following code takes a string input and will attempt to
    convert it to camel casing, assuming it is originally in
    snake case. For example, "this_is_an_example" would return
    "thisIsAnExample".

    Parameters
    ----------
    string : str
        A snake case string

    Returns
    -------
    str
        A camel case string
    """
    new_string = snake_to_pascal(string)
    return new_string[0].lower() + new_string[1:]


def snake_to_global(string: str):
    """Convert Snake to Global Case

    The following code takes a string input and will attempt to
    convert it to global casing, assuming it is originally in
    snake case. We use the Python PEP8 convention that global and
    constant variables should be snake cased in all caps. For example,
    "this_is_an_example" would return "THIS_IS_AN_EXAMPLE".

    Parameters
    ----------
    string : str
        A snake case string

    Returns
    -------
    str
        A global case string
    """
    return string.upper()


def snake_to_kebab(string: str):
    """Convert Snake to Kebab Case

    The following code takes a string input and will attempt to
    convert it to pascal casing, assuming it is originally in
    snake case. For example, "this_is_an_example" would return
    "this-is-an-example".

    Parameters
    ----------
    string : str
        A snake case string

    Returns
    -------
    str
        A kebab case string
    """
    return string.replace("_", "-")


def snake_to_pascal(string: str):
    """Convert Snake to Pascal Case

    The following code takes a string input and will attempt to
    convert it to pascal casing, assuming it is originally in
    snake case. For example, "this_is_an_example" would return
    "ThisIsAnExample".

    Parameters
    ----------
    string : str
        A snake case string

    Returns
    -------
    str
        A pascal case string
    """
    new_string = "".join(string.replace("_", " ").title().split())
    return new_string
