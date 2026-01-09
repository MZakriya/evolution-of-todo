import { auth } from '../../../../lib/auth';

// Export the Better Auth handler for all HTTP methods
export const GET = auth.handler;
export const POST = auth.handler;
export const PUT = auth.handler;
export const DELETE = auth.handler;