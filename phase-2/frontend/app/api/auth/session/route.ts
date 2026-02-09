/**
 * Session endpoint proxy to backend
 * [Task]: T-002 - Secure User Onboarding
 * [From]: speckit.specify §2.1
 */

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000';

export async function GET(request: Request) {
  try {
    // Forward Authorization header from client to backend
    const authHeader = request.headers.get('authorization');
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };
    if (authHeader) {
      headers['Authorization'] = authHeader;
    }

    // ... inside GET ...
    // Forward Cookie header if present (important for session!)
    const cookieHeader = request.headers.get('cookie');
    if (cookieHeader) {
      headers['Cookie'] = cookieHeader;
    }

    const response = await fetch(`${BACKEND_URL}/api/auth/session`, {
      method: 'GET',
      headers,
      credentials: 'include',
    });

    let data;
    const contentType = response.headers.get('content-type');
    if (contentType && contentType.includes('application/json')) {
      data = await response.json();
    } else {
        // If backend returns 401 with no body or text body, handled here
        data = null; 
    }
    
    // If backend returns 200, we expect data. If 401, data might be { detail: ... } or null.
    
    const responseHeaders = new Headers();
    responseHeaders.set('Content-Type', 'application/json');
    if (response.headers.get('set-cookie')) {
        responseHeaders.set('Set-Cookie', response.headers.get('set-cookie')!);
    }

    return new Response(JSON.stringify(data), {
      status: response.status,
      headers: responseHeaders,
    });
  } catch (error) {
    return new Response(
      JSON.stringify({ error: 'Failed to get session', details: String(error) }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
}
