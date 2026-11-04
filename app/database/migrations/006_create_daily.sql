CREATE TABLE IF NOT EXISTS daily (
    id              INTEGER          GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    energy          NUMERIC(10, 1)   NOT NULL,
    fat             NUMERIC(10, 1)   NOT NULL,
    saturates       NUMERIC(10, 1)   NOT NULL,
    carbohydrate    NUMERIC(10, 1)   NOT NULL,
    sugars          NUMERIC(10, 1)   NOT NULL,
    protein         NUMERIC(10, 1)   NOT NULL,
    salt            NUMERIC(10, 1)   NOT NULL,
    date            DATE             NOT NULL DEFAULT NOW()
);