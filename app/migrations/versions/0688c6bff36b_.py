"""empty message

Revision ID: 0688c6bff36b
Revises: fa3d06bd79d0
Create Date: 2021-06-08 22:58:34.286028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0688c6bff36b'
down_revision = 'fa3d06bd79d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_account', 'public_id',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.drop_constraint('user_notification_feed_to_user_id_fkey', 'user_notification_feed', type_='foreignkey')
    op.drop_constraint('user_notification_feed_from_user_id_fkey', 'user_notification_feed', type_='foreignkey')
    op.create_foreign_key(None, 'user_notification_feed', 'user_account', ['to_user_id'], ['public_id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'user_notification_feed', 'user_account', ['from_user_id'], ['public_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_notification_feed', type_='foreignkey')
    op.drop_constraint(None, 'user_notification_feed', type_='foreignkey')
    op.create_foreign_key('user_notification_feed_from_user_id_fkey', 'user_notification_feed', 'user_account', ['from_user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('user_notification_feed_to_user_id_fkey', 'user_notification_feed', 'user_account', ['to_user_id'], ['id'], ondelete='CASCADE')
    op.alter_column('user_account', 'public_id',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    # ### end Alembic commands ###
