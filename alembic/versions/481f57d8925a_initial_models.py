"""Initial models

Revision ID: 481f57d8925a
Revises: None
Create Date: 2012-07-21 16:24:15.786056

"""

# revision identifiers, used by Alembic.
revision = '481f57d8925a'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('drive_id', sa.BigInteger(), nullable=True),
    sa.Column('drive_token', sa.String(length=255), nullable=True),
    sa.Column('dropbox_id', sa.BigInteger(), nullable=True),
    sa.Column('dropbox_token', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('chunk',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chunk')
    op.drop_table('file')
    op.drop_table('user')
    ### end Alembic commands ###