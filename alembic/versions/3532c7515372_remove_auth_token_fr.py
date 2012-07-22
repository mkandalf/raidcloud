"""Remove auth token from users

Revision ID: 3532c7515372
Revises: 42fdd0e6f5b0
Create Date: 2012-07-21 21:47:24.214177

"""

# revision identifiers, used by Alembic.
revision = '3532c7515372'
down_revision = '42fdd0e6f5b0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', u'auth_token')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column(u'auth_token', sa.VARCHAR(length=36), nullable=False))
    ### end Alembic commands ###