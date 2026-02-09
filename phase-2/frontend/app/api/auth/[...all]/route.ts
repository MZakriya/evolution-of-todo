/**
 * Auth API proxy route - forwards requests to backend auth endpoints
 */

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000';

export async function GET(request: Request) {
  const pathname = new URL(request.url).pathname;
  const endpoint = pathname.replace('/api/auth/', '');
  const backendUrl = `${BACKEND_URL}/api/auth/${endpoint}`;
  
  try {
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };

    // Forward Authorization header if present
    const authHeader = request.headers.get('authorization');
    if (authHeader) {
      headers['Authorization'] = authHeader;
    }

    // Forward Cookie header if present (for session validation)
    const cookieHeader = request.headers.get('cookie');
    if (cookieHeader) {
      headers['Cookie'] = cookieHeader;
    }

    const response = await fetch(backendUrl, {
      method: 'GET',
      headers,
      credentials: 'include',
    });

    if (!response.ok) {
        // Try to parse error details
        const errorData = await response.json().catch(() => ({}));
      return new Response(JSON.stringify(errorData || { error: `Backend returned ${response.status}` }), {
        status: response.status,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const data = await response.json();
    
    const responseHeaders = new Headers();
    responseHeaders.set('Content-Type', 'application/json');
    if (response.headers.get('set-cookie')) {
        responseHeaders.set('Set-Cookie', response.headers.get('set-cookie')!);
    }

    return new Response(JSON.stringify(data), {
      status: 200,
      headers: responseHeaders,
    });
  } catch (error) {
    return new Response(
      JSON.stringify({ error: 'Backend service unavailable', details: String(error) }),
      { status: 503, headers: { 'Content-Type': 'application/json' } }
    );
  }
}

export async function POST(request: Request) {
    // ... handle POST similarly if needed, but sign-in/sign-up are handled by specific files ...
    // The catch-all POST might be used for other things.
  const pathname = new URL(request.url).pathname;
  const endpoint = pathname.replace('/api/auth/', '');
  const backendUrl = `${BACKEND_URL}/api/auth/${endpoint}`;
  
  try {
    const body = await request.json();
    
    const headers: Record<string, string> = {
        'Content-Type': 'application/json',
    };
    const authHeader = request.headers.get('authorization');
    if (authHeader) headers['Authorization'] = authHeader;
    const cookieHeader = request.headers.get('cookie');
    if (cookieHeader) headers['Cookie'] = cookieHeader;

    // ... (inside POST)
    console.log(`[Proxy] Forwarding POST to ${backendUrl}`);
    const response = await fetch(backendUrl, {
      method: 'POST',
      headers,
      body: JSON.stringify(body),
      credentials: 'include',
    });

    console.log(`[Proxy] Backend responded with status ${response.status}`);
    
    let data;
    const contentType = response.headers.get('content-type');
    if (contentType && contentType.includes('application/json')) {
      data = await response.json();
    } else {
      const text = await response.text();
      console.error('[Proxy] Backend returned non-JSON response:', text);
      // We still return it as JSON error to the client
      data = { error: `Backend returned ${response.status}`, details: text.slice(0, 200) };
    }
    
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
    const errorMsg = error instanceof Error ? error.message : String(error);
    console.error(`[Proxy] Error:`, errorMsg);
    return new Response(
      JSON.stringify({ error: 'Backend service unavailable', details: errorMsg }),
      { status: 503, headers: { 'Content-Type': 'application/json' } }
    );
  }
}