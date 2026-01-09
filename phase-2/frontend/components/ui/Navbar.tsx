'use client';

import React from 'react';
import Link from 'next/link';
import { useAuth } from '../../components/auth/AuthContext';
import Button from './Button';

const Navbar = () => {
  const { user, isLoading, signOut } = useAuth();

  const handleSignOut = async () => {
    await signOut();
  };

  return (
    <nav className="bg-white shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link href="/" className="flex-shrink-0 flex items-center">
              <span className="text-xl font-bold text-gray-800">Todo App</span>
            </Link>
          </div>
          <div className="flex items-center space-x-4">
            {isLoading ? (
              <div>Loading...</div>
            ) : user ? (
              <>
                <span className="text-gray-700">Welcome, {user.name || user.email}</span>
                <Button variant="ghost" onClick={handleSignOut}>
                  Logout
                </Button>
              </>
            ) : (
              <>
                <Link href="/login">
                  <Button variant="ghost">Login</Button>
                </Link>
                <Link href="/signup">
                  <Button variant="primary">Sign Up</Button>
                </Link>
              </>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;