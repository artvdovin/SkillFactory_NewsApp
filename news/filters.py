from django_filters import FilterSet, ModelMultipleChoiceFilter,DateTimeFilter
from django.forms import DateTimeInput
from .models import Post, PostCategory, Category

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    data = DateTimeFilter(
        field_name = 'date_add',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    category = ModelMultipleChoiceFilter(
        field_name = 'postcategory__categoryThround',
        queryset=Category.objects.all(),
        label = 'Категория',

    )
    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'title': ['icontains'],
       }