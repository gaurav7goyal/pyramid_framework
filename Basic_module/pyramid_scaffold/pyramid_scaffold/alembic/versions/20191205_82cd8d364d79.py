"""use new models Page and User

Revision ID: 82cd8d364d79
Revises: b13abca671eb
Create Date: 2019-12-05 16:29:24.954352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82cd8d364d79'
down_revision = 'b13abca671eb'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('role', sa.Text(), nullable=False),
    sa.Column('password_hash', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('name', name=op.f('uq_users_name'))
    )
    op.create_table('pages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('data', sa.Text(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], name=op.f('fk_pages_creator_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_pages')),
    sa.UniqueConstraint('name', name=op.f('uq_pages_name'))
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pages')
    op.drop_table('users')
    # ### end Alembic commands ###