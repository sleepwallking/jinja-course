from jinja2 import Template

cars = [
    {'model': 'Ауди', 'price': 23000},
    {'model': 'Бмв', 'price': 12000},
    {'model': 'Мерседес', 'price': 16500},
    {'model': 'Порш', 'price': 30000}
]

tpl = "Суммарная стоимость автомобилей {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)
