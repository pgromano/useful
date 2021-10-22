from useful.text import casing


camel_string = "thisIsAnExample"
pascal_string = "ThisIsAnExample"
global_string = "THIS_IS_AN_EXAMPLE"
kebab_string = "this-is-an-example"
snake_string = "this_is_an_example"


def test_infer_camel():
    assert casing.infer_casing(camel_string) == "camel"


def test_infer_pascal():
    assert casing.infer_casing(pascal_string) == "pascal"


def test_infer_global():
    assert casing.infer_casing(global_string) == "global"


def test_infer_kebab():
    assert casing.infer_casing(kebab_string) == "kebab"


def test_infer_snake():
    assert casing.infer_casing(snake_string) == "snake"


def test_conversion_camel_to_global():
    assert casing.camel_to_global(camel_string) == global_string


def test_conversion_camel_to_kebab():
    assert casing.camel_to_kebab(camel_string) == kebab_string


def test_conversion_camel_to_pascal():
    assert casing.camel_to_pascal(camel_string) == pascal_string


def test_conversion_camel_to_snake():
    assert casing.camel_to_snake(camel_string) == snake_string


def test_conversion_global_to_camel():
    assert casing.global_to_camel(global_string) == camel_string


def test_conversion_global_to_kebab():
    assert casing.global_to_kebab(global_string) == kebab_string


def test_conversion_global_to_pascal():
    assert casing.global_to_pascal(global_string) == pascal_string


def test_conversion_global_to_snake():
    assert casing.global_to_snake(global_string) == snake_string


def test_conversion_kebab_to_camel():
    assert casing.kebab_to_camel(kebab_string) == camel_string


def test_conversion_kebab_to_global():
    assert casing.kebab_to_global(kebab_string) == global_string


def test_conversion_kebab_to_pascal():
    assert casing.kebab_to_pascal(kebab_string) == pascal_string


def test_conversion_kebab_to_snake():
    assert casing.kebab_to_snake(kebab_string) == snake_string


def test_conversion_pascal_to_camel():
    assert casing.pascal_to_camel(pascal_string) == camel_string


def test_conversion_pascal_to_global():
    assert casing.pascal_to_global(pascal_string) == global_string


def test_conversion_pascal_to_kebab():
    assert casing.pascal_to_kebab(pascal_string) == kebab_string


def test_conversion_pascal_to_snake():
    assert casing.pascal_to_snake(pascal_string) == snake_string


def test_conversion_snake_to_camel():
    assert casing.snake_to_camel(snake_string) == camel_string


def test_conversion_snake_to_global():
    assert casing.snake_to_global(snake_string) == global_string


def test_conversion_snake_to_kebab():
    assert casing.snake_to_kebab(snake_string) == kebab_string


def test_conversion_snake_to_pascal():
    assert casing.snake_to_pascal(snake_string) == pascal_string
