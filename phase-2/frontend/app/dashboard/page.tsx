'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { authClient } from '../../lib/auth-client';
import { taskAPI } from '../../lib/api';
import CreateTaskForm from '../../components/CreateTaskForm';
import TaskCard from '../../components/TaskCard';

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

export default function DashboardPage() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [user, setUser] = useState<any>(null);
  const router = useRouter();

  useEffect(() => {
    const checkAuthAndLoadData = async () => {
      try {
        // Check if user is authenticated
        const sessionResponse = await authClient.getSession();
        if (!sessionResponse || !('user' in sessionResponse) || !sessionResponse.user) {
          // Redirect to login if not authenticated
          router.push('/login');
          return;
        }

        setUser(sessionResponse.user);

        // Load tasks
        const userTasks = await taskAPI.getTasks();
        setTasks(userTasks);
      } catch (error) {
        console.error('Error checking auth or loading data:', error);
        router.push('/login');
      } finally {
        setLoading(false);
      }
    };

    checkAuthAndLoadData();
  }, [router]);

  const handleTaskCreated = async (newTask: Task) => {
    // Add the new task to the list
    setTasks(prev => [newTask, ...prev]);
  };

  const handleTaskDeleted = async (taskId: string) => {
    try {
      await taskAPI.deleteTask(taskId);
      // Remove the task from the list
      setTasks(prev => prev.filter(task => task.id !== taskId));
    } catch (error) {
      console.error('Error deleting task:', error);
    }
  };

  const handleTaskCompleted = async (taskId: string) => {
    try {
      const updatedTask = await taskAPI.completeTask(taskId);
      // Update the task in the list
      setTasks(prev =>
        prev.map(task =>
          task.id === taskId ? updatedTask : task
        )
      );
    } catch (error) {
      console.error('Error completing task:', error);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-xl">Loading...</div>
      </div>
    );
  }

  if (!user) {
    return null; // Will be redirected by useEffect
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-4xl mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">
          Hello, {user.name || user.email}
        </h1>

        <div className="bg-white rounded-lg shadow-md p-6 mb-8">
          <h2 className="text-xl font-semibold text-gray-800 mb-4">Add New Task</h2>
          <CreateTaskForm onTaskCreated={handleTaskCreated} />
        </div>

        <div className="bg-white rounded-lg shadow-md p-6">
          <h2 className="text-xl font-semibold text-gray-800 mb-4">Your Tasks ({tasks.length})</h2>

          {tasks.length === 0 ? (
            <p className="text-gray-500 italic">No tasks yet. Add your first task above!</p>
          ) : (
            <div className="space-y-4">
              {tasks.map((task) => (
                <TaskCard
                  key={task.id}
                  task={task}
                  onDelete={() => handleTaskDeleted(task.id)}
                  onComplete={() => handleTaskCompleted(task.id)}
                />
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}