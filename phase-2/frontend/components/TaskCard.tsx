import React from 'react';
import Button from './ui/Button';

interface Task {
  id: string;
  title: string;
  description: string;
  status: 'todo' | 'in_progress' | 'done';
  priority: 'low' | 'medium' | 'high';
  user_id: string;
  created_at: string;
  updated_at: string;
}

interface TaskCardProps {
  task: Task;
  onDelete: () => void;
  onComplete: () => void;
}

const TaskCard: React.FC<TaskCardProps> = ({ task, onDelete, onComplete }) => {
  // Function to get priority color
  const getPriorityColor = (priority: string) => {
    switch (priority) {
      case 'high':
        return 'bg-red-100 text-red-800';
      case 'medium':
        return 'bg-yellow-100 text-yellow-800';
      case 'low':
        return 'bg-green-100 text-green-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  // Function to get status color
  const getStatusColor = (status: string) => {
    switch (status) {
      case 'done':
        return 'bg-green-100 text-green-800';
      case 'in_progress':
        return 'bg-blue-100 text-blue-800';
      case 'todo':
        return 'bg-gray-100 text-gray-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
      <div className="flex justify-between items-start">
        <div className="flex-1">
          <h3 className="font-semibold text-lg text-gray-900">{task.title}</h3>
          <p className="text-gray-600 mt-1">{task.description}</p>

          <div className="flex gap-2 mt-3">
            <span className={`px-2 py-1 rounded-full text-xs font-medium ${getPriorityColor(task.priority)}`}>
              {task.priority.charAt(0).toUpperCase() + task.priority.slice(1)} Priority
            </span>
            <span className={`px-2 py-1 rounded-full text-xs font-medium ${getStatusColor(task.status)}`}>
              {task.status.replace('_', ' ').charAt(0).toUpperCase() + task.status.slice(1).replace('_', ' ')}
            </span>
          </div>

          <div className="text-xs text-gray-500 mt-2">
            Created: {new Date(task.created_at).toLocaleDateString()}
          </div>
        </div>

        <div className="flex flex-col gap-2 ml-4">
          <Button
            onClick={onComplete}
            variant={task.status === 'done' ? 'secondary' : 'primary'}
            size="sm"
            disabled={task.status === 'done'}
          >
            {task.status === 'done' ? 'Completed' : 'Complete'}
          </Button>
          <Button
            onClick={onDelete}
            variant="secondary"
            size="sm"
          >
            Delete
          </Button>
        </div>
      </div>
    </div>
  );
};

export default TaskCard;