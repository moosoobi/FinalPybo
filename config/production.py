from config.default import *

from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b's^\xf5\x8d-\xa9q?a\x8eH\xde\xc8\xc4P\xc2'