"""reg_mail

Revision ID: 0195df0d9e9b
Revises: 50f1c9e1d6e6
Create Date: 2022-10-04 22:43:28.514952

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '0195df0d9e9b'
down_revision = '50f1c9e1d6e6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('registrationmail',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_registrationmail_email'), 'registrationmail', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_registrationmail_email'), table_name='registrationmail')
    op.drop_table('registrationmail')
    # ### end Alembic commands ###