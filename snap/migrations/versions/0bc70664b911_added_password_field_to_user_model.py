"""Added password field to user model

Revision ID: 0bc70664b911
Revises: 
Create Date: 2024-02-14 16:48:45.317639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bc70664b911'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=60), nullable=True))
        batch_op.add_column(sa.Column('created_on', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('created_on')
        batch_op.drop_column('password')

    # ### end Alembic commands ###
