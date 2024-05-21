"""

Revision ID: 0a2d56b333d5
Revises: 8444bf1b90aa
Create Date: 2024-05-20 23:05:33.427333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a2d56b333d5'
down_revision = '8444bf1b90aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('phase', sa.Column('feedback_send', sa.Boolean(), nullable=False), schema='portal')
    op.sync_enum_values('portal', 'candidatestatus', ['first_communication', 'waiting_tech_stage', 'failed_tech_stage', 'success_tech_stage', 'waiting_final_stage', 'failed_final_stage', 'success_final_stage', 'waiting_offer', 'declined_offer', 'accepted_offer'],
                        [('candidate', 'status')],
                        enum_values_to_rename=[])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.sync_enum_values('portal', 'candidatestatus', ['first_communication', 'waiting_tech_stage', 'failed_tech_stage', 'success_tech_stage', 'waiting_final_stage', 'failed_final_stage', 'waiting_offer', 'declined_offer', 'accepted_offer'],
                        [('candidate', 'status')],
                        enum_values_to_rename=[])
    op.drop_column('phase', 'feedback_send', schema='portal')
    # ### end Alembic commands ###