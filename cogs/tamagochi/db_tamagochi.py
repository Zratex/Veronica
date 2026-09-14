async def get_or_create_user(pool, user_id: int):
    """Récupère un utilisateur ou le crée s'il n'existe pas."""
    async with pool.acquire() as conn:
        user = await conn.fetchrow('SELECT * FROM users WHERE id = $1', user_id)
        if not user:
            await conn.execute('INSERT INTO users (id, money) VALUES ($1, 500.0)', user_id)
            user = await conn.fetchrow('SELECT * FROM users WHERE id = $1', user_id)
        return dict(user)

async def update_money(pool, user_id: int, amount: float):
    """Ajoute ou retire de l'argent (amount peut être négatif)."""
    await get_or_create_user(pool, user_id)
    async with pool.acquire() as conn:
        await conn.execute('UPDATE users SET money = money + $2 WHERE id = $1', user_id, amount)

async def create_tamagotchi(pool, user_id: int, name: str):
    """Crée un nouveau Tamagotchi lié à un utilisateur."""
    await get_or_create_user(pool, user_id)
    async with pool.acquire() as conn:
        await conn.execute(
            'INSERT INTO tamagotchis (user_id, name) VALUES ($1, $2)',
            user_id, name
        )

async def get_user_tamagotchis(pool, user_id: int):
    """Récupère tous les tamagotchis d'un joueur."""
    async with pool.acquire() as conn:
        records = await conn.fetch('SELECT * FROM tamagotchis WHERE user_id = $1', user_id)
        return [dict(record) for record in records]

async def update_tamagotchi_stats(pool, tamagotchi_id: int, energy_change: int, fun_change: int):
    """Met à jour l'énergie et le fun d'un tamagotchi spécifique, en respectant les limites (0-max)."""
    async with pool.acquire() as conn:
        await conn.execute('''
            UPDATE tamagotchis 
            SET current_energy = GREATEST(0, LEAST(max_energy, current_energy + $2)),
                current_fun = GREATEST(0, LEAST(max_fun, current_fun + $3))
            WHERE id = $1
        ''', tamagotchi_id, energy_change, fun_change)