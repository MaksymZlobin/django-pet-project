from django.forms import ModelForm, CharField, Textarea
from news.models import Article, Comment, User


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'picture', 'author']


class CommentForm(ModelForm):
    comment_text = CharField(widget=Textarea, label='Enter comment text')
    author_name = CharField(label='Enter your name')

    class Meta:
        model = Comment
        fields = ['author_name', 'comment_text']