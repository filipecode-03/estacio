#removendo espaços em branco

texto_com_espacos = "   Olá, Mundo!   "

texto_sem_espacos = texto_com_espacos.strip()
print(f"Texto sem espaços extras: {texto_sem_espacos}")