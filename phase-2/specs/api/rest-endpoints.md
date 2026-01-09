# REST API Endpoints Specification

## Feature Overview

**Feature**: REST API Endpoints for Task Management
**Version**: 1.0
**Date**: 2025-12-31
**Status**: Specification

## API Base Structure

### Base URL
- **Production**: `https://api.todoapp.com/v1`
- **Staging**: `https://staging-api.todoapp.com/v1`
- **Development**: `http://localhost:8000/v1`

### Authentication
All endpoints require valid JWT token in the Authorization header:
```
Authorization: Bearer {jwt_token}
```

### Content Type
All requests and responses use JSON format with appropriate content type headers:
- Request: `Content-Type: application/json`
- Response: `Content-Type: application/json`

## Endpoint Definitions

### Task Management Endpoints

#### GET /api/{user_id}/tasks
**Description**: Retrieve all tasks for the specified user

**Authentication**: Required (JWT token must match user_id or user has admin privileges)

**Parameters**:
- `user_id` (path): The ID of the user whose tasks to retrieve (required)
- `status` (query, optional): Filter tasks by status (todo, in_progress, done)
- `priority` (query, optional): Filter tasks by priority (low, medium, high)
- `limit` (query, optional): Maximum number of tasks to return (default: 50, max: 100)
- `offset` (query, optional): Number of tasks to skip for pagination (default: 0)

**Response Codes**:
- `200`: Success - Returns list of tasks
- `401`: Unauthorized - Invalid or missing JWT token
- `403`: Forbidden - User does not have permission to access these tasks
- `404`: Not Found - User ID does not exist

