from bootstrap_datepicker_plus import DatePickerInput
from django import forms


class MyDatePickerInput(DatePickerInput):
    template_name = 'kanban/date-picker.html'

class ToDoForm(forms.Form):
    date = forms.DateField(
        widget=MyDatePickerInput(format='%m/%d/%Y')
    )