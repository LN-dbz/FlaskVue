class Role(db.Model):
    """
    角色表
    """
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, commit="角色名")
    permissions = db.Column(db.Integer, commit="权限总值")

    @staticmethod
    def init_role():
        role_name_list = ['user', 'admin']
        roles_permission_map = {
            'user': [Permissions.USER_MANAGE],
            'admin': [Permissions.USER_MANAGE, Permissions.UPDATE_PERMISSION]
        }
        try:
            for role_name in role_name_list:
                role = Role.query.filter_by(name=role_name).first()
                if not role:
                    role = Role(name=role_name)
                role.reset_permissions()
                for permission in roles_permission_map[role_name]:
                    role.add_permission(permission)
                db.session.add(role)
            db.session.commit()
        except:
            db.session.rollback()
        db.session.close()

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, permission):
        return self.permissions & permission == permission

    def add_permission(self, permission):
        if not self.has_permission(permission):
            self.permissions += permission

class Permissions:
    """
    权限类
    """
    USER_MANAGE = 0X01
    UPDATE_PERMISSION = 0x02