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
