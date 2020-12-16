"""empty message

Revision ID: e771a9031e76
Revises: 
Create Date: 2020-12-16 22:57:30.519926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e771a9031e76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roomName', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teamName', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('teamName')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('fullname', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=64), nullable=False),
    sa.Column('teamId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['teamId'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('meeting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('teamId', sa.Integer(), nullable=True),
    sa.Column('roomId', sa.Integer(), nullable=False),
    sa.Column('bookerId', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('startTime', sa.Integer(), nullable=False),
    sa.Column('endTime', sa.Integer(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bookerId'], ['user.id'], ),
    sa.ForeignKeyConstraint(['roomId'], ['room.id'], ),
    sa.ForeignKeyConstraint(['teamId'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('participants_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('meeting', sa.String(length=64), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['meeting'], ['meeting.title'], ),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('participants_user')
    op.drop_table('meeting')
    op.drop_table('user')
    op.drop_table('team')
    op.drop_table('room')
    # ### end Alembic commands ###
