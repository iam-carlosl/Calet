"""Miniframework de GUI 'Calet', basado en Flet
   - Módulo de errores"""

class ClError(Exception):

    def __init__(self, error:str):
        super().__init__()
        self.error = error