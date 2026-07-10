SELECT c.customer_id,
       c.customer_name
FROM Customers c
WHERE c.customer_id IN (

    SELECT customer_id
    FROM Orders
    WHERE product_name = 'A'

    INTERSECT

    SELECT customer_id
    FROM Orders
    WHERE product_name = 'B'

    EXCEPT

    SELECT customer_id
    FROM Orders
    WHERE product_name = 'C'

)
ORDER BY c.customer_name;