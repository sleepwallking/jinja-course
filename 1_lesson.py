from jinja2 import Template


# data = '''{% raw %}Модуль Jinja вместо определения {{ name }} подставляет соответствующее значение{% endraw %}'''

# link = '''В HTML-документе ссылки определяются так:
# <a href="#">Ссылка</a>'''

# msg = escape(link)
# msg = tm.render(link=link)

# print(msg)

cities = [{'id': 1, 'city': 'Москва'},
          {'id': 5, 'city': 'Смоленск'},
          {'id': 6, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 9, 'city': 'Калуга'}]

link = '''<select name="cities">
{% for c in cities %}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor %}
</select>'''

tm = Template(link)
print(tm.render(cities=cities))
