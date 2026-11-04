CREATE TABLE IF NOT EXISTS food_groups (
    id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name            TEXT            UNIQUE NOT NULL
);