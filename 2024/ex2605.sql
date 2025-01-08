SELECT products.name AS name_products, providers.name AS name_providers
FROM products
JOIN providers ON products.id_providers = providers.id
WHERE products.id_categories = 6;
