"""unique contraints on episode, guest, reference

Revision ID: c640bf5b87ae
Revises: 818227f1d447
Create Date: 2020-10-16 02:49:30.838313

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'c640bf5b87ae'
down_revision = '818227f1d447'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'episode', ['name'])
    op.create_unique_constraint(None, 'guest', ['name'])
    op.create_unique_constraint(None, 'reference', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reference', type_='unique')
    op.drop_constraint(None, 'guest', type_='unique')
    op.drop_constraint(None, 'episode', type_='unique')
    # ### end Alembic commands ###