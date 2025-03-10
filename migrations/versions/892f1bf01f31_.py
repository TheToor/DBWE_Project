"""empty message

Revision ID: 892f1bf01f31
Revises: e40317739856
Create Date: 2025-03-03 13:12:36.292197

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '892f1bf01f31'
down_revision = 'e40317739856'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('school_rating', schema=None) as batch_op:
        batch_op.alter_column('rating',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Float(),
               existing_nullable=True)

    with op.batch_alter_table('teacher_rating', schema=None) as batch_op:
        batch_op.alter_column('rating',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Float(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('teacher_rating', schema=None) as batch_op:
        batch_op.alter_column('rating',
               existing_type=sa.Float(),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=True)

    with op.batch_alter_table('school_rating', schema=None) as batch_op:
        batch_op.alter_column('rating',
               existing_type=sa.Float(),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=True)

    # ### end Alembic commands ###
