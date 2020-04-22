#!/bin/bash
#!/bin/sh

# create a demo user if it doesnt exist
# python manage.py shell << END
# from django.contrib.auth.models import User
# if not User.objects.filter(username='foo').exists():
#     user = User.objects.create_user('foo', password='bar')

# END

set -o errexit
set -o pipefail
set -o nounset

# collect static files
python manage.py collectstatic --noinput
python manage.py shell <<END
from core.models import User
User.objects.create_superuser('admin@example.com', 'adminpass')
END

# run gunicorn
# gunicorn -b 0.0.0.0:5000 config.wsgi --workers ${GUNICORN_WORKERS} --timeout ${GUNICORN_TIMEOUT} $*

# run daphne
daphne -b 0.0.0.0 -p 5000 config.asgi:application -v 2 --proxy-headers $*

# python manage.py runserver 0.0.0.0:5000
