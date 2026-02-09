# ADR-001: Enhanced Task Model with ENUM Types and Advanced API Features

## Status
Accepted

## Context
For the Hackathon II submission, we needed to upgrade our basic Todo application to include intermediate-level features. The original Task model had simple boolean status and limited filtering capabilities. We needed to enhance the model and API to support richer functionality including ENUM-based status and priority, due dates, descriptions, and advanced filtering/sorting.

## Decision
We decided to:

1. **Change Task Status from Boolean to ENUM**: Replace the simple boolean status with a three-state ENUM ('todo', 'in_progress', 'done') to provide more granular task tracking.

2. **Add Priority ENUM**: Implement a priority ENUM ('low', 'medium', 'high') to allow users to categorize task importance.

3. **Include Due Date and Description**: Add nullable TIMESTAMP for due_date and TEXT field for description to enhance task detail.

4. **Implement Advanced API Filtering**: Add query parameters for search, status filtering, priority filtering, and dynamic sorting capabilities.

5. **Update Migration Strategy**: Modify Alembic migrations to handle the creation of ENUM types and column additions.

## Alternatives Considered

### Alternative 1: Text-based Status Fields
Instead of ENUMs, we could have used TEXT fields with validation at the application level. However, ENUMs provide better database-level integrity and performance benefits.

### Alternative 2: Separate Status Table
We could have created a separate status table with foreign key relationships. This would have added complexity without significant benefits for a simple enum-like structure.

### Alternative 3: JSON Field for Extended Properties
Using a JSON field to store extended properties like priority and due date. This would have reduced query performance and made sorting/filtering more complex.

## Consequences

### Positive
- Improved data integrity through database-level ENUM constraints
- Better performance for filtering and sorting operations
- Clearer semantic meaning for task states and priorities
- Enhanced API capabilities for rich client experiences
- Better user experience with more granular task management

### Negative
- More complex database migrations to handle ENUM creation
- Potential challenges with ENUM modification in the future
- Slightly increased database schema complexity

## Implementation Notes
- Alembic migrations must properly handle ENUM type creation
- Frontend forms need to provide appropriate controls (dropdowns) for ENUM fields
- API endpoints need robust query parameter validation
- Consider internationalization for ENUM values in future iterations

## Links
- Related to: Phase 2 Full Stack Todo App Specification
- Implements: Hackathon II intermediate level requirements