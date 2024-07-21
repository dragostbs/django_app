# Create a new project
django-admin startproject django_app

# Start the application
python manage.py runserver 

# Create apps folder
python manage.py startapp starting_app

# Create migration for db
python manage.py makemigrations 

# Start the migration for db
python manage.py migrate

# Interact with db
python manage.py shell

- from data_app.models import Book
- book = Book(title='Harry Potter', rating=5)
- book.save()
- Book.objects.create(title='Harry Potter', rating=5)
- Book.objects.all()
- Book.objects.all()[1]
- Book.objects.all()[1].author
- Book.objects.get(id=1)
- Book.objects.filter(is_bestseller=True)
- Book.objects.filter(rating__lte=2) # lower then or equal to 2

- from django.db.models import Q
- Book.objects.filter(Q(rating__lte=2) | Q(is_bestseller=True), Q(title='Harry Potter'))

# Administration
python manage.py createsuperuser
