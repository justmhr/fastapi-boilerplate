"""0__28_02_23_09_48

Revision ID: bc8ab7e98a8d
Revises: 
Create Date: 2023-02-28 15:18:26.307425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc8ab7e98a8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Text(length=36), nullable=False),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('is_verified', sa.Boolean(), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.Column('providers', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('email_otps',
    sa.Column('id', sa.Text(length=36), nullable=False),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('otp', sa.String(), nullable=True),
    sa.Column('attempts', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_email_otps_user_id'), 'email_otps', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_email_otps_user_id'), table_name='email_otps')
    op.drop_table('email_otps')
    op.drop_table('users')
    # ### end Alembic commands ###
