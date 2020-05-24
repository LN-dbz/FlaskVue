from back_end.module.database.base import db_session
from back_end.module.database.user import User
import json
u = User('admin', 'admin@localhost')
db_session.add(u)
db_session.commit()
row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
for v in User.query.with_entities(User.name).all():
    print(v.to_json())
print(User.query.all())
