from back_end.module.database.base import db_session
from back_end.module.database.user import User
from back_end.module.database import init_db

# 初始化数据库
# init_db()
u = User('admin', '123', '231')
# db_session.add(u)
# db_session.commit()
# # row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
# for v in User.query.with_entities(User.name).all():
#     print(v.to_json())
# print(User.query.all())

import time
t = u.genTokenSeq()
time.sleep(2)
print(print(u.tokenAuth(t)))
print(time.time())