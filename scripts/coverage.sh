coverage run --source='../' --omit="../projeto/migrations/*,../pms/*,../scrips/*,../docs/*,../*/__*,../projeto/admin.py,../projeto/forms.py,../manage.py" ../manage.py test projeto
coverage html --directory="../coverage/"