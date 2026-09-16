async def get_or_create_user(pool, user_id: int) -> dict:
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

async def count_user_tamagotchis(pool, user_id: int) -> int:
    """Compte le nombre de tamagotchis possédés par un utilisateur."""
    async with pool.acquire() as conn:
        # fetchval est utilisé au lieu de fetchrow car on attend une seule valeur (le compteur)
        count = await conn.fetchval(
            'SELECT COUNT(*) FROM tamagotchis WHERE user_id = $1', 
            user_id
        )
        # On retourne le compte, ou 0 si la requête ne renvoie rien
        return count or 0


async def update_tamagotchi_stats(pool, tamagotchi_id: int, energy_change: int, fun_change: int):
    """Met à jour l'énergie et le fun d'un tamagotchi spécifique, en respectant les limites (0-max)."""
    async with pool.acquire() as conn:
        await conn.execute('''
            UPDATE tamagotchis 
            SET current_energy = GREATEST(0, LEAST(max_energy, current_energy + $2)),
                current_fun = GREATEST(0, LEAST(max_fun, current_fun + $3))
            WHERE id = $1
        ''', tamagotchi_id, energy_change, fun_change)

async def get_user_money(pool, userid: int) -> float:
    """Retourne l'argent dans le compte en banque de l'utilisateur, identifié par son id"""
    async with pool.acquire() as conn:
        money = await conn.fetchval('SELECT money FROM users WHERE id=$1', userid)
        return money or 0

# === Valeurs par défaut de l'admin shop
async def get_base_price_to_buy_tamagotchi(pool) -> float:
    """Retourne le prix par défaut d'un tamagotchi"""
    async with pool.acquire() as conn:
        amount = await conn.fetchval('SELECT tamagotchi_base_price FROM admin_shop_pricings WHERE id=1')
        return amount or 0

async def create_admin_shop(pool):
    """Récupère les informations de l'admin shop, ou alors on le créer"""
    async with pool.acquire() as conn:
        shop = await conn.fetchrow('SELECT * FROM admin_shop_pricings WHERE id = 1')
        if not shop:
            await conn.execute('INSERT INTO admin_shop_pricings (id, tamagotchi_base_price, tamagotchi_skin_base_price) VALUES (1, 500.0,100.0)')