CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
);

"OPTIONS": {
    # ...
    "timeout": 20,
    # ...
}