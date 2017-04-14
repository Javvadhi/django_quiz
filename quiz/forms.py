from django import forms
from django.forms.widgets import RadioSelect, Textarea
from multichoice.models import *
from true_false.models import *

# from PIL import Image


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        # import pdb;pdb.set_trace();
        # question.__class__ = MCQuestion
        # mc = MCQuestion.objects.all()
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list,
                                                   widget=RadioSelect)


class EssayForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(EssayForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(
            widget=Textarea(attrs={'style': 'width:100%'}))
