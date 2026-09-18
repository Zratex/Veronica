import asyncpg
import os

from cogs.tamagotchi.db_tamagotchi import create_admin_shop

async def create_db_pool():
    """Crée le pool de connexion à la base de données PostgreSQL."""
    return await asyncpg.create_pool(
        user=os.environ.get("POSTGRES_USER", "postgres"),
        password=os.environ.get("POSTGRES_PASSWORD", "password"),
        database=os.environ.get("POSTGRES_DB", "veronica"),
        host=os.environ.get("POSTGRES_HOST", "db") # 'db' correspond au nom du service dans docker-compose
    )

async def init_db(pool):
    """Initialise les tables si elles n'existent pas."""
    async with pool.acquire() as conn:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id BIGINT PRIMARY KEY,
                money DOUBLE PRECISION DEFAULT 0.0
            );

            CREATE TABLE IF NOT EXISTS tamagotchis (
                id SERIAL PRIMARY KEY,
                user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
                name VARCHAR(255) NOT NULL,
                age VARCHAR(255) DEFAULT 0,
                max_energy INT DEFAULT 100,
                current_energy INT DEFAULT 100,
                max_fun INT DEFAULT 100,
                current_fun INT DEFAULT 100
            );

            CREATE TABLE IF NOT EXISTS admin_shop_pricings (
                id SERIAL PRIMARY KEY,
                tamagotchi_base_price DOUBLE PRECISION DEFAULT 500.0,
                tamagotchi_skin_base_price DOUBLE PRECISION DEFAULT 100.0
            );
        ''')

        await create_admin_shop(pool=pool)