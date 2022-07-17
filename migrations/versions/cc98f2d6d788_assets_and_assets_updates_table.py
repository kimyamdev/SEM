"""assets and assets updates table

Revision ID: cc98f2d6d788
Revises: e5b15397ab8b
Create Date: 2022-07-17 13:28:48.171855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc98f2d6d788'
down_revision = 'e5b15397ab8b'
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
    op.create_table('asset__update',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('asset_update_title', sa.String(length=140), nullable=True),
    sa.Column('asset_update_content', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('asset_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['asset_id'], ['asset.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_asset__update_asset_update_content'), 'asset__update', ['asset_update_content'], unique=False)
    op.create_index(op.f('ix_asset__update_timestamp'), 'asset__update', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_asset__update_timestamp'), table_name='asset__update')
    op.drop_index(op.f('ix_asset__update_asset_update_content'), table_name='asset__update')
    op.drop_table('asset__update')
    op.drop_index(op.f('ix_asset_asset_thesis'), table_name='asset')
    op.drop_index(op.f('ix_asset_asset_name'), table_name='asset')
    op.drop_table('asset')
    # ### end Alembic commands ###