**Success Response (200)**:
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Sample Task",
      "description": "Task description",
      "status": "todo",
      "priority": "medium",
      "created_at": "2025-12-31T10:00:00Z",
      "updated_at": "2025-12-31T10:00:00Z"
    }
  ],
  "total_count": 1,
  "limit": 50,
  "offset": 0
}
```

#### POST /api/{user_id}/tasks
**Description**: Create a new task for the specified user

**Authentication**: Required (JWT token must match user_id)

**Parameters**:
- `user_id` (path): The ID of the user creating the task (required)

**Request Body**:
```json
{
  "title": "Task title (required, max 255 characters)",
  "description": "Task description (optional, max 1000 characters)",
  "priority": "medium (optional, default: medium, values: low, medium, high)"
}
```

**Response Codes**:
- `201`: Created - Task successfully created
- `400`: Bad Request - Invalid request body or validation errors
- `401`: Unauthorized - Invalid or missing JWT token
- `403`: Forbidden - User does not have permission to create tasks for this user_id

**Success Response (201)**:
```json
{
  "id": 1,
  "title": "Task title",
  "description": "Task description",
  "status": "todo",
  "priority": "medium",
  "user_id": 123,
  "created_at": "2025-12-31T10:00:00Z",
  "updated_at": "2025-12-31T10:00:00Z"
}
```

#### GET /api/{user_id}/tasks/{task_id}
**Description**: Retrieve a specific task for the specified user

**Authentication**: Required (JWT token must match user_id)

**Parameters**:
- `user_id` (path): The ID of the user (required)
- `task_id` (path): The ID of the task to retrieve (required)

**Response Codes**:
- `200`: Success - Returns the requested task
- `401`: Unauthorized - Invalid or missing JWT token
- `403`: Forbidden - User does not have permission to access this task
- `404`: Not Found - Task or user does not exist

**Success Response (200)**:
```json
{
  "id": 1,
  "title": "Task title",
  "description": "Task description",
  "status": "todo",
  "priority": "medium",
  "user_id": 123,
  "created_at": "2025-12-31T10:00:00Z",
  "updated_at": "2025-12-31T10:00:00Z"
}
```

#### PUT /api/{user_id}/tasks/{task_id}
**Description**: Update an existing task for the specified user

**Authentication**: Required (JWT token must match user_id)

**Parameters**:
- `user_id` (path): The ID of the user (required)
- `task_id` (path): The ID of the task to update (required)

**Request Body** (all fields optional):
```json
{
  "title": "Updated task title (optional, max 255 characters)",
  "description": "Updated task description (optional, max 1000 characters)",
  "status": "in_progress (optional, values: todo, in_progress, done)",
  "priority": "high (optional, values: low, medium, high)"
}
```

**Response Codes**:
- `200`: Success - Task successfully updated
- `400`: Bad Request - Invalid request body or validation errors
- `401`: Unauthorized - Invalid or missing JWT token
- `403`: Forbidden - User does not have permission to update this task
- `404`: Not Found - Task or user does not exist

**Success Response (200)**:
```json
{
  "id": 1,
  "title": "Updated task title",
  "description": "Updated task description",
  "status": "in_progress",
  "priority": "high",
  "user_id": 123,
  "created_at": "2025-12-31T10:00:00Z",
  "updated_at": "2025-12-31T11:00:00Z"
}
```

#### DELETE /api/{user_id}/tasks/{task_id}
**Description**: Delete a specific task for the specified user

**Authentication**: Required (JWT token must match user_id)

**Parameters**:
- `user_id` (path): The ID of the user (required)
- `task_id` (path): The ID of the task to delete (required)

**Response Codes**:
- `204`: No Content - Task successfully deleted
- `401`: Unauthorized - Invalid or missing JWT token
- `403`: Forbidden - User does not have permission to delete this task
- `404`: Not Found - Task or user does not exist

## Common Response Models

### Task Object
```json
{
  "id": 1,
  "title": "string (required, max 255 characters)",
  "description": "string (optional, max 1000 characters)",
  "status": "enum (todo, in_progress, done)",
  "priority": "enum (low, medium, high)",
  "user_id": "integer (foreign key reference)",
  "created_at": "ISO 8601 datetime string",
  "updated_at": "ISO 8601 datetime string"
}
```

### Error Response
```json
{
  "detail": "Human-readable error message",
  "error_code": "string (machine-readable error code)",
  "timestamp": "ISO 8601 datetime string"
}
```

### List Response
```json
{
  "tasks": "[Task Object array]",
  "total_count": "integer (total number of tasks matching query)",
  "limit": "integer (number of tasks returned)",
  "offset": "integer (number of tasks skipped)"
}
```

## Validation Rules

### Title Validation
- **Requirement**: Task title must be provided and not empty
- **Testable Condition**: Title length > 0 and contains non-whitespace characters
- **Error Response**: 400 Bad Request with validation error message

### Description Validation
- **Requirement**: Task description must not exceed 1000 characters
- **Testable Condition**: Description length <= 1000 characters
- **Error Response**: 400 Bad Request with validation error message

### Priority Validation
- **Requirement**: Priority must be one of: low, medium, high
- **Testable Condition**: Priority value matches allowed enum values
- **Error Response**: 400 Bad Request with validation error message

### Status Validation
- **Requirement**: Status must be one of: todo, in_progress, done
- **Testable Condition**: Status value matches allowed enum values
- **Error Response**: 400 Bad Request with validation error message

### User Ownership Validation
- **Requirement**: Users can only access tasks that belong to them
- **Testable Condition**: Request user_id matches task's user_id
- **Error Response**: 403 Forbidden when attempting to access other users' tasks

## Success Criteria

### API Reliability
- 100% of authenticated requests to valid endpoints return appropriate responses
- 99.9% uptime for API services during normal operation
- 100% of requests properly validate user ownership before operations

### Performance Measures
- 95% of API requests complete within 200ms
- 99% of API requests complete within 500ms
- Support for 1000+ concurrent API requests during peak usage

### Consistency Measures
- 100% of API responses follow documented JSON schema
- 100% of error responses include appropriate HTTP status codes
- 100% of successful task operations return complete task objects

## Assumptions

- JWT tokens are properly validated by authentication middleware
- Database operations complete within acceptable timeframes
- Network connectivity is available for API operations
- Client applications can properly handle JSON responses
- Error responses provide sufficient information for debugging

## Dependencies

- Authentication system for JWT token validation
- Database schema supporting task and user relationships
- FastAPI framework for endpoint implementation
- Proper SSL certificate configuration for secure communication
- Input validation framework for request body validation