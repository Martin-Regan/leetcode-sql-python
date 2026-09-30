# Write your MySQL query statement below
WITH running_total AS (
    SELECT
        person_name,
        sum(weight) OVER (ORDER BY turn) as total_weight,
        turn
        FROM queue
)
SELECT
    person_name
    FROM running_total
    WHERE total_weight <=1000
    ORDER BY turn DESC
    LIMIT 1;
