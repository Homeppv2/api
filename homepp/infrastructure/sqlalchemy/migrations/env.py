from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

from homepp.core.user.domain.models import Base

config = context.config

config.set_main_option('sqlalchemy.url', 'sqlite:///test')

target_metadata = Base.metadata

def run_migrations_offline():
    """
    Run migrations in 'offline' mode.
    """
    url = config.get_main_option('sqlalchemy.url')
    context.configure(url=url)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """
    Run migrations in 'online' mode.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()