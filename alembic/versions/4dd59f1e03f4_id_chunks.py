"""id chunks

Revision ID: 4dd59f1e03f4
Revises: 55aa0348c271
Create Date: 2012-07-22 09:50:56.086107

"""

# revision identifiers, used by Alembic.
revision = '4dd59f1e03f4'
down_revision = '55aa0348c271'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chunk', sa.Column('drive_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chunk', 'drive_id')
    ### end Alembic commands ###
