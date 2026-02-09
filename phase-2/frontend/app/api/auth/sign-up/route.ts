/**
 * Sign-up endpoint proxy to backend
 * [Task]: T-002 - Secure User Onboarding
 * [From]: speckit.specify §2.1
 */

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    
    const response = await fetch(`${BACKEND_URL}/api/auth/sign-up`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
      credentials: 'include',
    });

    // Try to parse JSON, but handle non-JSON responses (like 500 Internal Server Error HTML)
    let data;
    const contentType = response.headers.get('content-type');
    if (contentType && contentType.includes('application/json')) {
      data = await response.json();
    } else {
      const text = await response.text();
      console.error('Backend returned non-JSON response:', text);
      return new Response(
        JSON.stringify({ error: `Backend returned ${response.status}`, details: text.slice(0, 200) }),
        { status: response.status, headers: { 'Content-Type': 'application/json' } }
      );
    }
    
    const headers = new Headers();
    headers.set('Content-Type', 'application/json');
    
    const setCookie = response.headers.get('set-cookie');
    if (setCookie) {
      headers.set('Set-Cookie', setCookie);
    }

    return new Response(JSON.stringify(data), {
      status: response.status,
      headers: headers,
    });
  } catch (error) {
    console.error('Sign-up proxy error:', error);
    return new Response(
      JSON.stringify({ error: 'Failed to sign up', details: String(error) }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
}
