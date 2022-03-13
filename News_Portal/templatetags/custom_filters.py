from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, # то Django никогда не узнает, где именно их искать и фильтры потеряются

@register.filter(name='Censor2')  # регистрируем наш фильтр под именем Censor, чтоб django понимал, что это именно фильтр, а не простая функция
def Censor2(value):  # первый аргумент здесь это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т. е. примерно следующее будет в шаблоне value|Censor
    bad = ['строк', 'сайт', 'люд', 'Python']
    string = value.split()
    for i in range(0, len(string)):
        if string[i] in bad:
            string[i] = f'#CENSOR# ({string[i]})'
    return " ".join(string)  # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон

@register.filter(name='Censor')  # регистрируем наш фильтр под именем Censor, чтоб django понимал, что это именно фильтр, а не простая функция
def Censor(value):  # первый аргумент здесь это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т. е. примерно следующее будет в шаблоне value|Censor
    bad = ['строк', 'сайт', 'люд', 'Python']
    a = ''
    for i in range(0, len(bad)):
        a = value.replace(bad[i], f'#CENSOR# ({bad[i]})')
    return a