SELECT c.name AS "Nome do Cliente", r.rentals_date AS "Data de Locação"
FROM customers c
JOIN rentals r ON c.id = r.id_customers
WHERE r.rentals_date BETWEEN '2016-09-01' AND '2016-09-30';
