# Database Schema Specification

## Feature Overview

**Feature**: Database Schema for User and Task Management
**Version**: 1.0
**Date**: 2025-12-31
**Status**: Specification

## Database Technology

The application will use SQLModel for database schema definition and ORM operations. The database will support user authentication (managed by Better Auth) and task management with proper relationships between users and their tasks.

## Entity Definitions

### User Table
**Managed by**: Better Auth (external system)
**Purpose**: Store user account information for authentication

**Fields** (as managed by Better Auth):
- `id` (Primary Key): Unique identifier for the user
- `email`: User's email address for login
- `created_at`: Timestamp when the account was created
- `updated_at`: Timestamp when the account was last updated
- Additional fields as required by Better Auth

**Constraints**:
- Email must be unique across all users
- Email must follow valid email format
- User ID must be unique and non-null

### Task Table
**Managed by**: Application (using SQLModel)
**Purpose**: Store task information linked to specific users

**Fields**:
- `id` (Primary Key): Auto-incrementing unique identifier for the task
- `title` (String, max 255, not null): Title of the task
- `description` (Text, optional): Detailed description of the task (max 1000 characters)
- `status` (Enum, not null): Current status of the task (todo, in_progress, done)
- `priority` (Enum, not null): Priority level of the task (low, medium, high)
- `user_id` (Integer, not null, foreign key): Reference to the user who owns the task
- `created_at` (Timestamp, not null): When the task was created
- `updated_at` (Timestamp, not null): When the task was last modified

**Constraints**:
- Title must not be empty or consist only of whitespace
- Status must be one of the allowed enum values (todo, in_progress, done)
- Priority must be one of the allowed enum values (low, medium, high)
- user_id must reference a valid user in the Better Auth system
- All tasks must be associated with a valid user

## Table Relationships

### User-Task Relationship
- **Relationship Type**: One-to-Many (One user can have many tasks)
- **Foreign Key**: Task table's `user_id` references User table's `id`
- **Cardinality**: 1 User : N Tasks
- **Constraint**: Cascade delete not enabled to preserve data integrity

### Referential Integrity
- **On Update**: CASCADE - If user ID changes (rare), update all related task records
- **On Delete**: RESTRICT - Prevent deletion of users who have tasks (application logic handles this)
- **Indexing**: Foreign key field (user_id) should be indexed for performance

## Database Schema Requirements

### User Table Requirements
- **Requirement**: User table is managed by Better Auth external system
- **Testable Condition**: User authentication and account management handled by Better Auth
- **User Impact**: Consistent, secure user management with industry-standard practices

### Task Table Requirements
- **Requirement**: Task table must have foreign key relationship to user table
- **Testable Condition**: Every task record has a valid user_id that references an existing user
- **User Impact**: Ensures proper data isolation between users

### Data Validation Requirements
- **Requirement**: All task fields must be properly validated at the database level
- **Testable Condition**: Database constraints prevent invalid data from being stored
- **User Impact**: Maintains data integrity and consistency across the application

### Indexing Requirements
- **Requirement**: Proper indexes must be created for performance optimization
- **Testable Condition**: Query performance meets response time requirements
- **User Impact**: Fast access to user's tasks and efficient filtering operations

## Field Specifications

### Task.title
- **Data Type**: String (VARCHAR)
- **Length**: Maximum 255 characters
- **Nullability**: Not null
- **Validation**: Must contain at least one non-whitespace character
- **Index**: Consider adding for search functionality

### Task.description
- **Data Type**: Text
- **Length**: Maximum 1000 characters
- **Nullability**: Nullable (optional field)
- **Default**: NULL

### Task.status
- **Data Type**: Enum
- **Allowed Values**: 'todo', 'in_progress', 'done'
- **Nullability**: Not null
- **Default**: 'todo'

### Task.priority
- **Data Type**: Enum
- **Allowed Values**: 'low', 'medium', 'high'
- **Nullability**: Not null
- **Default**: 'medium'

### Task.user_id
- **Data Type**: Integer
- **Nullability**: Not null
- **Foreign Key**: References User.id (when integrated with Better Auth)
- **Index**: Required for performance

### Task.created_at
- **Data Type**: Timestamp
- **Nullability**: Not null
- **Default**: Current timestamp at creation

### Task.updated_at
- **Data Type**: Timestamp
- **Nullability**: Not null
- **Default**: Current timestamp at creation, updated automatically on modification

## Success Criteria

### Data Integrity Outcomes
- 100% of task records have valid user_id references
- 0% of task records have empty or whitespace-only titles
- 100% of task records have valid enum values for status and priority
- 0% of orphaned task records exist without valid user references

### Performance Measures
- Task retrieval queries complete within 100ms for up to 1000 tasks per user
- Task creation operations complete within 50ms
- Task update operations complete within 50ms
- Database supports 1000+ concurrent connections during peak usage

### Scalability Measures
- Schema supports 1,000,000+ task records efficiently
- Proper indexing enables fast filtering and sorting operations
- Foreign key relationships maintain data integrity at scale

## Assumptions

- Better Auth provides reliable user management and ID system
- SQLModel properly integrates with the chosen database engine
- Database engine supports foreign key constraints and referential integrity
- Indexing strategies will be optimized based on usage patterns
- Database backup and recovery procedures are in place

## Dependencies

- Better Auth system for user account management
- SQLModel ORM framework for schema definition
- Database engine supporting foreign key relationships
- Application logic for handling user-task associations
- Migration framework for schema versioning and updates

## Security Considerations

### Data Isolation
- **Requirement**: Users can only access tasks linked to their user_id
- **Testable Condition**: Database queries always filter by user_id
- **User Impact**: Ensures privacy and prevents unauthorized data access

### Access Control
- **Requirement**: Database-level constraints support application-level access controls
- **Testable Condition**: Invalid user-task combinations are prevented at database level
- **User Impact**: Additional security layer beyond application logic