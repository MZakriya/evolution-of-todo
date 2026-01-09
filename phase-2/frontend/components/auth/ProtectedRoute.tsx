'use client';

import { ReactNode } from 'react';
import { useRouter, usePathname } from 'next/navigation';
import { useAuth } from './AuthContext';

interface ProtectedRouteProps {
  children: ReactNode;
  fallback?: ReactNode; // Component to show while checking authentication
  redirectPath?: string; // Path to redirect to if not authenticated
  allowedRoles?: string[]; // Roles allowed to access the route
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({
  children,
  fallback = <div>Loading...</div>,
  redirectPath = '/login',
  allowedRoles,
}) => {
  const { user, isLoading } = useAuth();
  const router = useRouter();
  const pathname = usePathname();

  // If still loading, show fallback
  if (isLoading) {
    return fallback;
  }

  // If user is not authenticated, redirect to login
  if (!user) {
    // Store the attempted path for redirect after login
    localStorage.setItem('redirectAfterLogin', pathname);
    router.push(redirectPath);
    return null;
  }

  // If roles are specified, check if user has one of the allowed roles
  if (allowedRoles && user.role && !allowedRoles.includes(user.role)) {
    // Redirect to unauthorized page or home
    router.push('/');
    return null;
  }

  // User is authenticated and authorized
  return <>{children}</>;
};

export default ProtectedRoute;