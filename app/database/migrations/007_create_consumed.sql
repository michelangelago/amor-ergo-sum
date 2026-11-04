CREATE TABLE IF NOT EXISTS consumed (
    id              INTEGER          GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    food_id         INTEGER          REFERENCES foods(id),
    daily_id        INTEGER          REFERENCES daily(id),
    time            TIMESTAMPTZ       NOT NULL DEFAULT NOW()
);