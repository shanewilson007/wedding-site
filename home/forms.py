from django import forms
from .models import RSVP, Post
from .choices import choice, plusOnes


class PostForm(forms.ModelForm):
    post = forms.CharField(widget=forms.Textarea, label='Post')

    class Meta:
        model = Post
        fields = ('post',)


class ReceptionForm(forms.ModelForm):
    receptions = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=choice,
            required=True,
            initial='No Response',
    )

    class Meta:
        model = RSVP
        fields =('reception',)

class ExtrasForm(forms.ModelForm):
    extras = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=plusOnes,
            required=True,
            initial='0',
    )

    class Meta:
        model = RSVP
        fields =('extra',)
