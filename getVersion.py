import subprocess

def get_version() -> str:
    """
    Retourne la dernière version du projet basée sur le dernier Git tag.
    """
    try:
        result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            capture_output=True,
            text=True,
            check=True,
        )

        return result.stdout.strip()

    except subprocess.CalledProcessError as e:
        print("Erreur Git :", e.stderr)
        return "unknown"
    except FileNotFoundError:
        print("Git n'est pas installé ou n'est pas accessible.")
        return "unknown"