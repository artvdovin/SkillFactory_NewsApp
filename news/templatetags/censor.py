from django import template


register = template.Library()


bad_words = ['биткоин','спорт','биткоина','сша','openai']

@register.filter()
def censor(text):

    words = text.split()  # Используем другое имя для списка слов
    censor_list = []

    for word in words:
        if word.lower() in bad_words:
            # Заменяем все символы слова, кроме первого, на символ "*"
            censor_word = word[0] + '*' * (len(word) - 1)

            censor_list.append(censor_word)
        else:
            censor_list.append(word)

    return ' '.join(censor_list)

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()

