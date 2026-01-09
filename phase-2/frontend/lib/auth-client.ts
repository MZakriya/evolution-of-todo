import { createAuthClient } from 'better-auth/client';

// Create the auth client
export const authClient = createAuthClient({
  baseURL: process.env.BETTER_AUTH_URL || 'http://localhost:3000',
});

// Export for convenience
export { type Session } from 'better-auth/client';