"""empty message

Revision ID: ede21694a7ae
Revises: 22f2ab4c427a
Create Date: 2019-03-23 17:37:09.381107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ede21694a7ae'
down_revision = '22f2ab4c427a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('created', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('updated', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'updated')
    op.drop_column('user', 'created')
    # ### end Alembic commands ###
