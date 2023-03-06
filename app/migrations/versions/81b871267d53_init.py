"""init

Revision ID: 81b871267d53
Revises: 
Create Date: 2023-03-05 14:47:26.729004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81b871267d53'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)

    # ### end Alembic commands ###
