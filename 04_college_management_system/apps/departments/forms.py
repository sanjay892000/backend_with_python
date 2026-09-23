from django import forms

from .models import Department

INPUT_CLASS = """
w-full
rounded-xl
border
border-slate-300
bg-white
px-4
py-3
text-slate-700
placeholder:text-slate-400
focus:outline-none
focus:ring-2
focus:ring-indigo-500
focus:border-indigo-500
transition
"""

TEXTAREA_CLASS = """
w-full
rounded-xl
border
border-slate-300
bg-white
px-4
py-3
text-slate-700
placeholder:text-slate-400
focus:outline-none
focus:ring-2
focus:ring-indigo-500
focus:border-indigo-500
transition
resize-none
"""

CHECKBOX_CLASS = """
w-5
h-5
rounded
text-indigo-600
focus:ring-indigo-500
border-slate-300
"""


class DepartmentForm(forms.ModelForm):

    class Meta:

        model = Department

        fields = (
            "name",
            "code",
            "description",
            "is_active",
        )

        widgets = {
            "name": forms.TextInput(
                attrs={"class": INPUT_CLASS, "placeholder": "Enter department name"}
            ),
            "code": forms.TextInput(
                attrs={"class": INPUT_CLASS, "placeholder": "Example : CSE"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": TEXTAREA_CLASS,
                    "rows": 5,
                    "placeholder": "Write short description...",
                }
            ),
            "is_active": forms.CheckboxInput(attrs={"class": CHECKBOX_CLASS}),
        }

    def clean_name(self):

        name = self.cleaned_data["name"].strip()

        if len(name) < 3:

            raise forms.ValidationError(
                "Department name must be at least 3 characters."
            )

        return name.title()

    def clean_code(self):

        code = self.cleaned_data["code"].strip().upper()

        if len(code) < 2:

            raise forms.ValidationError("Department code is too short.")

        return code

    def clean(self):

        cleaned_data = super().clean()

        name = cleaned_data.get("name")

        code = cleaned_data.get("code")

        if name and code:

            exists = Department.objects.filter(name__iexact=name, code__iexact=code)

            if self.instance.pk:

                exists = exists.exclude(pk=self.instance.pk)

            if exists.exists():

                raise forms.ValidationError("This department already exists.")

        return cleaned_data
