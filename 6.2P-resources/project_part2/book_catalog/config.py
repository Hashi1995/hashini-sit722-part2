import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://book_catalog_xheb_user:4ZSG0aGSFwZw9ZmNQvMPQxkb10iztHGD@dpg-crhb3ng8fa8c738v3pvg-a.singapore-postgres.render.com/book_catalog_xheb")

settings = Settings()
