# coding=utf-8
from django import forms

ZONE_CHOICES = (
    ('local','本地'),
    ('s001','1区'),
    ('s002','2区'),
    ('s003','3区'),
    ('all','所有'),
)
CHECK_TABLES = (
    ('match','战役'),
    ('soulproba','抽奖'),
    ('reward','普通抽奖'),
)

class CheckForm(forms.Form):
    # a = forms.IntegerField()
    # checkTable = forms.CharField(
    #     label="(战役:match;抽奖:soulproba)表单:",
    #     max_length=100
        # widget=forms.Textarea
    # )
    zone = forms.ChoiceField(choices=ZONE_CHOICES,label='选择分区')
    checkTable = forms.ChoiceField(choices=CHECK_TABLES,label='选择表单')