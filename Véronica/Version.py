def version()->str:
    """Retourne la version actuelle du bot. Cette fonction retourne juste le contenu du fichier Version.txt"""
    import os
    current_dir = os.path.abspath(os.path.dirname(__file__))
    output_full_path = os.path.join(current_dir, "Version.txt")
    file = open(output_full_path,'r')
    for x in file:
        result=x
    file.close()
    return result