# v0.1.2
# { "Depends": "py-genlayer:latest" }

# CleanStorage
# Minimal GenLayer contract demonstrating persistent storage,
# read/write methods, and full consensus execution.

from genlayer import *


class CleanStorage(gl.Contract):
    value: str

    def __init__(self, initial_value: str):
        self.value = initial_value

    @gl.public.view
    def get(self) -> str:
        return self.value

    @gl.public.write
    def set(self, new_value: str) -> None:
        self.value = new_value
