CREATE TABLE IF NOT EXISTS diets (
    id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name            TEXT            UNIQUE,
    description     TEXT,
    created_on      TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    user_id         INTEGER         REFERENCES users(id)
);