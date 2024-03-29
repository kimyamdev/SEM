"""initial migration

Revision ID: 0e203f86600e
Revises: 
Create Date: 2022-07-18 20:01:39.219120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e203f86600e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('asset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('asset_name', sa.String(length=140), nullable=True),
    sa.Column('asset_thesis', sa.String(length=1200), nullable=True),
    sa.Column('asset_type', sa.String(length=140), nullable=True),
    sa.Column('asset_class', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_asset_asset_name'), 'asset', ['asset_name'], unique=True)
    op.create_index(op.f('ix_asset_asset_thesis'), 'asset', ['asset_thesis'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('asset__update',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('asset_update_title', sa.String(length=140), nullable=True),
    sa.Column('asset_update_content', sa.String(length=2000), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('asset_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['asset_id'], ['asset.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_asset__update_timestamp'), 'asset__update', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_asset__update_timestamp'), table_name='asset__update')
    op.drop_table('asset__update')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_asset_asset_thesis'), table_name='asset')
    op.drop_index(op.f('ix_asset_asset_name'), table_name='asset')
    op.drop_table('asset')
    # ### end Alembic commands ###
