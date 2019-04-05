# Lesson 14 23/03/2019
### Documentation
1. https://docs.djangoproject.com/en/2.1/ - дока по Django
2. https://docs.djangoproject.com/en/2.1/topics/db/models/ - дока по моделям джанги


### Homework
1. Почитать про джангу. Оперировать терминами - проект, приложения, модель, вью.
2. Придумать(описать) модели для нашего приложения (социальная сеть с рецептами).
К примеру: Рецепт, коментарий, репост, закладки и тд. Не прошу описывать все, хотя бы немного.

# Lesson 15 26/03/2019
1. https://docs.djangoproject.com/en/2.1/ - дока по Django

### Homework
1. Добавить в админку все созданые модели.
2. Попрактиковаться в написаниее view:
- сделать view которая будет на POST запрос создавать новую запись в таблице рецептов.
- описать шаблон с формой создания этого рецепта. (Пока достаточно несколько полей, title, text, level). Рецепт пока создаем без привязки к пользователю.

# Lesson 16 30/03/2019
1. https://docs.djangoproject.com/en/2.1/ - дока по Django
2. https://docs.djangoproject.com/en/2.1/topics/templates/ - по темплейтам

### Homework
1. Добавить bootstrap статику в проект. https://getbootstrap.com/
2. Используя bootstrap привести сайт к нормальному виду
- На Странице сайта должен быть header в котором будут ссылки на разные страницы, а так же информация
о залогиненом пользвателе или кнопки войти/выйти
- Header должен содержать в себе кнопки **Feed** | **My Recipes** | **Create new recipe**
- В **Feed** должен быть список всек рецептов в хронологическом порядке. (Оформить в виде поста при нажатии которого открывается новая страница с полным содержимым)
- **Feed** должен поддерживать пагинацию https://docs.djangoproject.com/en/2.1/topics/pagination/
- На странице **My Recipes** должна быть точно такая же лента как и в **Feed**, но только список должен быть пользователя под которым мы залогинены на сайте.
- Кнопка **Create new recipe** открывает страницу в которой создается новый рецепт. (сделать такую страницу)
- ! если пользователь не авторизован, то выводить только **Feed** и кнопку login

# Lesson 17 02/04/2019
1. https://ccbv.co.uk/ - как работать с классами view

### Homework
1. Сделать красивой страницу создания + страницу с регистрацией.
2. Добавить страницу с редактированием поста (редактировать может тот, кто создавал этот пост)
3. Добавить к посту возможность ставить лайки и оставлять комменты.

# Lesson 18 05/04/2019
1. https://docs.djangoproject.com/en/2.2/topics/http/middleware/ - мидлвари
2. https://docs.djangoproject.com/en/2.1/ref/templates/api/#writing-your-own-context-processors - контекст процессоры
3. https://docs.djangoproject.com/en/2.1/topics/i18n/translation/ - переводы
4. https://docs.djangoproject.com/en/2.2/ref/contrib/admin/ - админка
5. https://docs.djangoproject.com/en/2.2/topics/db/aggregation/#aggregating-annotations - агрегации запросов

Пример агрегации через анотацию
```cython
from django.db.models import Case, IntegerField
from django.db.models import Count
from django.db.models import When
from cooking.models import Recipe

queryset = Recipe.objects.all().annotate(
    likes_count=Count(
        Case(
            When(
                reactions__status='like',
                then=1
            ),
            output_field=IntegerField()
        )
    ),
)
print(queryset[0].likes_count)
```

### Homework
0. Домашка из Lesson 17
1. Создать middleware, которая будет писать в базу 500 ошибки приложения(Если такие будут). 
(Придумать модель куда будете писать)
2. Добавить модель в админку. Добавить поиск, фильтрацию по полям которые придумаете.