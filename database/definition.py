from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

db = SQLAlchemy()


def object_to_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}


def get_count(rows):
    count_rows = rows.statement.with_only_columns(
        [func.count()]).order_by(None)
    count = rows.session.execute(count_rows).scalar()
    return count


def to_dict(rows):
    count = get_count(rows)
    if count < 1:
        return []
    elif count == 1:
        return object_to_dict(rows)
    else:
        return [object_to_dict(row) for row in rows]
