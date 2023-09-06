
# Shipment Tracker App

A simple Django based application that allows searching through sample shipment data using tracking_number and carrier designations and returns a payload containing shipment information and current weather information at the receiver's location.

## Installation

After cloning the project from its git repo, go through the simple steps below to install the application.

Use pip to install virtualenv if you don't already have it installed: 

```bash
  pip install virtualenv
```
Go to the project directory and create a virtual environment folder:

```bash
  virtualenv env
```

Activate your virtual environment:

```bash
  source env/bin/activate
```

Install all requirements using `requirements.txt`:

```bash
  pip install -r requirements.txt
```

Run the project locally using Django's internal server:

```bash
  python manage.py runserver 0:8000
```

You can use any port or local IP address you are comfortable with.
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

Please note that you can combine the two query parameters. Such that:

```http
  GET /api/v1/shipment/track/?carrier=carrier-name&tracking_number=tracking-number
```

## Running Tests

This project includes a number of unit and component tests.

To run these tests run the commands below after going throught the installation process: 

```bash
  python manage.py tests
```
