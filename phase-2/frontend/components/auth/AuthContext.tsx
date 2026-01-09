'use client';

import { createContext, useContext, useEffect, useState, ReactNode } from 'react';
import { authClient } from '../../lib/auth-client';

interface AuthContextType {
  user: any | null; // Better Auth user object
  session: any | null; // Better Auth session object
  isLoading: boolean;
  signIn: (email: string, password: string) => Promise<any>;
  signUp: (name: string, email: string, password: string) => Promise<any>;
  signOut: () => Promise<void>;
  refreshSession: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [user, setUser] = useState<any | null>(null);
  const [session, setSession] = useState<any | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  useEffect(() => {
    const initializeAuth = async () => {
      try {
        const sessionData = await authClient.getSession();
        if (sessionData && 'session' in sessionData && 'user' in sessionData && sessionData.session && sessionData.user) {
          setSession(sessionData.session);
          setUser(sessionData.user);
        }
      } catch (error) {
        console.error('Error initializing auth:', error);
      } finally {
        setIsLoading(false);
      }
    };

    initializeAuth();

    // Note: Better Auth client may not have onSessionChange method
    // If needed, this would be implemented differently based on the actual API
    return () => {
      // Cleanup function - currently empty
    };
  }, []);

  const signIn = async (email: string, password: string) => {
    try {
      const response = await authClient.signIn.email({
        email,
        password,
      });

      if (response && 'session' in response && response.session && 'user' in response && response.user) {
        setSession(response.session);
        setUser(response.user);
      }

      return response;
    } catch (error) {
      console.error('Sign in error:', error);
      throw error;
    }
  };

  const signUp = async (name: string, email: string, password: string) => {
    try {
      const response = await authClient.signUp.email({
        name,
        email,
        password,
      });

      if (response && 'session' in response && response.session && 'user' in response && response.user) {
        setSession(response.session);
        setUser(response.user);
      }

      return response;
    } catch (error) {
      console.error('Sign up error:', error);
      throw error;
    }
  };

  const signOut = async () => {
    try {
      await authClient.signOut();
      setSession(null);
      setUser(null);
    } catch (error) {
      console.error('Sign out error:', error);
      // Even if sign out fails, clear local state
      setSession(null);
      setUser(null);
    }
  };

  const refreshSession = async () => {
    try {
      const sessionData = await authClient.getSession();
      if (sessionData && 'session' in sessionData && 'user' in sessionData && sessionData.session && sessionData.user) {
        setSession(sessionData.session);
        setUser(sessionData.user);
      } else {
        setSession(null);
        setUser(null);
      }
    } catch (error) {
      console.error('Error refreshing session:', error);
    }
  };

  const value: AuthContextType = {
    user,
    session,
    isLoading,
    signIn,
    signUp,
    signOut,
    refreshSession,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};