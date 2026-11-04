CREATE TABLE IF NOT EXISTS diet_foods (
    id              INTEGER         GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    diet_id         INTEGER         REFERENCES diets(id),
    food_id         INTEGER         REFERENCES foods(id),
    quantity        INTEGER         NOT NULL
);