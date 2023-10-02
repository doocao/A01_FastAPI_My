from tortoise import Model, fields


class TodoData666(Model):
    """创建数据库中的表 tododata666，类名是啥，那么创建的表名就是该类名的全部小写"""
    id = fields.IntField(pk=True)  # pk主键 primary key
    content = fields.CharField(max_length=500)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

