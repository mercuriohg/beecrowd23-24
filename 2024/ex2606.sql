SELECT 
    p.id AS product_id,
    p.name AS product_name
FROM 
    products p
JOIN 
    categories c ON p.id_categories = c.id
WHERE 
    c.name ILIKE 'super%';
