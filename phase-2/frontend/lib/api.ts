// API Client for Todo Application
// Handles communication with the backend API

import { authClient } from './auth-client';

const BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface ApiOptions extends RequestInit {
  token?: string;
}

class ApiClient {
  private baseUrl: string;

  constructor() {
    this.baseUrl = BASE_URL;
  }

  private async request<T>(endpoint: string, options: ApiOptions = {}): Promise<T> {
    const { token, headers, ...restOptions } = options;

    const url = `${this.baseUrl}${endpoint}`;

    const requestHeaders: Record<string, string> = {
      'Content-Type': 'application/json',
    };

    // Add any provided headers
    if (headers) {
      Object.entries(headers).forEach(([key, value]) => {
        if (typeof value === 'string') {
          requestHeaders[key] = value;
        }
      });
    }

    // Add authorization header if token is provided
    if (token) {
      requestHeaders['Authorization'] = `Bearer ${token}`;
    } else {
      // Try to get the session from Better Auth
      try {
        // Use a dynamic import to avoid server-side issues
        const session = await authClient.getSession();
        if (session && typeof session === 'object' && 'session' in session && session.session && typeof session.session === 'object' && 'token' in session.session) {
          requestHeaders['Authorization'] = `Bearer ${(session.session as any).token}`;
        }
      } catch (error) {
        console.warn('Could not get session for API request:', error);
        // If session is not available, continue without auth header
      }
    }

    const response = await fetch(url, {
      headers: requestHeaders,
      ...restOptions,
    });

    if (!response.ok) {
      // Check if it's an authentication error
      if (response.status === 401) {
        // Session might be expired, try to refresh or redirect to login
        console.warn('Authentication failed, redirecting to login');
        // In a real app, we might redirect to login page here
      }
      throw new Error(`API request failed: ${response.status} ${response.statusText}`);
    }

    // Handle responses that might not have JSON content
    const contentType = response.headers.get('content-type');
    if (contentType && contentType.includes('application/json')) {
      return await response.json();
    } else {
      // For responses without JSON content (like DELETE operations)
      return response.text() as unknown as T;
    }
  }

  // Generic GET request
  async get<T>(endpoint: string, options: ApiOptions = {}): Promise<T> {
    return this.request<T>(endpoint, { ...options, method: 'GET' });
  }

  // Generic POST request
  async post<T, D = any>(endpoint: string, data?: D, options: ApiOptions = {}): Promise<T> {
    return this.request<T>(endpoint, {
      ...options,
      method: 'POST',
      body: data ? JSON.stringify(data) : undefined,
    });
  }

  // Generic PUT request
  async put<T, D = any>(endpoint: string, data?: D, options: ApiOptions = {}): Promise<T> {
    return this.request<T>(endpoint, {
      ...options,
      method: 'PUT',
      body: data ? JSON.stringify(data) : undefined,
    });
  }

  // Generic DELETE request
  async delete<T>(endpoint: string, options: ApiOptions = {}): Promise<T> {
    return this.request<T>(endpoint, { ...options, method: 'DELETE' });
  }
}

// Task-related API methods
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

interface CreateTaskData {
  title: string;
  description: string;
  priority: 'low' | 'medium' | 'high';
}

class TaskAPI {
  // Get all tasks for the current user
  async getTasks(): Promise<Task[]> {
    try {
      // Get user ID from session
      const session = await authClient.getSession();
      if (!session || typeof session !== 'object' || !('user' in session) || !(session as any).user?.id) {
        throw new Error('User not authenticated');
      }
      const userId = (session as any).user.id;
      return await apiClient.get<Task[]>(`/api/${userId}/tasks`);
    } catch (error) {
      console.error('Error fetching tasks:', error);
      throw error;
    }
  }

  // Create a new task
  async createTask(data: CreateTaskData): Promise<Task> {
    try {
      // Get user ID from session
      const session = await authClient.getSession();
      if (!session || typeof session !== 'object' || !('user' in session) || !(session as any).user?.id) {
        throw new Error('User not authenticated');
      }
      const userId = (session as any).user.id;
      return await apiClient.post<Task, CreateTaskData>(`/api/${userId}/tasks`, data);
    } catch (error) {
      console.error('Error creating task:', error);
      throw error;
    }
  }

  // Update a task
  async updateTask(taskId: string, data: Partial<CreateTaskData> & { status?: 'todo' | 'in_progress' | 'done' }): Promise<Task> {
    try {
      // Get user ID from session
      const session = await authClient.getSession();
      if (!session || typeof session !== 'object' || !('user' in session) || !(session as any).user?.id) {
        throw new Error('User not authenticated');
      }
      const userId = (session as any).user.id;
      return await apiClient.put<Task, Partial<CreateTaskData>>(`/api/${userId}/tasks/${taskId}`, data);
    } catch (error) {
      console.error('Error updating task:', error);
      throw error;
    }
  }

  // Delete a task
  async deleteTask(taskId: string): Promise<void> {
    try {
      // Get user ID from session
      const session = await authClient.getSession();
      if (!session || typeof session !== 'object' || !('user' in session) || !(session as any).user?.id) {
        throw new Error('User not authenticated');
      }
      const userId = (session as any).user.id;
      await apiClient.delete<void>(`/api/${userId}/tasks/${taskId}`);
    } catch (error) {
      console.error('Error deleting task:', error);
      throw error;
    }
  }

  // Complete a task
  async completeTask(taskId: string): Promise<Task> {
    return this.updateTask(taskId, { status: 'done' });
  }
}

// Create and export a singleton instance
export const apiClient = new ApiClient();

// Export the class in case someone wants to create their own instance
export default ApiClient;

// Export task-specific API methods
export const taskAPI = new TaskAPI();