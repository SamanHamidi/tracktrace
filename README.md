
## API Reference

Please note that an auto-generated OpenAPI document can be accessed by calling this address:

#### Show OpenAPI documentations

```http
  GET /openapi
```

#### get all existing shipment items

```http
  GET /api/v1/shipment/track/
```

No extra parameters are required. The API does not require authentication. 

#### Get item by carrier name

```http
  GET /api/v1/shipment/track/?carrier=carrier-name
```

| Query Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `carrier`      | `string` | **Required**. name of carrier     |

#### Get item by tracking number name

```http
  GET /api/v1/shipment/track/?tracking_number=tracking-number
```

| Query Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `tracking_number`      | `string` | **Required**. tracking number ID     |
