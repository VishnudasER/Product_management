# Product Management API

This RESTful API allows you to manage a simple product inventory system.

## Tech Stack
- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Docker

## Setup

```bash
git clone https://github.com/yourusername/product-api
cd product-api
docker-compose up --build
```

## Endpoints

| Method | Endpoint                | Description          |
|--------|-------------------------|----------------------|
| GET    | /api/products/          | List all products    |
| POST   | /api/products/          | Create a new product |
| GET    | /api/products/<id>      | Get a single product |
| PUT    | /api/products/<id>      | Update a product     |
| DELETE | /api/products/<id>      | Delete a product     |

## Sample Product Payload

```json
{
  "name": "Laptop",
  "description": "Gaming laptop",
  "price": 1500.00,
  "quantity": 5
}
```

## Error Handling

Returns:
- `404 Not Found` if product does not exist
- `400 Bad Request` for validation errors

## License

MIT
#   P r o d u c t _ m a n a g e m e n t  
 #   P r o d u c t _ m a n a g e m e n t  
 