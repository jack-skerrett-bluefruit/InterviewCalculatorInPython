import maths

def test_fresh_calculator_has_current_number_as_zero_by_default():
    test_class = maths.Math()
    assert test_class.current_number == "0"

def test_fresh_calculator_has_stored_number_as_nothing_by_default():
    test_class = maths.Math()
    assert test_class.stored_number == ""

def test_fresh_calculator_has_stored_operator_as_nothing_by_default():
    test_class = maths.Math()
    assert test_class.stored_number == ""

def test_fresh_calculator_has_operator_pressed_as_false_by_default():
    test_class = maths.Math()
    assert test_class.operator_pressed == False

def test_fresh_calculator_sets_input_as_current_number():
    test_class = maths.Math()
    test_class.enter_number("5")
    assert test_class.current_number == "5"

def test_successive_number_presses_are_appended_to_current_number():
    test_class = maths.Math()
    test_class.enter_number("5")
    test_class.enter_number("1")
    test_class.enter_number("3")
    test_class.enter_number("9")
    assert test_class.current_number == "5139"

def test_decimal_point_is_added_when_no_number_has_been_input_and_is_appended_to_zero():
    test_class = maths.Math()
    test_class.decimal_point(".")
    assert test_class.current_number == "0."
    
def test_decimal_point_is_added_when_there_is_an_integer_in_current_number_and_the_decimal_point_is_appended():
    test_class = maths.Math()
    test_class.enter_number("1")
    test_class.enter_number("7")
    test_class.decimal_point(".")
    assert test_class.current_number == "17."

def test_numbers_can_be_appended_to_current_number_string_after_a_decimal_point_press():
    pass

def test_only_one_decimal_point_can_be_added_to_the_current_number_string():
    pass
