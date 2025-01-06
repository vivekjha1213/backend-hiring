## CURL Commands Documentation

This document provides instructions and examples for using CURL commands to interact with an API.

### Creating a Site

Use the following command to create a new site:

```bash
curl --location 'http://localhost:8000/api/sites/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Test Site",
    "domain": "https://test.com",
    "url": "https://test.com",
    "description": "Test site description",
    "record_capicity": 1
}'
```

#### Parameters:
- **name**: Name of the site (e.g., "Test Site").
- **domain**: The domain of the site (e.g., "https://test.com").
- **url**: URL of the site (e.g., "https://test.com").
- **description**: A brief description of the site (e.g., "Test site description").
- **record_capicity**: Record capacity of the site (integer).

### Executing a Task on a Site

Use the following command to execute a task for a specific site. Replace `1` in the URL with the ID of the site:

```bash
curl --location 'http://localhost:8000/api/sites/1/execute_task/' \
--header 'Content-Type: application/json' \
--data '{
    "job_type": 2
}'
```

#### Parameters:
- **job_type**: The type of job to execute (integer).

### Retrieving All Sites

To retrieve a list of all sites, use the following command:

```bash
curl --location 'http://localhost:8000/api/sites/'
```

#### Response:
The response will contain details of all sites available in the system.

### Notes:
- Ensure the API server is running on `http://localhost:8000`.

