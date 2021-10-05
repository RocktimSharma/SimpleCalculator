from django import forms

operations = (
    ("+", "Addition"),
    ("-", "Subtraction"),
    ("x", "Multiplication"),
    ("/", "Division"),
)

# Calculator Form Class
class CalculatorForm(forms.Form):
    firstNumber = forms.IntegerField(label="First Number", widget=forms.NumberInput(
        attrs={'placeholder': 'Enter First Number', 'id': 'firstNumber'}))

    secondNumber = forms.IntegerField(label='Second Number', widget=forms.NumberInput(
        attrs={'placeholder': 'Enter Second Number', 'id': 'secondNumber'}))

    operation = forms.ChoiceField(choices=operations)
