# CafeApp API

## Summary

RESTful API to manage Avo's data

## Usage

### Format

```json
{
    "message": "Extra description of what is going on",
    "data": "Mixed typed content of the response"
}
```

### Requests

- `GET /food?day=<int:day>`

###### `Future` - Other data might be needed

**Response**

 - `200 OK`
 
```json
{
    "message": "There is or isn't a menu today",
    "data": 
    [
        {"title": "breakfast", "data": ["List of foods in breakfast menu", "[] if no food"]},
        {"title": "lunch", "data": ["List of foods in lunch menu", "[] if no food"]},
        {"title": "dinner", "data": ["List of foods in dinner menu", "[] if no food"]}
    ]
}
```

